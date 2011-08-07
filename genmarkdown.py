#!/usr/bin/env python
#
# Copyright 2011 Splunk, Inc.

from glob import glob
import csv, os, re, sys, time
import poc, json
import cgi
from optparse import OptionParser

MANUAL_MARKER="|"

# First, we read the groupings
def load_section_list(groupings_file):
    links_to_sections = {}
    sections_to_links = {}
    inFd = open(groupings_file, "r")
    prevLine = ""
    
    for rawLine in inFd:
        line = rawLine.strip()
        if 0 == len(line):
            continue

        if "#" == line[0]:
            line = line[1:]
            if "/" == line[0]:
                line = prevLine + line
                links_to_sections[line] = curSection
                sections_to_links[curSection].append(line)
                continue

        if line.startswith("["):
            curSection = line.strip("[]")
            sections_to_links[curSection] = []
            continue

        links_to_sections[line] = curSection
        sections_to_links[curSection].append(line)
        prevLine = line
    return sections_to_links, links_to_sections

def read_endpoints(csvr):
    endpoints = {}

    for line in csvr:
        endpoint = line[0]

        if endpoint.startswith('/services/'):
            endpoint = endpoint[len('/services/'):]

        if endpoint.startswith('#'):
            continue # Ignore comment

        # skip lines with {name} in them, these are not real endpoints.
        if '{' in endpoint:
            continue

        # lines starting with | are to be doc'd manually (non-EAI endpoints).
        # in this script, we don't care - convert all .po files.
        filename = endpoint.replace("/", ".").lstrip(MANUAL_MARKER)
        pofile   = 'po/%s.po' % filename

        # Get more endpoint descriptions
        if os.path.exists(pofile):
            endpoints.update(poc.get_endpoints(pofile))

    return endpoints
        
    # OK, we have all the endpoints in the dictionary
    # Now, we get a regex to parse out the in-url ({foo}) parameters
    url_param_regex = re.compile(r'\{([0-9a-zA-Z+_-]+)\}', re.IGNORECASE)
    for url in endpoints.keys():
        url_params = {}
        for url_param_match in url_param_regex.finditer(url):
            # Group 1 has just the thing inside the curly braces
            url_param = url_param_match.group(1)

            # Make sure that this URL does not have the same parameter twice
            assert not url_params.has_key(url_param)

            # All URL parameters are required by definition
            url_params[url_param] = {
                    "required": "true",
                    "summary": url_param,
                    "datatype": "String",
            }

        for method in endpoints[url]["methods"].keys():
            # For each method of this URL, we augment it with the URL parameters
            endpoints[url]["methods"][method]["urlParams"] = url_params 

# Given an endpoint URL, convert it to a "slug"
def slugify(url):
    return url.replace("/", "").replace("{", "").replace("}", "").replace("_", "").replace("-", "")

# Given a textual example, parse it into its constituent parts
def parse_example(example):   
    lines = example.split("\n")
    
    summary = ""
    request = ""
    response = ""

    is_summary = False
    is_example = False
    is_response = False
    for raw_line in lines:
        line = raw_line.strip()
        
        if len(line) == 0:
            continue

        if line == "==== Example ====":
            is_summary = True
            continue
            
        if not is_example and line[0] != "{":
            if is_summary:
                summary += line + "\n"
            continue
            
        if line[0] == "{" and not is_example:
            is_summary = False
            is_example = True
            continue
            
        if line[0] == "|":
            if line[1] == "}":
                is_example = False
                is_response = True
            continue
            
        if line == "<pre>" or line == "</pre>":
            continue
            
        if is_response:
            response += raw_line + "\n"
        else:
            request += raw_line + "\n"
    
    return (
        summary.strip(),
        request.rstrip(),
        response.rstrip(),
    )

class DocFile(object):
    def __init__(self, path, title):
        # Open the file
        self.file = open(path, 'w')
        self.title = title

    def writeline(self, str = None):
        str = str or ""
        return self.file.write(str + "\n")

    def write_endpoint(self, url, method, endpoint, emit_anchor):
        if emit_anchor:
            self.writeline("<a name='%s'/>" % slugify(url))
            self.writeline()
            
        self.writeline("## %s" % url)      
        self.writeline()
        self.writeline(endpoint.get("summary", ""))
        self.writeline()
        self.writeline("\t[%s] %s" % (method, url))
        self.writeline() 

        # Write out the parameters
        self.write_parameters(endpoint)

        # Write out the status code table
        self.write_status_code_table(endpoint)

        # Get the success status code, and write out the example
        success_code = int(sorted(endpoint["returns"].keys())[0])
        example = endpoint.get("description", "")
        self.write_example(example, success_code)

    def write_parameter(self, name, parameter):            
        required = "Required" if parameter.get("required", "false") == "true" else "Optional"
        param_type = parameter.get("datatype", "String")

        summary = parameter["summary"].replace("\n\n", "<br/><br/>")
        self.writeline(name)
        self.writeline(": _%s_ **%s** %s" % (required, param_type, summary))
        self.writeline()

    def write_parameters(self, endpoint):
        params = endpoint.get("params", [])
        url_params = endpoint.get("urlParams", [])

        # We only output the Parameters section if we have
        # any parameters
        if params or url_params:
            self.writeline("### Parameters")
            self.writeline()
        else:
            return

        # Output the URL parameters
        for param_name in sorted(url_params):
            parameter = url_params[param_name]
            self.write_parameter(param_name, parameter)

        # Output the regular parameters
        for param_name in sorted(params):
            parameter = params[param_name]
            self.write_parameter(param_name, parameter)

    def write_file_header(self):        
        self.writeline("---")
        self.writeline("title: %s" % self.title)
        self.writeline("---")
        self.writeline()
        self.writeline("# %s APIs" % self.title)
        self.writeline()

    def write_status_code_table(self, endpoint):    
        codes = endpoint["returns"]
        
        self.writeline("### Status Codes")
        self.writeline()
        self.writeline("| Status Code       | Description |")
        self.writeline("|:------------------|:------------|")

        for code in sorted(codes.keys()):
            summary = codes[code]["summary"]
            self.writeline("| **%s** | %s |" % (code, summary))
            self.writeline("|--------------------------------")

        self.writeline()

    def write_example(self, example, success_code):
        summary, request, response = parse_example(example)        

        self.writeline("### Example")
        self.writeline()
        self.writeline(summary)
        self.writeline()
        self.writeline("#### Request")
        self.writeline("<pre class='terminal'>")
        self.writeline(cgi.escape(request))
        self.writeline("</pre>")
        self.writeline("<p></p>")
        self.writeline()
        self.writeline("#### Response")
        self.writeline("<%%= headers %d %%>" % success_code)
        self.writeline("<pre class='highlight'><code class='language-xml'>")
        self.writeline(cgi.escape(response))
        self.writeline("</code></pre>")
        self.writeline()

def emit_markdown(section_files, links_to_sections, endpoints):
    for url in sorted(endpoints.keys()):
        f = section_files[links_to_sections[url]]
        endpoint = endpoints[url]
        methods = endpoint["methods"]
        emit_anchor = True

        for method_name in sorted(methods.keys()):
            method = methods[method_name]
            f.write_endpoint(url, method_name, method, emit_anchor)
            emit_anchor = False
      
def emit_toc(file, endpoints, sections_to_links):
    for section in sorted(sections_to_links.keys()):
        print >> file, '<li class="js-topic">'
        print >> file, '  <h3><a href="#" class="js-expand-btn collapsed">&nbsp;</a><a href="/api/%s/">%s</a></h3>' % (
            section.lower(), section
        )
        print >> file, '  <ul class="js-guides">'
        for url in sections_to_links[section]:
            if url not in endpoints.keys():   
                continue

            print >> file, '    <li><a href="/api/%s/#%s">%s</a></li>' % (
                section.lower(), slugify(url), url
            )
        print >> file, '  </ul>'
        print >> file, '</li>'
        print >> file

def error(message, exitcode = None):
    print >> sys.stderr, "Error: %s" % message
    if not exitcode is None: sys.exit(exitcode)

def parse(argv):
    parser = OptionParser()
    parser.add_option(
        "--endpoints", 
        dest="endpoints",
        help="CSV file to read endpoints from",
        metavar="ENDPOINTS")
    parser.add_option(
        "--groupings", 
        dest="groupings",
        help="File to read groupings from",
        metavar="GROUPINGS")
    parser.add_option(
        "--toc", 
        dest="toc",
        help="File to output TOC too",
        metavar="TOC")
    parser.add_option(
        "--output", 
        dest="output",
        help="Directory to output Markdown files too",
        metavar="OUTPUT")

    options, args = parser.parse_args(argv)

    if not options.endpoints:
        error("Must supply endpoints file", 2)

    if not options.groupings:
        error("Must supply groupings file", 2)

    if not options.toc:
        error("Must supply TOC output file", 2)

    if not options.output:
        error("Must supply Markdown output directory", 2)

    return options.endpoints, options.groupings, options.toc, options.output

def main(argv):
    endpoints_file_name, groupings, toc, output = parse(argv)

    # Create a CSV Reader for the endpoints CSV file
    endpoints_file = open(endpoints_file_name, 'r')
    csvr = csv.reader(endpoints_file)

    # Get the endpoints dictionary
    endpoints = read_endpoints(csvr)

    # Load the section information from the groupings file
    sections_to_links, links_to_sections = load_section_list(groupings)

    # Create a file for each section
    section_names = set(sections_to_links.keys())
    section_files = {}
    for section_name in section_names:
        section_files[section_name] = DocFile(os.path.join(output, section_name.lower() + ".md"), section_name)

    # Now, emit all the markdown files
    emit_markdown(section_files, links_to_sections, endpoints)

    # Emit the TOC
    toc_file = open(toc, 'w')
    emit_toc(toc_file, endpoints, sections_to_links)

    # And we're done
    return
        
if __name__ == "__main__":
    main(sys.argv[1:])
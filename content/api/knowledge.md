## data/lookup-table-files
{: name='datalookuptablefiles'}

List lookup table files.

	[GET] data/lookup-table-files

### Parameters

count
: _Optional_ **Number** Maximum number of items to return.

offset
: _Optional_ **Number** Index for first item to return.

search
: _Optional_ **String** Boolean predicate to filter results.

sort_dir
: _Optional_ **Enum** Direction to sort by (asc/desc).

sort_key
: _Optional_ **String** Field to sort by.

sort_mode
: _Optional_ **Enum** Collating sequence for the sort (auto, alpha, alpha_case, num).

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view lookup-table file. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Retrieve the list of lookup table files.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/data/lookup-table-files
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;lookup-table-files&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/lookup-table-files&lt;/id&gt;
  &lt;updated&gt;2011-07-21T19:26:11-07:00&lt;/updated&gt;
  &lt;generator version="104309"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/data/lookup-table-files/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/admin/search/data/lookup-table-files/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;lookup.csv&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/lookup-table-files/lookup.csv&lt;/id&gt;
    &lt;updated&gt;2011-07-21T19:26:11-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/data/lookup-table-files/lookup.csv" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/admin/search/data/lookup-table-files/lookup.csv" rel="list"/&gt;
    &lt;link href="/servicesNS/admin/search/data/lookup-table-files/lookup.csv/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/admin/search/data/lookup-table-files/lookup.csv" rel="edit"/&gt;
    &lt;link href="/servicesNS/admin/search/data/lookup-table-files/lookup.csv" rel="remove"/&gt;
    &lt;link href="/servicesNS/admin/search/data/lookup-table-files/lookup.csv/move" rel="move"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:appName"&gt;search&lt;/s:key&gt;
        &lt;s:key name="eai:data"&gt;
&lt;![CDATA[/opt/splunk/etc/users/admin/search/lookups/lookup.csv]]&gt;        &lt;/s:key&gt;
        &lt;s:key name="eai:userName"&gt;admin&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/lookup-table-files
{: name='datalookuptablefiles'}

Create a lookup table file by moving a file from the upload staging area into $SPLUNK_HOME.

	[POST] data/lookup-table-files

### Parameters

eai:data
: _Required_ **String** Move a lookup table file from the given path into $SPLUNK_HOME. This path must have the lookup staging area as an ancestor.

name
: _Required_ **String** The lookup table filename.

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **201** | Created successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **402** | The Splunk license in use has disabled this feature. |
|--------------------------------
| **403** | Insufficient permissions to create lookup-table file. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Create a private lookup table file from a file in the lookup staging area.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/data/lookup-table-files \
	-d eai:data=/opt/splunk/var/run/splunk/lookup_tmp/lookup-in-staging-dir.csv \
	-d name=lookup.csv
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;lookup-table-files&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/lookup-table-files&lt;/id&gt;
  &lt;updated&gt;2011-07-21T18:26:35-07:00&lt;/updated&gt;
  &lt;generator version="104309"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/data/lookup-table-files/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/admin/search/data/lookup-table-files/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;lookup.csv&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/lookup-table-files/lookup.csv&lt;/id&gt;
    &lt;updated&gt;2011-07-21T18:26:35-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/data/lookup-table-files/lookup.csv" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/admin/search/data/lookup-table-files/lookup.csv" rel="list"/&gt;
    &lt;link href="/servicesNS/admin/search/data/lookup-table-files/lookup.csv/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/admin/search/data/lookup-table-files/lookup.csv" rel="edit"/&gt;
    &lt;link href="/servicesNS/admin/search/data/lookup-table-files/lookup.csv" rel="remove"/&gt;
    &lt;link href="/servicesNS/admin/search/data/lookup-table-files/lookup.csv/move" rel="move"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:appName"&gt;search&lt;/s:key&gt;
        &lt;s:key name="eai:data"&gt;
&lt;![CDATA[/opt/splunk/etc/users/admin/search/lookups/lookup.csv]]&gt;        &lt;/s:key&gt;
        &lt;s:key name="eai:userName"&gt;admin&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/lookup-table-files/{name}
{: name='datalookuptablefilesname'}

Delete the named lookup table file.

	[DELETE] data/lookup-table-files/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deleted successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to delete look-up table file. |
|--------------------------------
| **404** | Look-up table file does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Delete the lookup table file created earlier.

#### Request
<pre class='terminal'>
curl -k -u admin:pass --request DELETE \
	https://localhost:8089/servicesNS/admin/search/data/lookup-table-files/lookup.csv
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;lookup-table-files&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/lookup-table-files&lt;/id&gt;
  &lt;updated&gt;2011-07-21T18:43:11-07:00&lt;/updated&gt;
  &lt;generator version="104309"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/data/lookup-table-files/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/admin/search/data/lookup-table-files/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## data/lookup-table-files/{name}
{: name='datalookuptablefilesname'}

List a single lookup table file.

	[GET] data/lookup-table-files/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view look-up table files. |
|--------------------------------
| **404** | Look-up table file does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Retrieve the newly created lookup table file.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/servicesNS/admin/search/data/lookup-table-files/lookup.csv
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;lookup-table-files&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/lookup-table-files&lt;/id&gt;
  &lt;updated&gt;2011-07-21T18:37:25-07:00&lt;/updated&gt;
  &lt;generator version="104309"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/data/lookup-table-files/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/admin/search/data/lookup-table-files/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;lookup.csv&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/lookup-table-files/lookup.csv&lt;/id&gt;
    &lt;updated&gt;2011-07-21T18:37:25-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/data/lookup-table-files/lookup.csv" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/admin/search/data/lookup-table-files/lookup.csv" rel="list"/&gt;
    &lt;link href="/servicesNS/admin/search/data/lookup-table-files/lookup.csv/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/admin/search/data/lookup-table-files/lookup.csv" rel="edit"/&gt;
    &lt;link href="/servicesNS/admin/search/data/lookup-table-files/lookup.csv" rel="remove"/&gt;
    &lt;link href="/servicesNS/admin/search/data/lookup-table-files/lookup.csv/move" rel="move"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:appName"&gt;search&lt;/s:key&gt;
        &lt;s:key name="eai:attributes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="optionalFields"&gt;
              &lt;s:list/&gt;
            &lt;/s:key&gt;
            &lt;s:key name="requiredFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;eai:data&lt;/s:item&gt;
              &lt;/s:list&gt;
            &lt;/s:key&gt;
            &lt;s:key name="wildcardFields"&gt;
              &lt;s:list/&gt;
            &lt;/s:key&gt;
          &lt;/s:dict&gt;
        &lt;/s:key&gt;
        &lt;s:key name="eai:data"&gt;
&lt;![CDATA[/opt/splunk/etc/users/admin/search/lookups/lookup.csv]]&gt;        &lt;/s:key&gt;
        &lt;s:key name="eai:userName"&gt;admin&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/lookup-table-files/{name}
{: name='datalookuptablefilesname'}

Modify a lookup table file by replacing it with a file from the upload staging area.

	[POST] data/lookup-table-files/{name}

### Parameters

eai:data
: _Required_ **INHERITED** INHERITED

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Updated successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **402** | The Splunk license in use has disabled this feature. |
|--------------------------------
| **403** | Insufficient permissions to edit look-up tble file. |
|--------------------------------
| **404** | Look-up table file does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Replace the contents of an existing lookup table file with the contents of a file in the lookup staging area.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/servicesNS/admin/search/data/lookup-table-files/lookup.csv \
	-d eai:data=/opt/splunk/var/run/splunk/lookup_tmp/another-lookup-in-staging-dir.csv
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;lookup-table-files&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/lookup-table-files&lt;/id&gt;
  &lt;updated&gt;2011-07-21T18:41:52-07:00&lt;/updated&gt;
  &lt;generator version="104309"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/data/lookup-table-files/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/admin/search/data/lookup-table-files/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;lookup.csv&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/lookup-table-files/lookup.csv&lt;/id&gt;
    &lt;updated&gt;2011-07-21T18:41:52-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/data/lookup-table-files/lookup.csv" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/admin/search/data/lookup-table-files/lookup.csv" rel="list"/&gt;
    &lt;link href="/servicesNS/admin/search/data/lookup-table-files/lookup.csv/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/admin/search/data/lookup-table-files/lookup.csv" rel="edit"/&gt;
    &lt;link href="/servicesNS/admin/search/data/lookup-table-files/lookup.csv" rel="remove"/&gt;
    &lt;link href="/servicesNS/admin/search/data/lookup-table-files/lookup.csv/move" rel="move"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:appName"&gt;search&lt;/s:key&gt;
        &lt;s:key name="eai:data"&gt;
&lt;![CDATA[/opt/splunk/etc/users/admin/search/lookups/lookup.csv]]&gt;        &lt;/s:key&gt;
        &lt;s:key name="eai:userName"&gt;admin&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/props/extractions
{: name='datapropsextractions'}

List field extractions.

	[GET] data/props/extractions

### Parameters

count
: _Optional_ **Number** Maximum number of items to return.

offset
: _Optional_ **Number** Index for first item to return.

search
: _Optional_ **String** Boolean predicate to filter results.

sort_dir
: _Optional_ **Enum** Direction to sort by (asc/desc).

sort_key
: _Optional_ **String** Field to sort by.

sort_mode
: _Optional_ **Enum** Collating sequence for the sort (auto, alpha, alpha_case, num).

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view extractions. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Retrieve the list of search-time extractions.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/data/props/extractions
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;props-extract&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/props/extractions&lt;/id&gt;
  &lt;updated&gt;2011-07-10T22:55:04-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/data/props/extractions/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;access_combined : REPORT-access&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/data/props/extractions/access_combined%20%3A%20REPORT-access&lt;/id&gt;
    &lt;updated&gt;2011-07-10T22:55:04-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/data/props/extractions/access_combined%20%3A%20REPORT-access" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/data/props/extractions/access_combined%20%3A%20REPORT-access" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/props/extractions/access_combined%20%3A%20REPORT-access" rel="edit"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="attribute"&gt;REPORT-access&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="stanza"&gt;access_combined&lt;/s:key&gt;
        &lt;s:key name="type"&gt;Uses transform&lt;/s:key&gt;
        &lt;s:key name="value"&gt;access-extractions&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/props/extractions
{: name='datapropsextractions'}

Create a new field extraction.

	[POST] data/props/extractions

### Parameters

name
: _Required_ **String** The user-specified part of the field extraction name. The full name of the field extraction includes this identifier as a suffix.

stanza
: _Required_ **String** The props.conf stanza to which this field extraction applies, e.g. the sourcetype or source that triggers this field extraction. The full name of the field extraction includes this stanza name as a prefix.

type
: _Required_ **Enum** Valid values: (REPORT &#124; EXTRACT)<br/><br/>An EXTRACT-type field extraction is defined with an "inline" regular expression. A REPORT-type field extraction refers to a transforms.conf stanza.

value
: _Required_ **String** If this is an EXTRACT-type field extraction, specify a regular expression with named capture groups that define the desired fields. If this is a REPORT-type field extraction, specify a comma- or space-delimited list of transforms.conf stanza names that define the field transformations to apply.

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **201** | Created successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **402** | The Splunk license in use has disabled this feature. |
|--------------------------------
| **403** | Insufficient permissions to create extraction. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Create a new search-time extraction that extracts the port value from this FTP server log.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/data/props/extractions \
	-d name=port \
	-d stanza=ftp_log \
	-d type=EXTRACT \
	-d "value=port (?&lt;port_number&gt;\d+)"
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;props-extract&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/props/extractions&lt;/id&gt;
  &lt;updated&gt;2011-07-10T22:56:17-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/data/props/extractions/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;ftp_log : EXTRACT-port&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/props/extractions/ftp_log%20%3A%20EXTRACT-port&lt;/id&gt;
    &lt;updated&gt;2011-07-10T22:56:17-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/data/props/extractions/ftp_log%20%3A%20EXTRACT-port" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/admin/search/data/props/extractions/ftp_log%20%3A%20EXTRACT-port" rel="list"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/extractions/ftp_log%20%3A%20EXTRACT-port" rel="edit"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/extractions/ftp_log%20%3A%20EXTRACT-port" rel="remove"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/extractions/ftp_log%20%3A%20EXTRACT-port/move" rel="move"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="attribute"&gt;EXTRACT-port&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="stanza"&gt;ftp_log&lt;/s:key&gt;
        &lt;s:key name="type"&gt;Inline&lt;/s:key&gt;
        &lt;s:key name="value"&gt;port (?&amp;lt;port_number&amp;gt;\d )&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/props/extractions/{name}
{: name='datapropsextractionsname'}

Delete the named field extraction.

	[DELETE] data/props/extractions/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deleted successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to delete named extraction. |
|--------------------------------
| **404** | Named extraction does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Remove the extraction created earlier.

#### Request
<pre class='terminal'>
curl -k -u admin:pass --request DELETE \
	https://localhost:8089/servicesNS/admin/search/data/props/extractions/ftp_log%20%3A%20EXTRACT-port
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;props-extract&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/props/extractions&lt;/id&gt;
  &lt;updated&gt;2011-07-10T23:05:42-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/data/props/extractions/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## data/props/extractions/{name}
{: name='datapropsextractionsname'}

List a single field extraction.

	[GET] data/props/extractions/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view named extraction. |
|--------------------------------
| **404** | Named extraction does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Retrieve the newly created extraction.  Note that the name is an aggregate of extraction, affected stanza, and extraction type.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/servicesNS/admin/search/data/props/extractions/ftp_log%20%3A%20EXTRACT-port
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;props-extract&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/props/extractions&lt;/id&gt;
  &lt;updated&gt;2011-07-10T23:02:31-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/data/props/extractions/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;ftp_log : EXTRACT-port&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/props/extractions/ftp_log%20%3A%20EXTRACT-port&lt;/id&gt;
    &lt;updated&gt;2011-07-10T23:02:31-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/data/props/extractions/ftp_log%20%3A%20EXTRACT-port" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/admin/search/data/props/extractions/ftp_log%20%3A%20EXTRACT-port" rel="list"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/extractions/ftp_log%20%3A%20EXTRACT-port" rel="edit"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/extractions/ftp_log%20%3A%20EXTRACT-port" rel="remove"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/extractions/ftp_log%20%3A%20EXTRACT-port/move" rel="move"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="attribute"&gt;EXTRACT-port&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:attributes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="optionalFields"&gt;
              &lt;s:list/&gt;
            &lt;/s:key&gt;
            &lt;s:key name="requiredFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;value&lt;/s:item&gt;
              &lt;/s:list&gt;
            &lt;/s:key&gt;
            &lt;s:key name="wildcardFields"&gt;
              &lt;s:list/&gt;
            &lt;/s:key&gt;
          &lt;/s:dict&gt;
        &lt;/s:key&gt;
        &lt;s:key name="stanza"&gt;ftp_log&lt;/s:key&gt;
        &lt;s:key name="type"&gt;Inline&lt;/s:key&gt;
        &lt;s:key name="value"&gt;connection on port (?&amp;lt;port_number&amp;gt;\d )&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/props/extractions/{name}
{: name='datapropsextractionsname'}

Modify the named field extraction.

	[POST] data/props/extractions/{name}

### Parameters

value
: _Required_ **INHERITED** INHERITED

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Updated successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **402** | The Splunk license in use has disabled this feature. |
|--------------------------------
| **403** | Insufficient permissions to edit named extraction. |
|--------------------------------
| **404** | Named extraction does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Adjust the regular expression for the recently created extraction.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/servicesNS/admin/search/data/props/extractions/ftp_log%20%3A%20EXTRACT-port \
	-d "value=connection on port (?&lt;port_number&gt;\d+)"
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;props-extract&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/props/extractions&lt;/id&gt;
  &lt;updated&gt;2011-07-10T23:05:05-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/data/props/extractions/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;ftp_log : EXTRACT-port&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/props/extractions/ftp_log%20%3A%20EXTRACT-port&lt;/id&gt;
    &lt;updated&gt;2011-07-10T23:05:05-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/data/props/extractions/ftp_log%20%3A%20EXTRACT-port" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/admin/search/data/props/extractions/ftp_log%20%3A%20EXTRACT-port" rel="list"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/extractions/ftp_log%20%3A%20EXTRACT-port" rel="edit"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/extractions/ftp_log%20%3A%20EXTRACT-port" rel="remove"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/extractions/ftp_log%20%3A%20EXTRACT-port/move" rel="move"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="attribute"&gt;EXTRACT-port&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="stanza"&gt;ftp_log&lt;/s:key&gt;
        &lt;s:key name="type"&gt;Inline&lt;/s:key&gt;
        &lt;s:key name="value"&gt;connection on port (?&amp;lt;port_number&amp;gt;\d )&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/props/fieldaliases
{: name='datapropsfieldaliases'}

List field aliases.

	[GET] data/props/fieldaliases

### Parameters

count
: _Optional_ **Number** Maximum number of items to return.

offset
: _Optional_ **Number** Index for first item to return.

search
: _Optional_ **String** Boolean predicate to filter results.

sort_dir
: _Optional_ **Enum** Direction to sort by (asc/desc).

sort_key
: _Optional_ **String** Field to sort by.

sort_mode
: _Optional_ **Enum** Collating sequence for the sort (auto, alpha, alpha_case, num).

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view filed aliases. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Retrieve the list of field aliases.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/data/props/fieldaliases
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;fieldaliases&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/props/fieldaliases&lt;/id&gt;
  &lt;updated&gt;2011-07-21T19:31:41-07:00&lt;/updated&gt;
  &lt;generator version="104309"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/data/props/fieldaliases/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;my_sourcetype : FIELDALIAS-alias_name&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/props/fieldaliases/my_sourcetype%20%3A%20FIELDALIAS-alias_name&lt;/id&gt;
    &lt;updated&gt;2011-07-21T19:31:41-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/data/props/fieldaliases/my_sourcetype%20%3A%20FIELDALIAS-alias_name" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/admin/search/data/props/fieldaliases/my_sourcetype%20%3A%20FIELDALIAS-alias_name" rel="list"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/fieldaliases/my_sourcetype%20%3A%20FIELDALIAS-alias_name" rel="edit"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/fieldaliases/my_sourcetype%20%3A%20FIELDALIAS-alias_name" rel="remove"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/fieldaliases/my_sourcetype%20%3A%20FIELDALIAS-alias_name/move" rel="move"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="alias.foo"&gt;bar&lt;/s:key&gt;
        &lt;s:key name="attribute"&gt;FIELDALIAS-alias_name&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="stanza"&gt;my_sourcetype&lt;/s:key&gt;
        &lt;s:key name="type"&gt;FIELDALIAS&lt;/s:key&gt;
        &lt;s:key name="value"&gt;foo AS bar&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/props/fieldaliases
{: name='datapropsfieldaliases'}

Create a new field alias.

	[POST] data/props/fieldaliases

### Parameters

name
: _Required_ **String** The user-specified part of the field alias name. The full name of the field alias includes this identifier as a suffix.

stanza
: _Required_ **String** The props.conf stanza to which this field alias applies, e.g. the sourcetype or source that causes this field alias to be applied. The full name of the field alias includes this stanza name as a prefix.

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **201** | Created successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **402** | The Splunk license in use has disabled this feature. |
|--------------------------------
| **403** | Insufficient permissions to create field alias. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Create a new field alias.
Alias the field "foo" as "bar" for sourcetype "my_sourctype".

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/data/props/fieldaliases \
	-d name=alias_name \
	-d stanza=my_sourcetype \
	-d alias.foo=bar
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;fieldaliases&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/props/fieldaliases&lt;/id&gt;
  &lt;updated&gt;2011-07-21T19:30:17-07:00&lt;/updated&gt;
  &lt;generator version="104309"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/data/props/fieldaliases/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;my_sourcetype : FIELDALIAS-alias_name&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/props/fieldaliases/my_sourcetype%20%3A%20FIELDALIAS-alias_name&lt;/id&gt;
    &lt;updated&gt;2011-07-21T19:30:17-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/data/props/fieldaliases/my_sourcetype%20%3A%20FIELDALIAS-alias_name" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/admin/search/data/props/fieldaliases/my_sourcetype%20%3A%20FIELDALIAS-alias_name" rel="list"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/fieldaliases/my_sourcetype%20%3A%20FIELDALIAS-alias_name" rel="edit"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/fieldaliases/my_sourcetype%20%3A%20FIELDALIAS-alias_name" rel="remove"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/fieldaliases/my_sourcetype%20%3A%20FIELDALIAS-alias_name/move" rel="move"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="alias.foo"&gt;bar&lt;/s:key&gt;
        &lt;s:key name="attribute"&gt;FIELDALIAS-alias_name&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="stanza"&gt;my_sourcetype&lt;/s:key&gt;
        &lt;s:key name="type"&gt;FIELDALIAS&lt;/s:key&gt;
        &lt;s:key name="value"&gt;foo AS bar&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/props/fieldaliases/{name}
{: name='datapropsfieldaliasesname'}

Delete the named field alias.

	[DELETE] data/props/fieldaliases/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deleted successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to delete field alias. |
|--------------------------------
| **404** | Field alias does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Remove the recently created field alias.

#### Request
<pre class='terminal'>
curl -k -u admin:pass --request DELETE \
	https://localhost:8089/servicesNS/admin/search/data/props/fieldaliases/my_sourcetype%20%3A%20FIELDALIAS-alias_name
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;fieldaliases&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/props/fieldaliases&lt;/id&gt;
  &lt;updated&gt;2011-07-21T19:37:45-07:00&lt;/updated&gt;
  &lt;generator version="104309"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/data/props/fieldaliases/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## data/props/fieldaliases/{name}
{: name='datapropsfieldaliasesname'}

List a single field alias.

	[GET] data/props/fieldaliases/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view field alias. |
|--------------------------------
| **404** | Field alias does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Retrieve the newly created field alias.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/servicesNS/admin/search/data/props/fieldaliases/my_sourcetype%20%3A%20FIELDALIAS-alias_name
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;fieldaliases&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/props/fieldaliases&lt;/id&gt;
  &lt;updated&gt;2011-07-21T19:33:00-07:00&lt;/updated&gt;
  &lt;generator version="104309"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/data/props/fieldaliases/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;my_sourcetype : FIELDALIAS-alias_name&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/props/fieldaliases/my_sourcetype%20%3A%20FIELDALIAS-alias_name&lt;/id&gt;
    &lt;updated&gt;2011-07-21T19:33:00-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/data/props/fieldaliases/my_sourcetype%20%3A%20FIELDALIAS-alias_name" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/admin/search/data/props/fieldaliases/my_sourcetype%20%3A%20FIELDALIAS-alias_name" rel="list"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/fieldaliases/my_sourcetype%20%3A%20FIELDALIAS-alias_name" rel="edit"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/fieldaliases/my_sourcetype%20%3A%20FIELDALIAS-alias_name" rel="remove"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/fieldaliases/my_sourcetype%20%3A%20FIELDALIAS-alias_name/move" rel="move"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="alias.foo"&gt;bar&lt;/s:key&gt;
        &lt;s:key name="attribute"&gt;FIELDALIAS-alias_name&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:attributes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="optionalFields"&gt;
              &lt;s:list/&gt;
            &lt;/s:key&gt;
            &lt;s:key name="requiredFields"&gt;
              &lt;s:list/&gt;
            &lt;/s:key&gt;
            &lt;s:key name="wildcardFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;alias\..*&lt;/s:item&gt;
              &lt;/s:list&gt;
            &lt;/s:key&gt;
          &lt;/s:dict&gt;
        &lt;/s:key&gt;
        &lt;s:key name="stanza"&gt;my_sourcetype&lt;/s:key&gt;
        &lt;s:key name="type"&gt;FIELDALIAS&lt;/s:key&gt;
        &lt;s:key name="value"&gt;foo AS bar&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/props/fieldaliases/{name}
{: name='datapropsfieldaliasesname'}

Modify the named field alias.

	[POST] data/props/fieldaliases/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Updated successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **402** | The Splunk license in use has disabled this feature. |
|--------------------------------
| **403** | Insufficient permissions to edit field alias. |
|--------------------------------
| **404** | Field alias does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Adjust the newly created field alias.
Alias the fields "hi and "bye" as "hello" and "goodbye", respectively.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/servicesNS/admin/search/data/props/fieldaliases/my_sourcetype%20%3A%20FIELDALIAS-alias_name \
	-d alias.hi=hello \
	-d alias.bye=goodbye
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;fieldaliases&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/props/fieldaliases&lt;/id&gt;
  &lt;updated&gt;2011-07-21T19:34:36-07:00&lt;/updated&gt;
  &lt;generator version="104309"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/data/props/fieldaliases/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;my_sourcetype : FIELDALIAS-alias_name&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/props/fieldaliases/my_sourcetype%20%3A%20FIELDALIAS-alias_name&lt;/id&gt;
    &lt;updated&gt;2011-07-21T19:34:36-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/data/props/fieldaliases/my_sourcetype%20%3A%20FIELDALIAS-alias_name" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/admin/search/data/props/fieldaliases/my_sourcetype%20%3A%20FIELDALIAS-alias_name" rel="list"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/fieldaliases/my_sourcetype%20%3A%20FIELDALIAS-alias_name" rel="edit"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/fieldaliases/my_sourcetype%20%3A%20FIELDALIAS-alias_name" rel="remove"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/fieldaliases/my_sourcetype%20%3A%20FIELDALIAS-alias_name/move" rel="move"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="alias.bye"&gt;goodbye&lt;/s:key&gt;
        &lt;s:key name="alias.hi"&gt;hello&lt;/s:key&gt;
        &lt;s:key name="attribute"&gt;FIELDALIAS-alias_name&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="stanza"&gt;my_sourcetype&lt;/s:key&gt;
        &lt;s:key name="type"&gt;FIELDALIAS&lt;/s:key&gt;
        &lt;s:key name="value"&gt;bye AS goodbye hi AS hello&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/props/lookups
{: name='datapropslookups'}

List automatic lookups.

	[GET] data/props/lookups

### Parameters

count
: _Optional_ **Number** Maximum number of items to return.

offset
: _Optional_ **Number** Index for first item to return.

search
: _Optional_ **String** Boolean predicate to filter results.

sort_dir
: _Optional_ **Enum** Direction to sort by (asc/desc).

sort_key
: _Optional_ **String** Field to sort by.

sort_mode
: _Optional_ **Enum** Collating sequence for the sort (auto, alpha, alpha_case, num).

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view lookups. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Retrieve the list of automatic lookups.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/data/props/lookups
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;props-lookup&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/props/lookups&lt;/id&gt;
  &lt;updated&gt;2011-08-01T20:43:53-07:00&lt;/updated&gt;
  &lt;generator version="105049"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/data/props/lookups/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;my_sourcetype : LOOKUP-my_lookup&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/props/lookups/my_sourcetype%20%3A%20LOOKUP-my_lookup&lt;/id&gt;
    &lt;updated&gt;2011-08-01T20:43:53-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/data/props/lookups/my_sourcetype%20%3A%20LOOKUP-my_lookup" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/admin/search/data/props/lookups/my_sourcetype%20%3A%20LOOKUP-my_lookup" rel="list"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/lookups/my_sourcetype%20%3A%20LOOKUP-my_lookup" rel="edit"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/lookups/my_sourcetype%20%3A%20LOOKUP-my_lookup" rel="remove"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/lookups/my_sourcetype%20%3A%20LOOKUP-my_lookup/move" rel="move"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="attribute"&gt;LOOKUP-my_lookup&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="lookup.field.input.foo"/&gt;
        &lt;s:key name="lookup.field.output.fuzz"/&gt;
        &lt;s:key name="overwrite"&gt;1&lt;/s:key&gt;
        &lt;s:key name="stanza"&gt;my_sourcetype&lt;/s:key&gt;
        &lt;s:key name="transform"&gt;my_transform&lt;/s:key&gt;
        &lt;s:key name="type"&gt;LOOKUP&lt;/s:key&gt;
        &lt;s:key name="value"&gt;my_transform foo OUTPUT fuzz&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/props/lookups
{: name='datapropslookups'}

Create a new automatic lookup.

	[POST] data/props/lookups

### Parameters

name
: _Required_ **String** The user-specified part of the automatic lookup name. The full name of the automatic lookup includes this identifier as a suffix.

overwrite
: _Required_ **Boolean** If set to true, output fields are always overridden. If set to false, output fields are only written out if they do not already exist.

stanza
: _Required_ **String** The props.conf stanza to which this automatic lookup applies, e.g. the sourcetype or source that automatically triggers this lookup. The full name of the automatic lookup includes this stanza name as a prefix.

transform
: _Required_ **String** The transforms.conf stanza that defines the lookup to apply.

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **201** | Created successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **402** | The Splunk license in use has disabled this feature. |
|--------------------------------
| **403** | Insufficient permissions to create a lookup. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Create an automatic lookup named "my_lookup" on the sourcetype "my_sourcetype".
Use the lookup definition named "my_transform".
Match on the field "foo", and output the field "fuzz".

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/data/props/lookups \
	-d name=my_lookup \
	-d overwrite=1 \
	-d stanza=my_sourcetype \
	-d transform=my_transform \
	-d lookup.field.input.foo= \
	-d lookup.field.output.fuzz=
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;props-lookup&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/props/lookups&lt;/id&gt;
  &lt;updated&gt;2011-08-01T20:43:31-07:00&lt;/updated&gt;
  &lt;generator version="105049"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/data/props/lookups/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;my_sourcetype : LOOKUP-my_lookup&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/props/lookups/my_sourcetype%20%3A%20LOOKUP-my_lookup&lt;/id&gt;
    &lt;updated&gt;2011-08-01T20:43:31-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/data/props/lookups/my_sourcetype%20%3A%20LOOKUP-my_lookup" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/admin/search/data/props/lookups/my_sourcetype%20%3A%20LOOKUP-my_lookup" rel="list"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/lookups/my_sourcetype%20%3A%20LOOKUP-my_lookup" rel="edit"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/lookups/my_sourcetype%20%3A%20LOOKUP-my_lookup" rel="remove"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/lookups/my_sourcetype%20%3A%20LOOKUP-my_lookup/move" rel="move"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="attribute"&gt;LOOKUP-my_lookup&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="lookup.field.input.foo"/&gt;
        &lt;s:key name="lookup.field.output.fuzz"/&gt;
        &lt;s:key name="overwrite"&gt;1&lt;/s:key&gt;
        &lt;s:key name="stanza"&gt;my_sourcetype&lt;/s:key&gt;
        &lt;s:key name="transform"&gt;my_transform&lt;/s:key&gt;
        &lt;s:key name="type"&gt;LOOKUP&lt;/s:key&gt;
        &lt;s:key name="value"&gt;my_transform foo OUTPUT fuzz&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/props/lookups/{name}
{: name='datapropslookupsname'}

Delete the named automatic lookup.

	[DELETE] data/props/lookups/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deleted successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to delete lookup. |
|--------------------------------
| **404** | Lookup does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Remove the recently created automatic lookup.

#### Request
<pre class='terminal'>
curl -k -u admin:pass --request DELETE \
	https://localhost:8089/servicesNS/admin/search/data/props/lookups/my_sourcetype%20%3A%20LOOKUP-my_lookup
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;props-lookup&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/props/lookups&lt;/id&gt;
  &lt;updated&gt;2011-08-01T20:44:32-07:00&lt;/updated&gt;
  &lt;generator version="105049"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/data/props/lookups/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## data/props/lookups/{name}
{: name='datapropslookupsname'}

List a single automatic lookup.

	[GET] data/props/lookups/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view lookup. |
|--------------------------------
| **404** | Lookup does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Retrieve the newly created automatic lookup.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/servicesNS/admin/search/data/props/lookups/my_sourcetype%20%3A%20LOOKUP-my_lookup
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;props-lookup&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/props/lookups&lt;/id&gt;
  &lt;updated&gt;2011-08-01T20:44:06-07:00&lt;/updated&gt;
  &lt;generator version="105049"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/data/props/lookups/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;my_sourcetype : LOOKUP-my_lookup&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/props/lookups/my_sourcetype%20%3A%20LOOKUP-my_lookup&lt;/id&gt;
    &lt;updated&gt;2011-08-01T20:44:06-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/data/props/lookups/my_sourcetype%20%3A%20LOOKUP-my_lookup" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/admin/search/data/props/lookups/my_sourcetype%20%3A%20LOOKUP-my_lookup" rel="list"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/lookups/my_sourcetype%20%3A%20LOOKUP-my_lookup" rel="edit"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/lookups/my_sourcetype%20%3A%20LOOKUP-my_lookup" rel="remove"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/lookups/my_sourcetype%20%3A%20LOOKUP-my_lookup/move" rel="move"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="attribute"&gt;LOOKUP-my_lookup&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:attributes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="optionalFields"&gt;
              &lt;s:list/&gt;
            &lt;/s:key&gt;
            &lt;s:key name="requiredFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;overwrite&lt;/s:item&gt;
                &lt;s:item&gt;transform&lt;/s:item&gt;
              &lt;/s:list&gt;
            &lt;/s:key&gt;
            &lt;s:key name="wildcardFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;lookup\.field\.input\..*&lt;/s:item&gt;
                &lt;s:item&gt;lookup\.field\.output\..*&lt;/s:item&gt;
              &lt;/s:list&gt;
            &lt;/s:key&gt;
          &lt;/s:dict&gt;
        &lt;/s:key&gt;
        &lt;s:key name="lookup.field.input.foo"/&gt;
        &lt;s:key name="lookup.field.output.fuzz"/&gt;
        &lt;s:key name="overwrite"&gt;1&lt;/s:key&gt;
        &lt;s:key name="stanza"&gt;my_sourcetype&lt;/s:key&gt;
        &lt;s:key name="transform"&gt;my_transform&lt;/s:key&gt;
        &lt;s:key name="type"&gt;LOOKUP&lt;/s:key&gt;
        &lt;s:key name="value"&gt;my_transform foo OUTPUT fuzz&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/props/lookups/{name}
{: name='datapropslookupsname'}

Modify the named automatic lookup.

	[POST] data/props/lookups/{name}

### Parameters

overwrite
: _Required_ **INHERITED** INHERITED

transform
: _Required_ **INHERITED** INHERITED

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Updated successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **402** | The Splunk license in use has disabled this feature. |
|--------------------------------
| **403** | Insufficient permissions to edit lookup. |
|--------------------------------
| **404** | Lookup does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Change the lookup and input/output fields for the recently created automatic lookup.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/servicesNS/admin/search/data/props/lookups/my_sourcetype%20%3A%20LOOKUP-my_lookup \
	-d overwrite=1 \
	-d transform=other_transform \
	-d lookup.field.input.bar= \
	-d lookup.field.output.buzz=
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;props-lookup&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/props/lookups&lt;/id&gt;
  &lt;updated&gt;2011-08-01T20:44:21-07:00&lt;/updated&gt;
  &lt;generator version="105049"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/data/props/lookups/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;my_sourcetype : LOOKUP-my_lookup&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/props/lookups/my_sourcetype%20%3A%20LOOKUP-my_lookup&lt;/id&gt;
    &lt;updated&gt;2011-08-01T20:44:21-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/data/props/lookups/my_sourcetype%20%3A%20LOOKUP-my_lookup" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/admin/search/data/props/lookups/my_sourcetype%20%3A%20LOOKUP-my_lookup" rel="list"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/lookups/my_sourcetype%20%3A%20LOOKUP-my_lookup" rel="edit"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/lookups/my_sourcetype%20%3A%20LOOKUP-my_lookup" rel="remove"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/lookups/my_sourcetype%20%3A%20LOOKUP-my_lookup/move" rel="move"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="attribute"&gt;LOOKUP-my_lookup&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="lookup.field.input.bar"/&gt;
        &lt;s:key name="lookup.field.output.buzz"/&gt;
        &lt;s:key name="overwrite"&gt;1&lt;/s:key&gt;
        &lt;s:key name="stanza"&gt;my_sourcetype&lt;/s:key&gt;
        &lt;s:key name="transform"&gt;other_transform&lt;/s:key&gt;
        &lt;s:key name="type"&gt;LOOKUP&lt;/s:key&gt;
        &lt;s:key name="value"&gt;other_transform bar OUTPUT buzz&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/props/sourcetype-rename
{: name='datapropssourcetyperename'}

List renamed sourcetypes.

	[GET] data/props/sourcetype-rename

### Parameters

count
: _Optional_ **Number** Maximum number of items to return.

offset
: _Optional_ **Number** Index for first item to return.

search
: _Optional_ **String** Boolean predicate to filter results.

sort_dir
: _Optional_ **Enum** Direction to sort by (asc/desc).

sort_key
: _Optional_ **String** Field to sort by.

sort_mode
: _Optional_ **Enum** Collating sequence for the sort (auto, alpha, alpha_case, num).

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view sourcetype renames. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Retrieve the list of renamed sourcetypes. The sourcetype, hardware, was renamed to "hw" in the POST operation to this endpoint.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/data/props/sourcetype-rename
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;sourcetype-rename&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/props/sourcetype-rename&lt;/id&gt;
  &lt;updated&gt;2011-07-12T15:40:53-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/data/props/sourcetype-rename/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;hardware&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/props/sourcetype-rename/hardware&lt;/id&gt;
    &lt;updated&gt;2011-07-12T15:40:53-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/data/props/sourcetype-rename/hardware" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/admin/search/data/props/sourcetype-rename/hardware" rel="list"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/sourcetype-rename/hardware" rel="edit"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/sourcetype-rename/hardware" rel="remove"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/sourcetype-rename/hardware/move" rel="move"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="attribute"&gt;rename&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="stanza"&gt;hardware&lt;/s:key&gt;
        &lt;s:key name="type"&gt;rename&lt;/s:key&gt;
        &lt;s:key name="value"&gt;hw&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/props/sourcetype-rename
{: name='datapropssourcetyperename'}

Rename a sourcetype.

	[POST] data/props/sourcetype-rename

### Parameters

name
: _Required_ **String** The original sourcetype name.

value
: _Required_ **String** The new sourcetype name.

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **201** | Created successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **402** | The Splunk license in use has disabled this feature. |
|--------------------------------
| **403** | Insufficient permissions to create a rename for a sourcetype. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Rename the sourcetype, hardware, to "hw."

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/data/props/sourcetype-rename \
	-d name=hardware \
	-d value=hw
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;sourcetype-rename&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/props/sourcetype-rename&lt;/id&gt;
  &lt;updated&gt;2011-07-12T15:39:57-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/data/props/sourcetype-rename/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;hardware&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/props/sourcetype-rename/hardware&lt;/id&gt;
    &lt;updated&gt;2011-07-12T15:39:57-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/data/props/sourcetype-rename/hardware" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/admin/search/data/props/sourcetype-rename/hardware" rel="list"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/sourcetype-rename/hardware" rel="edit"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/sourcetype-rename/hardware" rel="remove"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/sourcetype-rename/hardware/move" rel="move"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="attribute"&gt;rename&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="stanza"&gt;hardware&lt;/s:key&gt;
        &lt;s:key name="type"&gt;rename&lt;/s:key&gt;
        &lt;s:key name="value"&gt;hw&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/props/sourcetype-rename/{name}
{: name='datapropssourcetyperenamename'}

Restore a sourcetype's original name.

	[DELETE] data/props/sourcetype-rename/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deleted successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to delete the rename for the sourcetype. |
|--------------------------------
| **404** | Rename for the sourcetype does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Restore the sourcetype hardware to its original name.

#### Request
<pre class='terminal'>
curl -k -u admin:pass --request DELETE \
	https://localhost:8089/servicesNS/admin/search/data/props/sourcetype-rename/hardware
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;sourcetype-rename&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/props/sourcetype-rename&lt;/id&gt;
  &lt;updated&gt;2011-07-12T15:49:16-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/data/props/sourcetype-rename/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## data/props/sourcetype-rename/{name}
{: name='datapropssourcetyperenamename'}

List a single renamed sourcetype.

	[GET] data/props/sourcetype-rename/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view renames for sourcetypes. |
|--------------------------------
| **404** | Rename for sourcetype does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

List the new name for the sourcetype, hardware.
This sourcetype was renamed to "hw" in the POST operation to this endpoint.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/servicesNS/admin/search/data/props/sourcetype-rename/hardware
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;sourcetype-rename&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/props/sourcetype-rename&lt;/id&gt;
  &lt;updated&gt;2011-07-12T15:44:47-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/data/props/sourcetype-rename/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;hardware&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/props/sourcetype-rename/hardware&lt;/id&gt;
    &lt;updated&gt;2011-07-12T15:44:47-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/data/props/sourcetype-rename/hardware" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/admin/search/data/props/sourcetype-rename/hardware" rel="list"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/sourcetype-rename/hardware" rel="edit"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/sourcetype-rename/hardware" rel="remove"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/sourcetype-rename/hardware/move" rel="move"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="attribute"&gt;rename&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:attributes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="optionalFields"&gt;
              &lt;s:list/&gt;
            &lt;/s:key&gt;
            &lt;s:key name="requiredFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;value&lt;/s:item&gt;
              &lt;/s:list&gt;
            &lt;/s:key&gt;
            &lt;s:key name="wildcardFields"&gt;
              &lt;s:list/&gt;
            &lt;/s:key&gt;
          &lt;/s:dict&gt;
        &lt;/s:key&gt;
        &lt;s:key name="stanza"&gt;hardware&lt;/s:key&gt;
        &lt;s:key name="type"&gt;rename&lt;/s:key&gt;
        &lt;s:key name="value"&gt;hw&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/props/sourcetype-rename/{name}
{: name='datapropssourcetyperenamename'}

Rename a sourcetype again, i.e. modify a sourcetype's new name.

	[POST] data/props/sourcetype-rename/{name}

### Parameters

value
: _Required_ **INHERITED** INHERITED

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Updated successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **402** | The Splunk license in use has disabled this feature. |
|--------------------------------
| **403** | Insufficient permissions to edit renames for the sourcetype. |
|--------------------------------
| **404** | Rename for the sourcetype does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Rename the sourcetype hardware again, this time to hrdwr.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/servicesNS/admin/search/data/props/sourcetype-rename/hardware \
	-d value=hrdwr
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;sourcetype-rename&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/props/sourcetype-rename&lt;/id&gt;
  &lt;updated&gt;2011-07-12T15:46:58-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/data/props/sourcetype-rename/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;hardware&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/props/sourcetype-rename/hardware&lt;/id&gt;
    &lt;updated&gt;2011-07-12T15:46:58-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/data/props/sourcetype-rename/hardware" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/admin/search/data/props/sourcetype-rename/hardware" rel="list"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/sourcetype-rename/hardware" rel="edit"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/sourcetype-rename/hardware" rel="remove"/&gt;
    &lt;link href="/servicesNS/admin/search/data/props/sourcetype-rename/hardware/move" rel="move"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="attribute"&gt;rename&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="stanza"&gt;hardware&lt;/s:key&gt;
        &lt;s:key name="type"&gt;rename&lt;/s:key&gt;
        &lt;s:key name="value"&gt;hrdwr&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/transforms/extractions
{: name='datatransformsextractions'}

List field transformations.

	[GET] data/transforms/extractions

### Parameters

count
: _Optional_ **Number** Maximum number of items to return.

offset
: _Optional_ **Number** Index for first item to return.

search
: _Optional_ **String** Boolean predicate to filter results.

sort_dir
: _Optional_ **Enum** Direction to sort by (asc/desc).

sort_key
: _Optional_ **String** Field to sort by.

sort_mode
: _Optional_ **Enum** Collating sequence for the sort (auto, alpha, alpha_case, num).

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view field transformations. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Retrieve the list of field transformations.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/data/transforms/extractions
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;transforms-extract&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/transforms/extractions&lt;/id&gt;
  &lt;updated&gt;2011-07-21T20:28:03-07:00&lt;/updated&gt;
  &lt;generator version="104309"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/data/transforms/extractions/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/admin/search/data/transforms/extractions/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;access-extractions&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/data/transforms/extractions/access-extractions&lt;/id&gt;
    &lt;updated&gt;2011-07-21T20:28:03-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/data/transforms/extractions/access-extractions" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/data/transforms/extractions/access-extractions" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/transforms/extractions/access-extractions/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/transforms/extractions/access-extractions" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/transforms/extractions/access-extractions/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="CAN_OPTIMIZE"&gt;1&lt;/s:key&gt;
        &lt;s:key name="CLEAN_KEYS"&gt;1&lt;/s:key&gt;
        &lt;s:key name="DEFAULT_VALUE"/&gt;
        &lt;s:key name="DEST_KEY"/&gt;
        &lt;s:key name="FORMAT"/&gt;
        &lt;s:key name="KEEP_EMPTY_VALS"&gt;0&lt;/s:key&gt;
        &lt;s:key name="LOOKAHEAD"&gt;4096&lt;/s:key&gt;
        &lt;s:key name="MV_ADD"&gt;0&lt;/s:key&gt;
        &lt;s:key name="REGEX"&gt;
&lt;![CDATA[^&amp;#91;&amp;#91;nspaces:clientip&amp;#93;&amp;#93;\s++&amp;#91;&amp;#91;nspaces:ident&amp;#93;&amp;#93;\s++&amp;#91;&amp;#91;nspaces:user&amp;#93;&amp;#93;\s++&amp;#91;&amp;#91;sbstring:req_time&amp;#93;&amp;#93;\s++&amp;#91;&amp;#91;access-request&amp;#93;&amp;#93;\s++&amp;#91;&amp;#91;nspaces:status&amp;#93;&amp;#93;\s++&amp;#91;&amp;#91;nspaces:bytes&amp;#93;&amp;#93;(?:\s++"(?&lt;referer&gt;&amp;#91;&amp;#91;bc_domain:referer_&amp;#93;&amp;#93;?+[^"]*+)"(?:\s++&amp;#91;&amp;#91;qstring:useragent&amp;#93;&amp;#93;(?:\s++&amp;#91;&amp;#91;qstring:cookie&amp;#93;&amp;#93;)?+)?+)?&amp;#91;&amp;#91;all:other&amp;#93;&amp;#93;&amp;#93;&amp;#93;&gt;        &lt;/s:key&gt;
        &lt;s:key name="SOURCE_KEY"&gt;_raw&lt;/s:key&gt;
        &lt;s:key name="WRITE_META"&gt;0&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:appName"&gt;search&lt;/s:key&gt;
        &lt;s:key name="eai:userName"&gt;admin&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/transforms/extractions
{: name='datatransformsextractions'}

Create a new field transformation.

	[POST] data/transforms/extractions

### Parameters

CAN_OPTIMIZE
: _Optional_ **Bool** Controls whether Splunk can optimize this extraction out (another way of saying the extraction is disabled).  You might use this when you have field discovery turned off--it ensures that certain fields are *always* discovered.  Splunk only disables an extraction if it can determine that none of the fields identified by the extraction will ever be needed for the successful evaluation of a search.<br/><br/>NOTE: This option should rarely be set to false.

CLEAN_KEYS
: _Optional_ **Boolean** If set to true, Splunk "cleans" the field names extracted at search time by replacing non-alphanumeric characters with underscores and stripping leading underscores.

FORMAT
: _Optional_ **String** This option is valid for both index-time and search-time field extractions. However, FORMAT behaves differently depending on whether the extraction is performed at index time or search time.<br/><br/>This attribute specifies the format of the event, including any field names or values you want to add.<br/><br/>FORMAT for index-time extractions:<br/><br/>Use $n (for example $1, $2, etc) to specify the output of each REGEX match.<br/><br/>If REGEX does not have n groups, the matching fails.<br/><br/>The special identifier $0 represents what was in the DEST_KEY before the REGEX was performed.<br/><br/>At index-time only, you can use FORMAT to create concatenated fields: FORMAT = ipaddress::$1.$2.$3.$4<br/><br/>When you create concatenated fields with FORMAT, "$" is the only special character. It is treated as a prefix for regex-capturing groups only if it is followed by a number and only if the number applies to an existing capturing group. So if REGEX has only one capturing group and its value is "bar", then:
\t"FORMAT = foo$1" yields "foobar"
\t"FORMAT = foo$bar" yields "foo$bar"
\t"FORMAT = foo$1234" yields "foo$1234"
\t"FORMAT = foo$1\\$2" yields "foobar\\$2"<br/><br/>At index-time, FORMAT defaults to <stanza-name>::$1<br/><br/>FORMAT for search-time extractions:<br/><br/>The format of this field as used during search time extractions is as follows:
\tFORMAT = <field-name>::<field-value>( <field-name>::<field-value>)*
\tfield-name  = [<string>|$<extracting-group-number>]
\tfield-value = [<string>|$<extracting-group-number>]<br/><br/>Search-time extraction examples:
\tFORMAT = first::$1 second::$2 third::other-value
\tFORMAT = $1::$2<br/><br/>You cannot create concatenated fields with FORMAT at search time. That functionality is only available at index time.<br/><br/>At search-time, FORMAT defaults to an empty string.

KEEP_EMPTY_VALS
: _Optional_ **Boolean** If set to true, Splunk preserves extracted fields with empty values.

MV_ADD
: _Optional_ **Boolean** If Splunk extracts a field that already exists and MV_ADD is set to true, the field becomes multivalued, and the newly-extracted value is appended. If MV_ADD is set to false, the newly-extracted value is discarded.

REGEX
: _Required_ **String** Specify a regular expression to operate on your data.<br/><br/>This attribute is valid for both index-time and search-time field extractions:
\tREGEX is required for all search-time transforms unless you are setting up a delimiter-based field extraction, in which case you use DELIMS (see the DELIMS attribute description, below).
\tREGEX is required for all index-time transforms.<br/><br/>REGEX and the FORMAT attribute:<br/><br/>Name-capturing groups in the REGEX are extracted directly to fields. This means that you do not need to specify the FORMAT attribute for simple field extraction cases.<br/><br/>If the REGEX extracts both the field name and its corresponding field value, you can use the following special capturing groups if you want to skip specifying the mapping in FORMAT: _KEY_<string>, _VAL_<string>.<br/><br/>For example, the following are equivalent:
\tUsing FORMAT:
\t\tREGEX  = ([a-z]+)=([a-z]+)
\t\tFORMAT = $1::$2
\tWithout using FORMAT
\t\tREGEX  = (?<_KEY_1>[a-z]+)=(?<_VAL_1>[a-z]+)<br/><br/>REGEX defaults to an empty string.

SOURCE_KEY
: _Required_ **String** Specify the KEY to which Splunk applies REGEX.

disabled
: _Optional_ **Boolean** Specifies whether the field transformation is disabled.

name
: _Required_ **String** The name of the field transformation.

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **201** | Created successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **402** | The Splunk license in use has disabled this feature. |
|--------------------------------
| **403** | Insufficient permissions to create field transformation. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Create a new field transformation.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/data/transforms/extractions \
	-d REGEX="(?&lt;_KEY_1&gt;[a-z]*),(?&lt;_VAL_1&gt;[a-z]*)" \
	-d SOURCE_KEY=_raw \
	-d name=my_transform
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;transforms-extract&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/transforms/extractions&lt;/id&gt;
  &lt;updated&gt;2011-07-21T20:25:20-07:00&lt;/updated&gt;
  &lt;generator version="104309"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/data/transforms/extractions/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/admin/search/data/transforms/extractions/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;my_transform&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/transforms/extractions/my_transform&lt;/id&gt;
    &lt;updated&gt;2011-07-21T20:25:20-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/extractions/my_transform" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/extractions/my_transform" rel="list"/&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/extractions/my_transform/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/extractions/my_transform" rel="edit"/&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/extractions/my_transform" rel="remove"/&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/extractions/my_transform/move" rel="move"/&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/extractions/my_transform/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="CAN_OPTIMIZE"&gt;1&lt;/s:key&gt;
        &lt;s:key name="CLEAN_KEYS"&gt;1&lt;/s:key&gt;
        &lt;s:key name="DEFAULT_VALUE"/&gt;
        &lt;s:key name="DEST_KEY"/&gt;
        &lt;s:key name="FORMAT"/&gt;
        &lt;s:key name="KEEP_EMPTY_VALS"&gt;0&lt;/s:key&gt;
        &lt;s:key name="LOOKAHEAD"&gt;4096&lt;/s:key&gt;
        &lt;s:key name="MV_ADD"&gt;0&lt;/s:key&gt;
        &lt;s:key name="REGEX"&gt;(?&amp;lt;_KEY_1&amp;gt;[a-z]*),(?&amp;lt;_VAL_1&amp;gt;[a-z]*)&lt;/s:key&gt;
        &lt;s:key name="SOURCE_KEY"&gt;_raw&lt;/s:key&gt;
        &lt;s:key name="WRITE_META"&gt;0&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:appName"&gt;search&lt;/s:key&gt;
        &lt;s:key name="eai:userName"&gt;admin&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/transforms/extractions/{name}
{: name='datatransformsextractionsname'}

Delete the named field transformation.

	[DELETE] data/transforms/extractions/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deleted successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to delete named field transformation. |
|--------------------------------
| **404** | Named field transformation does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Remove the newly created field transformation.

#### Request
<pre class='terminal'>
curl -k -u admin:pass --request DELETE \
	https://localhost:8089/servicesNS/admin/search/data/transforms/extractions/my_transform
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;transforms-extract&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/transforms/extractions&lt;/id&gt;
  &lt;updated&gt;2011-07-21T20:34:30-07:00&lt;/updated&gt;
  &lt;generator version="104309"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/data/transforms/extractions/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/admin/search/data/transforms/extractions/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## data/transforms/extractions/{name}
{: name='datatransformsextractionsname'}

List a single field transformation.

	[GET] data/transforms/extractions/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view named field transformation. |
|--------------------------------
| **404** | Named field transformation does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Retrieve the newly created field transformation.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/servicesNS/admin/search/data/transforms/extractions/my_transform
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;transforms-extract&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/transforms/extractions&lt;/id&gt;
  &lt;updated&gt;2011-07-21T20:29:00-07:00&lt;/updated&gt;
  &lt;generator version="104309"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/data/transforms/extractions/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/admin/search/data/transforms/extractions/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;my_transform&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/transforms/extractions/my_transform&lt;/id&gt;
    &lt;updated&gt;2011-07-21T20:29:00-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/extractions/my_transform" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/extractions/my_transform" rel="list"/&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/extractions/my_transform/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/extractions/my_transform" rel="edit"/&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/extractions/my_transform" rel="remove"/&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/extractions/my_transform/move" rel="move"/&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/extractions/my_transform/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="CAN_OPTIMIZE"&gt;1&lt;/s:key&gt;
        &lt;s:key name="CLEAN_KEYS"&gt;1&lt;/s:key&gt;
        &lt;s:key name="DEFAULT_VALUE"/&gt;
        &lt;s:key name="DEST_KEY"/&gt;
        &lt;s:key name="FORMAT"/&gt;
        &lt;s:key name="KEEP_EMPTY_VALS"&gt;0&lt;/s:key&gt;
        &lt;s:key name="LOOKAHEAD"&gt;4096&lt;/s:key&gt;
        &lt;s:key name="MV_ADD"&gt;0&lt;/s:key&gt;
        &lt;s:key name="REGEX"&gt;(?&amp;lt;_KEY_1&amp;gt;[a-z]*),(?&amp;lt;_VAL_1&amp;gt;[a-z]*)&lt;/s:key&gt;
        &lt;s:key name="SOURCE_KEY"&gt;_raw&lt;/s:key&gt;
        &lt;s:key name="WRITE_META"&gt;0&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:appName"&gt;search&lt;/s:key&gt;
        &lt;s:key name="eai:attributes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="optionalFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;CAN_OPTIMIZE&lt;/s:item&gt;
                &lt;s:item&gt;CLEAN_KEYS&lt;/s:item&gt;
                &lt;s:item&gt;FORMAT&lt;/s:item&gt;
                &lt;s:item&gt;KEEP_EMPTY_VALS&lt;/s:item&gt;
                &lt;s:item&gt;MV_ADD&lt;/s:item&gt;
                &lt;s:item&gt;disabled&lt;/s:item&gt;
              &lt;/s:list&gt;
            &lt;/s:key&gt;
            &lt;s:key name="requiredFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;REGEX&lt;/s:item&gt;
                &lt;s:item&gt;SOURCE_KEY&lt;/s:item&gt;
              &lt;/s:list&gt;
            &lt;/s:key&gt;
            &lt;s:key name="wildcardFields"&gt;
              &lt;s:list/&gt;
            &lt;/s:key&gt;
          &lt;/s:dict&gt;
        &lt;/s:key&gt;
        &lt;s:key name="eai:userName"&gt;admin&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/transforms/extractions/{name}
{: name='datatransformsextractionsname'}

Modify the named field transformation.

	[POST] data/transforms/extractions/{name}

### Parameters

CAN_OPTIMIZE
: _Optional_ **INHERITED** INHERITED

CLEAN_KEYS
: _Optional_ **INHERITED** INHERITED

FORMAT
: _Optional_ **INHERITED** INHERITED

KEEP_EMPTY_VALS
: _Optional_ **INHERITED** INHERITED

MV_ADD
: _Optional_ **INHERITED** INHERITED

REGEX
: _Required_ **INHERITED** INHERITED

SOURCE_KEY
: _Required_ **INHERITED** INHERITED

disabled
: _Optional_ **INHERITED** INHERITED

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Updated successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **402** | The Splunk license in use has disabled this feature. |
|--------------------------------
| **403** | Insufficient permissions to edit named field transformation. |
|--------------------------------
| **404** | Named field transformation does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Disable key cleaning on the newly created field transformation.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/servicesNS/admin/search/data/transforms/extractions/my_transform \
	-d REGEX="(?&lt;_KEY_1&gt;[a-z]*),(?&lt;_VAL_1&gt;[a-z]*)" \
	-d SOURCE_KEY=_raw \
	-d CLEAN_KEYS=false
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;transforms-extract&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/transforms/extractions&lt;/id&gt;
  &lt;updated&gt;2011-07-21T20:33:13-07:00&lt;/updated&gt;
  &lt;generator version="104309"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/data/transforms/extractions/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/admin/search/data/transforms/extractions/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;my_transform&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/transforms/extractions/my_transform&lt;/id&gt;
    &lt;updated&gt;2011-07-21T20:33:13-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/extractions/my_transform" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/extractions/my_transform" rel="list"/&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/extractions/my_transform/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/extractions/my_transform" rel="edit"/&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/extractions/my_transform" rel="remove"/&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/extractions/my_transform/move" rel="move"/&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/extractions/my_transform/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="CAN_OPTIMIZE"&gt;1&lt;/s:key&gt;
        &lt;s:key name="CLEAN_KEYS"&gt;0&lt;/s:key&gt;
        &lt;s:key name="DEFAULT_VALUE"/&gt;
        &lt;s:key name="DEST_KEY"/&gt;
        &lt;s:key name="FORMAT"/&gt;
        &lt;s:key name="KEEP_EMPTY_VALS"&gt;0&lt;/s:key&gt;
        &lt;s:key name="LOOKAHEAD"&gt;4096&lt;/s:key&gt;
        &lt;s:key name="MV_ADD"&gt;0&lt;/s:key&gt;
        &lt;s:key name="REGEX"&gt;(?&amp;lt;_KEY_1&amp;gt;[a-z]*),(?&amp;lt;_VAL_1&amp;gt;[a-z]*)&lt;/s:key&gt;
        &lt;s:key name="SOURCE_KEY"&gt;_raw&lt;/s:key&gt;
        &lt;s:key name="WRITE_META"&gt;0&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:appName"&gt;search&lt;/s:key&gt;
        &lt;s:key name="eai:userName"&gt;admin&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/transforms/lookups
{: name='datatransformslookups'}

List lookup definitions.

	[GET] data/transforms/lookups

### Parameters

count
: _Optional_ **Number** Maximum number of items to return.

offset
: _Optional_ **Number** Index for first item to return.

search
: _Optional_ **String** Boolean predicate to filter results.

sort_dir
: _Optional_ **Enum** Direction to sort by (asc/desc).

sort_key
: _Optional_ **String** Field to sort by.

sort_mode
: _Optional_ **Enum** Collating sequence for the sort (auto, alpha, alpha_case, num).

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view lookups. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Retrieve the list of lookup definitions.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/data/transforms/lookups
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;transforms-lookup&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/transforms/lookups&lt;/id&gt;
  &lt;updated&gt;2011-08-01T21:10:44-07:00&lt;/updated&gt;
  &lt;generator version="105049"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/data/transforms/lookups/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/admin/search/data/transforms/lookups/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;dnslookup&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/data/transforms/lookups/dnslookup&lt;/id&gt;
    &lt;updated&gt;2011-08-01T21:10:44-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/data/transforms/lookups/dnslookup" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/data/transforms/lookups/dnslookup" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/transforms/lookups/dnslookup/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/transforms/lookups/dnslookup" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/transforms/lookups/dnslookup/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="CAN_OPTIMIZE"&gt;1&lt;/s:key&gt;
        &lt;s:key name="CLEAN_KEYS"&gt;1&lt;/s:key&gt;
        &lt;s:key name="DEFAULT_VALUE"/&gt;
        &lt;s:key name="DEST_KEY"/&gt;
        &lt;s:key name="FORMAT"/&gt;
        &lt;s:key name="KEEP_EMPTY_VALS"&gt;0&lt;/s:key&gt;
        &lt;s:key name="LOOKAHEAD"&gt;4096&lt;/s:key&gt;
        &lt;s:key name="MV_ADD"&gt;0&lt;/s:key&gt;
        &lt;s:key name="REGEX"/&gt;
        &lt;s:key name="SOURCE_KEY"&gt;_raw&lt;/s:key&gt;
        &lt;s:key name="WRITE_META"&gt;0&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:appName"&gt;search&lt;/s:key&gt;
        &lt;s:key name="eai:userName"&gt;admin&lt;/s:key&gt;
        &lt;s:key name="external_cmd"&gt;external_lookup.py clienthost clientip&lt;/s:key&gt;
        &lt;s:key name="fields_list"&gt;clienthost clientip&lt;/s:key&gt;
        &lt;s:key name="type"&gt;external&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/transforms/lookups
{: name='datatransformslookups'}

Create a new lookup definition.

	[POST] data/transforms/lookups

### Parameters

default_match
: _Optional_ **String** If min_matches is greater than zero and Splunk has less than min_matches for any given input, it provides this default_match value one or more times until the min_matches threshold is reached.

disabled
: _Optional_ **Boolean** Specifies whether the lookup definition is disabled.

external_cmd
: _Optional_ **String** Provides the command and arguments to invoke to perform a lookup. Use this for external (or "scripted") lookups, where you interface with with an external script rather than a lookup table.

fields_list
: _Optional_ **String** A comma- and space-delimited list of all fields that are supported by the external command. Use this for external (or "scripted") lookups.

filename
: _Optional_ **String** The name of the static lookup table file.

max_matches
: _Optional_ **Number** The maximum number of possible matches for each input lookup value.

max_offset_secs
: _Optional_ **Number** For temporal lookups, this is the maximum time (in seconds) that the event timestamp can be later than the lookup entry time for a match to occur.

min_matches
: _Optional_ **Number** The minimum number of possible matches for each input lookup value.

min_offset_secs
: _Optional_ **Number** For temporal lookups, this is the minimum time (in seconds) that the event timestamp can be later than the lookup entry timestamp for a match to occur.

name
: _Required_ **String** The name of the lookup definition.

time_field
: _Optional_ **String** For temporal lookups, this is the field in the lookup table that represents the timestamp.

time_format
: _Optional_ **String** For temporal lookups, this specifies the "strptime" format of the timestamp field.

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **201** | Created successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **402** | The Splunk license in use has disabled this feature. |
|--------------------------------
| **403** | Insufficient permissions to create lookup. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Create a new file-based lookup associated with lookup.csv.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/data/transforms/lookups \
	-d name=my_lookup \
	-d filename=lookup.csv
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;transforms-lookup&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/transforms/lookups&lt;/id&gt;
  &lt;updated&gt;2011-08-01T21:10:33-07:00&lt;/updated&gt;
  &lt;generator version="105049"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/data/transforms/lookups/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/admin/search/data/transforms/lookups/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;my_lookup&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/transforms/lookups/my_lookup&lt;/id&gt;
    &lt;updated&gt;2011-08-01T21:10:33-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/lookups/my_lookup" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/lookups/my_lookup" rel="list"/&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/lookups/my_lookup/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/lookups/my_lookup" rel="edit"/&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/lookups/my_lookup" rel="remove"/&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/lookups/my_lookup/move" rel="move"/&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/lookups/my_lookup/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="CAN_OPTIMIZE"&gt;1&lt;/s:key&gt;
        &lt;s:key name="CLEAN_KEYS"&gt;1&lt;/s:key&gt;
        &lt;s:key name="DEFAULT_VALUE"/&gt;
        &lt;s:key name="DEST_KEY"/&gt;
        &lt;s:key name="FORMAT"/&gt;
        &lt;s:key name="KEEP_EMPTY_VALS"&gt;0&lt;/s:key&gt;
        &lt;s:key name="LOOKAHEAD"&gt;4096&lt;/s:key&gt;
        &lt;s:key name="MV_ADD"&gt;0&lt;/s:key&gt;
        &lt;s:key name="REGEX"/&gt;
        &lt;s:key name="SOURCE_KEY"&gt;_raw&lt;/s:key&gt;
        &lt;s:key name="WRITE_META"&gt;0&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:appName"&gt;search&lt;/s:key&gt;
        &lt;s:key name="eai:userName"&gt;admin&lt;/s:key&gt;
        &lt;s:key name="filename"&gt;lookup.csv&lt;/s:key&gt;
        &lt;s:key name="type"&gt;file&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/transforms/lookups/{name}
{: name='datatransformslookupsname'}

Delete the named lookup definition.

	[DELETE] data/transforms/lookups/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deleted successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to delete named lookup. |
|--------------------------------
| **404** | Named lookup does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Remove the newly created lookup definition.

#### Request
<pre class='terminal'>
curl -k -u admin:pass --request DELETE \
	https://localhost:8089/servicesNS/admin/search/data/transforms/lookups/my_lookup
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;transforms-lookup&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/transforms/lookups&lt;/id&gt;
  &lt;updated&gt;2011-07-21T20:03:24-07:00&lt;/updated&gt;
  &lt;generator version="104309"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/data/transforms/lookups/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/admin/search/data/transforms/lookups/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## data/transforms/lookups/{name}
{: name='datatransformslookupsname'}

List a single lookup definition.

	[GET] data/transforms/lookups/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view named lookup. |
|--------------------------------
| **404** | Named lookup does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Retrieve the newly created lookup definition.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/servicesNS/admin/search/data/transforms/lookups/my_lookup
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;transforms-lookup&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/transforms/lookups&lt;/id&gt;
  &lt;updated&gt;2011-08-01T21:11:01-07:00&lt;/updated&gt;
  &lt;generator version="105049"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/data/transforms/lookups/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/admin/search/data/transforms/lookups/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;my_lookup&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/transforms/lookups/my_lookup&lt;/id&gt;
    &lt;updated&gt;2011-08-01T21:11:01-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/lookups/my_lookup" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/lookups/my_lookup" rel="list"/&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/lookups/my_lookup/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/lookups/my_lookup" rel="edit"/&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/lookups/my_lookup" rel="remove"/&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/lookups/my_lookup/move" rel="move"/&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/lookups/my_lookup/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="CAN_OPTIMIZE"&gt;1&lt;/s:key&gt;
        &lt;s:key name="CLEAN_KEYS"&gt;1&lt;/s:key&gt;
        &lt;s:key name="DEFAULT_VALUE"/&gt;
        &lt;s:key name="DEST_KEY"/&gt;
        &lt;s:key name="FORMAT"/&gt;
        &lt;s:key name="KEEP_EMPTY_VALS"&gt;0&lt;/s:key&gt;
        &lt;s:key name="LOOKAHEAD"&gt;4096&lt;/s:key&gt;
        &lt;s:key name="MV_ADD"&gt;0&lt;/s:key&gt;
        &lt;s:key name="REGEX"/&gt;
        &lt;s:key name="SOURCE_KEY"&gt;_raw&lt;/s:key&gt;
        &lt;s:key name="WRITE_META"&gt;0&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:appName"&gt;search&lt;/s:key&gt;
        &lt;s:key name="eai:attributes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="optionalFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;default_match&lt;/s:item&gt;
                &lt;s:item&gt;disabled&lt;/s:item&gt;
                &lt;s:item&gt;external_cmd&lt;/s:item&gt;
                &lt;s:item&gt;fields_list&lt;/s:item&gt;
                &lt;s:item&gt;filename&lt;/s:item&gt;
                &lt;s:item&gt;max_matches&lt;/s:item&gt;
                &lt;s:item&gt;max_offset_secs&lt;/s:item&gt;
                &lt;s:item&gt;min_matches&lt;/s:item&gt;
                &lt;s:item&gt;min_offset_secs&lt;/s:item&gt;
                &lt;s:item&gt;time_field&lt;/s:item&gt;
                &lt;s:item&gt;time_format&lt;/s:item&gt;
              &lt;/s:list&gt;
            &lt;/s:key&gt;
            &lt;s:key name="requiredFields"&gt;
              &lt;s:list/&gt;
            &lt;/s:key&gt;
            &lt;s:key name="wildcardFields"&gt;
              &lt;s:list/&gt;
            &lt;/s:key&gt;
          &lt;/s:dict&gt;
        &lt;/s:key&gt;
        &lt;s:key name="eai:userName"&gt;admin&lt;/s:key&gt;
        &lt;s:key name="filename"&gt;lookup.csv&lt;/s:key&gt;
        &lt;s:key name="type"&gt;file&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/transforms/lookups/{name}
{: name='datatransformslookupsname'}

Modify the named lookup definition.

	[POST] data/transforms/lookups/{name}

### Parameters

default_match
: _Optional_ **INHERITED** INHERITED

disabled
: _Optional_ **INHERITED** INHERITED

external_cmd
: _Optional_ **INHERITED** INHERITED

fields_list
: _Optional_ **INHERITED** INHERITED

filename
: _Optional_ **INHERITED** INHERITED

max_matches
: _Optional_ **INHERITED** INHERITED

max_offset_secs
: _Optional_ **INHERITED** INHERITED

min_matches
: _Optional_ **INHERITED** INHERITED

min_offset_secs
: _Optional_ **INHERITED** INHERITED

time_field
: _Optional_ **INHERITED** INHERITED

time_format
: _Optional_ **INHERITED** INHERITED

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Updated successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **402** | The Splunk license in use has disabled this feature. |
|--------------------------------
| **403** | Insufficient permissions to edit named lookup. |
|--------------------------------
| **404** | Named lookup does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Change the newly created lookup to be based on a script instead of a lookup table file.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/servicesNS/admin/search/data/transforms/lookups/my_lookup \
	-d external_cmd=myscript.py \
	-d fields_list=a,b,c
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;transforms-lookup&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/transforms/lookups&lt;/id&gt;
  &lt;updated&gt;2011-07-21T20:00:07-07:00&lt;/updated&gt;
  &lt;generator version="104309"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/data/transforms/lookups/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/admin/search/data/transforms/lookups/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;my_lookup&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/transforms/lookups/my_lookup&lt;/id&gt;
    &lt;updated&gt;2011-07-21T20:00:07-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/lookups/my_lookup" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/lookups/my_lookup" rel="list"/&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/lookups/my_lookup/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/lookups/my_lookup" rel="edit"/&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/lookups/my_lookup" rel="remove"/&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/lookups/my_lookup/move" rel="move"/&gt;
    &lt;link href="/servicesNS/admin/search/data/transforms/lookups/my_lookup/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="CAN_OPTIMIZE"&gt;1&lt;/s:key&gt;
        &lt;s:key name="CLEAN_KEYS"&gt;1&lt;/s:key&gt;
        &lt;s:key name="DEFAULT_VALUE"/&gt;
        &lt;s:key name="DEST_KEY"/&gt;
        &lt;s:key name="FORMAT"/&gt;
        &lt;s:key name="KEEP_EMPTY_VALS"&gt;0&lt;/s:key&gt;
        &lt;s:key name="LOOKAHEAD"&gt;4096&lt;/s:key&gt;
        &lt;s:key name="MV_ADD"&gt;0&lt;/s:key&gt;
        &lt;s:key name="REGEX"/&gt;
        &lt;s:key name="SOURCE_KEY"&gt;_raw&lt;/s:key&gt;
        &lt;s:key name="WRITE_META"&gt;0&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:appName"&gt;search&lt;/s:key&gt;
        &lt;s:key name="eai:userName"&gt;admin&lt;/s:key&gt;
        &lt;s:key name="external_cmd"&gt;myscript.py&lt;/s:key&gt;
        &lt;s:key name="fields_list"&gt;a,b,c&lt;/s:key&gt;
        &lt;s:key name="type"&gt;external&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## directory
{: name='directory'}

Provides an enumeration of the following app scoped objects:

* event types
* saved searches
* time configurations
* views
* navs
* manager XML
* quickstart XML
* search commands
* macros
* tags
* field extractions
* lookups
* workflow actions
* field aliases
* sourcetype renames

This is useful to see which apps provide which objects, or all the objects provided by a specific app. To change the visibility of an object type in this listing, use the showInDirSvc in <code>restmap.conf</code>.

	[GET] directory

### Parameters

count
: _Optional_ **Number** Maximum number of items to return.

offset
: _Optional_ **Number** Index for first item to return.

search
: _Optional_ **String** Boolean predicate to filter results.

sort_dir
: _Optional_ **Enum** Direction to sort by (asc/desc).

sort_key
: _Optional_ **String** Field to sort by.

sort_mode
: _Optional_ **Enum** Collating sequence for the sort (auto, alpha, alpha_case, num).

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view user configurable objects. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Lists a variety of configuration object types visible to the admin user in the context of the search app.  Note that this includes objects that belong to other users or apps, but are exported into this context.
Most results in this example have been elided for brevity.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/directory
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom" 
  xmlns:s="http://dev.splunk.com/ns/rest" 
  xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;directory&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/directory&lt;/id&gt;
  &lt;updated&gt;2011-05-16T19:03:40-0700&lt;/updated&gt;
  &lt;generator version="98144"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;_admin&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/data/ui/views/_admin&lt;/id&gt;
    &lt;updated&gt;2011-05-16T19:03:40-0700&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/data/ui/views/_admin" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/data/ui/views/_admin" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/ui/views/_admin/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/ui/views/_admin" rel="edit"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:type"&gt;views&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;abc&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/ui/views/abc&lt;/id&gt;
    &lt;updated&gt;2011-05-16T19:03:40-0700&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/search/data/ui/views/abc" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;ssorkin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/search/data/ui/views/abc" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/ui/views/abc/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/ui/views/abc" rel="edit"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:type"&gt;views&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## directory/{name}
{: name='directoryname'}

Displays information about a single entity in the directory service enumeration.

This is rarely used. Typically after using the directory service enumeration, a client follows the specific link for an object in an enumeration.

	[GET] directory/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view the user configurable object. |
|--------------------------------
| **404** | User configurable object does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

This example displays information about a single enitity in the directory service enumeration.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/directory/dashboard_live
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:s="http://dev.splunk.com/ns/rest"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;directory&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/directory&lt;/id&gt;
  &lt;updated&gt;2011-05-16T19:09:59-0700&lt;/updated&gt;
  &lt;generator version="98144"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;dashboard_live&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/ui/views/dashboard_live&lt;/id&gt;
    &lt;updated&gt;2011-05-16T19:09:59-0700&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/search/data/ui/views/dashboard_live" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/search/data/ui/views/dashboard_live" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/ui/views/dashboard_live/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/ui/views/dashboard_live" rel="edit"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:attributes"&gt;
            &lt;s:dict&gt;
                &lt;s:key name="optionalFields"&gt;
                    &lt;s:list/&gt;
                &lt;/s:key&gt;
                &lt;s:key name="requiredFields"&gt;
                    &lt;s:list/&gt;
                &lt;/s:key&gt;
                &lt;s:key name="wildcardFields"&gt;
                    &lt;s:list/&gt;
                &lt;/s:key&gt;
            &lt;/s:dict&gt;
        &lt;/s:key&gt;
        &lt;s:key name="eai:type"&gt;views&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## saved/eventtypes
{: name='savedeventtypes'}

Retrieve saved event types.

	[GET] saved/eventtypes

### Parameters

count
: _Optional_ **Number** Maximum number of items to return.

offset
: _Optional_ **Number** Index for first item to return.

search
: _Optional_ **String** Boolean predicate to filter results.

sort_dir
: _Optional_ **Enum** Direction to sort by (asc/desc).

sort_key
: _Optional_ **String** Field to sort by.

sort_mode
: _Optional_ **Enum** Collating sequence for the sort (auto, alpha, alpha_case, num).

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view event types. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Lists all saved event types accessible to the admin user in the search app.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/saved/eventtypes
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;eventtypes&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/saved/eventtypes&lt;/id&gt;
  &lt;updated&gt;2011-07-10T23:46:52-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/saved/eventtypes/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/admin/search/saved/eventtypes/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;internal_search_terms&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/saved/eventtypes/internal_search_terms&lt;/id&gt;
    &lt;updated&gt;2011-07-10T23:46:52-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/saved/eventtypes/internal_search_terms" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/saved/eventtypes/internal_search_terms" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/saved/eventtypes/internal_search_terms/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/system/saved/eventtypes/internal_search_terms" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/system/saved/eventtypes/internal_search_terms/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="description"/&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:appName"&gt;search&lt;/s:key&gt;
        &lt;s:key name="eai:userName"&gt;admin&lt;/s:key&gt;
        &lt;s:key name="priority"&gt;1&lt;/s:key&gt;
        &lt;s:key name="search"&gt;
&lt;![CDATA[( "After evaluating args" OR "Before evaluating args" OR "context dispatched for search=" OR "SearchParser - PARSING" OR "got search" OR "_dispatchNewSearch - search" OR "search:* - q" OR ( decomposition fullsearch ) OR "PAAAAAARSER! - search" OR "view:* - DECOMPOSITION" OR "Splunk.Module.SearchBar .setInputField" OR ( typeahead prefix ) OR "DEBUG HTTPServer - Deleting request=GET" OR /en-US/api/search/typeahead )]]&gt;        &lt;/s:key&gt;
        &lt;s:key name="tags"&gt;
          &lt;s:list/&gt;
        &lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## saved/eventtypes
{: name='savedeventtypes'}

Creates a new event type.

	[POST] saved/eventtypes

### Parameters

description
: _Optional_ **String** Human-readable description of this event type.

disabled
: _Optional_ **Boolean** If True, disables the event type.

name
: _Required_ **String** The name for the event type.

priority
: _Optional_ **Number** Specify an integer from 1 to 10 for the value used to determine the order in which the matching event types of an event are displayed. 1 is the highest priority.

search
: _Required_ **String** Search terms for this event type.

tags
: _Optional_ **String** Deprecated. Use tags.conf.spec file to assign tags to groups of events with related field values.

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **201** | Created successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **402** | The Splunk license in use has disabled this feature. |
|--------------------------------
| **403** | Insufficient permissions to create an event type. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Creates an event type, client-errors, for the specified search.
URI-encode the search string if it contains any of the following characters: =, &, ?, %
Otherwise, these characters can be interpreted as part of the HTTP request.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/saved/eventtypes \
	-d name="client-errors" --data-urlencode search=search="http client error NOT (403 OR 404)"
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;eventtypes&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/saved/eventtypes&lt;/id&gt;
  &lt;updated&gt;2011-07-10T23:47:10-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/saved/eventtypes/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/admin/search/saved/eventtypes/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;client-errors&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/admin/search/saved/eventtypes/client-errors&lt;/id&gt;
    &lt;updated&gt;2011-07-10T23:47:10-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/saved/eventtypes/client-errors" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/admin/search/saved/eventtypes/client-errors" rel="list"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/eventtypes/client-errors/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/eventtypes/client-errors" rel="edit"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/eventtypes/client-errors" rel="remove"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/eventtypes/client-errors/move" rel="move"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/eventtypes/client-errors/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="description"/&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:appName"&gt;search&lt;/s:key&gt;
        &lt;s:key name="eai:userName"&gt;admin&lt;/s:key&gt;
        &lt;s:key name="priority"&gt;1&lt;/s:key&gt;
        &lt;s:key name="search"&gt;search&lt;/s:key&gt;
        &lt;s:key name="tags"&gt;
          &lt;s:list/&gt;
        &lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## saved/eventtypes/{name}
{: name='savedeventtypesname'}

Deletes this event type.

	[DELETE] saved/eventtypes/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deleted successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to delete event type. |
|--------------------------------
| **404** | Event type does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Deletes the saved event type, client-errors.

#### Request
<pre class='terminal'>
curl -k -u admin:pass --request DELETE \
	https://localhost:8089/servicesNS/admin/search/saved/eventtypes/client-errors
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;eventtypes&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/saved/eventtypes&lt;/id&gt;
  &lt;updated&gt;2011-07-10T23:48:29-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/saved/eventtypes/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/admin/search/saved/eventtypes/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## saved/eventtypes/{name}
{: name='savedeventtypesname'}

Returns information on this event type.

	[GET] saved/eventtypes/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view event type. |
|--------------------------------
| **404** | Event type does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Returns details on the event type, client-errors.
The example for the POST operation of saved/eventtypes creates this event type.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/saved/eventtypes/client-errors
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;eventtypes&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/saved/eventtypes&lt;/id&gt;
  &lt;updated&gt;2011-07-10T23:47:17-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/saved/eventtypes/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/admin/search/saved/eventtypes/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;client-errors&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/admin/search/saved/eventtypes/client-errors&lt;/id&gt;
    &lt;updated&gt;2011-07-10T23:47:17-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/saved/eventtypes/client-errors" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/admin/search/saved/eventtypes/client-errors" rel="list"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/eventtypes/client-errors/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/eventtypes/client-errors" rel="edit"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/eventtypes/client-errors" rel="remove"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/eventtypes/client-errors/move" rel="move"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/eventtypes/client-errors/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="description"/&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:appName"&gt;search&lt;/s:key&gt;
        &lt;s:key name="eai:attributes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="optionalFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;description&lt;/s:item&gt;
                &lt;s:item&gt;disabled&lt;/s:item&gt;
                &lt;s:item&gt;priority&lt;/s:item&gt;
                &lt;s:item&gt;tags&lt;/s:item&gt;
              &lt;/s:list&gt;
            &lt;/s:key&gt;
            &lt;s:key name="requiredFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;search&lt;/s:item&gt;
              &lt;/s:list&gt;
            &lt;/s:key&gt;
            &lt;s:key name="wildcardFields"&gt;
              &lt;s:list/&gt;
            &lt;/s:key&gt;
          &lt;/s:dict&gt;
        &lt;/s:key&gt;
        &lt;s:key name="eai:userName"&gt;admin&lt;/s:key&gt;
        &lt;s:key name="priority"&gt;1&lt;/s:key&gt;
        &lt;s:key name="search"&gt;search&lt;/s:key&gt;
        &lt;s:key name="tags"&gt;
          &lt;s:list/&gt;
        &lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## saved/eventtypes/{name}
{: name='savedeventtypesname'}

Updates this event type.

	[POST] saved/eventtypes/{name}

### Parameters

description
: _Optional_ **INHERITED** INHERITED

disabled
: _Optional_ **INHERITED** INHERITED

priority
: _Optional_ **INHERITED** INHERITED

search
: _Required_ **INHERITED** INHERITED

tags
: _Optional_ **INHERITED** INHERITED

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Updated successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **402** | The Splunk license in use has disabled this feature. |
|--------------------------------
| **403** | Insufficient permissions to edit event type. |
|--------------------------------
| **404** | Event type does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Updates the event type, client-errors, to specify a description for the event type.  Note that the search must be re-specified for this edit.
URI-encode the search string if it contains any of the following characters: =, &, ?, %
Otherwise, these characters can be interpreted as part of the HTTP request.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/saved/eventtypes/client-errors \
	-d description="HTTP Client Errors" --data-urlencode search=search="http client error NOT (403 OR 404)"
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;eventtypes&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/saved/eventtypes&lt;/id&gt;
  &lt;updated&gt;2011-07-10T23:48:22-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/saved/eventtypes/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/admin/search/saved/eventtypes/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;client-errors&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/admin/search/saved/eventtypes/client-errors&lt;/id&gt;
    &lt;updated&gt;2011-07-10T23:48:22-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/saved/eventtypes/client-errors" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/admin/search/saved/eventtypes/client-errors" rel="list"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/eventtypes/client-errors/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/eventtypes/client-errors" rel="edit"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/eventtypes/client-errors" rel="remove"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/eventtypes/client-errors/move" rel="move"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/eventtypes/client-errors/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="description"&gt;HTTP Client Errors&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:appName"&gt;search&lt;/s:key&gt;
        &lt;s:key name="eai:userName"&gt;admin&lt;/s:key&gt;
        &lt;s:key name="priority"&gt;1&lt;/s:key&gt;
        &lt;s:key name="search"&gt;search&lt;/s:key&gt;
        &lt;s:key name="tags"&gt;
          &lt;s:list/&gt;
        &lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## search/fields
{: name='searchfields'}

Returns a list of fields registered for field configuration.

	[GET] search/fields

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------

### Example

Returns the list of fields that have tags applied to them.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/search/fields
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;Fields&lt;/title&gt;
  &lt;id&gt;/servicesNS/admin/search/search/fields&lt;/id&gt;
  &lt;updated&gt;2011-07-11T10:04:51-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;entry&gt;
    &lt;title&gt;_indextime&lt;/title&gt;
    &lt;id&gt;/servicesNS/admin/search/search/fields/_indextime&lt;/id&gt;
    &lt;updated&gt;2011-07-11T10:04:51-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/search/fields/_indextime" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;_sourcetype&lt;/title&gt;
    &lt;id&gt;/servicesNS/admin/search/search/fields/_sourcetype&lt;/id&gt;
    &lt;updated&gt;2011-07-11T10:04:51-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/search/fields/_sourcetype" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;date_hour&lt;/title&gt;
    &lt;id&gt;/servicesNS/admin/search/search/fields/date_hour&lt;/id&gt;
    &lt;updated&gt;2011-07-11T10:04:51-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/search/fields/date_hour" rel="alternate"/&gt;
  &lt;/entry&gt;
  . . .
  &lt;entry&gt;
    &lt;title&gt;splunk_server&lt;/title&gt;
    &lt;id&gt;/servicesNS/admin/search/search/fields/splunk_server&lt;/id&gt;
    &lt;updated&gt;2011-07-11T10:04:51-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/search/fields/splunk_server" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;timeendpos&lt;/title&gt;
    &lt;id&gt;/servicesNS/admin/search/search/fields/timeendpos&lt;/id&gt;
    &lt;updated&gt;2011-07-11T10:04:51-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/search/fields/timeendpos" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;timestartpos&lt;/title&gt;
    &lt;id&gt;/servicesNS/admin/search/search/fields/timestartpos&lt;/id&gt;
    &lt;updated&gt;2011-07-11T10:04:51-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/search/fields/timestartpos" rel="alternate"/&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## search/fields/{field_name}
{: name='searchfieldsfieldname'}

Retrieves information about the named field.

	[GET] search/fields/{field_name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------

### Example

Returns information about the field configuration for the sourcetype search field.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/search/fields/sourcetype
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;entry xmlns="http://www.w3.org/2005/Atom" xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;sourcetype&lt;/title&gt;
  &lt;id&gt;/servicesNS/admin/search/search/fields/sourcetype&lt;/id&gt;
  &lt;updated&gt;2011-07-11T10:08:54-07:00&lt;/updated&gt;
  &lt;link href="/servicesNS/admin/search/search/fields/sourcetype" rel="alternate"/&gt;
  &lt;content type="text"&gt;	Attr:INDEXED	True
	Attr:INDEXED_VALUE	False
	Attr:TOKENIZER	
&lt;/content&gt;
&lt;/entry&gt;
</code></pre>

## search/fields/{field_name}/tags
{: name='searchfieldsfieldnametags'}

Returns a list of tags that have been associated with the field specified by {field_name}.

	[GET] search/fields/{field_name}/tags

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **404** | Named field does not exist. |
|--------------------------------

### Example

Return the tags associated with the field host.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/search/fields/host/tags
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom" xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;Tags for the host field&lt;/title&gt;
  &lt;id&gt;/servicesNS/admin/search/search/fields/host/tags&lt;/id&gt;
  &lt;updated&gt;2011-07-11T10:41:46-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;entry&gt;
    &lt;title&gt;location::sfo&lt;/title&gt;
    &lt;id&gt;/servicesNS/admin/search/search/fields/host/tags#location::sfo&lt;/id&gt;
    &lt;updated&gt;2011-07-11T10:41:46-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/search/fields/host/tags#location::sfo" rel="alternate"/&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## search/fields/{field_name}/tags
{: name='searchfieldsfieldnametags'}

Update the tags associated with the field specified by {field_name}.

The <code>field_value</code> parameter specifies the specific value on which to bind tag actions. Multiple tags can be attached by passing multiple add or delete form parameters. The server processes all of the adds first, and then processes the deletes.

	[POST] search/fields/{field_name}/tags

### Parameters

add
: _Optional_ **String** The tag to attach to this <code>field_name:field_value</code> combination.

delete
: _Optional_ **String** The tag to remove to this <code>field_name::field_value</code> combination.

field_value
: _Required_ **String** The specific field value on which to bind the tags.

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Tags updated. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------

### Example

For the field host, adds the tag sfo and deletes the tag nyc for the value location.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/search/fields/host/tags \
	-d add=sfo \
	-d delete=nyc \
	-d value=location
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;response&gt;
  &lt;messages&gt;
    &lt;msg type='INFO'&gt;Successfully processed adds/deletes for field host&lt;/msg&gt;
  &lt;/messages&gt;
&lt;/response&gt;
</code></pre>

## search/tags
{: name='searchtags'}

Returns a list of all search time tags.

	[GET] search/tags

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------

### Example

Display search time tags for this Splunk instance.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/search/tags
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;Tags&lt;/title&gt;
  &lt;id&gt;/servicesNS/admin/search/search/tags&lt;/id&gt;
  &lt;updated&gt;2011-07-08T01:35:09-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;entry&gt;
    &lt;title&gt;machine&lt;/title&gt;
    &lt;id&gt;/servicesNS/admin/search/search/tags/machine&lt;/id&gt;
    &lt;updated&gt;2011-07-08T01:35:09-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/search/tags/machine" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;user&lt;/title&gt;
    &lt;id&gt;/servicesNS/admin/search/search/tags/user&lt;/id&gt;
    &lt;updated&gt;2011-07-08T01:35:09-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/search/tags/user" rel="alternate"/&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## search/tags/{tag_name}
{: name='searchtagstagname'}

Deletes the tag, and its associated field:value pair assignments. The resulting change in tags.conf is to set all field:value pairs to <code>disabled</code>.


	[DELETE] search/tags/{tag_name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deleted successfully. |
|--------------------------------
| **404** | Search tag does not exist. |
|--------------------------------

### Example

Deletes the user tag.
tags.conf has been updated to mark this tag disabled.

#### Request
<pre class='terminal'>
curl -k -u admin:pass --request DELETE \
	https://localhost:8089/servicesNS/admin/search/search/tags/user
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;response&gt;
  &lt;messages&gt;
    &lt;msg type="INFO"&gt;Tag successfully deleted&lt;/msg&gt;
  &lt;/messages&gt;
&lt;/response&gt;
</code></pre>

## search/tags/{tag_name}
{: name='searchtagstagname'}

Returns a list of field:value pairs that have been associated with the tag specified by {tag_name}.

	[GET] search/tags/{tag_name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **404** | Search tag does not exist. |
|--------------------------------

### Example

Returns field:value pairs associated with the tag name "user."

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/search/tags/user
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;Field::Value pairs with tag user&lt;/title&gt;
  &lt;id&gt;/servicesNS/admin/search/search/tags/user&lt;/id&gt;
  &lt;updated&gt;2011-07-08T01:35:28-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;entry&gt;
    &lt;title&gt;eventtype::userupdate&lt;/title&gt;
    &lt;id&gt;/servicesNS/admin/search/search/tags/user#eventtype::userupdate&lt;/id&gt;
    &lt;updated&gt;2011-07-08T01:35:28-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/search/tags/user#eventtype::userupdate" rel="alternate"/&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## search/tags/{tag_name}
{: name='searchtagstagname'}

Updates the field:value pairs associated with {tag_name}. 

Multiple field:value pairs can be attached by passing multiple add or delete form parameters. The server processes all of the adds first, and then deletes.

If {tag_name} does not exist, then the tag is created inline. Notification is sent to the client using the HTTP 201 status.

	[POST] search/tags/{tag_name}

### Parameters

add
: _Optional_ **String** A field:value pair to tag with {tag_name}.

delete
: _Optional_ **String** A field:value pair to remove from {tag_name}.

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Updated successfully. |
|--------------------------------
| **201** | Field successfuly added to tag. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------

### Example

Adds a field::value pair and deletes an existing field::value pair.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/search/tags/user \
	-d add=eventtype::userupdate \
	-d delete=eventtype::useradd-suse
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;response&gt;
  &lt;messages&gt;
    &lt;msg type="INFO"&gt;Processed adds/deletes for tag&lt;/msg&gt;
  &lt;/messages&gt;
&lt;/response&gt;
</code></pre>


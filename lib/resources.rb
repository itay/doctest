require 'pp'
require 'yajl/json_gem'
require 'stringio'
require 'kramdown'

module Splunk
  module Resources
    module Helpers
      STATUSES = {
        200 => '200 Operating Successful',
        201 => '201 Object Created Successfully',
        204 => '204 Successful, but no content was returned',
        400 => '400 Request error. See response body for explanation',
        401 => '401 Authentication failure: must pass valid credentials with request. Session may have timed out',
        402 => '402 The Splunk license in use has disabled this feature',
        403 => '403 Insufficient permissions to view/edit/create/disable/delete',
        404 => '404 Object does not exist',
        405 => '405 Method Not Allowed (e.g. supports GET but not POST)',
        409 => '409 Request error: this operation is invalid for this item. See response body for explanation',
        422 => '422 Unprocessable Entity',
        500 => '500 Internal server error. See response body for explanation',
        503 => '503 This feature has been disabled in Splunk configuration files'
      }

      CACHED_TOC = nil

      def headers(status, head = {})
        css_class = (status == 204 || status == 404) ? 'headers no-response' : 'headers'
        lines = ["Status: #{STATUSES[status]}"]
        head.each do |key, value|
          lines << "#{key}: #{value}"
        end

        %(<pre class="#{css_class}"><code>#{lines * "\n"}</code></pre>\n)
      end

      def json(key)
        hash = case key
          when Hash
            h = {}
            key.each { |k, v| h[k.to_s] = v }
            h
          when Array
            key
          else Resources.const_get(key.to_s.upcase)
        end

        hash = yield hash if block_given?

        %(<pre class="highlight"><code class="language-javascript">) +
          JSON.pretty_generate(hash) + "</code></pre>"
      end

      def toc
        parent_dir = File.expand_path(File.dirname(File.dirname(__FILE__)))
        
        toc_file = File.open(File.join(parent_dir, "toc/toc.html"), File::RDONLY)
        toc = toc_file.read()
        
        return toc.gsub("\n", "\n          ")
      end
    end
  end
end

include Splunk::Resources::Helpers

<a name='datainputsad'/>

## data/inputs/ad

Gets current AD monitoring configuration.

	[GET] data/inputs/ad

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
| **403** | Insufficient permissions to view AD monitoring configuration. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Lists all configured AD monitoring stanza.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/data/inputs/ad
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;win-admon&lt;/title&gt;
  &lt;id&gt;https://10.1.5.157:8089/services/data/inputs/ad&lt;/id&gt;
  &lt;updated&gt;2011-07-29T19:13:28-07:00&lt;/updated&gt;
  &lt;generator version="104976"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/data/inputs/ad/_new" rel="create"/&gt;
  &lt;link href="/services/data/inputs/ad/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;NearestDC&lt;/title&gt;
    &lt;id&gt;https://10.1.5.157:8089/servicesNS/nobody/windows/data/inputs/ad/NearestDC&lt;/id&gt;
    &lt;updated&gt;2011-07-29T19:13:28-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/ad/NearestDC" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/ad/NearestDC" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/ad/NearestDC/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/ad/NearestDC" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/ad/NearestDC/enable" rel="enable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="disabled"&gt;1&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="index"&gt;default&lt;/s:key&gt;
        &lt;s:key name="monitorSubtree"&gt;1&lt;/s:key&gt;
        &lt;s:key name="startingNode"/&gt;
        &lt;s:key name="targetDc"/&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/inputs/ad

Creates new or modifies existing performance monitoring settings.

	[POST] data/inputs/ad

### Parameters

disabled
: _Optional_ **Number** Indicates whether the monitoring is disabled.

index
: _Optional_ **String** The index in which to store the gathered data.

monitorSubtree
: _Required_ **Number** Whether or not to monitor the subtree(s) of a given directory tree path.  1 means yes, 0 means no.

name
: _Required_ **String** A unique name that represents a configuration or set of configurations for a specific domain controller (DC).

startingNode
: _Optional_ **String** Where in the Active Directory directory tree to start monitoring.  If not specified, will attempt to start at the root of the directory tree.

targetDc
: _Optional_ **String** Specifies a fully qualified domain name of a valid, network-accessible DC.  If not specified, Splunk will obtain the local computer's DC.

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
| **403** | Insufficient permissions to create monitoring stanza. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Creates a new AD monitoring stanza, naming it 'newdc', without sub-tree monitoring.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/data/inputs/ad \
	-d monitorSubtree=0 \
	-d name=newdc
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;win-admon&lt;/title&gt;
  &lt;id&gt;https://10.1.5.157:8089/servicesNS/nobody/search/data/inputs/ad&lt;/id&gt;
  &lt;updated&gt;2011-07-29T19:14:57-07:00&lt;/updated&gt;
  &lt;generator version="104976"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/ad/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/ad/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

<a name='datainputsadname'/>

## data/inputs/ad/{name}

Deletes a given AD monitoring stanza.

	[DELETE] data/inputs/ad/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deleted successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to delete AD monitoring stanza. |
|--------------------------------
| **404** | AD monitoring stanza does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Deletes a given stanza.

#### Request
<pre class='terminal'>
curl -k -u admin:pass --request DELETE \
	https://localhost:8089/servicesNS/nobody/search/data/inputs/ad/newdc
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;win-admon&lt;/title&gt;
  &lt;id&gt;https://10.1.5.157:8089/servicesNS/nobody/search/data/inputs/ad&lt;/id&gt;
  &lt;updated&gt;2011-07-29T19:22:50-07:00&lt;/updated&gt;
  &lt;generator version="104976"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/ad/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/ad/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## data/inputs/ad/{name}

Gets the current configuration for a given AD monitoring stanza.

	[GET] data/inputs/ad/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view AD monitoring configuration. |
|--------------------------------
| **404** | AD monitoring stanza does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Gets configuration for a given AD monitoring stanza.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/nobody/search/data/inputs/ad/newdc
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;win-admon&lt;/title&gt;
  &lt;id&gt;https://10.1.5.157:8089/servicesNS/nobody/search/data/inputs/ad&lt;/id&gt;
  &lt;updated&gt;2011-07-29T19:18:18-07:00&lt;/updated&gt;
  &lt;generator version="104976"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/ad/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/ad/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;newdc&lt;/title&gt;
    &lt;id&gt;https://10.1.5.157:8089/servicesNS/nobody/search/data/inputs/ad/newdc&lt;/id&gt;
    &lt;updated&gt;2011-07-29T19:18:18-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/ad/newdc" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/ad/newdc" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/ad/newdc/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/ad/newdc" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/ad/newdc" rel="remove"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/ad/newdc/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:attributes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="optionalFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;disabled&lt;/s:item&gt;
                &lt;s:item&gt;index&lt;/s:item&gt;
                &lt;s:item&gt;startingNode&lt;/s:item&gt;
                &lt;s:item&gt;targetDc&lt;/s:item&gt;
              &lt;/s:list&gt;
            &lt;/s:key&gt;
            &lt;s:key name="requiredFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;monitorSubtree&lt;/s:item&gt;
              &lt;/s:list&gt;
            &lt;/s:key&gt;
            &lt;s:key name="wildcardFields"&gt;
              &lt;s:list/&gt;
            &lt;/s:key&gt;
          &lt;/s:dict&gt;
        &lt;/s:key&gt;
        &lt;s:key name="index"&gt;default&lt;/s:key&gt;
        &lt;s:key name="monitorSubtree"&gt;0&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/inputs/ad/{name}

Modifies a given AD monitoring stanza.

	[POST] data/inputs/ad/{name}

### Parameters

disabled
: _Optional_ **INHERITED** INHERITED

index
: _Optional_ **INHERITED** INHERITED

monitorSubtree
: _Required_ **INHERITED** INHERITED

startingNode
: _Optional_ **INHERITED** INHERITED

targetDc
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
| **403** | Insufficient permissions to edit AD monitoring stanza. |
|--------------------------------
| **404** | AD monitoring stanza does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Modifies an existing AD monitoring stanza.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/nobody/search/data/inputs/ad/newdc \
	-d monitorSubtree=1
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;win-admon&lt;/title&gt;
  &lt;id&gt;https://10.1.5.157:8089/servicesNS/nobody/search/data/inputs/ad&lt;/id&gt;
  &lt;updated&gt;2011-07-29T19:20:16-07:00&lt;/updated&gt;
  &lt;generator version="104976"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/ad/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/ad/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

<a name='datainputsmonitor'/>

## data/inputs/monitor

List enabled and disabled monitor inputs.

	[GET] data/inputs/monitor

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
| **403** | Insufficient permissions to view monitored input. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Provides information on all enabled and disabled inputs for monitoring by this Splunk instance.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/data/inputs/monitor
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;monitor&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/data/inputs/monitor&lt;/id&gt;
  &lt;updated&gt;2011-07-10T14:25:53-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/data/inputs/monitor/_new" rel="create"/&gt;
  &lt;link href="/services/data/inputs/monitor/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;$SPLUNK_HOME/etc/splunk.version&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/data/inputs/monitor/%24SPLUNK_HOME%252Fetc%252Fsplunk.version&lt;/id&gt;
    &lt;updated&gt;2011-07-10T14:25:53-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/data/inputs/monitor/%24SPLUNK_HOME%252Fetc%252Fsplunk.version" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/data/inputs/monitor/%24SPLUNK_HOME%252Fetc%252Fsplunk.version" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/inputs/monitor/%24SPLUNK_HOME%252Fetc%252Fsplunk.version/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/inputs/monitor/%24SPLUNK_HOME%252Fetc%252Fsplunk.version" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/inputs/monitor/%24SPLUNK_HOME%252Fetc%252Fsplunk.version/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="_TCP_ROUTING"&gt;*&lt;/s:key&gt;
        &lt;s:key name="_rcvbuf"&gt;1572864&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="filecount"&gt;1&lt;/s:key&gt;
        &lt;s:key name="host"&gt;MrT&lt;/s:key&gt;
        &lt;s:key name="index"&gt;_internal&lt;/s:key&gt;
        &lt;s:key name="sourcetype"&gt;splunk_version&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/inputs/monitor

Create a new file or directory monitor input.

	[POST] data/inputs/monitor

### Parameters

blacklist
: _Optional_ **String** Specify a regular expression for a file path. The file path that matches this regular expression is not indexed.

check-index
: _Optional_ **Boolean** If set to true, the "index" value will be checked to ensure that it is the name of a valid index.

check-path
: _Optional_ **Boolean** If set to true, the "name" value will be checked to ensure that it exists.

crc-salt
: _Optional_ **String** A string that modifies the file tracking identity for files in this input.  The magic value "<SOURCE>" invokes special behavior (see admin documentation).

followTail
: _Optional_ **Boolean** If set to true, files that are seen for the first time will be read from the end.

host
: _Optional_ **String** The value to populate in the host field for events from this data input.

host_regex
: _Optional_ **String** Specify a regular expression for a file path. If the path for a file matches this regular expression, the captured value is used to populate the host field for events from this data input.  The regular expression must have one capture group.

host_segment
: _Optional_ **Number** Use the specified slash-separate segment of the filepath as the host field value.

ignore-older-than
: _Optional_ **String** Specify a time value. If the modification time of a file being monitored falls outside of this rolling time window, the file is no longer being monitored.

index
: _Optional_ **String** Which index events from this input should be stored in.

name
: _Required_ **String** The file or directory path to monitor on the system.

recursive
: _Optional_ **Boolean** Setting this to "false" will prevent monitoring of any subdirectories encountered within this data input.

rename-source
: _Optional_ **String** The value to populate in the source field for events from this data input.  The same source should not be used for multiple data inputs.

sourcetype
: _Optional_ **String** The value to populate in the sourcetype field for incoming events.

time-before-close
: _Optional_ **Number** When Splunk reaches the end of a file that is being read, the file will be kept open for a minimum of the number of seconds specified in this value.  After this period has elapsed, the file will be checked again for more data.

whitelist
: _Optional_ **String** Specify a regular expression for a file path. Only file paths that match this regular expression are indexed.

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
| **403** | Insufficient permissions to create monitored input. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Configures the Unix /var/log directory as a monitored input.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/nobody/search/data/inputs/monitor \
	-d name=/var/log
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;monitor&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/inputs/monitor&lt;/id&gt;
  &lt;updated&gt;2011-07-10T14:27:57-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/monitor/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/monitor/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

<a name='datainputsmonitorname'/>

## data/inputs/monitor/{name}

Disable the named monitor data input and remove it from the configuration.

	[DELETE] data/inputs/monitor/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deleted successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to delete monitored input. |
|--------------------------------
| **404** | Monitored input does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Removes the following file as a monitored input. This monitored input was created in the example for the POST operation of this endpoint.
/Applications/splunk/var/log/splunk/web_access.log
The {name} field in the DELETE operation is specially URI-encoded. See the REST API overview for details on URI encoding of filenames.

#### Request
<pre class='terminal'>
curl -k -u admin:pass --request DELETE \
	https://localhost:8089/servicesNS/nobody/search/data/inputs/monitor/%252Fvar%252Flog
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;monitor&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/inputs/monitor&lt;/id&gt;
  &lt;updated&gt;2011-07-10T14:35:35-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/monitor/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/monitor/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## data/inputs/monitor/{name}

List the properties of a single monitor data input.

	[GET] data/inputs/monitor/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view monitored input. |
|--------------------------------
| **404** | Monitored input does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Returns information on the monitored directory /var/log.
The {name} field in the GET operation is specially URI-encoded. See the REST API overview for details on URI encoding of filenames.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/servicesNS/nobody/search/data/inputs/monitor/%252Fvar%252Flog
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;monitor&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/inputs/monitor&lt;/id&gt;
  &lt;updated&gt;2011-07-10T14:33:54-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/monitor/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/monitor/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;/var/log&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/inputs/monitor/%252Fvar%252Flog&lt;/id&gt;
    &lt;updated&gt;2011-07-10T14:33:54-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/monitor/%252Fvar%252Flog" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/monitor/%252Fvar%252Flog" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/monitor/%252Fvar%252Flog/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/monitor/%252Fvar%252Flog" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/monitor/%252Fvar%252Flog/members" rel="members"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/monitor/%252Fvar%252Flog" rel="remove"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/monitor/%252Fvar%252Flog/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="_rcvbuf"&gt;1572864&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:attributes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="optionalFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;blacklist&lt;/s:item&gt;
                &lt;s:item&gt;check-index&lt;/s:item&gt;
                &lt;s:item&gt;check-path&lt;/s:item&gt;
                &lt;s:item&gt;crc-salt&lt;/s:item&gt;
                &lt;s:item&gt;followTail&lt;/s:item&gt;
                &lt;s:item&gt;host&lt;/s:item&gt;
                &lt;s:item&gt;host_regex&lt;/s:item&gt;
                &lt;s:item&gt;host_segment&lt;/s:item&gt;
                &lt;s:item&gt;ignore-older-than&lt;/s:item&gt;
                &lt;s:item&gt;index&lt;/s:item&gt;
                &lt;s:item&gt;recursive&lt;/s:item&gt;
                &lt;s:item&gt;rename-source&lt;/s:item&gt;
                &lt;s:item&gt;sourcetype&lt;/s:item&gt;
                &lt;s:item&gt;time-before-close&lt;/s:item&gt;
                &lt;s:item&gt;whitelist&lt;/s:item&gt;
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
        &lt;s:key name="filecount"&gt;108&lt;/s:key&gt;
        &lt;s:key name="host"&gt;MrT&lt;/s:key&gt;
        &lt;s:key name="index"&gt;default&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/inputs/monitor/{name}

Update properties of the named monitor input.

	[POST] data/inputs/monitor/{name}

### Parameters

blacklist
: _Optional_ **INHERITED** INHERITED

check-index
: _Optional_ **INHERITED** INHERITED

check-path
: _Optional_ **INHERITED** INHERITED

crc-salt
: _Optional_ **INHERITED** INHERITED

followTail
: _Optional_ **INHERITED** INHERITED

host
: _Optional_ **INHERITED** INHERITED

host_regex
: _Optional_ **INHERITED** INHERITED

host_segment
: _Optional_ **INHERITED** INHERITED

ignore-older-than
: _Optional_ **INHERITED** INHERITED

index
: _Optional_ **INHERITED** INHERITED

recursive
: _Optional_ **INHERITED** INHERITED

rename-source
: _Optional_ **INHERITED** INHERITED

sourcetype
: _Optional_ **INHERITED** INHERITED

time-before-close
: _Optional_ **INHERITED** INHERITED

whitelist
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
| **403** | Insufficient permissions to edit monitored input. |
|--------------------------------
| **404** | Monitored input does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Updates the monitored input such that it does not recurse through subdirectories.  This monitored input was created in the example for the POST operation of this endpoint.
The {name} field in the POST operation is specially URI-encoded. See the REST API overview for details on URI encoding of filenames.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/servicesNS/nobody/search/data/inputs/monitor/%252Fvar%252Flog \
	-d recursive=false
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;monitor&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/inputs/monitor&lt;/id&gt;
  &lt;updated&gt;2011-07-10T14:35:28-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/monitor/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/monitor/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

<a name='datainputsmonitornamemembers'/>

## data/inputs/monitor/{name}/members

Lists all files monitored under the named monitor input.

	[GET] data/inputs/monitor/{name}/members

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
| **403** | Insufficient permissions to view monitored input's files. |
|--------------------------------
| **404** | Monitor input does not exist or does not have any members. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Retrieves the list of files under /var/log that this input is monitoring.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/servicesNS/nobody/search/data/inputs/monitor/%252Fvar%252Flog/members
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;monitor&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/inputs/monitor&lt;/id&gt;
  &lt;updated&gt;2011-07-10T14:34:28-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/monitor/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/monitor/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;/var/log/acpid&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/inputs/monitor/%252Fvar%252Flog%252Facpid&lt;/id&gt;
    &lt;updated&gt;2011-07-10T14:34:28-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/monitor/%252Fvar%252Flog%252Facpid" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/monitor/%252Fvar%252Flog%252Facpid" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/monitor/%252Fvar%252Flog%252Facpid/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/monitor/%252Fvar%252Flog%252Facpid" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/monitor/%252Fvar%252Flog%252Facpid" rel="remove"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
  &lt;!-- many more file entries elided for brevity. --&gt;
&lt;/feed&gt;
</code></pre>

<a name='datainputsoneshot'/>

## data/inputs/oneshot

Enumerates in-progress oneshot inputs. As soon as an input is complete, it is removed from this list.

	[GET] data/inputs/oneshot

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
| **403** | Insufficient permissions to view inputs. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Lists the in-progress one shot inputs for this Splunk instance.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/data/inputs/oneshot
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;oneshotinput&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/data/inputs/oneshot&lt;/id&gt;
  &lt;updated&gt;2011-07-08T01:48:04-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/data/inputs/oneshot/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;/var/log/distccd.log&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/data/inputs/oneshot/%252Fvar%252Flog%252Fdistccd.log&lt;/id&gt;
    &lt;updated&gt;2011-07-08T01:48:04-07:00&lt;/updated&gt;
    &lt;link href="/services/data/inputs/oneshot/%252Fvar%252Flog%252Fdistccd.log" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/data/inputs/oneshot/%252Fvar%252Flog%252Fdistccd.log" rel="list"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="Bytes Indexed"&gt;7200768&lt;/s:key&gt;
        &lt;s:key name="Offset"&gt;7200768&lt;/s:key&gt;
        &lt;s:key name="Size"&gt;449630160&lt;/s:key&gt;
        &lt;s:key name="Sources Indexed"&gt;0&lt;/s:key&gt;
        &lt;s:key name="Spool Time"&gt;Fri Jul  8 01:47:53 PDT 2011&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/inputs/oneshot

Queues a file for immediate indexing by the file input subsystem. The file must be locally accessible from the server.

This endpoint can handle any single file: plain, compressed or archive. The file is indexed in full, regardless of whether it has been indexed before.

	[POST] data/inputs/oneshot

### Parameters

host
: _Optional_ **String** The value of the "host" field to be applied to data from this file.

host_regex
: _Optional_ **String** A regex to be used to extract a "host" field from the path.<br/><br/>If the path matches this regular expression, the captured value is used to populate the host field for events from this data input. The regular expression must have one capture group.

host_segment
: _Optional_ **Number** Use the specified slash-separate segment of the path as the host field value.

index
: _Optional_ **String** The destination index for data processed from this file.

name
: _Required_ **String** The path to the file to be indexed. The file must be locally accessible by the server.

rename-source
: _Optional_ **String** The value of the "source" field to be applied to data from this file.

sourcetype
: _Optional_ **String** The value of the "sourcetype" field to be applied to data from this file.

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
| **403** | Insufficient permissions to create input. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

This example queues the file /var/log/messages for indexing.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/data/inputs/oneshot \
	-d name=/var/log/messages
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;oneshotinput&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/data/inputs/oneshot&lt;/id&gt;
  &lt;updated&gt;2011-07-08T01:48:04-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/data/inputs/oneshot/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

<a name='datainputsoneshotname'/>

## data/inputs/oneshot/{name}

Finds information about a single in-flight one shot input. This is a subset of the information in the full enumeration.

	[GET] data/inputs/oneshot/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view input. |
|--------------------------------
| **404** | Input does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

List information about the named in-progress one shot input in this Splunk instance.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/services/data/inputs/oneshot/%252Fvar%252Flog%252Fmessages
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;oneshotinput&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/data/inputs/oneshot&lt;/id&gt;
  &lt;updated&gt;2011-07-08T01:49:20-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/data/inputs/oneshot/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;/var/log/messages&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/data/inputs/oneshot/%252Fvar%252Flog%252Fmessages&lt;/id&gt;
    &lt;updated&gt;2011-07-08T01:49:20-07:00&lt;/updated&gt;
    &lt;link href="/services/data/inputs/oneshot/%252Fvar%252Flog%252Fmessages" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/data/inputs/oneshot/%252Fvar%252Flog%252Fmessages" rel="list"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="Bytes Indexed"&gt;114822&lt;/s:key&gt;
        &lt;s:key name="Offset"&gt;114822&lt;/s:key&gt;
        &lt;s:key name="Size"&gt;114822&lt;/s:key&gt;
        &lt;s:key name="Sources Indexed"&gt;0&lt;/s:key&gt;
        &lt;s:key name="Spool Time"&gt;Fri Jul  8 01:48:04 PDT 2011&lt;/s:key&gt;
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
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

<a name='datainputsregistry'/>

## data/inputs/registry

Gets current registry monitoring configuration.

	[GET] data/inputs/registry

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
| **403** | Insufficient permissions to view registry monitoring configuration. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Gets current registry inputs configuration.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/data/inputs/registry
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;win-regmon&lt;/title&gt;
  &lt;id&gt;https://10.1.5.157:8089/services/data/inputs/registry&lt;/id&gt;
  &lt;updated&gt;2011-07-29T19:31:32-07:00&lt;/updated&gt;
  &lt;generator version="104976"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/data/inputs/registry/_new" rel="create"/&gt;
  &lt;link href="/services/data/inputs/registry/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;Machine keys&lt;/title&gt;
    &lt;id&gt;https://10.1.5.157:8089/servicesNS/nobody/search/data/inputs/registry/Machine%20keys&lt;/id&gt;
    &lt;updated&gt;2011-07-29T19:31:32-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/registry/Machine%20keys" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/registry/Machine%20keys" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/registry/Machine%20keys/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/registry/Machine%20keys" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/registry/Machine%20keys/enable" rel="enable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="baseline"&gt;0&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;1&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="hive"&gt;HKLM&lt;/s:key&gt;
        &lt;s:key name="index"&gt;default&lt;/s:key&gt;
        &lt;s:key name="monitorSubnodes"&gt;1&lt;/s:key&gt;
        &lt;s:key name="proc"&gt;c:\.*&lt;/s:key&gt;
        &lt;s:key name="type"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;set&lt;/s:item&gt;
            &lt;s:item&gt;create&lt;/s:item&gt;
            &lt;s:item&gt;delete&lt;/s:item&gt;
            &lt;s:item&gt;rename&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/inputs/registry

Creates new or modifies existing registry monitoring settings.

	[POST] data/inputs/registry

### Parameters

baseline
: _Required_ **Number** Specifies whether or not to establish a baseline value for the registry keys.  1 means yes, 0 no.

disabled
: _Optional_ **Number** Indicates whether the monitoring is disabled.

hive
: _Required_ **String** Specifies the registry hive under which to monitor for changes.

index
: _Optional_ **String** The index in which to store the gathered data.

monitorSubnodes
: _Optional_ **Number** If set to '1', will monitor all sub-nodes under a given hive.

name
: _Required_ **String** Name of the configuration stanza.

proc
: _Required_ **String** Specifies a regex.  If specified, will only collected changes if a process name matches that regex.

type
: _Required_ **String** A regular expression that specifies the type(s) of Registry event(s) that you want to monitor.

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
| **403** | Insufficient permissions to create registry monitoring stanza. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Creates a new registry monitoring stanza.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/nobody/search/data/inputs/registry \
	-d baseline=1 \
	-d hive="HKU\\.*" \
	-d name=mykeys \
	-d proc="c:\\.*" \
	-d type="set|create|delete|rename"
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;win-regmon&lt;/title&gt;
  &lt;id&gt;https://10.1.5.157:8089/servicesNS/nobody/search/data/inputs/registry&lt;/id&gt;
  &lt;updated&gt;2011-07-29T19:29:18-07:00&lt;/updated&gt;
  &lt;generator version="104976"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/registry/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/registry/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

<a name='datainputsregistryname'/>

## data/inputs/registry/{name}

Deletes registry monitoring configuration stanza.

	[DELETE] data/inputs/registry/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deleted successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to delete registry configuration stanza. |
|--------------------------------
| **404** | Registry monitoring configuration stanza does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Deletes existing configuration stanza.

#### Request
<pre class='terminal'>
curl -k -u admin:pass --request DELETE \
	https://localhost:8089/servicesNS/nobody/search/data/inputs/registry/mykeys
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;win-regmon&lt;/title&gt;
  &lt;id&gt;https://10.1.5.157:8089/servicesNS/nobody/search/data/inputs/registry&lt;/id&gt;
  &lt;updated&gt;2011-07-29T19:36:54-07:00&lt;/updated&gt;
  &lt;generator version="104976"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/registry/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/registry/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## data/inputs/registry/{name}

Gets current registry monitoring configuration stanza.

	[GET] data/inputs/registry/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view registry monitoring configuration stanza. |
|--------------------------------
| **404** | Registry monitoring stanza does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Gets current configuration for a given stanza.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/nobody/search/data/inputs/registry/mykeys
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;win-regmon&lt;/title&gt;
  &lt;id&gt;https://10.1.5.157:8089/servicesNS/nobody/search/data/inputs/registry&lt;/id&gt;
  &lt;updated&gt;2011-07-29T19:33:21-07:00&lt;/updated&gt;
  &lt;generator version="104976"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/registry/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/registry/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;mykeys&lt;/title&gt;
    &lt;id&gt;https://10.1.5.157:8089/servicesNS/nobody/search/data/inputs/registry/mykeys&lt;/id&gt;
    &lt;updated&gt;2011-07-29T19:33:21-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/registry/mykeys" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/registry/mykeys" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/registry/mykeys/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/registry/mykeys" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/registry/mykeys" rel="remove"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/registry/mykeys/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="baseline"&gt;1&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:attributes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="optionalFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;disabled&lt;/s:item&gt;
                &lt;s:item&gt;index&lt;/s:item&gt;
                &lt;s:item&gt;monitorSubnodes&lt;/s:item&gt;
              &lt;/s:list&gt;
            &lt;/s:key&gt;
            &lt;s:key name="requiredFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;baseline&lt;/s:item&gt;
                &lt;s:item&gt;hive&lt;/s:item&gt;
                &lt;s:item&gt;proc&lt;/s:item&gt;
                &lt;s:item&gt;type&lt;/s:item&gt;
              &lt;/s:list&gt;
            &lt;/s:key&gt;
            &lt;s:key name="wildcardFields"&gt;
              &lt;s:list/&gt;
            &lt;/s:key&gt;
          &lt;/s:dict&gt;
        &lt;/s:key&gt;
        &lt;s:key name="hive"&gt;HKU&lt;/s:key&gt;
        &lt;s:key name="index"&gt;default&lt;/s:key&gt;
        &lt;s:key name="monitorSubnodes"&gt;1&lt;/s:key&gt;
        &lt;s:key name="proc"&gt;c:\.*&lt;/s:key&gt;
        &lt;s:key name="type"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;set&lt;/s:item&gt;
            &lt;s:item&gt;create&lt;/s:item&gt;
            &lt;s:item&gt;delete&lt;/s:item&gt;
            &lt;s:item&gt;rename&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/inputs/registry/{name}

Modifies given registry monitoring stanza.

	[POST] data/inputs/registry/{name}

### Parameters

baseline
: _Required_ **INHERITED** INHERITED

disabled
: _Optional_ **INHERITED** INHERITED

hive
: _Required_ **INHERITED** INHERITED

index
: _Optional_ **INHERITED** INHERITED

monitorSubnodes
: _Optional_ **INHERITED** INHERITED

proc
: _Required_ **INHERITED** INHERITED

type
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
| **403** | Insufficient permissions to edit registry monitoring stanza. |
|--------------------------------
| **404** | Registry monitoring stanza does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Modifies existing registry configuration.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/nobody/search/data/inputs/registry/mykeys \
	-d baseline=1 \
	-d hive="HKU\\.*" \
	-d proc="c:\\.*" \
	-d type="set|create"
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;win-regmon&lt;/title&gt;
  &lt;id&gt;https://10.1.5.157:8089/servicesNS/nobody/search/data/inputs/registry&lt;/id&gt;
  &lt;updated&gt;2011-07-29T19:36:07-07:00&lt;/updated&gt;
  &lt;generator version="104976"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/registry/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/registry/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

<a name='datainputsscript'/>

## data/inputs/script

Gets the configuration settings for scripted inputs.

	[GET] data/inputs/script

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
| **403** | Insufficient permissions to view script. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Lists configuration settings for all scripted inputs for this Splunk instance.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/data/inputs/script
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;script&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/data/inputs/script&lt;/id&gt;
  &lt;updated&gt;2011-07-09T20:16:11-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/data/inputs/script/_new" rel="create"/&gt;
  &lt;link href="/services/data/inputs/script/_reload" rel="_reload"/&gt;
  &lt;link href="/services/data/inputs/script/restart" rel="restart"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;/Applications/splunk4.3/etc/apps/unix/bin/cpu.sh&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/unix/data/inputs/script/.%252Fbin%252Fcpu.sh&lt;/id&gt;
    &lt;updated&gt;2011-07-09T20:16:11-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/unix/data/inputs/script/.%252Fbin%252Fcpu.sh" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/unix/data/inputs/script/.%252Fbin%252Fcpu.sh" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/unix/data/inputs/script/.%252Fbin%252Fcpu.sh/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/unix/data/inputs/script/.%252Fbin%252Fcpu.sh" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/unix/data/inputs/script/.%252Fbin%252Fcpu.sh/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="_rcvbuf"&gt;1572864&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="endtime"&gt;Sat Jul  9 20:15:54 2011&lt;/s:key&gt;
        &lt;s:key name="group"&gt;exec commands&lt;/s:key&gt;
        &lt;s:key name="host"&gt;vgenovese-mbp15.splunk.com&lt;/s:key&gt;
        &lt;s:key name="index"&gt;os&lt;/s:key&gt;
        &lt;s:key name="interval"&gt;30&lt;/s:key&gt;
        &lt;s:key name="source"&gt;cpu&lt;/s:key&gt;
        &lt;s:key name="sourcetype"&gt;cpu&lt;/s:key&gt;
        &lt;s:key name="starttime"&gt;Sat Jul  9 20:15:52 2011&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/inputs/script

Configures settings for new scripted inputs.

	[POST] data/inputs/script

### Parameters

disabled
: _Optional_ **Boolean** Specifies whether the input script is disabled.

host
: _Optional_ **String** Sets the host for events from this input. Defaults to whatever host sent the event.

index
: _Optional_ **String** Sets the index for events from this input. Defaults to the main index.

interval
: _Required_ **Number** Specify an integer or cron schedule. This parameter specifies how often to execute the specified script, in seconds or a valid cron schedule. If you specify a cron schedule, the script is not executed on start-up.

name
: _Required_ **String** Specify the name of the scripted input.

rename-source
: _Optional_ **String** Specify a new name for the source field for the script.

source
: _Optional_ **String** Sets the source key/field for events from this input. Defaults to the input file path.<br/><br/>Sets the source key's initial value. The key is used during parsing/indexing, in particular to set the source field during indexing.  It is also the source field used at search time. As a convenience, the chosen string is prepended with 'source::'.<br/><br/>Note: Overriding the source key is generally not recommended.  Typically, the input layer provides a more accurate string to aid in problem analysis and investigation, accurately recording the file  from which the data was retreived. Consider use of source types, tagging, and search wildcards before overriding this value.<br/><br/>

sourcetype
: _Optional_ **String** Sets the sourcetype key/field for events from this input. If unset, Splunk picks a source type based on various aspects of the data. As a convenience, the chosen string is prepended with 'sourcetype::'. There is no hard-coded default.<br/><br/>Sets the sourcetype key's initial value. The key is used during parsing/indexing, in particular to set the source type field during indexing. It is also the source type field used at search time.<br/><br/>Primarily used to explicitly declare the source type for this data, as opposed to allowing it to be determined via automated methods.  This is typically important both for searchability and for applying the relevant configuration for this type of data during parsing and indexing.

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
| **403** | Insufficient permissions to create script. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Configures a new script, myScript.sh, as a disabled scripted input with an interval of 3600 seconds (one hour).
This example assumes there is a script located at:
/Applications/splunk/etc/apps/myApp/bin/myScript.sh

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/nobody/search/data/inputs/script \
	-d name=/Applications/splunk4.3/etc/apps/myApp/bin/myScript.sh \
	-d disabled=true \
	-d interval=3600
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;script&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/inputs/script&lt;/id&gt;
  &lt;updated&gt;2011-07-09T20:25:17-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/script/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/script/_reload" rel="_reload"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/script/restart" rel="restart"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

<a name='datainputsscriptrestart'/>

## data/inputs/script/restart

Causes a restart on a given scripted input.

	[POST] data/inputs/script/restart

### Parameters

script
: _Required_ **String** Path to the script to be restarted.  This path must match an already-configured existing scripted input.

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Scripted input restarted successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **402** | The Splunk license in use has disabled this feature. |
|--------------------------------
| **403** | Insufficient permissions to restart scripted input. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Causes the running script named by the "script" parameter to restart.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/nobody/search/data/inputs/script/restart \
	-d script=/Applications/splunk/bin/scripts/myScript.sh
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;script&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/inputs/script&lt;/id&gt;
  &lt;updated&gt;2011-07-09T20:38:38-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/script/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/script/_reload" rel="_reload"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/script/restart" rel="restart"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

<a name='datainputsscriptname'/>

## data/inputs/script/{name}

Removes the scripted input specified by {name}.

	[DELETE] data/inputs/script/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deleted successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to delete script. |
|--------------------------------
| **404** | Script does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Delete the configuration for the scripted input, myScript.sh.
This example assumes there is a script located at:
/Applications/splunk/etc/apps/myApp/bin/myScript.sh
The {name} field in the DELETE operation is specially URI-encoded.  See the REST API overview for details on URI encoding of filenames.

#### Request
<pre class='terminal'>
curl -k -u admin:pass --request DELETE \
	https://localhost:8089/servicesNS/nobody/search/data/inputs/script/%252FApplications%252Fsplunk4.3%252Fetc%252Fapps%252FmyApp%252Fbin%252FmyScript.sh
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;script&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/inputs/script&lt;/id&gt;
  &lt;updated&gt;2011-07-09T20:29:18-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/script/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/script/_reload" rel="_reload"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/script/restart" rel="restart"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## data/inputs/script/{name}

Returns the configuration settings for the scripted input specified by {name}.

	[GET] data/inputs/script/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view script. |
|--------------------------------
| **404** | Script does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Return information about the scripted input, myScript.sh.
This example assumes there is a script located at:
/Applications/splunk/etc/apps/myApp/bin/myScript.sh
The {name} field in the POST operation is specially URI-encoded.  See the REST API overview for details on URI encoding of filenames.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/servicesNS/nobody/search/data/inputs/script/%252FApplications%252Fsplunk%252Fetc%252Fapps%252FmyApp%252Fbin%252FmyScript.sh
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;script&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/inputs/script&lt;/id&gt;
  &lt;updated&gt;2011-07-09T21:53:43-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/script/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/script/_reload" rel="_reload"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/script/restart" rel="restart"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;/Applications/splunk/etc/apps/myApp/bin/myScript.sh&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/inputs/script/%252FApplications%252Fsplunk%252Fetc%252Fapps%252FmyApp%252Fbin%252FmyScript.sh&lt;/id&gt;
    &lt;updated&gt;2011-07-09T21:53:43-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/script/%252FApplications%252Fsplunk%252Fetc%252Fapps%252FmyApp%252Fbin%252FmyScript.sh" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/script/%252FApplications%252Fsplunk%252Fetc%252Fapps%252FmyApp%252Fbin%252FmyScript.sh" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/script/%252FApplications%252Fsplunk%252Fetc%252Fapps%252FmyApp%252Fbin%252FmyScript.sh/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/script/%252FApplications%252Fsplunk%252Fetc%252Fapps%252FmyApp%252Fbin%252FmyScript.sh" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/script/%252FApplications%252Fsplunk%252Fetc%252Fapps%252FmyApp%252Fbin%252FmyScript.sh" rel="remove"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/script/%252FApplications%252Fsplunk%252Fetc%252Fapps%252FmyApp%252Fbin%252FmyScript.sh/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="_rcvbuf"&gt;1572864&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:attributes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="optionalFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;disabled&lt;/s:item&gt;
                &lt;s:item&gt;host&lt;/s:item&gt;
                &lt;s:item&gt;index&lt;/s:item&gt;
                &lt;s:item&gt;interval&lt;/s:item&gt;
                &lt;s:item&gt;rename-source&lt;/s:item&gt;
                &lt;s:item&gt;source&lt;/s:item&gt;
                &lt;s:item&gt;sourcetype&lt;/s:item&gt;
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
        &lt;s:key name="group"&gt;exec commands&lt;/s:key&gt;
        &lt;s:key name="host"&gt;ombroso-mbp15.splunk.com&lt;/s:key&gt;
        &lt;s:key name="index"&gt;default&lt;/s:key&gt;
        &lt;s:key name="interval"&gt;3600&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/inputs/script/{name}

Configures settings for scripted input specified by {name}.

	[POST] data/inputs/script/{name}

### Parameters

disabled
: _Optional_ **INHERITED** INHERITED

host
: _Optional_ **INHERITED** INHERITED

index
: _Optional_ **INHERITED** INHERITED

interval
: _Optional_ **INHERITED** INHERITED

rename-source
: _Optional_ **INHERITED** INHERITED

source
: _Optional_ **INHERITED** INHERITED

sourcetype
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
| **403** | Insufficient permissions to edit script. |
|--------------------------------
| **404** | Script does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Update the script, myScript.sh by setting the interval to 24 hours (86,400 seconds).
This example assumes there is a script located at:
/Applications/splunk/etc/apps/myApp/bin/myScript.sh
The {name} field in the POST operation is specially URI-encoded.  See the REST API overview for details on URI encoding of filenames.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/servicesNS/nobody/search/data/inputs/script/%252FApplications%252Fsplunk%252Fetc%252Fapps%252FmyApp%252Fbin%252FmyScript.sh \
	-d interval=86400
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;script&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/inputs/script&lt;/id&gt;
  &lt;updated&gt;2011-07-09T20:27:59-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/script/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/script/_reload" rel="_reload"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/script/restart" rel="restart"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

<a name='datainputstcpcooked'/>

## data/inputs/tcp/cooked

Returns information about all cooked TCP inputs.

	[GET] data/inputs/tcp/cooked

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
| **403** | Insufficient permissions to view inputs. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Retrieves all cooked TCP inputs in this instance of Splunk.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/data/inputs/tcp/cooked
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;cooked&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/data/inputs/tcp/cooked&lt;/id&gt;
  &lt;updated&gt;2011-07-10T14:50:50-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/data/inputs/tcp/cooked/_new" rel="create"/&gt;
  &lt;link href="/services/data/inputs/tcp/cooked/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;9993&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/inputs/tcp/cooked/9993&lt;/id&gt;
    &lt;updated&gt;2011-07-10T14:50:50-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/cooked/9993" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/cooked/9993" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/cooked/9993/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/cooked/9993" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/cooked/9993" rel="remove"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/cooked/9993/connections" rel="connections"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/cooked/9993/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="_rcvbuf"&gt;1572864&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="group"&gt;listenerports&lt;/s:key&gt;
        &lt;s:key name="host"&gt;MrT&lt;/s:key&gt;
        &lt;s:key name="index"&gt;default&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/inputs/tcp/cooked

Creates a new container for managing cooked data.

	[POST] data/inputs/tcp/cooked

### Parameters

SSL
: _Optional_ **Boolean** If SSL is not already configured, error is returned

connection_host
: _Optional_ **Enum** Valid values: (ip &#124; dns &#124; none)<br/><br/>Set the host for the remote server that is sending data.<br/><br/><code>ip</code> sets the host to the IP address of the remote server sending data. <code>dns</code> sets the host to the reverse DNS entry for the IP address of the remote server sending data. <code>none</code> leaves the host as specified in inputs.conf.<br/><br/>Default value is dns.

disabled
: _Optional_ **Boolean** Indicates whether the input is disabled.

host
: _Optional_ **String** The default value to fill in for events lacking a host value.

name
: _Required_ **Number** The port number of this input.

restrictToHost
: _Optional_ **String** Restrict incoming connections on this port to the host specified here.

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **201** | Created successfully. |
|--------------------------------
| **400** | Some arguments were invalid |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **402** | The Splunk license in use has disabled this feature. |
|--------------------------------
| **403** | Insufficient permissions to create input. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | There was an error; see body contents for messages |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Create a cooked TCP data input listening on port 9998.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/nobody/search/data/inputs/tcp/cooked \
	-d name=9998
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;cooked&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/inputs/tcp/cooked&lt;/id&gt;
  &lt;updated&gt;2011-07-10T14:52:33-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/cooked/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/cooked/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

<a name='datainputstcpcookedname'/>

## data/inputs/tcp/cooked/{name}

Removes the cooked TCP inputs for port or host:port specified by <code>{name}</code>

	[DELETE] data/inputs/tcp/cooked/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deleted successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to delete input. |
|--------------------------------
| **404** | Input does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Remove the cooked TCP input listening on port 9998.  Note that the name of this input changed due to the example that restricted incoming connections by host.

#### Request
<pre class='terminal'>
curl -k -u admin:pass --request DELETE \
	https://localhost:8089/servicesNS/nobody/search/data/inputs/tcp/cooked/tiny:9998
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;cooked&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/inputs/tcp/cooked&lt;/id&gt;
  &lt;updated&gt;2011-07-10T14:54:45-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/cooked/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/cooked/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## data/inputs/tcp/cooked/{name}

Returns information for the cooked TCP input specified by <code>{name}</code>.

If port is restricted to a host, name should be URI-encoded host:port.

	[GET] data/inputs/tcp/cooked/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | OK |
|--------------------------------
| **400** | ''TO DO: provide the rest of the status codes'' |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view input. |
|--------------------------------
| **404** | Input does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Retrieve settings for the cooked TCP data port.
First request displays settings for cooked TCP data listening on port 9998.
Second request displays settings for TCP data input listening on port 9997
but restricting data from host fwd1.splunk.com.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/nobody/search/data/inputs/tcp/cooked/9998
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;cooked&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/inputs/tcp/cooked&lt;/id&gt;
  &lt;updated&gt;2011-07-10T14:52:40-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/cooked/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/cooked/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;9998&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/inputs/tcp/cooked/9998&lt;/id&gt;
    &lt;updated&gt;2011-07-10T14:52:40-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/cooked/9998" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/cooked/9998" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/cooked/9998/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/cooked/9998" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/cooked/9998" rel="remove"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/cooked/9998/connections" rel="connections"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/cooked/9998/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="_rcvbuf"&gt;1572864&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:attributes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="optionalFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;SSL&lt;/s:item&gt;
                &lt;s:item&gt;connection_host&lt;/s:item&gt;
                &lt;s:item&gt;disabled&lt;/s:item&gt;
                &lt;s:item&gt;host&lt;/s:item&gt;
                &lt;s:item&gt;index&lt;/s:item&gt;
                &lt;s:item&gt;queue&lt;/s:item&gt;
                &lt;s:item&gt;restrictToHost&lt;/s:item&gt;
                &lt;s:item&gt;source&lt;/s:item&gt;
                &lt;s:item&gt;sourcetype&lt;/s:item&gt;
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
        &lt;s:key name="group"&gt;listenerports&lt;/s:key&gt;
        &lt;s:key name="host"&gt;MrT&lt;/s:key&gt;
        &lt;s:key name="index"&gt;default&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
curl -k -u admin:pass \
	https://localhost:8089/servicesNS/nobody/search/data/inputs/tcp/cooked/fwd1.splunk.com%3A9997
&lt;feed xmlns="http://www.w3.org/2005/Atom" 
      xmlns:s="http://dev.splunk.com/ns/rest" 
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;cooked&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/inputs/tcp/cooked&lt;/id&gt;
  &lt;updated&gt;2011-07-14T11:32:03-0700&lt;/updated&gt;
  &lt;generator version="101277"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/cooked/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/cooked/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;fwd1.splunk.com:9997&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/data/inputs/tcp/cooked/fwd1.splunk.com%3A9997&lt;/id&gt;
    &lt;updated&gt;2011-07-14T11:32:03-0700&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/data/inputs/tcp/cooked/fwd1.splunk.com%3A9997" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/data/inputs/tcp/cooked/fwd1.splunk.com%3A9997" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/inputs/tcp/cooked/fwd1.splunk.com%3A9997/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/inputs/tcp/cooked/fwd1.splunk.com%3A9997" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/inputs/tcp/cooked/fwd1.splunk.com%3A9997" rel="remove"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/inputs/tcp/cooked/fwd1.splunk.com%3A9997/connections" rel="connections"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/inputs/tcp/cooked/fwd1.splunk.com%3A9997/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="_rcvbuf"&gt;1572864&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:attributes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="optionalFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;SSL&lt;/s:item&gt;
                &lt;s:item&gt;connection_host&lt;/s:item&gt;
                &lt;s:item&gt;disabled&lt;/s:item&gt;
                &lt;s:item&gt;host&lt;/s:item&gt;
                &lt;s:item&gt;index&lt;/s:item&gt;
                &lt;s:item&gt;queue&lt;/s:item&gt;
                &lt;s:item&gt;restrictToHost&lt;/s:item&gt;
                &lt;s:item&gt;source&lt;/s:item&gt;
                &lt;s:item&gt;sourcetype&lt;/s:item&gt;
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
        &lt;s:key name="group"&gt;listenerports&lt;/s:key&gt;
        &lt;s:key name="index"&gt;default&lt;/s:key&gt;
        &lt;s:key name="restrictToHost"&gt;fwd1.splunk.com&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/inputs/tcp/cooked/{name}

Updates the container for managaing cooked data.

	[POST] data/inputs/tcp/cooked/{name}

### Parameters

SSL
: _Optional_ **INHERITED** INHERITED

connection_host
: _Optional_ **INHERITED** INHERITED

disabled
: _Optional_ **INHERITED** INHERITED

host
: _Optional_ **INHERITED** INHERITED

restrictToHost
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
| **403** | Insufficient permissions to edit input. |
|--------------------------------
| **404** | Input does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Restrict the cooked TCP input listening on port 9998 to only accept data from the host "tiny".

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/nobody/search/data/inputs/tcp/cooked/9998 \
	-d restrictToHost=tiny
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;cooked&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/inputs/tcp/cooked&lt;/id&gt;
  &lt;updated&gt;2011-07-10T14:52:54-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/cooked/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/cooked/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

<a name='datainputstcpcookednameconnections'/>

## data/inputs/tcp/cooked/{name}/connections

Retrieves list of active connections to the named port.

	[GET] data/inputs/tcp/cooked/{name}/connections

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed connections successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view input's connections. |
|--------------------------------
| **404** | TCP input does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Displays all connections to this cooked TCP input.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/servicesNS/nobody/search/data/inputs/tcp/cooked/9998/connections
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:s="http://dev.splunk.com/ns/rest"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;cooked&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/inputs/tcp/cooked&lt;/id&gt;
  &lt;updated&gt;2011-07-13T14:55:18-0700&lt;/updated&gt;
  &lt;generator version="101277"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/cooked/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/cooked/_reload" rel="_reload"/&gt;
  &lt;opensearch:totalResults&gt;1&lt;/opensearch:totalResults&gt;
  &lt;opensearch:itemsPerPage&gt;30&lt;/opensearch:itemsPerPage&gt;
  &lt;opensearch:startIndex&gt;0&lt;/opensearch:startIndex&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;Cooked:9998:127.0.0.1:20089&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/inputs/tcp/cooked/Cooked%3A9998%3A127.0.0.1%3A20089&lt;/id&gt;
    &lt;updated&gt;2011-07-13T14:55:18-0700&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/cooked/Cooked%3A9998%3A127.0.0.1%3A20089" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/cooked/Cooked%3A9998%3A127.0.0.1%3A20089" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/cooked/Cooked%3A9998%3A127.0.0.1%3A20089/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/cooked/Cooked%3A9998%3A127.0.0.1%3A20089" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/cooked/Cooked%3A9998%3A127.0.0.1%3A20089" rel="remove"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="connection"&gt;9998:127.0.0.1:20089&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="servername"&gt;fool03.splunk.com&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

<a name='datainputstcpraw'/>

## data/inputs/tcp/raw

Returns information about all raw TCP inputs.

	[GET] data/inputs/tcp/raw

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
| **403** | Insufficient permissions to view input. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Display all raw TCP inputs in this Splunk instance.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/data/inputs/tcp/raw
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;raw&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/data/inputs/tcp/raw&lt;/id&gt;
  &lt;updated&gt;2011-07-08T02:30:30-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/data/inputs/tcp/raw/_new" rel="create"/&gt;
  &lt;link href="/services/data/inputs/tcp/raw/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;44000&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/inputs/tcp/raw/44000&lt;/id&gt;
    &lt;updated&gt;2011-07-08T02:30:30-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/raw/44000" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/raw/44000" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/raw/44000/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/raw/44000" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/raw/44000" rel="remove"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/raw/44000/connections" rel="connections"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/raw/44000/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="_rcvbuf"&gt;1572864&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="group"&gt;listenerports&lt;/s:key&gt;
        &lt;s:key name="host"&gt;MrT&lt;/s:key&gt;
        &lt;s:key name="index"&gt;default&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/inputs/tcp/raw

Creates a new data input for accepting raw TCP data.

	[POST] data/inputs/tcp/raw

### Parameters

SSL
: _Optional_ **Boolean** 

connection_host
: _Optional_ **Enum** Valid values: (ip &#124; dns &#124; none)<br/><br/>Specify the remote server that is the connection host.<br/><br/>ip: specifies the IP address of the remote server. <br/><br/>dns: sets the host to the DNS entry of the remote server.<br/><br/>none: leaves the host as specified.

disabled
: _Optional_ **Boolean** Indicates whether the inputs are disabled.

host
: _Optional_ **String** The host from which the indexer gets data.

index
: _Optional_ **String** The index in which to store all generated events.

name
: _Required_ **String** The input port which splunk receives raw data in.

queue
: _Optional_ **Enum** Valid values: (parsingQueue &#124; indexQueue)<br/><br/>Specifies where the input processor should deposit the events it reads. Defaults to parsingQueue.<br/><br/>Set queue to <code>parsingQueue</code> to apply props.conf and other parsing rules to your data.  For more information about props.conf and rules for timestamping and linebreaking, refer to <code>props.conf</code> and the online documentation at [[Documentation:Data:Editinputs.conf]]<br/><br/>Set queue to <code>indexQueue</code> to send your data directly into the index.

restrictToHost
: _Optional_ **String** Allows for restricting this input to only accept data from the host specified here.

source
: _Optional_ **String** Sets the source key/field for events from this input. Defaults to the input file path.<br/><br/>Sets the source key's initial value. The key is used during parsing/indexing, in particular to set the source field during indexing. It is also the source field used at search time. As a convenience, the chosen string is prepended with 'source::'.<br/><br/>'''Note:''' Overriding the source key is generally not recommended.Typically, the input layer provides a more accurate string to aid in problem analysis and investigation, accurately recording the file from which the data was retreived. Consider use of source types, tagging, and search wildcards before overriding this value.

sourcetype
: _Optional_ **String** Set the source type for events from this input.<br/><br/>"sourcetype=" is automatically prepended to <string>.<br/><br/>Defaults to audittrail (if signedaudit=true) or fschange (if signedaudit=false).

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **201** | Created successfully. |
|--------------------------------
| **400** | Some arguments were invalid |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **402** | The Splunk license in use has disabled this feature. |
|--------------------------------
| **403** | Insufficient permissions to create input. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | There was an error; see body contents for messages |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Create a TCP input on port 44343 listening for raw data.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/nobody/search/data/inputs/tcp/raw \
	-d name=44343
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;raw&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/inputs/tcp/raw&lt;/id&gt;
  &lt;updated&gt;2011-07-08T02:30:30-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/raw/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/raw/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

<a name='datainputstcprawname'/>

## data/inputs/tcp/raw/{name}

Removes the raw inputs for port or host:port specified by <code>{name}</code>

	[DELETE] data/inputs/tcp/raw/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deleted successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to delete input. |
|--------------------------------
| **404** | Input does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Disable the raw TCP data input listening on port 44343.

#### Request
<pre class='terminal'>
curl -k -u admin:pass --request DELETE \
	https://localhost:8089/servicesNS/nobody/search/data/inputs/tcp/raw/44343
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;raw&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/inputs/tcp/raw&lt;/id&gt;
  &lt;updated&gt;2011-07-08T02:30:31-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/raw/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/raw/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## data/inputs/tcp/raw/{name}

Returns information about raw TCP input port <code>{name}</code>.

If port is restricted to a host, name should be URI-encoded host:port.

	[GET] data/inputs/tcp/raw/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | OK |
|--------------------------------
| **400** | ''TO DO: provide the rest of the status codes'' |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view input. |
|--------------------------------
| **404** | Input does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Display only the settings for the TCP data input port.
First request displays settings for TCP data input listening on port 44343.
Second request displays settings for TCP data input listening on port 9998
but restricting data from host host1.splunk.com.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/nobody/search/data/inputs/tcp/raw/44343
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;raw&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/inputs/tcp/raw&lt;/id&gt;
  &lt;updated&gt;2011-07-08T02:37:09-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/raw/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/raw/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;44343&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/inputs/tcp/raw/44343&lt;/id&gt;
    &lt;updated&gt;2011-07-08T02:37:09-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/raw/44343" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/raw/44343" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/raw/44343/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/raw/44343" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/raw/44343" rel="remove"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/raw/44343/connections" rel="connections"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/raw/44343/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="_rcvbuf"&gt;1572864&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:attributes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="optionalFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;SSL&lt;/s:item&gt;
                &lt;s:item&gt;connection_host&lt;/s:item&gt;
                &lt;s:item&gt;disabled&lt;/s:item&gt;
                &lt;s:item&gt;host&lt;/s:item&gt;
                &lt;s:item&gt;index&lt;/s:item&gt;
                &lt;s:item&gt;queue&lt;/s:item&gt;
                &lt;s:item&gt;restrictToHost&lt;/s:item&gt;
                &lt;s:item&gt;source&lt;/s:item&gt;
                &lt;s:item&gt;sourcetype&lt;/s:item&gt;
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
        &lt;s:key name="group"&gt;listenerports&lt;/s:key&gt;
        &lt;s:key name="host"&gt;MrT&lt;/s:key&gt;
        &lt;s:key name="index"&gt;default&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
curl -k -u admin:pass \
	https://localhost:8089/servicesNS/nobody/search/data/inputs/tcp/raw/host1.splunk.com%3A9998
&lt;feed xmlns="http://www.w3.org/2005/Atom" xmlns:s="http://dev.splunk.com/ns/rest" xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;raw&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/inputs/tcp/raw&lt;/id&gt;
  &lt;updated&gt;2011-07-14T11:28:39-0700&lt;/updated&gt;
  &lt;generator version="101277"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/raw/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/raw/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;host1.splunk.com:9998&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/data/inputs/tcp/raw/host1.splunk.com%3A9998&lt;/id&gt;
    &lt;updated&gt;2011-07-14T11:28:39-0700&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/data/inputs/tcp/raw/host1.splunk.com%3A9998" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/data/inputs/tcp/raw/host1.splunk.com%3A9998" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/inputs/tcp/raw/host1.splunk.com%3A9998/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/inputs/tcp/raw/host1.splunk.com%3A9998" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/inputs/tcp/raw/host1.splunk.com%3A9998" rel="remove"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/inputs/tcp/raw/host1.splunk.com%3A9998/connections" rel="connections"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/inputs/tcp/raw/host1.splunk.com%3A9998/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="_rcvbuf"&gt;1572864&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:attributes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="optionalFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;SSL&lt;/s:item&gt;
                &lt;s:item&gt;connection_host&lt;/s:item&gt;
                &lt;s:item&gt;disabled&lt;/s:item&gt;
                &lt;s:item&gt;host&lt;/s:item&gt;
                &lt;s:item&gt;index&lt;/s:item&gt;
                &lt;s:item&gt;queue&lt;/s:item&gt;
                &lt;s:item&gt;restrictToHost&lt;/s:item&gt;
                &lt;s:item&gt;source&lt;/s:item&gt;
                &lt;s:item&gt;sourcetype&lt;/s:item&gt;
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
        &lt;s:key name="group"&gt;listenerports&lt;/s:key&gt;
        &lt;s:key name="index"&gt;default&lt;/s:key&gt;
        &lt;s:key name="restrictToHost"&gt;host1.splunk.com&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/inputs/tcp/raw/{name}

Updates the container for managing raw data.

	[POST] data/inputs/tcp/raw/{name}

### Parameters

SSL
: _Optional_ **INHERITED** INHERITED

connection_host
: _Optional_ **INHERITED** INHERITED

disabled
: _Optional_ **INHERITED** INHERITED

host
: _Optional_ **INHERITED** INHERITED

index
: _Optional_ **INHERITED** INHERITED

queue
: _Optional_ **INHERITED** INHERITED

restrictToHost
: _Optional_ **INHERITED** INHERITED

source
: _Optional_ **INHERITED** INHERITED

sourcetype
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
| **403** | Insufficient permissions to edit input. |
|--------------------------------
| **404** | Inpuat does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Change the sourcetype to syslog for incoming events on the TCP data input listening on port 44343.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/nobody/search/data/inputs/tcp/raw/44343 \
	-d sourcetype=syslog
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;raw&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/inputs/tcp/raw&lt;/id&gt;
  &lt;updated&gt;2011-07-08T02:30:30-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/raw/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/tcp/raw/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

<a name='datainputstcprawnameconnections'/>

## data/inputs/tcp/raw/{name}/connections

View all connections to the named data input.

	[GET] data/inputs/tcp/raw/{name}/connections

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed connections successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view input's connections. |
|--------------------------------
| **404** | TCP input does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Displays all connections to this raw TCP input.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/data/inputs/tcp/raw/9998/connections
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:s="http://dev.splunk.com/ns/rest"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;raw&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/data/inputs/tcp/raw&lt;/id&gt;
  &lt;updated&gt;2011-07-13T16:14:33-07:00&lt;/updated&gt;
  &lt;generator version="103477"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/data/inputs/tcp/raw/_new" rel="create"/&gt;
  &lt;link href="/services/data/inputs/tcp/raw/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;Raw:9998:127.0.0.1&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/data/inputs/tcp/raw/Raw%3A9998%3A127.0.0.1&lt;/id&gt;
    &lt;updated&gt;2011-07-13T16:14:33-07:00&lt;/updated&gt;
    &lt;link href="/services/data/inputs/tcp/raw/Raw%3A9998%3A127.0.0.1" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/data/inputs/tcp/raw/Raw%3A9998%3A127.0.0.1" rel="list"/&gt;
    &lt;link href="/services/data/inputs/tcp/raw/Raw%3A9998%3A127.0.0.1/_reload" rel="_reload"/&gt;
    &lt;link href="/services/data/inputs/tcp/raw/Raw%3A9998%3A127.0.0.1" rel="edit"/&gt;
    &lt;link href="/services/data/inputs/tcp/raw/Raw%3A9998%3A127.0.0.1" rel="remove"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="connection"&gt;9998:127.0.0.1&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="servername"&gt;&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

<a name='datainputstcpssl'/>

## data/inputs/tcp/ssl

Returns SSL configuration. There is only one SSL configuration for all input ports.

	[GET] data/inputs/tcp/ssl

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
| **403** | Insufficient permissions to view inputs. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Return the SSL attributes for this instance of Splunk.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/data/inputs/tcp/ssl
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;ssl&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/data/inputs/tcp/ssl&lt;/id&gt;
  &lt;updated&gt;2011-07-12T15:02:58-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/data/inputs/tcp/ssl/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title/&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/data/inputs/tcp/ssl/&lt;/id&gt;
    &lt;updated&gt;2011-07-12T15:02:58-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/data/inputs/tcp/ssl/" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/data/inputs/tcp/ssl/" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/inputs/tcp/ssl//_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/inputs/tcp/ssl/" rel="edit"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="_rcvbuf"&gt;1572864&lt;/s:key&gt;
        &lt;s:key name="cipherSuite"&gt;ALL:!aNULL:!eNULL:!LOW:!EXP:RC4+RSA:+HIGH:+MEDIUM&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;1&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="host"&gt;ombroso-mbp15.splunk.com&lt;/s:key&gt;
        &lt;s:key name="index"&gt;default&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

<a name='datainputstcpsslname'/>

## data/inputs/tcp/ssl/{name}

Returns the SSL configuration for the host {name}.

	[GET] data/inputs/tcp/ssl/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view input. |
|--------------------------------
| **404** | Input does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Return the SSL attributes for tcp input. Note that "ssl" is the only valid name here.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/data/inputs/tcp/ssl/ssl
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;ssl&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/data/inputs/tcp/ssl&lt;/id&gt;
  &lt;updated&gt;2011-07-12T15:04:41-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/data/inputs/tcp/ssl/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title/&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/data/inputs/tcp/ssl/&lt;/id&gt;
    &lt;updated&gt;2011-07-12T15:04:41-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/data/inputs/tcp/ssl/" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/data/inputs/tcp/ssl/" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/inputs/tcp/ssl//_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/inputs/tcp/ssl/" rel="edit"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="_rcvbuf"&gt;1572864&lt;/s:key&gt;
        &lt;s:key name="cipherSuite"&gt;ALL:!aNULL:!eNULL:!LOW:!EXP:RC4+RSA:+HIGH:+MEDIUM&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;1&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="host"&gt;ombroso-mbp15.splunk.com&lt;/s:key&gt;
        &lt;s:key name="index"&gt;default&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/inputs/tcp/ssl/{name}

Configures SSL attributes for the host {name}.

	[POST] data/inputs/tcp/ssl/{name}

### Parameters

disabled
: _Optional_ **Boolean** Indicates whether the inputs are disabled.

password
: _Optional_ **String** Server certifcate password, if any.

requireClientCert
: _Optional_ **Boolean** Determines whether a client must authenticate.

rootCA
: _Optional_ **String** Certificate authority list (root file)

serverCert
: _Optional_ **String** Full path to the server certificate.

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
| **403** | Insufficient permissions to edit input. |
|--------------------------------
| **404** | Input does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Disable inputs for this SSL server configuration. Note that "ssl" is the only valid name here.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/data/inputs/tcp/ssl/ssl \
	-d disabled=true
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;ssl&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/data/inputs/tcp/ssl&lt;/id&gt;
  &lt;updated&gt;2011-07-12T15:05:42-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/data/inputs/tcp/ssl/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

<a name='datainputsudp'/>

## data/inputs/udp

List enabled and disabled UDP data inputs.

	[GET] data/inputs/udp

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
| **403** | Insufficient permissions to view inputs. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Returns a list of configured UDP data inputs.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/data/inputs/udp
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;udp&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/data/inputs/udp&lt;/id&gt;
  &lt;updated&gt;2011-07-08T14:11:57-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/data/inputs/udp/_new" rel="create"/&gt;
  &lt;link href="/services/data/inputs/udp/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;44000&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/inputs/udp/44000&lt;/id&gt;
    &lt;updated&gt;2011-07-08T14:11:57-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/udp/44000" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/udp/44000" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/udp/44000/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/udp/44000" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/udp/44000" rel="remove"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/udp/44000/connections" rel="connections"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/udp/44000/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="_rcvbuf"&gt;1572864&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="group"&gt;listenerports&lt;/s:key&gt;
        &lt;s:key name="host"&gt;MrT&lt;/s:key&gt;
        &lt;s:key name="index"&gt;default&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/inputs/udp

Create a new UDP data input.

	[POST] data/inputs/udp

### Parameters

connection_host
: _Optional_ **Enum** Valid values: (ip &#124; dns &#124; none)<br/><br/>ip: The <code>host</code> field for incoming events is set to the IP address of the remote server.  <br/><br/>dns: The <code>host</code> field is set to the DNS entry of the remote server.  <br/><br/>none: The <code>host</code> field remains unchanged.  <br/><br/>Defaults to <code>ip</code>.

host
: _Optional_ **String** The value to populate in the host field for incoming events.

index
: _Optional_ **String** Which index events from this input should be stored in.

name
: _Required_ **String** The UDP port that this input should listen on.

no_appending_timestamp
: _Optional_ **Boolean** If set to true, prevents Splunk from prepending a timestamp and hostname to incoming events.

no_priority_stripping
: _Optional_ **Boolean** If set to true, Splunk will not remove the priority field from incoming syslog events.

queue
: _Optional_ **String** Which queue events from this input should be sent to.  Generally this does not need to be changed.

source
: _Optional_ **String** The value to populate in the source field for incoming events.  The same source should not be used for multiple data inputs.

sourcetype
: _Optional_ **String** The value to populate in the sourcetype field for incoming events.

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
| **403** | Insufficient permissions to create input. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Creates a UDP data input listening on port 44321.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/nobody/search/data/inputs/udp \
	-d name=44321
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;udp&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/inputs/udp&lt;/id&gt;
  &lt;updated&gt;2011-07-08T14:12:13-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/udp/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/udp/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

<a name='datainputsudpname'/>

## data/inputs/udp/{name}

Disable the named UDP data input and remove it from the configuration.

	[DELETE] data/inputs/udp/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deleted successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to delete input. |
|--------------------------------
| **404** | Input does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Removes the UDP data input listening on port 44321.

#### Request
<pre class='terminal'>
curl -k -u admin:pass --request DELETE \
	https://localhost:8089/servicesNS/nobody/search/data/inputs/udp/44321
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;udp&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/inputs/udp&lt;/id&gt;
  &lt;updated&gt;2011-07-08T14:12:53-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/udp/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/udp/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## data/inputs/udp/{name}

List the properties of a single UDP data input port or host:port <code>{name}</code>.
If port is restricted to a host, name should be URI-encoded host:port.

	[GET] data/inputs/udp/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view input configuration. |
|--------------------------------
| **404** | Input does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Returns only configuration information for the UDP data input port.
First request displays settings for UDP data input listening on port 44321.
Second request displays settings for UDP data input listening on port 9997
but restricting data from host host1.splunk.com.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/nobody/search/data/inputs/udp/44321
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;udp&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/inputs/udp&lt;/id&gt;
  &lt;updated&gt;2011-07-08T14:12:27-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/udp/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/udp/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;44321&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/inputs/udp/44321&lt;/id&gt;
    &lt;updated&gt;2011-07-08T14:12:27-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/udp/44321" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/udp/44321" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/udp/44321/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/udp/44321" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/udp/44321" rel="remove"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/udp/44321/connections" rel="connections"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/udp/44321/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="_rcvbuf"&gt;1572864&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:attributes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="optionalFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;connection_host&lt;/s:item&gt;
                &lt;s:item&gt;host&lt;/s:item&gt;
                &lt;s:item&gt;index&lt;/s:item&gt;
                &lt;s:item&gt;no_appending_timestamp&lt;/s:item&gt;
                &lt;s:item&gt;no_priority_stripping&lt;/s:item&gt;
                &lt;s:item&gt;queue&lt;/s:item&gt;
                &lt;s:item&gt;source&lt;/s:item&gt;
                &lt;s:item&gt;sourcetype&lt;/s:item&gt;
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
        &lt;s:key name="group"&gt;listenerports&lt;/s:key&gt;
        &lt;s:key name="host"&gt;MrT&lt;/s:key&gt;
        &lt;s:key name="index"&gt;default&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
curl -k -u admin:pass \
	https://localhost:8089/servicesNS/nobody/search/data/inputs/udp/host1.splunk.com%3A9997
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:s="http://dev.splunk.com/ns/rest"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;udp&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/inputs/udp&lt;/id&gt;
  &lt;updated&gt;2011-07-14T11:40:20-0700&lt;/updated&gt;
  &lt;generator version="101277"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/udp/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/udp/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;host1.splunk.com:9997&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/data/inputs/udp/host1.splunk.com%3A9997&lt;/id&gt;
    &lt;updated&gt;2011-07-14T11:40:20-0700&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/data/inputs/udp/host1.splunk.com%3A9997" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/data/inputs/udp/host1.splunk.com%3A9997" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/inputs/udp/host1.splunk.com%3A9997/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/inputs/udp/host1.splunk.com%3A9997" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/inputs/udp/host1.splunk.com%3A9997" rel="remove"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/inputs/udp/host1.splunk.com%3A9997/connections" rel="connections"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/inputs/udp/host1.splunk.com%3A9997/enable" rel="enable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="_rcvbuf"&gt;1572864&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;1&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:attributes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="optionalFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;connection_host&lt;/s:item&gt;
                &lt;s:item&gt;disabled&lt;/s:item&gt;
                &lt;s:item&gt;host&lt;/s:item&gt;
                &lt;s:item&gt;index&lt;/s:item&gt;
                &lt;s:item&gt;no_appending_timestamp&lt;/s:item&gt;
                &lt;s:item&gt;no_priority_stripping&lt;/s:item&gt;
                &lt;s:item&gt;queue&lt;/s:item&gt;
                &lt;s:item&gt;source&lt;/s:item&gt;
                &lt;s:item&gt;sourcetype&lt;/s:item&gt;
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
        &lt;s:key name="index"&gt;default&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/inputs/udp/{name}

Edit properties of the named UDP data input.

	[POST] data/inputs/udp/{name}

### Parameters

connection_host
: _Optional_ **INHERITED** INHERITED

host
: _Optional_ **INHERITED** INHERITED

index
: _Optional_ **INHERITED** INHERITED

no_appending_timestamp
: _Optional_ **INHERITED** INHERITED

no_priority_stripping
: _Optional_ **INHERITED** INHERITED

queue
: _Optional_ **INHERITED** INHERITED

source
: _Optional_ **INHERITED** INHERITED

sourcetype
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
| **403** | Insufficient permissions to edit input. |
|--------------------------------
| **404** | Input does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Changes the sourcetype for incoming events to "syslog" for the UDP data input listening on port 44321.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/nobody/search/data/inputs/udp/44321 \
	-d sourcetype=syslog
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;udp&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/inputs/udp&lt;/id&gt;
  &lt;updated&gt;2011-07-08T14:12:47-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/udp/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/udp/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

<a name='datainputsudpnameconnections'/>

## data/inputs/udp/{name}/connections

Lists connections to the named UDP input.

	[GET] data/inputs/udp/{name}/connections

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed connections successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view input connections. |
|--------------------------------
| **404** | UDP input does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Returns a list of connections to the UDP input listening on port 9998.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/servicesNS/nobody/search/data/inputs/udp/9998/connections
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:s="http://dev.splunk.com/ns/rest"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;udp&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/inputs/udp&lt;/id&gt;
  &lt;updated&gt;2011-07-13T17:08:18-07:00&lt;/updated&gt;
  &lt;generator version="103477"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/udp/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/udp/_reload" rel="_reload"/&gt;
  &lt;opensearch:totalResults&gt;1&lt;/opensearch:totalResults&gt;
  &lt;opensearch:itemsPerPage&gt;30&lt;/opensearch:itemsPerPage&gt;
  &lt;opensearch:startIndex&gt;0&lt;/opensearch:startIndex&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;127.0.0.1&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/inputs/udp/127.0.0.1&lt;/id&gt;
    &lt;updated&gt;2011-07-13T17:08:18-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/udp/127.0.0.1" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/udp/127.0.0.1" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/udp/127.0.0.1/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/udp/127.0.0.1" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/udp/127.0.0.1" rel="remove"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="group"&gt;hosts&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

<a name='datainputswineventlogcollections'/>

## data/inputs/win-event-log-collections

Retrieves a list of configured event log collections.

	[GET] data/inputs/win-event-log-collections

### Parameters

count
: _Optional_ **Number** Maximum number of items to return.

lookup_host
: _Optional_ **String** For internal use.  Used by the UI when editing the initial host from which we gather event log data.

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
| **403** | Insufficient permissions to view event log collections. |
|--------------------------------
| **404** | Event log collection does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Provides information on all Windows event log collection inputs for monitoring by this Splunk instance.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/data/inputs/win-event-log-collections
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;win-event-log-collections&lt;/title&gt;
  &lt;id&gt;https://10.1.5.157:8089/services/data/inputs/win-event-log-collections&lt;/id&gt;
  &lt;updated&gt;2011-07-27T11:26:47-07:00&lt;/updated&gt;
  &lt;generator version="103620"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/data/inputs/win-event-log-collections/_new" rel="create"/&gt;
  &lt;link href="/services/data/inputs/win-event-log-collections/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;localhost&lt;/title&gt;
    &lt;id&gt;https://10.1.5.157:8089/servicesNS/nobody/windows/data/inputs/win-event-log-collections/localhost&lt;/id&gt;
    &lt;updated&gt;2011-07-27T11:26:47-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/win-event-log-collections/localhost" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/win-event-log-collections/localhost" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/win-event-log-collections/localhost/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/win-event-log-collections/localhost" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/win-event-log-collections/localhost/enable" rel="enable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="disabled"&gt;1&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="hosts"&gt;localhost&lt;/s:key&gt;
        &lt;s:key name="index"&gt;default&lt;/s:key&gt;
        &lt;s:key name="logs"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;Application&lt;/s:item&gt;
            &lt;s:item&gt;ForwardedEvents&lt;/s:item&gt;
            &lt;s:item&gt;HardwareEvents&lt;/s:item&gt;
            &lt;s:item&gt;Internet Explorer&lt;/s:item&gt;
            &lt;s:item&gt;Security&lt;/s:item&gt;
            &lt;s:item&gt;Setup&lt;/s:item&gt;
            &lt;s:item&gt;System&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/inputs/win-event-log-collections

Creates of modifies existing event log collection settings.  You can configure both native and WMI collection with this endpoint.

	[POST] data/inputs/win-event-log-collections

### Parameters

hosts
: _Optional_ **String** A comma-separated list of addtional hosts to be used for monitoring.  The first host should be specified with "lookup_host", and the additional ones using this parameter.

index
: _Optional_ **String** The index in which to store the gathered data.

logs
: _Optional_ **String** A comma-separated list of event log names to gather data from.

lookup_host
: _Required_ **String** This is a host from which we will monitor log events.  To specify additional hosts to be monitored via WMI, use the "hosts" parameter.

name
: _Required_ **String** This is the name of the collection.  This name will appear in configuration file, as well as the source and the sourcetype of the indexed data.  If the value is "localhost", it will use native event log collection; otherwise, it will use WMI.

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
| **403** | Insufficient permissions to create event log collections. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Creates a new event log monitoring collection named mylogs on the localhost, monitoring the Application and the System event logs.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/servicesNS/nobody/search/data/inputs/win-event-log-collections \
	-d lookup_host=localhost \
	-d name=mylogs \
	-d logs=Application,System
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;win-event-log-collections&lt;/title&gt;
  &lt;id&gt;https://10.1.5.157:8089/servicesNS/nobody/search/data/inputs/win-event-log-collections&lt;/id&gt;
  &lt;updated&gt;2011-07-27T11:56:24-07:00&lt;/updated&gt;
  &lt;generator version="103620"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/win-event-log-collections/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/win-event-log-collections/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;localhost&lt;/title&gt;
    &lt;id&gt;https://10.1.5.157:8089/servicesNS/nobody/windows/data/inputs/win-event-log-collections/localhost&lt;/id&gt;
    &lt;updated&gt;2011-07-27T11:56:24-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/win-event-log-collections/localhost" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/win-event-log-collections/localhost" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/win-event-log-collections/localhost/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/win-event-log-collections/localhost" rel="edit"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="disabled"&gt;1&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="hosts"&gt;localhost&lt;/s:key&gt;
        &lt;s:key name="index"&gt;default&lt;/s:key&gt;
        &lt;s:key name="logs"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;Application&lt;/s:item&gt;
            &lt;s:item&gt;ForwardedEvents&lt;/s:item&gt;
            &lt;s:item&gt;HardwareEvents&lt;/s:item&gt;
            &lt;s:item&gt;Internet Explorer&lt;/s:item&gt;
            &lt;s:item&gt;Security&lt;/s:item&gt;
            &lt;s:item&gt;Setup&lt;/s:item&gt;
            &lt;s:item&gt;System&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
        &lt;s:key name="lookup_host"&gt;localhost&lt;/s:key&gt;
        &lt;s:key name="name"&gt;localhost&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

<a name='datainputswineventlogcollectionsname'/>

## data/inputs/win-event-log-collections/{name}

Deletes a given event log collection.

	[DELETE] data/inputs/win-event-log-collections/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deleted successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to delete event log collections. |
|--------------------------------
| **404** | Event log collection does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Deletes the existing mylogs event log collection.

#### Request
<pre class='terminal'>
curl -k -u admin:pass --request DELETE \
	https://localhost:8089/servicesNS/nobody/search/data/inputs/win-event-log-collections/mylogs
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;win-event-log-collections&lt;/title&gt;
  &lt;id&gt;https://10.1.5.157:8089/servicesNS/nobody/search/data/inputs/win-event-log-collections&lt;/id&gt;
  &lt;updated&gt;2011-07-27T13:45:24-07:00&lt;/updated&gt;
  &lt;generator version="103620"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/win-event-log-collections/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/win-event-log-collections/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## data/inputs/win-event-log-collections/{name}

Gets the configuration settings for a given event log collection.

	[GET] data/inputs/win-event-log-collections/{name}

### Parameters

lookup_host
: _Optional_ **String** For internal use.  Used by the UI when editing the initial host from which we gather event log data.

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view event log collections. |
|--------------------------------
| **404** | Event log collection does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Gets information about a given event log collection.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/servicesNS/nobody/search/data/inputs/win-event-log-collections/mylogs
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;win-event-log-collections&lt;/title&gt;
  &lt;id&gt;https://10.1.5.157:8089/servicesNS/nobody/search/data/inputs/win-event-log-collections&lt;/id&gt;
  &lt;updated&gt;2011-07-27T12:00:38-07:00&lt;/updated&gt;
  &lt;generator version="103620"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/win-event-log-collections/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/win-event-log-collections/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;mylogs&lt;/title&gt;
    &lt;id&gt;https://10.1.5.157:8089/servicesNS/nobody/search/data/inputs/win-event-log-collections/mylogs&lt;/id&gt;
    &lt;updated&gt;2011-07-27T12:00:38-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/win-event-log-collections/mylogs" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/win-event-log-collections/mylogs" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/win-event-log-collections/mylogs/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/win-event-log-collections/mylogs" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/win-event-log-collections/mylogs" rel="remove"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/win-event-log-collections/mylogs/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:attributes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="optionalFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;hosts&lt;/s:item&gt;
                &lt;s:item&gt;index&lt;/s:item&gt;
                &lt;s:item&gt;logs&lt;/s:item&gt;
              &lt;/s:list&gt;
            &lt;/s:key&gt;
            &lt;s:key name="requiredFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;lookup_host&lt;/s:item&gt;
              &lt;/s:list&gt;
            &lt;/s:key&gt;
            &lt;s:key name="wildcardFields"&gt;
              &lt;s:list/&gt;
            &lt;/s:key&gt;
          &lt;/s:dict&gt;
        &lt;/s:key&gt;
        &lt;s:key name="hosts"/&gt;
        &lt;s:key name="index"&gt;default&lt;/s:key&gt;
        &lt;s:key name="logs"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;Application,System&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
        &lt;s:key name="lookup_host"&gt;localhost&lt;/s:key&gt;
        &lt;s:key name="name"&gt;mylogs&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/inputs/win-event-log-collections/{name}

Modifies existing event log collection.

	[POST] data/inputs/win-event-log-collections/{name}

### Parameters

hosts
: _Optional_ **INHERITED** INHERITED

index
: _Optional_ **INHERITED** INHERITED

logs
: _Optional_ **INHERITED** INHERITED

lookup_host
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
| **403** | Insufficient permissions to edit event log collections. |
|--------------------------------
| **404** | Event log collection does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Modifies the mylogs collection by making it monitor the Application log only.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/servicesNS/nobody/search/data/inputs/win-event-log-collections/mylogs \
	-d lookup_host=localhost \
	-d logs=Application
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;win-event-log-collections&lt;/title&gt;
  &lt;id&gt;https://10.1.5.157:8089/servicesNS/nobody/search/data/inputs/win-event-log-collections&lt;/id&gt;
  &lt;updated&gt;2011-07-27T13:43:46-07:00&lt;/updated&gt;
  &lt;generator version="103620"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/win-event-log-collections/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/win-event-log-collections/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;localhost&lt;/title&gt;
    &lt;id&gt;https://10.1.5.157:8089/servicesNS/nobody/windows/data/inputs/win-event-log-collections/localhost&lt;/id&gt;
    &lt;updated&gt;2011-07-27T13:43:46-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/win-event-log-collections/localhost" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/win-event-log-collections/localhost" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/win-event-log-collections/localhost/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/win-event-log-collections/localhost" rel="edit"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="disabled"&gt;1&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="hosts"&gt;localhost&lt;/s:key&gt;
        &lt;s:key name="index"&gt;default&lt;/s:key&gt;
        &lt;s:key name="logs"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;Application&lt;/s:item&gt;
            &lt;s:item&gt;ForwardedEvents&lt;/s:item&gt;
            &lt;s:item&gt;HardwareEvents&lt;/s:item&gt;
            &lt;s:item&gt;Internet Explorer&lt;/s:item&gt;
            &lt;s:item&gt;Security&lt;/s:item&gt;
            &lt;s:item&gt;Setup&lt;/s:item&gt;
            &lt;s:item&gt;System&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
        &lt;s:key name="lookup_host"&gt;localhost&lt;/s:key&gt;
        &lt;s:key name="name"&gt;localhost&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

<a name='datainputswinperfmon'/>

## data/inputs/win-perfmon

Gets current performance monitoring configuration.

	[GET] data/inputs/win-perfmon

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
| **403** | Insufficient permissions to view performance monitoring configuration. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Lists all configured perfmon inputs.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/data/inputs/win-perfmon
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;win-perfmon&lt;/title&gt;
  &lt;id&gt;https://10.1.5.157:8089/services/data/inputs/win-perfmon&lt;/id&gt;
  &lt;updated&gt;2011-07-29T19:42:06-07:00&lt;/updated&gt;
  &lt;generator version="104976"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/data/inputs/win-perfmon/_new" rel="create"/&gt;
  &lt;link href="/services/data/inputs/win-perfmon/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;Available Memory&lt;/title&gt;
    &lt;id&gt;https://10.1.5.157:8089/servicesNS/nobody/windows/data/inputs/win-perfmon/Available%20Memory&lt;/id&gt;
    &lt;updated&gt;2011-07-29T19:42:06-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/win-perfmon/Available%20Memory" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/win-perfmon/Available%20Memory" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/win-perfmon/Available%20Memory/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/win-perfmon/Available%20Memory" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/win-perfmon/Available%20Memory/enable" rel="enable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="counters"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;Available Bytes&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;1&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="index"&gt;default&lt;/s:key&gt;
        &lt;s:key name="instances"&gt;
          &lt;s:list/&gt;
        &lt;/s:key&gt;
        &lt;s:key name="interval"&gt;10&lt;/s:key&gt;
        &lt;s:key name="object"&gt;Memory&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/inputs/win-perfmon

Creates new or modifies existing performance monitoring collection settings.

	[POST] data/inputs/win-perfmon

### Parameters

counters
: _Optional_ **String** A comma-separated list of all counters to monitor. A '*' is equivalent to all counters.

disabled
: _Optional_ **Number** Disables a given monitoring stanza.

index
: _Optional_ **String** The index in which to store the gathered data.

instances
: _Optional_ **String** Comma-separated list of counter instances.  A '*' is equivalent to all instances.

interval
: _Required_ **Number** How frequently to poll the performance counters.

name
: _Required_ **String** This is the name of the collection.  This name will appear in configuration file, as well as the source and the sourcetype of the indexed data.

object
: _Required_ **String** A valid performance monitor object (for example, 'Process,' 'Server,' 'PhysicalDisk.')

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
| **403** | Insufficient permissions to create monitoring stanza. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Creates a memory monitoring stanza.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/nobody/search/data/inputs/win-perfmon \
	-d interval=4 \
	-d name=mymemory \
	-d object=Memory
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;win-perfmon&lt;/title&gt;
  &lt;id&gt;https://10.1.5.157:8089/servicesNS/nobody/search/data/inputs/win-perfmon&lt;/id&gt;
  &lt;updated&gt;2011-07-29T19:40:38-07:00&lt;/updated&gt;
  &lt;generator version="104976"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/win-perfmon/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/win-perfmon/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;Available Memory&lt;/title&gt;
    &lt;id&gt;https://10.1.5.157:8089/servicesNS/nobody/windows/data/inputs/win-perfmon/Available%20Memory&lt;/id&gt;
    &lt;updated&gt;2011-07-29T19:40:38-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/win-perfmon/Available%20Memory" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/win-perfmon/Available%20Memory" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/win-perfmon/Available%20Memory/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/win-perfmon/Available%20Memory" rel="edit"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="counters"&gt;Available Bytes&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;1&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="instances"/&gt;
        &lt;s:key name="interval"&gt;10&lt;/s:key&gt;
        &lt;s:key name="object"&gt;Memory&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

<a name='datainputswinperfmonname'/>

## data/inputs/win-perfmon/{name}

Deletes a given monitoring stanza.

	[DELETE] data/inputs/win-perfmon/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deleted successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to delete monitoring stanza. |
|--------------------------------
| **404** | Monitoring stanza does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Deletes a given perfmon stanza.

#### Request
<pre class='terminal'>
curl -k -u admin:pass --request DELETE \
	https://localhost:8089/servicesNS/nobody/search/data/inputs/win-perfmon/mymemory
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;win-perfmon&lt;/title&gt;
  &lt;id&gt;https://10.1.5.157:8089/servicesNS/nobody/search/data/inputs/win-perfmon&lt;/id&gt;
  &lt;updated&gt;2011-07-29T19:47:06-07:00&lt;/updated&gt;
  &lt;generator version="104976"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/win-perfmon/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/win-perfmon/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## data/inputs/win-perfmon/{name}

Gets settings for a given perfmon stanza.

	[GET] data/inputs/win-perfmon/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view configuration settings. |
|--------------------------------
| **404** | Performance stanza does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Lists a given perfmon stanza.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/servicesNS/nobody/search/data/inputs/win-perfmon/mymemory
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;win-perfmon&lt;/title&gt;
  &lt;id&gt;https://10.1.5.157:8089/servicesNS/nobody/search/data/inputs/win-perfmon&lt;/id&gt;
  &lt;updated&gt;2011-07-29T19:44:21-07:00&lt;/updated&gt;
  &lt;generator version="104976"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/win-perfmon/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/win-perfmon/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;mymemory&lt;/title&gt;
    &lt;id&gt;https://10.1.5.157:8089/servicesNS/nobody/search/data/inputs/win-perfmon/mymemory&lt;/id&gt;
    &lt;updated&gt;2011-07-29T19:44:21-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/win-perfmon/mymemory" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/win-perfmon/mymemory" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/win-perfmon/mymemory/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/win-perfmon/mymemory" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/win-perfmon/mymemory" rel="remove"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/win-perfmon/mymemory/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="counters"&gt;
          &lt;s:list/&gt;
        &lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:attributes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="optionalFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;counters&lt;/s:item&gt;
                &lt;s:item&gt;disabled&lt;/s:item&gt;
                &lt;s:item&gt;index&lt;/s:item&gt;
                &lt;s:item&gt;instances&lt;/s:item&gt;
                &lt;s:item&gt;interval&lt;/s:item&gt;
                &lt;s:item&gt;object&lt;/s:item&gt;
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
        &lt;s:key name="index"&gt;default&lt;/s:key&gt;
        &lt;s:key name="instances"&gt;
          &lt;s:list/&gt;
        &lt;/s:key&gt;
        &lt;s:key name="interval"&gt;4&lt;/s:key&gt;
        &lt;s:key name="object"&gt;Memory&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/inputs/win-perfmon/{name}

Modifies existing monitoring stanza

	[POST] data/inputs/win-perfmon/{name}

### Parameters

counters
: _Optional_ **INHERITED** INHERITED

disabled
: _Optional_ **INHERITED** INHERITED

index
: _Optional_ **INHERITED** INHERITED

instances
: _Optional_ **INHERITED** INHERITED

interval
: _Optional_ **INHERITED** INHERITED

object
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
| **403** | Insufficient permissions to edit monitoring stanza. |
|--------------------------------
| **404** | Monitoring stanza does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Modifies the interval of the given perfmon stanza.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/servicesNS/nobody/search/data/inputs/win-perfmon/mymemory \
	-d interval=10
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;win-perfmon&lt;/title&gt;
  &lt;id&gt;https://10.1.5.157:8089/servicesNS/nobody/search/data/inputs/win-perfmon&lt;/id&gt;
  &lt;updated&gt;2011-07-29T19:45:59-07:00&lt;/updated&gt;
  &lt;generator version="104976"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/win-perfmon/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/win-perfmon/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;Available Memory&lt;/title&gt;
    &lt;id&gt;https://10.1.5.157:8089/servicesNS/nobody/windows/data/inputs/win-perfmon/Available%20Memory&lt;/id&gt;
    &lt;updated&gt;2011-07-29T19:45:59-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/win-perfmon/Available%20Memory" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/win-perfmon/Available%20Memory" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/win-perfmon/Available%20Memory/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/win-perfmon/Available%20Memory" rel="edit"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="counters"&gt;Available Bytes&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;1&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="instances"/&gt;
        &lt;s:key name="interval"&gt;10&lt;/s:key&gt;
        &lt;s:key name="object"&gt;Memory&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

<a name='datainputswinwmicollections'/>

## data/inputs/win-wmi-collections

Provides access to all configure WMI collections.

	[GET] data/inputs/win-wmi-collections

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
| **403** | Insufficient permissions to view collections. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Lists all enabled or disabled WMI collection items.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/data/inputs/win-wmi-collections
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;win-wmi-collections&lt;/title&gt;
  &lt;id&gt;https://10.1.5.157:8089/services/data/inputs/win-wmi-collections&lt;/id&gt;
  &lt;updated&gt;2011-07-27T14:00:24-07:00&lt;/updated&gt;
  &lt;generator version="103620"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/data/inputs/win-wmi-collections/_new" rel="create"/&gt;
  &lt;link href="/services/data/inputs/win-wmi-collections/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;CPUTime&lt;/title&gt;
    &lt;id&gt;https://10.1.5.157:8089/servicesNS/nobody/windows/data/inputs/win-wmi-collections/CPUTime&lt;/id&gt;
    &lt;updated&gt;2011-07-27T14:00:24-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/win-wmi-collections/CPUTime" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/win-wmi-collections/CPUTime" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/win-wmi-collections/CPUTime/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/win-wmi-collections/CPUTime" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/win-wmi-collections/CPUTime/enable" rel="enable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="class"&gt;Win32_PerfFormattedData_PerfOS_Processor&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;1&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="fields"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;PercentProcessorTime&lt;/s:item&gt;
            &lt;s:item&gt;PercentUserTime&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
        &lt;s:key name="index"&gt;default&lt;/s:key&gt;
        &lt;s:key name="instances"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;_Total&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
        &lt;s:key name="interval"&gt;3&lt;/s:key&gt;
        &lt;s:key name="name"/&gt;
        &lt;s:key name="server"&gt;localhost&lt;/s:key&gt;
        &lt;s:key name="wql"&gt;SELECT PercentProcessorTime,PercentUserTime FROM Win32_PerfFormattedData_PerfOS_Processor WHERE Name=&amp;quot;_Total&amp;quot;&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/inputs/win-wmi-collections

Creates of modifies existing WMI collection settings.

	[POST] data/inputs/win-wmi-collections

### Parameters

classes
: _Required_ **String** A valid WMI class name.

disabled
: _Optional_ **Number** Disables the given collection.

fields
: _Optional_ **String** A comma-separated list of all properties that you want to gather from the given class.

index
: _Optional_ **String** The index in which to store the gathered data.

instances
: _Optional_ **String** A comma-separated list of all instances of a given class for which data is to be gathered.

interval
: _Required_ **Number** The interval at which the WMI provider(s) will be queried.

lookup_host
: _Required_ **String** This is the server from which we will be gathering WMI data.  If you need to gather data from more than one machine, additional servers can be specified in the 'server' parameter.

name
: _Required_ **String** This is the name of the collection.  This name will appear in configuration file, as well as the source and the sourcetype of the indexed data.

server
: _Optional_ **String** A comma-separated list of additional servers that you want to gather data from.  Use this if you need to gather from more than a single machine.  See also lookup_host parameter.

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
| **403** | Insufficient permissions to create this collection. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Creates a new WMI collection named cpu, which gathers CPU information from the class Win32_PerfFormattedData_PerfOS_Processor, with an interval of 5 from localhost.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/servicesNS/nobody/search/data/inputs/win-wmi-collections \
	-d classes=Win32_PerfFormattedData_PerfOS_Processor \
	-d interval=5 \
	-d lookup_host=localhost \
	-d name=cpu
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;win-wmi-collections&lt;/title&gt;
  &lt;id&gt;https://10.1.5.157:8089/servicesNS/nobody/search/data/inputs/win-wmi-collections&lt;/id&gt;
  &lt;updated&gt;2011-07-27T14:05:43-07:00&lt;/updated&gt;
  &lt;generator version="103620"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/win-wmi-collections/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/win-wmi-collections/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;CPUTime&lt;/title&gt;
    &lt;id&gt;https://10.1.5.157:8089/servicesNS/nobody/windows/data/inputs/win-wmi-collections/CPUTime&lt;/id&gt;
    &lt;updated&gt;2011-07-27T14:05:43-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/win-wmi-collections/CPUTime" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/win-wmi-collections/CPUTime" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/win-wmi-collections/CPUTime/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/windows/data/inputs/win-wmi-collections/CPUTime" rel="edit"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="disabled"&gt;1&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="index"&gt;default&lt;/s:key&gt;
        &lt;s:key name="interval"&gt;3&lt;/s:key&gt;
        &lt;s:key name="wql"&gt;SELECT PercentProcessorTime,PercentUserTime FROM Win32_PerfFormattedData_PerfOS_Processor WHERE Name=&amp;quot;_Total&amp;quot;&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

<a name='datainputswinwmicollectionsname'/>

## data/inputs/win-wmi-collections/{name}

Deletes a given collection.

	[DELETE] data/inputs/win-wmi-collections/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deleted successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to delete a given collection. |
|--------------------------------
| **404** | Given collection does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Deletes an existing WMI collection.

#### Request
<pre class='terminal'>
curl -k -u admin:pass --request DELETE \
	https://localhost:8089/servicesNS/nobody/search/data/inputs/win-wmi-collections/cpu
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;win-wmi-collections&lt;/title&gt;
  &lt;id&gt;https://10.1.5.157:8089/servicesNS/nobody/search/data/inputs/win-wmi-collections&lt;/id&gt;
  &lt;updated&gt;2011-07-27T14:21:17-07:00&lt;/updated&gt;
  &lt;generator version="103620"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/win-wmi-collections/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/win-wmi-collections/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## data/inputs/win-wmi-collections/{name}

Gets information about a single collection.

	[GET] data/inputs/win-wmi-collections/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view WMI collections. |
|--------------------------------
| **404** | Given collection does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Gets information about a given event log collection.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/servicesNS/nobody/search/data/inputs/win-wmi-collections/cpu
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;win-wmi-collections&lt;/title&gt;
  &lt;id&gt;https://10.1.5.157:8089/servicesNS/nobody/search/data/inputs/win-wmi-collections&lt;/id&gt;
  &lt;updated&gt;2011-07-27T14:09:39-07:00&lt;/updated&gt;
  &lt;generator version="103620"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/win-wmi-collections/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/win-wmi-collections/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;cpu&lt;/title&gt;
    &lt;id&gt;https://10.1.5.157:8089/servicesNS/nobody/search/data/inputs/win-wmi-collections/cpu&lt;/id&gt;
    &lt;updated&gt;2011-07-27T14:09:39-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/win-wmi-collections/cpu" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/win-wmi-collections/cpu" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/win-wmi-collections/cpu/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/win-wmi-collections/cpu" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/win-wmi-collections/cpu" rel="remove"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/win-wmi-collections/cpu/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="classes"&gt;Win32_PerfFormattedData_PerfOS_Processor&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:attributes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="optionalFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;disabled&lt;/s:item&gt;
                &lt;s:item&gt;fields&lt;/s:item&gt;
                &lt;s:item&gt;index&lt;/s:item&gt;
                &lt;s:item&gt;instances&lt;/s:item&gt;
                &lt;s:item&gt;server&lt;/s:item&gt;
              &lt;/s:list&gt;
            &lt;/s:key&gt;
            &lt;s:key name="requiredFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;classes&lt;/s:item&gt;
                &lt;s:item&gt;interval&lt;/s:item&gt;
                &lt;s:item&gt;lookup_host&lt;/s:item&gt;
              &lt;/s:list&gt;
            &lt;/s:key&gt;
            &lt;s:key name="wildcardFields"&gt;
              &lt;s:list/&gt;
            &lt;/s:key&gt;
          &lt;/s:dict&gt;
        &lt;/s:key&gt;
        &lt;s:key name="fields"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;*&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
        &lt;s:key name="index"&gt;default&lt;/s:key&gt;
        &lt;s:key name="instances"&gt;
          &lt;s:list/&gt;
        &lt;/s:key&gt;
        &lt;s:key name="interval"&gt;5&lt;/s:key&gt;
        &lt;s:key name="lookup_host"&gt;localhost&lt;/s:key&gt;
        &lt;s:key name="name"&gt;cpu&lt;/s:key&gt;
        &lt;s:key name="server"/&gt;
        &lt;s:key name="wql"&gt;Select * from Win32_PerfFormattedData_PerfOS_Processor&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/inputs/win-wmi-collections/{name}

Modifies a given WMI collection.

	[POST] data/inputs/win-wmi-collections/{name}

### Parameters

classes
: _Required_ **INHERITED** INHERITED

disabled
: _Optional_ **INHERITED** INHERITED

fields
: _Optional_ **INHERITED** INHERITED

index
: _Optional_ **INHERITED** INHERITED

instances
: _Optional_ **INHERITED** INHERITED

interval
: _Required_ **INHERITED** INHERITED

lookup_host
: _Required_ **INHERITED** INHERITED

server
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
| **403** | Insufficient permissions to edit collection. |
|--------------------------------
| **404** | Collection does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Modifies an existing WMI collection item with the given parameters.  The new setting requests monitoring of three different machines via the lookup_host and the server parameters.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/servicesNS/nobody/search/data/inputs/win-wmi-collections/cpu \
	-d classes=Win32_PerfFormattedData_PerfOS_Processor \
	-d interval=5 \
	-d lookup_host=localhost \
	-d server=10.1.5.157,10.1.5.158
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;win-wmi-collections&lt;/title&gt;
  &lt;id&gt;https://10.1.5.157:8089/servicesNS/nobody/search/data/inputs/win-wmi-collections&lt;/id&gt;
  &lt;updated&gt;2011-07-27T14:15:33-07:00&lt;/updated&gt;
  &lt;generator version="103620"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/win-wmi-collections/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/inputs/win-wmi-collections/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;cpu&lt;/title&gt;
    &lt;id&gt;https://10.1.5.157:8089/servicesNS/nobody/search/data/inputs/win-wmi-collections/cpu&lt;/id&gt;
    &lt;updated&gt;2011-07-27T14:15:33-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/win-wmi-collections/cpu" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/win-wmi-collections/cpu" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/win-wmi-collections/cpu/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/win-wmi-collections/cpu" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/inputs/win-wmi-collections/cpu" rel="remove"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="classes"&gt;Win32_PerfFormattedData_PerfOS_Processor&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="fields"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;*&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
        &lt;s:key name="index"&gt;default&lt;/s:key&gt;
        &lt;s:key name="instances"&gt;
          &lt;s:list/&gt;
        &lt;/s:key&gt;
        &lt;s:key name="interval"&gt;5&lt;/s:key&gt;
        &lt;s:key name="lookup_host"&gt;localhost&lt;/s:key&gt;
        &lt;s:key name="name"&gt;cpu&lt;/s:key&gt;
        &lt;s:key name="server"/&gt;
        &lt;s:key name="wql"&gt;Select * from Win32_PerfFormattedData_PerfOS_Processor&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

<a name='receiverssimple'/>

## receivers/simple

Create events from the contents contained in the HTTP body.

	[POST] receivers/simple

### Parameters

&lt;arbitrary_data&gt;
: _Required_ **String** Raw event text.  This will be the entirety of the HTTP request body.

host
: _Optional_ **String** The value to populate in the host field for events from this data input.

host_regex
: _Optional_ **String** A regular expression used to extract the host value from each event.

index
: _Optional_ **String** The index to send events from this input to.

source
: _Optional_ **String** The source value to fill in the metadata for this input's events.

sourcetype
: _Optional_ **String** The sourcetype to apply to events from this input.

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Data accepted. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **404** | Receiver does not exist. |
|--------------------------------

### Example

Sends an event with the "web_event" sourcetype and "www" source to this Splunk indexer.

#### Request
<pre class='terminal'>
curl -k -u admin:pass "https://localhost:8089/services/receivers/simple?source=www&amp;sourcetype=web_event \
	curl -k -u admin:pass "https://localhost:8089/services/receivers/simple?source=www&amp;sourcetype=web_event" \
	-d "Sun Jul 10 15:56:02 PDT 2011   User vishalp logged in successfully."
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;response&gt;
  &lt;results&gt;
    &lt;result&gt;
      &lt;field k="_index"&gt;
        &lt;value&gt;
          &lt;text&gt;default&lt;/text&gt;
        &lt;/value&gt;
      &lt;/field&gt;
      &lt;field k="bytes"&gt;
        &lt;value&gt;
          &lt;text&gt;67&lt;/text&gt;
        &lt;/value&gt;
      &lt;/field&gt;
      &lt;field k="host"&gt;
        &lt;value&gt;
          &lt;text&gt;127.0.0.1&lt;/text&gt;
        &lt;/value&gt;
      &lt;/field&gt;
      &lt;field k="source"&gt;
        &lt;value&gt;
          &lt;text&gt;www&lt;/text&gt;
        &lt;/value&gt;
      &lt;/field&gt;
      &lt;field k="sourcetype"&gt;
        &lt;value&gt;
          &lt;text&gt;web_event&lt;/text&gt;
        &lt;/value&gt;
      &lt;/field&gt;
    &lt;/result&gt;
  &lt;/results&gt;
&lt;/response&gt;
</code></pre>

<a name='receiversstream'/>

## receivers/stream

Create events from the stream of data following HTTP headers.

	[POST] receivers/stream

### Parameters

&lt;data_stream&gt;
: _Required_ **String** Raw event text.  This does not need to be presented as a complete HTTP request, but can be streamed in as data is available.

host
: _Optional_ **String** The value to populate in the host field for events from this data input.

host_regex
: _Optional_ **String** A regular expression used to extract the host value from each event.

index
: _Optional_ **String** The index to send events from this input to.

source
: _Optional_ **String** The source value to fill in the metadata for this input's events.

sourcetype
: _Optional_ **String** The sourcetype to apply to events from this input.

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Data accepted. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **404** | Receiver does not exist. |
|--------------------------------

### Example

Streams an arbitrary number of events to Splunk.  This example is best demonstrated via a program rather than a curl request.  Below is a short python script that runs indefinitely, until the user presses Ctrl-C.  In the meantime, it will send one event per second to Splunk.  Note that for a streaming connection, the "x-splunk-input-mode" header must be specified.

#### Request
<pre class='terminal'>
import httplib, time
conn = httplib.HTTPSConnection("localhost", 8089)
conn.connect()
conn.putrequest("POST", "/services/receivers/stream?source=www&amp;sourcetype=web_data")
conn.putheader("Authorization", "Basic YWRtaW46cGFzcw&amp;#61;&amp;#61;")
conn.putheader("x-splunk-input-mode", "streaming")
conn.endheaders()
print "Looping..."
while True:
    conn.send("%s A sample event.\n" % time.asctime())
    time.sleep(1)
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>

</code></pre>


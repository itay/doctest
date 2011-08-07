## configs/conf-{file}
{: name='configsconffile'}

Lists all stanzas contained in the named configuration file.

	[GET] configs/conf-{file}

### Parameters

count
: _Optional_ **Number** Maximum number of items to return.

offset
: _Optional_ **Number** Index for first item to return.

search
: _Optional_ **String** Boolean predicate to filter results.

sort_dir
: _Optional_ **String** Direction to sort by (asc/desc).

sort_key
: _Optional_ **String** Field to sort by.

sort_mode
: _Optional_ **String** Collating sequence for the sort (auto, alpha, alpha_case, num).

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view configuration file. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Displays the stanzas existing in props.conf.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/configs/conf-props
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;conf-props&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/configs/conf-props&lt;/id&gt;
  &lt;updated&gt;2011-07-08T01:01:26-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/configs/conf-props/_new" rel="create"/&gt;
  &lt;link href="/services/configs/conf-props/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;(?i)source::....zip(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/configs/conf-props/%28%3Fi%29source%3A%3A....zip%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T01:01:26-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/configs/conf-props/%28%3Fi%29source%3A%3A....zip%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/configs/conf-props/%28%3Fi%29source%3A%3A....zip%28.%5Cd%2B%29%3F" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/configs/conf-props/%28%3Fi%29source%3A%3A....zip%28.%5Cd%2B%29%3F/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/system/configs/conf-props/%28%3Fi%29source%3A%3A....zip%28.%5Cd%2B%29%3F" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/system/configs/conf-props/%28%3Fi%29source%3A%3A....zip%28.%5Cd%2B%29%3F/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="ANNOTATE_PUNCT"&gt;1&lt;/s:key&gt;
        &lt;s:key name="BREAK_ONLY_BEFORE"/&gt;
        &lt;s:key name="BREAK_ONLY_BEFORE_DATE"&gt;1&lt;/s:key&gt;
        &lt;s:key name="CHARSET"&gt;UTF-8&lt;/s:key&gt;
        &lt;s:key name="DATETIME_CONFIG"&gt;/etc/datetime.xml&lt;/s:key&gt;
        &lt;s:key name="HEADER_MODE"/&gt;
        &lt;s:key name="LEARN_SOURCETYPE"&gt;1&lt;/s:key&gt;
        &lt;s:key name="LINE_BREAKER_LOOKBEHIND"&gt;100&lt;/s:key&gt;
        &lt;s:key name="MAX_DAYS_AGO"&gt;2000&lt;/s:key&gt;
        &lt;s:key name="MAX_DAYS_HENCE"&gt;2&lt;/s:key&gt;
        &lt;s:key name="MAX_DIFF_SECS_AGO"&gt;3600&lt;/s:key&gt;
        &lt;s:key name="MAX_DIFF_SECS_HENCE"&gt;604800&lt;/s:key&gt;
        &lt;s:key name="MAX_EVENTS"&gt;256&lt;/s:key&gt;
        &lt;s:key name="MAX_TIMESTAMP_LOOKAHEAD"&gt;128&lt;/s:key&gt;
        &lt;s:key name="MUST_BREAK_AFTER"/&gt;
        &lt;s:key name="MUST_NOT_BREAK_AFTER"/&gt;
        &lt;s:key name="MUST_NOT_BREAK_BEFORE"/&gt;
        &lt;s:key name="NO_BINARY_CHECK"&gt;1&lt;/s:key&gt;
        &lt;s:key name="SEGMENTATION"&gt;indexing&lt;/s:key&gt;
        &lt;s:key name="SEGMENTATION-all"&gt;full&lt;/s:key&gt;
        &lt;s:key name="SEGMENTATION-inner"&gt;inner&lt;/s:key&gt;
        &lt;s:key name="SEGMENTATION-outer"&gt;outer&lt;/s:key&gt;
        &lt;s:key name="SEGMENTATION-raw"&gt;none&lt;/s:key&gt;
        &lt;s:key name="SEGMENTATION-standard"&gt;standard&lt;/s:key&gt;
        &lt;s:key name="SHOULD_LINEMERGE"&gt;1&lt;/s:key&gt;
        &lt;s:key name="TRANSFORMS"/&gt;
        &lt;s:key name="TRUNCATE"&gt;10000&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:appName"&gt;search&lt;/s:key&gt;
        &lt;s:key name="eai:userName"&gt;admin&lt;/s:key&gt;
        &lt;s:key name="maxDist"&gt;100&lt;/s:key&gt;
        &lt;s:key name="sourcetype"&gt;preprocess-zip&lt;/s:key&gt;
        &lt;s:key name="unarchive_cmd"&gt;_auto&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## configs/conf-{file}
{: name='configsconffile'}

Allows for creating the stanza specified by "name" in the configuration file specified by {file}.

	[POST] configs/conf-{file}

### Parameters

&lt;arbitrary_stanza&gt;
: _Required_ **String** This operation accepts an arbitrary set of key/value pairs to populate in the created stanza.  (There is no actual parameter named "arbitrary_stanza".)

name
: _Required_ **String** The name of the stanza to create.

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **201** | Created successfully. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to create configuration stanza. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Configures the sourcetype "myweblogs" in props.conf to use the UTF-8 character set and disable line-merging.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/nobody/search/configs/conf-props \
	-d name=myweblogs \
	-d CHARSET=UTF-8 \
	-d SHOULD_LINEMERGE=false
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;conf-props&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/configs/conf-props&lt;/id&gt;
  &lt;updated&gt;2011-07-08T01:01:26-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/configs/conf-props/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/configs/conf-props/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;myweblogs&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/configs/conf-props/myweblogs&lt;/id&gt;
    &lt;updated&gt;2011-07-08T01:01:26-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/search/configs/conf-props/myweblogs" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/search/configs/conf-props/myweblogs" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/search/configs/conf-props/myweblogs/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/search/configs/conf-props/myweblogs" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/search/configs/conf-props/myweblogs" rel="remove"/&gt;
    &lt;link href="/servicesNS/nobody/search/configs/conf-props/myweblogs/move" rel="move"/&gt;
    &lt;link href="/servicesNS/nobody/search/configs/conf-props/myweblogs/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="ANNOTATE_PUNCT"&gt;1&lt;/s:key&gt;
        &lt;s:key name="BREAK_ONLY_BEFORE"/&gt;
        &lt;s:key name="BREAK_ONLY_BEFORE_DATE"&gt;1&lt;/s:key&gt;
        &lt;s:key name="CHARSET"&gt;UTF-8&lt;/s:key&gt;
        &lt;s:key name="DATETIME_CONFIG"&gt;/etc/datetime.xml&lt;/s:key&gt;
        &lt;s:key name="HEADER_MODE"/&gt;
        &lt;s:key name="LEARN_SOURCETYPE"&gt;1&lt;/s:key&gt;
        &lt;s:key name="LINE_BREAKER_LOOKBEHIND"&gt;100&lt;/s:key&gt;
        &lt;s:key name="MAX_DAYS_AGO"&gt;2000&lt;/s:key&gt;
        &lt;s:key name="MAX_DAYS_HENCE"&gt;2&lt;/s:key&gt;
        &lt;s:key name="MAX_DIFF_SECS_AGO"&gt;3600&lt;/s:key&gt;
        &lt;s:key name="MAX_DIFF_SECS_HENCE"&gt;604800&lt;/s:key&gt;
        &lt;s:key name="MAX_EVENTS"&gt;256&lt;/s:key&gt;
        &lt;s:key name="MAX_TIMESTAMP_LOOKAHEAD"&gt;128&lt;/s:key&gt;
        &lt;s:key name="MUST_BREAK_AFTER"/&gt;
        &lt;s:key name="MUST_NOT_BREAK_AFTER"/&gt;
        &lt;s:key name="MUST_NOT_BREAK_BEFORE"/&gt;
        &lt;s:key name="SEGMENTATION"&gt;indexing&lt;/s:key&gt;
        &lt;s:key name="SEGMENTATION-all"&gt;full&lt;/s:key&gt;
        &lt;s:key name="SEGMENTATION-inner"&gt;inner&lt;/s:key&gt;
        &lt;s:key name="SEGMENTATION-outer"&gt;outer&lt;/s:key&gt;
        &lt;s:key name="SEGMENTATION-raw"&gt;none&lt;/s:key&gt;
        &lt;s:key name="SEGMENTATION-standard"&gt;standard&lt;/s:key&gt;
        &lt;s:key name="SHOULD_LINEMERGE"&gt;0&lt;/s:key&gt;
        &lt;s:key name="TRANSFORMS"/&gt;
        &lt;s:key name="TRUNCATE"&gt;10000&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:appName"&gt;search&lt;/s:key&gt;
        &lt;s:key name="eai:userName"&gt;admin&lt;/s:key&gt;
        &lt;s:key name="maxDist"&gt;100&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## configs/conf-{file}/{name}
{: name='configsconffilename'}

Deletes the named stanza in the named configuration file.

	[DELETE] configs/conf-{file}/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deleted successfully. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to delete configuration stanza. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Deletes the configuration stanza for sourcetype "myweblogs" in props.conf.

#### Request
<pre class='terminal'>
curl -k -u admin:pass --request DELETE \
	https://localhost:8089/servicesNS/nobody/search/configs/conf-props/myweblogs
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;conf-props&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/configs/conf-props&lt;/id&gt;
  &lt;updated&gt;2011-07-08T01:01:27-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/configs/conf-props/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/configs/conf-props/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## configs/conf-{file}/{name}
{: name='configsconffilename'}

Display only the named stanza from the named configuration file.

	[GET] configs/conf-{file}/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view configuration stanza. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Displays only the configuration for the "myweblogs" sourcetype in props.conf.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/nobody/search/configs/conf-props/myweblogs
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;conf-props&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/configs/conf-props&lt;/id&gt;
  &lt;updated&gt;2011-07-08T01:01:26-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/configs/conf-props/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/configs/conf-props/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;myweblogs&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/configs/conf-props/myweblogs&lt;/id&gt;
    &lt;updated&gt;2011-07-08T01:01:26-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/search/configs/conf-props/myweblogs" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/search/configs/conf-props/myweblogs" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/search/configs/conf-props/myweblogs/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/search/configs/conf-props/myweblogs" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/search/configs/conf-props/myweblogs" rel="remove"/&gt;
    &lt;link href="/servicesNS/nobody/search/configs/conf-props/myweblogs/move" rel="move"/&gt;
    &lt;link href="/servicesNS/nobody/search/configs/conf-props/myweblogs/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="ANNOTATE_PUNCT"&gt;1&lt;/s:key&gt;
        &lt;s:key name="BREAK_ONLY_BEFORE"/&gt;
        &lt;s:key name="BREAK_ONLY_BEFORE_DATE"&gt;1&lt;/s:key&gt;
        &lt;s:key name="CHARSET"&gt;UTF-8&lt;/s:key&gt;
        &lt;s:key name="DATETIME_CONFIG"&gt;/etc/datetime.xml&lt;/s:key&gt;
        &lt;s:key name="HEADER_MODE"/&gt;
        &lt;s:key name="LEARN_SOURCETYPE"&gt;1&lt;/s:key&gt;
        &lt;s:key name="LINE_BREAKER_LOOKBEHIND"&gt;100&lt;/s:key&gt;
        &lt;s:key name="MAX_DAYS_AGO"&gt;2000&lt;/s:key&gt;
        &lt;s:key name="MAX_DAYS_HENCE"&gt;2&lt;/s:key&gt;
        &lt;s:key name="MAX_DIFF_SECS_AGO"&gt;3600&lt;/s:key&gt;
        &lt;s:key name="MAX_DIFF_SECS_HENCE"&gt;604800&lt;/s:key&gt;
        &lt;s:key name="MAX_EVENTS"&gt;256&lt;/s:key&gt;
        &lt;s:key name="MAX_TIMESTAMP_LOOKAHEAD"&gt;128&lt;/s:key&gt;
        &lt;s:key name="MUST_BREAK_AFTER"/&gt;
        &lt;s:key name="MUST_NOT_BREAK_AFTER"/&gt;
        &lt;s:key name="MUST_NOT_BREAK_BEFORE"/&gt;
        &lt;s:key name="SEGMENTATION"&gt;indexing&lt;/s:key&gt;
        &lt;s:key name="SEGMENTATION-all"&gt;full&lt;/s:key&gt;
        &lt;s:key name="SEGMENTATION-inner"&gt;inner&lt;/s:key&gt;
        &lt;s:key name="SEGMENTATION-outer"&gt;outer&lt;/s:key&gt;
        &lt;s:key name="SEGMENTATION-raw"&gt;none&lt;/s:key&gt;
        &lt;s:key name="SEGMENTATION-standard"&gt;standard&lt;/s:key&gt;
        &lt;s:key name="SHOULD_LINEMERGE"&gt;0&lt;/s:key&gt;
        &lt;s:key name="TRANSFORMS"/&gt;
        &lt;s:key name="TRUNCATE"&gt;10000&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:appName"&gt;search&lt;/s:key&gt;
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
                &lt;s:item&gt;.*&lt;/s:item&gt;
              &lt;/s:list&gt;
            &lt;/s:key&gt;
          &lt;/s:dict&gt;
        &lt;/s:key&gt;
        &lt;s:key name="eai:userName"&gt;admin&lt;/s:key&gt;
        &lt;s:key name="maxDist"&gt;100&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## configs/conf-{file}/{name}
{: name='configsconffilename'}

Allows for editing the named stanza from the named configuration file.

	[POST] configs/conf-{file}/{name}

### Parameters

&lt;arbitrary_key&gt;
: _Required_ **String** This operation accepts an arbitrary set of key/value pairs to populate in set in this stanza.  (There is no actual parameter named "arbitrary_key".)

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Updated successfully. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to edit configuration stanza. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Enables line-merging for the "myweblogs" sourcetype existing in props.conf.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/nobody/search/configs/conf-props/myweblogs \
	-d SHOULD_LINEMERGE=true
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;conf-props&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/configs/conf-props&lt;/id&gt;
  &lt;updated&gt;2011-07-08T01:01:26-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/configs/conf-props/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/configs/conf-props/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;myweblogs&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/configs/conf-props/myweblogs&lt;/id&gt;
    &lt;updated&gt;2011-07-08T01:01:26-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/search/configs/conf-props/myweblogs" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/search/configs/conf-props/myweblogs" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/search/configs/conf-props/myweblogs/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/search/configs/conf-props/myweblogs" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/search/configs/conf-props/myweblogs" rel="remove"/&gt;
    &lt;link href="/servicesNS/nobody/search/configs/conf-props/myweblogs/move" rel="move"/&gt;
    &lt;link href="/servicesNS/nobody/search/configs/conf-props/myweblogs/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="ANNOTATE_PUNCT"&gt;1&lt;/s:key&gt;
        &lt;s:key name="BREAK_ONLY_BEFORE"/&gt;
        &lt;s:key name="BREAK_ONLY_BEFORE_DATE"&gt;1&lt;/s:key&gt;
        &lt;s:key name="CHARSET"&gt;UTF-8&lt;/s:key&gt;
        &lt;s:key name="DATETIME_CONFIG"&gt;/etc/datetime.xml&lt;/s:key&gt;
        &lt;s:key name="HEADER_MODE"/&gt;
        &lt;s:key name="LEARN_SOURCETYPE"&gt;1&lt;/s:key&gt;
        &lt;s:key name="LINE_BREAKER_LOOKBEHIND"&gt;100&lt;/s:key&gt;
        &lt;s:key name="MAX_DAYS_AGO"&gt;2000&lt;/s:key&gt;
        &lt;s:key name="MAX_DAYS_HENCE"&gt;2&lt;/s:key&gt;
        &lt;s:key name="MAX_DIFF_SECS_AGO"&gt;3600&lt;/s:key&gt;
        &lt;s:key name="MAX_DIFF_SECS_HENCE"&gt;604800&lt;/s:key&gt;
        &lt;s:key name="MAX_EVENTS"&gt;256&lt;/s:key&gt;
        &lt;s:key name="MAX_TIMESTAMP_LOOKAHEAD"&gt;128&lt;/s:key&gt;
        &lt;s:key name="MUST_BREAK_AFTER"/&gt;
        &lt;s:key name="MUST_NOT_BREAK_AFTER"/&gt;
        &lt;s:key name="MUST_NOT_BREAK_BEFORE"/&gt;
        &lt;s:key name="SEGMENTATION"&gt;indexing&lt;/s:key&gt;
        &lt;s:key name="SEGMENTATION-all"&gt;full&lt;/s:key&gt;
        &lt;s:key name="SEGMENTATION-inner"&gt;inner&lt;/s:key&gt;
        &lt;s:key name="SEGMENTATION-outer"&gt;outer&lt;/s:key&gt;
        &lt;s:key name="SEGMENTATION-raw"&gt;none&lt;/s:key&gt;
        &lt;s:key name="SEGMENTATION-standard"&gt;standard&lt;/s:key&gt;
        &lt;s:key name="SHOULD_LINEMERGE"&gt;1&lt;/s:key&gt;
        &lt;s:key name="TRANSFORMS"/&gt;
        &lt;s:key name="TRUNCATE"&gt;10000&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:appName"&gt;search&lt;/s:key&gt;
        &lt;s:key name="eai:userName"&gt;admin&lt;/s:key&gt;
        &lt;s:key name="maxDist"&gt;100&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## properties
{: name='properties'}

Returns a list of configurations that are saved in configuration files.

	[GET] properties

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------

### Example

Lists the names of all configuration files known to the Splunk instance.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/properties
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;properties&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/properties&lt;/id&gt;
  &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;entry&gt;
    &lt;title&gt;alert_actions&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/alert_actions&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/alert_actions" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;app&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/app&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/app" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;audit&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/audit&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/audit" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;authentication&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/authentication&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/authentication" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;authorize&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/authorize&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/authorize" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;commands&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/commands&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/commands" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;conf&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/conf&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/conf" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;crawl&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/crawl&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/crawl" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;datatypesbnf&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/datatypesbnf&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/datatypesbnf" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;default-mode&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/default-mode&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/default-mode" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;deploymentclient&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/deploymentclient&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/deploymentclient" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;distsearch&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/distsearch&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/distsearch" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;event_renderers&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/event_renderers&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/event_renderers" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;eventdiscoverer&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/eventdiscoverer&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/eventdiscoverer" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;eventtypes&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/eventtypes&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/eventtypes" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;fields&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/fields&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/fields" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;indexes&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/indexes&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/indexes" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;inputs&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/inputs&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/inputs" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;launcher&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/launcher&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/launcher" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;limits&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/limits&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/limits" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;literals&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/literals&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/literals" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;lookups&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/lookups&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/lookups" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;macros&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/macros&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/macros" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;manager&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/manager&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/manager" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;nav&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/nav&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/nav" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;outputs&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/outputs&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/outputs" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;pdf_server&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/pdf_server&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/pdf_server" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;prefs&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/prefs&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/prefs" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;props&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;quickstart&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/quickstart&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/quickstart" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;restmap&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/restmap&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/restmap" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;savedsearches&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/savedsearches&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/savedsearches" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;searchbnf&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/searchbnf&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/searchbnf" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;searchscripts&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/searchscripts&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/searchscripts" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;segmenters&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/segmenters&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/segmenters" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;server&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/server&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/server" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;serverclass&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/serverclass&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/serverclass" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source-classifier&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/source-classifier&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/source-classifier" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;sourcetypes&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/sourcetypes&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/sourcetypes" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;tenants&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/tenants&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/tenants" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;times&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/times&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/times" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;transactiontypes&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/transactiontypes&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/transactiontypes" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;transforms&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/transforms&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/transforms" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;user-prefs&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/user-prefs&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/user-prefs" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;views&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/views&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/views" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;viewstates&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/viewstates&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/viewstates" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;web&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/web&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/web" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;workflow_actions&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/workflow_actions&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:33:18-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/workflow_actions" rel="alternate"/&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## properties
{: name='properties'}

Creates a new configuration file.

	[POST] properties

### Parameters

__conf
: _Optional_ **String** The name of the configuration file to create.<br/><br/><b>Note</b>: Double underscore before conf.

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **201** | Created successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------

### Example

Creates a new configuration file named myapp.conf.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/properties \
	-d __conf=myapp
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>

</code></pre>

## properties/{file_name}
{: name='propertiesfilename'}

Returns a list of stanzas in the configuration file specified by {name}.

	[GET] properties/{file_name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **404** | Named file does not exist. |
|--------------------------------

### Example

Display configuration stanzas for the props.conf file.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/properties/props
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;props&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/properties/props&lt;/id&gt;
  &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;entry&gt;
    &lt;title&gt;(?i)source::....zip(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/%28%3Fi%29source%3A%3A....zip%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/%28%3Fi%29source%3A%3A....zip%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;ActiveDirectory&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/ActiveDirectory&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/ActiveDirectory" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;PerformanceMonitor&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/PerformanceMonitor&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/PerformanceMonitor" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;WinRegistry&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/WinRegistry&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/WinRegistry" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;__singleline&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/__singleline&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/__singleline" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;access_combined&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/access_combined&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/access_combined" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;access_combined_wcookie&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/access_combined_wcookie&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/access_combined_wcookie" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;access_common&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/access_common&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/access_common" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;anaconda&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/anaconda&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/anaconda" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;anaconda_syslog&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/anaconda_syslog&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/anaconda_syslog" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;apache_error&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/apache_error&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/apache_error" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;asterisk_cdr&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/asterisk_cdr&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/asterisk_cdr" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;asterisk_event&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/asterisk_event&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/asterisk_event" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;asterisk_messages&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/asterisk_messages&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/asterisk_messages" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;asterisk_queue&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/asterisk_queue&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/asterisk_queue" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;backup_file&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/backup_file&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/backup_file" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;breakable_text&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/breakable_text&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/breakable_text" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;cisco_cdr&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/cisco_cdr&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/cisco_cdr" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;cisco_syslog&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/cisco_syslog&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/cisco_syslog" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;clavister&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/clavister&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/clavister" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;csv&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/csv&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/csv" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;cups_access&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/cups_access&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/cups_access" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;cups_error&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/cups_error&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/cups_error" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;db2_diag&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/db2_diag&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/db2_diag" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;default&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/default&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/default" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;delayedrule::breakable_text&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/delayedrule%3A%3Abreakable_text&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/delayedrule%3A%3Abreakable_text" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;delayedrule::syslog&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/delayedrule%3A%3Asyslog&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/delayedrule%3A%3Asyslog" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;dmesg&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/dmesg&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/dmesg" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;exchange&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/exchange&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/exchange" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;exim_main&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/exim_main&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/exim_main" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;exim_reject&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/exim_reject&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/exim_reject" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;fileTrackerCrcLog&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/fileTrackerCrcLog&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/fileTrackerCrcLog" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;fs_notification&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/fs_notification&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/fs_notification" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;ftp&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/ftp&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/ftp" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;ignored_type&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/ignored_type&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/ignored_type" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;iis&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/iis&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/iis" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;known_binary&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/known_binary&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/known_binary" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;lastlog&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/lastlog&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/lastlog" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;license_usage-too_small&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/license_usage-too_small&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/license_usage-too_small" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;linux_audit&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/linux_audit&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/linux_audit" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;linux_bootlog&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/linux_bootlog&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/linux_bootlog" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;linux_messages_syslog&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/linux_messages_syslog&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/linux_messages_syslog" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;linux_secure&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/linux_secure&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/linux_secure" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;log4j&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/log4j&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/log4j" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;log4php&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/log4php&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/log4php" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;manpage&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/manpage&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/manpage" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;misc_text&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/misc_text&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/misc_text" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;mysqld&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/mysqld&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/mysqld" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;mysqld_bin&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/mysqld_bin&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/mysqld_bin" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;mysqld_error&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/mysqld_error&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/mysqld_error" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;novell_groupwise&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/novell_groupwise&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/novell_groupwise" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;osx_asl&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/osx_asl&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/osx_asl" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;osx_crash_log&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/osx_crash_log&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/osx_crash_log" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;osx_crashreporter&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/osx_crashreporter&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/osx_crashreporter" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;osx_daily&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/osx_daily&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/osx_daily" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;osx_install&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/osx_install&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/osx_install" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;osx_monthly&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/osx_monthly&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/osx_monthly" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;osx_secure&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/osx_secure&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/osx_secure" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;osx_weekly&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/osx_weekly&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/osx_weekly" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;osx_window_server&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/osx_window_server&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/osx_window_server" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;postfix_syslog&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/postfix_syslog&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/postfix_syslog" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;preprocess-Z&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/preprocess-Z&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/preprocess-Z" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;preprocess-bzip&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/preprocess-bzip&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/preprocess-bzip" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;preprocess-gzip&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/preprocess-gzip&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/preprocess-gzip" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;preprocess-tar&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/preprocess-tar&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/preprocess-tar" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;preprocess-targz&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/preprocess-targz&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/preprocess-targz" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;preprocess-zip&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/preprocess-zip&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/preprocess-zip" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;procmail&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/procmail&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/procmail" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;rpmpkgs&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/rpmpkgs&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/rpmpkgs" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;rule::access_combined&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/rule%3A%3Aaccess_combined&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/rule%3A%3Aaccess_combined" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;rule::access_combined_wcookie&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/rule%3A%3Aaccess_combined_wcookie&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/rule%3A%3Aaccess_combined_wcookie" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;rule::access_common&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/rule%3A%3Aaccess_common&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/rule%3A%3Aaccess_common" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;rule::exim_main&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/rule%3A%3Aexim_main&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/rule%3A%3Aexim_main" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;rule::postfix_syslog&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/rule%3A%3Apostfix_syslog&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/rule%3A%3Apostfix_syslog" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;rule::sendmail_syslog&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/rule%3A%3Asendmail_syslog&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/rule%3A%3Asendmail_syslog" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;rule::snort&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/rule%3A%3Asnort&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/rule%3A%3Asnort" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;sar&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/sar&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/sar" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;sendmail_syslog&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/sendmail_syslog&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/sendmail_syslog" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;snort&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/snort&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/snort" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::...((.(bak|old))|,v|~|#)&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%28%28.%28bak%7Cold%29%29%7C%2Cv%7C~%7C%23%29&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%28%28.%28bak%7Cold%29%29%7C%2Cv%7C~%7C%23%29" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::....(0t|a|ali|asa|au|bmp|cg|cgi|class|d|dat|deb|del|dot|dvi|dylib|elc|eps|exe|ftn|gif|hlp|hqx|hs|icns|ico|inc|iso|jame|jin|jpeg|jpg|kml|la|lhs|lib|lo|lock|mcp|mid|mp3|mpg|msf|nib|o|obj|odt|ogg|ook|opt|os|pal|pbm|pdf|pem|pgm|plo|png|po|pod|pp|ppd|ppm|ppt|prc|ps|psd|psym|pyc|pyd|rast|rb|rde|rdf|rdr|rgb|ro|rpm|rsrc|so|ss|stg|strings|tdt|tif|tiff|tk|uue|vhd|xbm|xlb|xls|xlw)&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A....%280t%7Ca%7Cali%7Casa%7Cau%7Cbmp%7Ccg%7Ccgi%7Cclass%7Cd%7Cdat%7Cdeb%7Cdel%7Cdot%7Cdvi%7Cdylib%7Celc%7Ceps%7Cexe%7Cftn%7Cgif%7Chlp%7Chqx%7Chs%7Cicns%7Cico%7Cinc%7Ciso%7Cjame%7Cjin%7Cjpeg%7Cjpg%7Ckml%7Cla%7Clhs%7Clib%7Clo%7Clock%7Cmcp%7Cmid%7Cmp3%7Cmpg%7Cmsf%7Cnib%7Co%7Cobj%7Codt%7Cogg%7Cook%7Copt%7Cos%7Cpal%7Cpbm%7Cpdf%7Cpem%7Cpgm%7Cplo%7Cpng%7Cpo%7Cpod%7Cpp%7Cppd%7Cppm%7Cppt%7Cprc%7Cps%7Cpsd%7Cpsym%7Cpyc%7Cpyd%7Crast%7Crb%7Crde%7Crdf%7Crdr%7Crgb%7Cro%7Crpm%7Crsrc%7Cso%7Css%7Cstg%7Cstrings%7Ctdt%7Ctif%7Ctiff%7Ctk%7Cuue%7Cvhd%7Cxbm%7Cxlb%7Cxls%7Cxlw%29&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A....%280t%7Ca%7Cali%7Casa%7Cau%7Cbmp%7Ccg%7Ccgi%7Cclass%7Cd%7Cdat%7Cdeb%7Cdel%7Cdot%7Cdvi%7Cdylib%7Celc%7Ceps%7Cexe%7Cftn%7Cgif%7Chlp%7Chqx%7Chs%7Cicns%7Cico%7Cinc%7Ciso%7Cjame%7Cjin%7Cjpeg%7Cjpg%7Ckml%7Cla%7Clhs%7Clib%7Clo%7Clock%7Cmcp%7Cmid%7Cmp3%7Cmpg%7Cmsf%7Cnib%7Co%7Cobj%7Codt%7Cogg%7Cook%7Copt%7Cos%7Cpal%7Cpbm%7Cpdf%7Cpem%7Cpgm%7Cplo%7Cpng%7Cpo%7Cpod%7Cpp%7Cppd%7Cppm%7Cppt%7Cprc%7Cps%7Cpsd%7Cpsym%7Cpyc%7Cpyd%7Crast%7Crb%7Crde%7Crdf%7Crdr%7Crgb%7Cro%7Crpm%7Crsrc%7Cso%7Css%7Cstg%7Cstrings%7Ctdt%7Ctif%7Ctiff%7Ctk%7Cuue%7Cvhd%7Cxbm%7Cxlb%7Cxls%7Cxlw%29" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::....(?&amp;lt;!tar.)gz(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A....%28%3F%3C%21tar.%29gz%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A....%28%3F%3C%21tar.%29gz%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::....(cache|class|cxx|dylib|jar|lo|xslt|md5|rpm|deb|iso|vim)&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A....%28cache%7Cclass%7Ccxx%7Cdylib%7Cjar%7Clo%7Cxslt%7Cmd5%7Crpm%7Cdeb%7Ciso%7Cvim%29&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A....%28cache%7Cclass%7Ccxx%7Cdylib%7Cjar%7Clo%7Cxslt%7Cmd5%7Crpm%7Cdeb%7Ciso%7Cvim%29" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::....(css|htm|html|sgml|shtml|template)&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A....%28css%7Chtm%7Chtml%7Csgml%7Cshtml%7Ctemplate%29&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A....%28css%7Chtm%7Chtml%7Csgml%7Cshtml%7Ctemplate%29" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::....(jar)(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A....%28jar%29%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A....%28jar%29%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::....(tar.gz|tgz)(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A....%28tar.gz%7Ctgz%29%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A....%28tar.gz%7Ctgz%29%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::....(tbz|tbz2)(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A....%28tbz%7Ctbz2%29%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A....%28tbz%7Ctbz2%29%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::....Z(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A....Z%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A....Z%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::....bz2?(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A....bz2%3F%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A....bz2%3F%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::....crash.log(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A....crash.log%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A....crash.log%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::....csv&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A....csv&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A....csv" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::....tar(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A....tar%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A....tar%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../(apache|httpd).../error*&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2F%28apache%7Chttpd%29...%2Ferror%2A&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2F%28apache%7Chttpd%29...%2Ferror%2A" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../(ex|in|nc)(\d{4,8})*?.log&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2F%28ex%7Cin%7Cnc%29%28%5Cd%7B4%2C8%7D%29%2A%3F.log&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2F%28ex%7Cin%7Cnc%29%28%5Cd%7B4%2C8%7D%29%2A%3F.log" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../(readme|README)...&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2F%28readme%7CREADME%29...&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2F%28readme%7CREADME%29..." rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../man/man\d+/*.\d+&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fman%2Fman%5Cd%2B%2F%2A.%5Cd%2B&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fman%2Fman%5Cd%2B%2F%2A.%5Cd%2B" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../messages(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fmessages%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fmessages%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../mysql.log(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fmysql.log%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fmysql.log%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../private/var/log/mail.log(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fprivate%2Fvar%2Flog%2Fmail.log%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fprivate%2Fvar%2Flog%2Fmail.log%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../private/var/log/system.log(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fprivate%2Fvar%2Flog%2Fsystem.log%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fprivate%2Fvar%2Flog%2Fsystem.log%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../private/var/log/windowserver.log(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fprivate%2Fvar%2Flog%2Fwindowserver.log%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fprivate%2Fvar%2Flog%2Fwindowserver.log%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../procmail(_|.)log&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fprocmail%28_%7C.%29log&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fprocmail%28_%7C.%29log" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../splunkd.log(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fsplunkd.log%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fsplunkd.log%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../splunkd_access.log(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fsplunkd_access.log%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fsplunkd_access.log%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../syslog(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fsyslog%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fsyslog%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../var/log/anaconda.log(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fanaconda.log%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fanaconda.log%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../var/log/anaconda.syslog(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fanaconda.syslog%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fanaconda.syslog%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../var/log/asl.log(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fasl.log%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fasl.log%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../var/log/audit/audit.log(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Faudit%2Faudit.log%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Faudit%2Faudit.log%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../var/log/boot.log(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fboot.log%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fboot.log%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../var/log/crashreporter.log(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fcrashreporter.log%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fcrashreporter.log%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../var/log/cups/access_log(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fcups%2Faccess_log%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fcups%2Faccess_log%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../var/log/cups/error_log(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fcups%2Ferror_log%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fcups%2Ferror_log%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../var/log/daily.out(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fdaily.out%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fdaily.out%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../var/log/dmesg(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fdmesg%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fdmesg%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../var/log/ftp.log(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fftp.log%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fftp.log%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../var/log/httpd/error_log(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fhttpd%2Ferror_log%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fhttpd%2Ferror_log%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../var/log/httpd/httpd/ssl_error_log(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fhttpd%2Fhttpd%2Fssl_error_log%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fhttpd%2Fhttpd%2Fssl_error_log%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../var/log/install.log(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Finstall.log%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Finstall.log%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../var/log/lastlog(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Flastlog%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Flastlog%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../var/log/monthly.out(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fmonthly.out%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fmonthly.out%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../var/log/rpmpkgs(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Frpmpkgs%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Frpmpkgs%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../var/log/sa/sar\d+&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fsa%2Fsar%5Cd%2B&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fsa%2Fsar%5Cd%2B" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../var/log/secure(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fsecure%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fsecure%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../var/log/secure.log(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fsecure.log%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fsecure.log%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../var/log/splunk/(web|report)_access.log&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fsplunk%2F%28web%7Creport%29_access.log&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fsplunk%2F%28web%7Creport%29_access.log" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../var/log/splunk/(web|report)_service.log&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fsplunk%2F%28web%7Creport%29_service.log&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fsplunk%2F%28web%7Creport%29_service.log" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../var/log/splunk/audit.log(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fsplunk%2Faudit.log%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fsplunk%2Faudit.log%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../var/log/splunk/btool.log(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fsplunk%2Fbtool.log%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fsplunk%2Fbtool.log%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../var/log/splunk/crash-*.log&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fsplunk%2Fcrash-%2A.log&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fsplunk%2Fcrash-%2A.log" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../var/log/splunk/intentions.log(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fsplunk%2Fintentions.log%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fsplunk%2Fintentions.log%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../var/log/splunk/license_audit.log(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fsplunk%2Flicense_audit.log%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fsplunk%2Flicense_audit.log%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../var/log/splunk/metrics.log(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fsplunk%2Fmetrics.log%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fsplunk%2Fmetrics.log%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../var/log/splunk/python.log(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fsplunk%2Fpython.log%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fsplunk%2Fpython.log%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../var/log/splunk/scheduler.log(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fsplunk%2Fscheduler.log%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fsplunk%2Fscheduler.log%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../var/log/splunk/searches.log&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fsplunk%2Fsearches.log&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fsplunk%2Fsearches.log" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../var/log/splunk/searchhistory.log(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fsplunk%2Fsearchhistory.log%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fsplunk%2Fsearchhistory.log%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../var/log/splunk/splunk_stdout.log&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fsplunk%2Fsplunk_stdout.log&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fsplunk%2Fsplunk_stdout.log" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../var/log/splunk/splunkd_stderr.log&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fsplunk%2Fsplunkd_stderr.log&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fsplunk%2Fsplunkd_stderr.log" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../var/log/spooler(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fspooler%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fspooler%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../var/log/weekly.out(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fweekly.out%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fweekly.out%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::.../var/log/wtmp(.\d+)?&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fwtmp%28.%5Cd%2B%29%3F&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...%2Fvar%2Flog%2Fwtmp%28.%5Cd%2B%29%3F" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::...stash&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...stash&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...stash" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::...stash_new&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3A...stash_new&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3A...stash_new" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::WMI...&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3AWMI...&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3AWMI..." rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source::WinEventLog...&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source%3A%3AWinEventLog...&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source%3A%3AWinEventLog..." rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;source_archive&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/source_archive&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/source_archive" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;splunk-blocksignature&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/splunk-blocksignature&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/splunk-blocksignature" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;splunk_com_php_error&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/splunk_com_php_error&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/splunk_com_php_error" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;splunk_directory_monitor&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/splunk_directory_monitor&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/splunk_directory_monitor" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;splunk_directory_monitor_misc&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/splunk_directory_monitor_misc&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/splunk_directory_monitor_misc" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;splunk_help&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/splunk_help&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/splunk_help" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;splunk_search_history&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/splunk_search_history&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/splunk_search_history" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;splunk_web_access&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/splunk_web_access&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/splunk_web_access" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;splunk_web_service&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/splunk_web_service&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/splunk_web_service" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;splunkd&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/splunkd&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/splunkd" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;splunkd_access&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/splunkd_access&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/splunkd_access" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;splunkd_crash_log&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/splunkd_crash_log&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/splunkd_crash_log" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;splunkd_misc&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/splunkd_misc&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/splunkd_misc" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;splunkd_stderr&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/splunkd_stderr&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/splunkd_stderr" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;splunkd_stdout-too_small&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/splunkd_stdout-too_small&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/splunkd_stdout-too_small" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;spooler&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/spooler&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/spooler" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;ssl_error&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/ssl_error&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/ssl_error" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;stash&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/stash&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/stash" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;stash_new&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/stash_new&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/stash_new" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;syslog&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/syslog&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/syslog" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;tcp&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/tcp&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/tcp" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;too_small&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/too_small&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/too_small" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;web&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/web&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/web" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;weblogic_stdout&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/weblogic_stdout&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/weblogic_stdout" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;websphere_activity&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/websphere_activity&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/websphere_activity" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;websphere_core&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/websphere_core&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/websphere_core" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;websphere_trlog&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/websphere_trlog&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/websphere_trlog" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;windows_snare_syslog&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/windows_snare_syslog&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/windows_snare_syslog" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;wmi&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/wmi&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/wmi" rel="alternate"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;wtmp&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/wtmp&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:53:58-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/wtmp" rel="alternate"/&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## properties/{file_name}
{: name='propertiesfilename'}

Creates a new stanza in the configuratin file specified by {name}.

	[POST] properties/{file_name}

### Parameters

__stanza
: _Optional_ **String** The name of the stanza to create.<br/><br/><b>Note</b>: Double underscore before stanza.

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **201** | Stanza created successfully. |
|--------------------------------
| **303** | Stanza already exists. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------

### Example

Creates a stanza named proxylogs in props.conf.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/properties/props \
	-d __stanza=proxylogs
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>

</code></pre>

## properties/{file_name}/{stanza_name}
{: name='propertiesfilenamestanzaname'}

Returns the configuration values for the stanza represented by {stanza_name} in the configuration file specified by {file_name}.

	[GET] properties/{file_name}/{stanza_name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **404** | Stanza does not exist. |
|--------------------------------

### Example

Retrieves the stanza named proxylogs from props.conf.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/properties/props/proxylogs
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;proxylogs&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/properties/props/proxylogs&lt;/id&gt;
  &lt;updated&gt;2011-07-08T12:08:52-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;entry&gt;
    &lt;title&gt;ANNOTATE_PUNCT&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/proxylogs/ANNOTATE_PUNCT&lt;/id&gt;
    &lt;updated&gt;2011-07-08T12:08:52-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/proxylogs/ANNOTATE_PUNCT" rel="alternate"/&gt;
    &lt;content type="text"&gt;True&lt;/content&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;BREAK_ONLY_BEFORE&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/proxylogs/BREAK_ONLY_BEFORE&lt;/id&gt;
    &lt;updated&gt;2011-07-08T12:08:52-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/proxylogs/BREAK_ONLY_BEFORE" rel="alternate"/&gt;
    &lt;content type="text"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;BREAK_ONLY_BEFORE_DATE&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/proxylogs/BREAK_ONLY_BEFORE_DATE&lt;/id&gt;
    &lt;updated&gt;2011-07-08T12:08:52-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/proxylogs/BREAK_ONLY_BEFORE_DATE" rel="alternate"/&gt;
    &lt;content type="text"&gt;True&lt;/content&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;CHARSET&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/proxylogs/CHARSET&lt;/id&gt;
    &lt;updated&gt;2011-07-08T12:08:52-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/proxylogs/CHARSET" rel="alternate"/&gt;
    &lt;content type="text"&gt;UTF-8&lt;/content&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;DATETIME_CONFIG&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/proxylogs/DATETIME_CONFIG&lt;/id&gt;
    &lt;updated&gt;2011-07-08T12:08:52-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/proxylogs/DATETIME_CONFIG" rel="alternate"/&gt;
    &lt;content type="text"&gt;/etc/datetime.xml&lt;/content&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;HEADER_MODE&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/proxylogs/HEADER_MODE&lt;/id&gt;
    &lt;updated&gt;2011-07-08T12:08:52-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/proxylogs/HEADER_MODE" rel="alternate"/&gt;
    &lt;content type="text"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;LEARN_SOURCETYPE&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/proxylogs/LEARN_SOURCETYPE&lt;/id&gt;
    &lt;updated&gt;2011-07-08T12:08:52-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/proxylogs/LEARN_SOURCETYPE" rel="alternate"/&gt;
    &lt;content type="text"&gt;true&lt;/content&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;LINE_BREAKER_LOOKBEHIND&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/proxylogs/LINE_BREAKER_LOOKBEHIND&lt;/id&gt;
    &lt;updated&gt;2011-07-08T12:08:52-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/proxylogs/LINE_BREAKER_LOOKBEHIND" rel="alternate"/&gt;
    &lt;content type="text"&gt;100&lt;/content&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;MAX_DAYS_AGO&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/proxylogs/MAX_DAYS_AGO&lt;/id&gt;
    &lt;updated&gt;2011-07-08T12:08:52-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/proxylogs/MAX_DAYS_AGO" rel="alternate"/&gt;
    &lt;content type="text"&gt;2000&lt;/content&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;MAX_DAYS_HENCE&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/proxylogs/MAX_DAYS_HENCE&lt;/id&gt;
    &lt;updated&gt;2011-07-08T12:08:52-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/proxylogs/MAX_DAYS_HENCE" rel="alternate"/&gt;
    &lt;content type="text"&gt;2&lt;/content&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;MAX_DIFF_SECS_AGO&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/proxylogs/MAX_DIFF_SECS_AGO&lt;/id&gt;
    &lt;updated&gt;2011-07-08T12:08:52-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/proxylogs/MAX_DIFF_SECS_AGO" rel="alternate"/&gt;
    &lt;content type="text"&gt;3600&lt;/content&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;MAX_DIFF_SECS_HENCE&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/proxylogs/MAX_DIFF_SECS_HENCE&lt;/id&gt;
    &lt;updated&gt;2011-07-08T12:08:52-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/proxylogs/MAX_DIFF_SECS_HENCE" rel="alternate"/&gt;
    &lt;content type="text"&gt;604800&lt;/content&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;MAX_EVENTS&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/proxylogs/MAX_EVENTS&lt;/id&gt;
    &lt;updated&gt;2011-07-08T12:08:52-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/proxylogs/MAX_EVENTS" rel="alternate"/&gt;
    &lt;content type="text"&gt;256&lt;/content&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;MAX_TIMESTAMP_LOOKAHEAD&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/proxylogs/MAX_TIMESTAMP_LOOKAHEAD&lt;/id&gt;
    &lt;updated&gt;2011-07-08T12:08:52-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/proxylogs/MAX_TIMESTAMP_LOOKAHEAD" rel="alternate"/&gt;
    &lt;content type="text"&gt;128&lt;/content&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;MUST_BREAK_AFTER&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/proxylogs/MUST_BREAK_AFTER&lt;/id&gt;
    &lt;updated&gt;2011-07-08T12:08:52-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/proxylogs/MUST_BREAK_AFTER" rel="alternate"/&gt;
    &lt;content type="text"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;MUST_NOT_BREAK_AFTER&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/proxylogs/MUST_NOT_BREAK_AFTER&lt;/id&gt;
    &lt;updated&gt;2011-07-08T12:08:52-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/proxylogs/MUST_NOT_BREAK_AFTER" rel="alternate"/&gt;
    &lt;content type="text"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;MUST_NOT_BREAK_BEFORE&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/proxylogs/MUST_NOT_BREAK_BEFORE&lt;/id&gt;
    &lt;updated&gt;2011-07-08T12:08:52-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/proxylogs/MUST_NOT_BREAK_BEFORE" rel="alternate"/&gt;
    &lt;content type="text"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;SEGMENTATION&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/proxylogs/SEGMENTATION&lt;/id&gt;
    &lt;updated&gt;2011-07-08T12:08:52-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/proxylogs/SEGMENTATION" rel="alternate"/&gt;
    &lt;content type="text"&gt;indexing&lt;/content&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;SEGMENTATION-all&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/proxylogs/SEGMENTATION-all&lt;/id&gt;
    &lt;updated&gt;2011-07-08T12:08:52-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/proxylogs/SEGMENTATION-all" rel="alternate"/&gt;
    &lt;content type="text"&gt;full&lt;/content&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;SEGMENTATION-inner&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/proxylogs/SEGMENTATION-inner&lt;/id&gt;
    &lt;updated&gt;2011-07-08T12:08:52-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/proxylogs/SEGMENTATION-inner" rel="alternate"/&gt;
    &lt;content type="text"&gt;inner&lt;/content&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;SEGMENTATION-outer&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/proxylogs/SEGMENTATION-outer&lt;/id&gt;
    &lt;updated&gt;2011-07-08T12:08:52-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/proxylogs/SEGMENTATION-outer" rel="alternate"/&gt;
    &lt;content type="text"&gt;outer&lt;/content&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;SEGMENTATION-raw&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/proxylogs/SEGMENTATION-raw&lt;/id&gt;
    &lt;updated&gt;2011-07-08T12:08:52-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/proxylogs/SEGMENTATION-raw" rel="alternate"/&gt;
    &lt;content type="text"&gt;none&lt;/content&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;SEGMENTATION-standard&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/proxylogs/SEGMENTATION-standard&lt;/id&gt;
    &lt;updated&gt;2011-07-08T12:08:52-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/proxylogs/SEGMENTATION-standard" rel="alternate"/&gt;
    &lt;content type="text"&gt;standard&lt;/content&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;SHOULD_LINEMERGE&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/proxylogs/SHOULD_LINEMERGE&lt;/id&gt;
    &lt;updated&gt;2011-07-08T12:08:52-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/proxylogs/SHOULD_LINEMERGE" rel="alternate"/&gt;
    &lt;content type="text"&gt;True&lt;/content&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;TRANSFORMS&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/proxylogs/TRANSFORMS&lt;/id&gt;
    &lt;updated&gt;2011-07-08T12:08:52-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/proxylogs/TRANSFORMS" rel="alternate"/&gt;
    &lt;content type="text"/&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;TRUNCATE&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/proxylogs/TRUNCATE&lt;/id&gt;
    &lt;updated&gt;2011-07-08T12:08:52-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/proxylogs/TRUNCATE" rel="alternate"/&gt;
    &lt;content type="text"&gt;10000&lt;/content&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;maxDist&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/properties/props/proxylogs/maxDist&lt;/id&gt;
    &lt;updated&gt;2011-07-08T12:08:52-07:00&lt;/updated&gt;
    &lt;link href="/services/properties/props/proxylogs/maxDist" rel="alternate"/&gt;
    &lt;content type="text"&gt;100&lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## properties/{file_name}/{stanza_name}
{: name='propertiesfilenamestanzaname'}

Adds or updates key/value pairs in the specified stanza. One or more key/value pairs may be passed at one time to this endpoint.

	[POST] properties/{file_name}/{stanza_name}

### Parameters

&lt;key_name&gt;
: _Required_ **String** Specifies a key/value pair to update.

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Updated successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **404** | Stanza does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See returned XML for explanation. |
|--------------------------------

### Example

Modifies two settings at once for the proxylogs sourcetype in props.conf.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/properties/props/proxylogs \
	-d NO_BINARY_CHECK=true \
	-d CHARSET=UTF-8
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;response&gt;
  &lt;messages&gt;
    &lt;msg type="INFO"&gt;Successfully modified 2 key(s)&lt;/msg&gt;
  &lt;/messages&gt;
&lt;/response&gt;
</code></pre>

## properties/{file_name}/{stanza_name}/{key_name}
{: name='propertiesfilenamestanzanamekeyname'}

Returns the value of the key in plain text for specified stanza and configuration file.

	[GET] properties/{file_name}/{stanza_name}/{key_name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **404** | Key in the stanza does not exist. |
|--------------------------------

### Example

Retreive the raw value (not XML) of the SHOULD_LINEMERGE setting from the proxylogs stanza in props.conf.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/properties/props/proxylogs/SHOULD_LINEMERGE
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
True
</code></pre>

## properties/{file_name}/{stanza_name}/{key_name}
{: name='propertiesfilenamestanzanamekeyname'}

Update an existing key value.

	[POST] properties/{file_name}/{stanza_name}/{key_name}

### Parameters

value
: _Required_ **String** The value to set for the named key in this named stanza in the named configuration file.

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Updated successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **404** | Key does not exist in the stanza. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See returned XML for explanation. |
|--------------------------------

### Example

Disables line merging for the proxylogs sourcetype in props.conf.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/properties/props/proxylogs/SHOULD_LINEMERGE \
	-d value=false
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;response&gt;
  &lt;messages&gt;
    &lt;msg type="INFO"&gt;Successfully modified 1 key(s)&lt;/msg&gt;
  &lt;/messages&gt;
&lt;/response&gt;
</code></pre>


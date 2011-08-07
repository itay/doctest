## messages
{: name='messages'}

Enumerate all systemwide messages. This is typically used for splunkd to advertise issues involving license quotas, license expirations, misconfigured indexes and disk space to users in SplunkWeb.

	[GET] messages

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
| **403** | Insufficient permissions to view messages. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

This example lists all system messages.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/messages
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;messages&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/messages&lt;/id&gt;
  &lt;updated&gt;2011-07-08T01:14:21-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/messages/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;restart_required&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/messages/restart_required&lt;/id&gt;
    &lt;updated&gt;2011-07-08T01:14:21-07:00&lt;/updated&gt;
    &lt;link href="/services/messages/restart_required" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/messages/restart_required" rel="list"/&gt;
    &lt;link href="/services/messages/restart_required" rel="remove"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="restart_required"&gt;Splunk must be restarted for changes to take effect.&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## messages
{: name='messages'}

Create a persistent message displayed at /services/messages.

	[POST] messages

### Parameters

name
: _Required_ **String** The primary key of this message. It is not displayed in SplunkWeb.

value
: _Required_ **String** The text of the message displayed in SplunkWeb.

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
| **403** | Insufficient permissions to create message. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

This example creates the Splunk system message, "hello world."

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/messages \
	-d name=message \
	-d value="hello world"
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;messages&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/messages&lt;/id&gt;
  &lt;updated&gt;2011-07-08T01:14:21-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/messages/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## messages/{name}
{: name='messagesname'}

Deletes a message identified by {name}. After deleting the message, it no longer appears in SplunkWeb.

	[DELETE] messages/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deleted successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to delete message. |
|--------------------------------
| **404** | Message does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

This example deletes the message named message.
After invoking this operation, the message no longer displays on Splunk Web.

#### Request
<pre class='terminal'>
curl -k -u admin:pass --request DELETE https://localhost:8089/services/messages/message
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;messages&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/messages&lt;/id&gt;
  &lt;updated&gt;2011-07-08T01:14:21-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/messages/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## messages/{name}
{: name='messagesname'}

Get the entry corresponding of a single message identified by {name}.

	[GET] messages/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view message. |
|--------------------------------
| **404** | Message does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

This example lists the message named "message."

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/messages/message
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;messages&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/messages&lt;/id&gt;
  &lt;updated&gt;2011-07-08T01:14:21-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/messages/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;message&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/messages/message&lt;/id&gt;
    &lt;updated&gt;2011-07-08T01:14:21-07:00&lt;/updated&gt;
    &lt;link href="/services/messages/message" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/messages/message" rel="list"/&gt;
    &lt;link href="/services/messages/message" rel="remove"/&gt;
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
        &lt;s:key name="message"&gt;hello world&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## server/control
{: name='servercontrol'}

Lists the actions that can be performed at this endpoint.

	[GET] server/control

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
| **403** | Insufficient permissions to view server controls. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Displays actions available at server control endpoint.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/server/control
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;server-control&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/server/control&lt;/id&gt;
  &lt;updated&gt;2011-07-12T00:17:53-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/server/control/restart" rel="restart"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## server/control/restart
{: name='servercontrolrestart'}

Restarts the Splunk server.

	[POST] server/control/restart

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Restart requested successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **402** | The Splunk license in use has disabled this feature. |
|--------------------------------
| **403** | Insufficient permissions to restart Splunk. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Requests the Splunk process to restart.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/server/control/restart -X POST
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;server-control&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/server/control&lt;/id&gt;
  &lt;updated&gt;2011-07-12T00:18:08-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/server/control/restart" rel="restart"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## server/info
{: name='serverinfo'}

Enumerates the following information about the running splunkd: 

  build
  cpu_arch (CPU architecure)
  guid (GUID for this splunk instance)
  isFree
  isTrial
  licenseKeys (hashes)
  licenseSignature
  licenseState
  master_guid (GUID of the license master)
  mode
  os_build
  os_name
  os_version
  serverName
  version

	[GET] server/info

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
| **403** | Insufficient permissions to view server configuration info. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Lists information about the Splunk server.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/server/info
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:s="http://dev.splunk.com/ns/rest"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;server-info&lt;/title&gt;
  &lt;id&gt;https://mrt:8089/services/server/info&lt;/id&gt;
  &lt;updated&gt;2011-05-16T16:35:53-0700&lt;/updated&gt;
  &lt;generator version="98144"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;opensearch:totalResults&gt;1&lt;/opensearch:totalResults&gt;
  &lt;opensearch:itemsPerPage&gt;30&lt;/opensearch:itemsPerPage&gt;
  &lt;opensearch:startIndex&gt;0&lt;/opensearch:startIndex&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;server-info&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/server/info/server-info&lt;/id&gt;
    &lt;updated&gt;2011-05-16T16:35:53-0700&lt;/updated&gt;
    &lt;link href="/services/server/info/server-info" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/server/info/server-info" rel="list"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="build"&gt;98144&lt;/s:key&gt;
        &lt;s:key name="cpu_arch"&gt;x86_64&lt;/s:key&gt;
        &lt;s:key name="eai:acl"&gt;. . .&lt;/s:key&gt;
        &lt;s:key name="guid"&gt;57566295-F8A6-48C0-A15C-6903E80FD4A4&lt;/s:key&gt;
        &lt;s:key name="isFree"&gt;0&lt;/s:key&gt;
        &lt;s:key name="isTrial"&gt;1&lt;/s:key&gt;
        &lt;s:key name="licenseKeys"&gt;&lt;s:list&gt;&lt;s:item&gt;6EF3EBD59E3CEB22583E7CF67533809D1F6D198F0EAA463A3C4BBF741DADB145&lt;/s:item&gt;&lt;/s:list&gt;&lt;/s:key&gt;
        &lt;s:key name="licenseSignature"&gt;8392db4e3e6f4a5da2602d6154da3dd8&lt;/s:key&gt;
        &lt;s:key name="licenseState"&gt;OK&lt;/s:key&gt;
        &lt;s:key name="master_guid"&gt;57566295-F8A6-48C0-A15C-6903E80FD4A4&lt;/s:key&gt;
        &lt;s:key name="mode"&gt;normal&lt;/s:key&gt;
        &lt;s:key name="os_build"&gt;#1 SMP Thu Sep 3 03:28:30 EDT 2009&lt;/s:key&gt;
        &lt;s:key name="os_name"&gt;Linux&lt;/s:key&gt;
        &lt;s:key name="os_version"&gt;2.6.18-164.el5&lt;/s:key&gt;
        &lt;s:key name="serverName"&gt;MrT-ssorkin&lt;/s:key&gt;
        &lt;s:key name="version"&gt;20110414&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## server/info/{name}
{: name='serverinfoname'}

Provides the identical information as /services/server/info. The only valid {name} here is server-info.

	[GET] server/info/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view server configuration info. |
|--------------------------------
| **404** | Server configuration info does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Retrieves the "server-info" node, which is the only valid value for {name}.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/server/info/server-info
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>

</code></pre>

## server/logger
{: name='serverlogger'}

Enumerates all splunkd logging categories, either specified in code or in $SPLUNK_HOME/etc/log.cfg.

	[GET] server/logger

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
| **403** | Insufficient permissions to view logger info. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

This example lists all logging categories for the Splunk server.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/server/logger
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:s="http://dev.splunk.com/ns/rest"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;logger&lt;/title&gt;
  &lt;id&gt;https://mrt:8089/services/server/logger&lt;/id&gt;
  &lt;updated&gt;2011-05-16T20:29:38-0700&lt;/updated&gt;
  &lt;generator version="98144"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;opensearch:totalResults&gt;418&lt;/opensearch:totalResults&gt;
  &lt;opensearch:itemsPerPage&gt;30&lt;/opensearch:itemsPerPage&gt;
  &lt;opensearch:startIndex&gt;0&lt;/opensearch:startIndex&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;AdminHandler:AuthenticationHandler&lt;/title&gt;
    &lt;id&gt;https://mrt:8089/services/server/logger/AdminHandler%3AAuthenticationHandler&lt;/id&gt;
    &lt;updated&gt;2011-05-16T20:29:38-0700&lt;/updated&gt;
    &lt;link href="/services/server/logger/AdminHandler%3AAuthenticationHandler" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/server/logger/AdminHandler%3AAuthenticationHandler" rel="list"/&gt;
    &lt;link href="/services/server/logger/AdminHandler%3AAuthenticationHandler" rel="edit"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="eai:acl"&gt;. . .&lt;/s:key&gt;
        &lt;s:key name="level"&gt;WARN&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
  . . .
  &lt;entry&gt;
    &lt;title&gt;Application&lt;/title&gt;
    &lt;id&gt;https://mrt:8089/services/server/logger/Application&lt;/id&gt;
    &lt;updated&gt;2011-05-16T20:29:38-0700&lt;/updated&gt;
    &lt;link href="/services/server/logger/Application" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/server/logger/Application" rel="list"/&gt;
    &lt;link href="/services/server/logger/Application" rel="edit"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="eai:acl"&gt;. . .&lt;/s:key&gt;
        &lt;s:key name="level"&gt;WARN&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;ApplicationManager&lt;/title&gt;
    &lt;id&gt;https://mrt:8089/services/server/logger/ApplicationManager&lt;/id&gt;
    &lt;updated&gt;2011-05-16T20:29:38-0700&lt;/updated&gt;
    &lt;link href="/services/server/logger/ApplicationManager" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/server/logger/ApplicationManager" rel="list"/&gt;
    &lt;link href="/services/server/logger/ApplicationManager" rel="edit"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="eai:acl"&gt;. . .&lt;/s:key&gt;
        &lt;s:key name="level"&gt;WARN&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## server/logger/{name}
{: name='serverloggername'}

Describes a specific splunkd logging category.

	[GET] server/logger/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view logger info. |
|--------------------------------
| **404** | Logger info does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Describes the logger for the Application Manager.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/server/logger/Application
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:s="http://dev.splunk.com/ns/rest"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;logger&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/server/logger&lt;/id&gt;
  &lt;updated&gt;2011-07-02T15:10:44-07:00&lt;/updated&gt;
  &lt;generator version="100492"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;opensearch:totalResults&gt;1&lt;/opensearch:totalResults&gt;
  &lt;opensearch:itemsPerPage&gt;30&lt;/opensearch:itemsPerPage&gt;
  &lt;opensearch:startIndex&gt;0&lt;/opensearch:startIndex&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;Application&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/server/logger/Application&lt;/id&gt;
    &lt;updated&gt;2011-07-02T15:10:44-07:00&lt;/updated&gt;
    &lt;link href="/services/server/logger/Application" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/server/logger/Application" rel="list"/&gt;
    &lt;link href="/services/server/logger/Application" rel="edit"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="eai:acl"&gt;. . .&lt;/s:key&gt;
        &lt;s:key name="eai:attributes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="optionalFields"&gt;
              &lt;s:list/&gt;
            &lt;/s:key&gt;
            &lt;s:key name="requiredFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;level&lt;/s:item&gt;
              &lt;/s:list&gt;
            &lt;/s:key&gt;
            &lt;s:key name="wildcardFields"&gt;
              &lt;s:list/&gt;
            &lt;/s:key&gt;
          &lt;/s:dict&gt;
        &lt;/s:key&gt;
        &lt;s:key name="level"&gt;WARN&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## server/logger/{name}
{: name='serverloggername'}

Sets the logging level for a specific logging category.

	[POST] server/logger/{name}

### Parameters

level
: _Required_ **Enum** Valid values: (FATAL &#124; CRIT &#124; WARN &#124; INFO &#124; DEBUG)<br/><br/>The desired logging level for this category.

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
| **403** | Insufficient permissions to edit logger configuration. |
|--------------------------------
| **404** | Logger configuration does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Sets the level of ApplicationManager logger to INFO.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/server/logger/Application \
	-d level=INFO
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;logger&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/server/logger&lt;/id&gt;
  &lt;updated&gt;2011-07-07T00:24:02-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## server/settings
{: name='serversettings'}

Returns the server configuration of an instance of Splunk.

	[GET] server/settings

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
| **403** | Insufficient permissions to view server settings. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

List the server configuration of this instance of Splunk.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/server/settings
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;server-settings&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/server/settings&lt;/id&gt;
  &lt;updated&gt;2011-07-08T01:56:40-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;settings&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/server/settings/settings&lt;/id&gt;
    &lt;updated&gt;2011-07-08T01:56:40-07:00&lt;/updated&gt;
    &lt;link href="/services/server/settings/settings" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/server/settings/settings" rel="list"/&gt;
    &lt;link href="/services/server/settings/settings" rel="edit"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="SPLUNK_DB"&gt;/home/amrit/temp/curl/splunk/var/lib/splunk&lt;/s:key&gt;
        &lt;s:key name="SPLUNK_HOME"&gt;/home/amrit/temp/curl/splunk&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="enableSplunkWebSSL"&gt;0&lt;/s:key&gt;
        &lt;s:key name="host"&gt;MrT&lt;/s:key&gt;
        &lt;s:key name="httpport"&gt;8001&lt;/s:key&gt;
        &lt;s:key name="mgmtHostPort"&gt;8085&lt;/s:key&gt;
        &lt;s:key name="minFreeSpace"&gt;2000000&lt;/s:key&gt;
        &lt;s:key name="pass4SymmKey"&gt;changeme&lt;/s:key&gt;
        &lt;s:key name="serverName"&gt;MrT&lt;/s:key&gt;
        &lt;s:key name="sessionTimeout"&gt;1h&lt;/s:key&gt;
        &lt;s:key name="startwebserver"&gt;1&lt;/s:key&gt;
        &lt;s:key name="trustedIP"/&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## server/settings/{name}
{: name='serversettingsname'}

Returns the server configuration of this instance of Splunk.

	[GET] server/settings/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view server settings. |
|--------------------------------
| **404** | Server settings do not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Displays server settings just as server/settings does ("settings" is the only valid value for {name} here).

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/server/settings/settings
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>

</code></pre>

## server/settings/{name}
{: name='serversettingsname'}

Updates the server configuration of this instance of Splunk.

	[POST] server/settings/{name}

### Parameters

SPLUNK_DB
: _Optional_ **String** Path to the default index for this instance of Splunk.<br/><br/>The default location is:<br/><br/>  $SPLUNK_HOME/var/lib/splunk/defaultdb/db/

enableSplunkWebSSL
: _Optional_ **Boolean** Toggles between https and http. If true, enables https and SSL for Splunk Web. 

host
: _Optional_ **String** The default hostname to use for data inputs that do not override this setting.

httpport
: _Optional_ **String** Specifies the port on which Splunk Web is listening for this instance of Splunk. Defaults to 8000. If using SSL, set to the HTTPS port number.<br/><br/>httpport must be present for SplunkWeb to start. If omitted or 0 the server will NOT start an http listener.

mgmtHostPort
: _Optional_ **String** Specify IP address:Port to set the managment port for splunkd. <br/><br/>Defaults to 127.0.0.1:8089.

minFreeSpace
: _Optional_ **Number** Specifies, in MB, a safe amount of space that must exist for splunkd to continue operating.<br/><br/>minFreespace affects search and indexing:<br/><br/>Before attempting to launch a search, splunk requires this amount of free space on the filesystem where the dispatch directory is stored ($SPLUNK_HOME/var/run/splunk/dispatch).<br/><br/>Applied similarly to the search quota values in authorize.conf and limits.conf.<br/><br/>For indexing, periodically, the indexer checks space on all partitions that contain splunk indexes as specified by indexes.conf.  When you need to clear more disk space, indexing is paused and Splunk posts a ui banner + warning.

pass4SymmKey
: _Optional_ **String** Password string that is prepended to the splunk symmetric key to generate the final key that is used to sign all traffic between master/slave licenser.

serverName
: _Optional_ **String** Specify an ASCII String to set the name used to identify this Splunk instance for features such as distributed search. Defaults to <hostname>-<user running splunk>.

sessionTimeout
: _Optional_ **String** Specify a time range string to set the amount of time before a user session times out, expressed as a search-like time range. Default is 1h (one hour).<br/><br/>For example:<br/><br/>  24h: (24 hours)
  3d: (3 days)
  7200s: (7200 seconds, or two hours)


startwebserver
: _Optional_ **Boolean** Specify 1 to enable Splunk Web. 0 disables Splunk Web. Default is 1.

trustedIP
: _Optional_ **String** The IP address of the authenticating proxy. Set to a valid IP address to enable SSO.<br/><br/>Disabled by default. Normal value is '127.0.0.1'

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
| **403** | Insufficient permissions to edit server settings. |
|--------------------------------
| **404** | Server settings do not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Update the timout period for a user session to two hours.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/server/settings/settings \
	-d sessionTimeout=2h
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;server-settings&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/server/settings&lt;/id&gt;
  &lt;updated&gt;2011-07-08T01:56:40-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;settings&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/server/settings/settings&lt;/id&gt;
    &lt;updated&gt;2011-07-08T01:56:40-07:00&lt;/updated&gt;
    &lt;link href="/services/server/settings/settings" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/server/settings/settings" rel="list"/&gt;
    &lt;link href="/services/server/settings/settings" rel="edit"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="SPLUNK_DB"&gt;/home/amrit/temp/curl/splunk/var/lib/splunk&lt;/s:key&gt;
        &lt;s:key name="SPLUNK_HOME"&gt;/home/amrit/temp/curl/splunk&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="enableSplunkWebSSL"&gt;0&lt;/s:key&gt;
        &lt;s:key name="host"&gt;MrT&lt;/s:key&gt;
        &lt;s:key name="httpport"&gt;8001&lt;/s:key&gt;
        &lt;s:key name="mgmtHostPort"&gt;8085&lt;/s:key&gt;
        &lt;s:key name="minFreeSpace"&gt;2000000&lt;/s:key&gt;
        &lt;s:key name="pass4SymmKey"&gt;changeme&lt;/s:key&gt;
        &lt;s:key name="serverName"&gt;MrT&lt;/s:key&gt;
        &lt;s:key name="sessionTimeout"&gt;2h&lt;/s:key&gt;
        &lt;s:key name="startwebserver"&gt;1&lt;/s:key&gt;
        &lt;s:key name="trustedIP"/&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>


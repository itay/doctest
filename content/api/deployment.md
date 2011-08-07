## deployment/client
{: name='deploymentclient'}

Returns the status of the deployment client in this Splunk instance, including the host/port of its deployment server, and which server classes it is a part of.

A deployment client is a Splunk instance remotely configured by a deployment server. A Splunk instance can be both a deployment server and client at the same time. A Splunk deployment client belongs to one or more server classes.

	[GET] deployment/client

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
| **403** | Insufficient permissions to view deployment client status. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Retrieves deployment client status.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/deployment/client
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;deploymentclient&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/deployment/client&lt;/id&gt;
  &lt;updated&gt;2011-07-11T00:35:37-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;deployment-client&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/deployment/client/deployment-client&lt;/id&gt;
    &lt;updated&gt;2011-07-11T00:35:37-07:00&lt;/updated&gt;
    &lt;link href="/services/deployment/client/deployment-client" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/deployment/client/deployment-client" rel="list"/&gt;
    &lt;link href="/services/deployment/client/deployment-client" rel="edit"/&gt;
    &lt;link href="/services/deployment/client/deployment-client/reload" rel="reload"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="serverClasses"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;dstest:dstestapp&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
        &lt;s:key name="targetUri"&gt;essplunk:8089&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## deployment/client/{name}
{: name='deploymentclientname'}

Returns the configuration for the named deployment client.  The only valid name here is "deployment-client".  This is identical to accessing deployment/client without specifying a name.

	[GET] deployment/client/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view deployment client. |
|--------------------------------
| **404** | Deployment client does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Identical to retrieving deployment/client.  Note that "deployment-client" is the only valid name here.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/deployment/client/deployment-client
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>

</code></pre>

## deployment/client/{name}
{: name='deploymentclientname'}

Updates the configuration for this deployment client.

	[POST] deployment/client/{name}

### Parameters

disabled
: _Optional_ **Boolean** If true, disables this deployment client.

targetUri
: _Optional_ **String** URI of the deployment server for this deployment client.<br/><br/>Include the management port the server is listening on. For example:<br/><br/>  deployment_server_uri:mgmtPort<br/><br/>The default management port is 8089.

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
| **403** | Insufficient permissions to edit deployment client. |
|--------------------------------
| **404** | Deployment client does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Switch to being a client of the deployment server hosted at tiny:8089.  Note that "deployment-client" is the only valid name here.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/deployment/client/deployment-client \
	-d targetUri=tiny:8089
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;deploymentclient&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/deployment/client&lt;/id&gt;
  &lt;updated&gt;2011-07-11T00:39:17-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## deployment/client/{name}/reload
{: name='deploymentclientnamereload'}

Restarts the deployment client, reloading configuration from disk.

	[GET] deployment/client/{name}/reload

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deployment client restarted successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to restart deployment client. |
|--------------------------------
| **404** | Deployment client does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Reload the deployment client configuration from disk.  Note that "deployment-client" is the only valid name here.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/deployment/client/deployment-client/reload
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;deploymentclient&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/deployment/client&lt;/id&gt;
  &lt;updated&gt;2011-07-11T00:39:23-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;deployment-client&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/deployment/client/deployment-client&lt;/id&gt;
    &lt;updated&gt;2011-07-11T00:39:23-07:00&lt;/updated&gt;
    &lt;link href="/services/deployment/client/deployment-client" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/deployment/client/deployment-client" rel="list"/&gt;
    &lt;link href="/services/deployment/client/deployment-client" rel="edit"/&gt;
    &lt;link href="/services/deployment/client/deployment-client/reload" rel="reload"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="serverClasses"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;dstest:dstestapp&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
        &lt;s:key name="targetUri"&gt;tiny:8089&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## deployment/server
{: name='deploymentserver'}

Returns the configurations of all deployment servers.

A deployment server is a Splunk instance that acts as a centralized configuration manager.
Deployment clients poll server periodically to retrieve configurations.

	[GET] deployment/server

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
| **403** | Insufficient permissions to view all deployment server configurations. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Retrieves global configuration for deployment server instances.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/deployment/server
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:s="http://dev.splunk.com/ns/rest"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;deploymentserver&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/deployment/server&lt;/id&gt;
  &lt;updated&gt;2011-07-22T10:47:20-0700&lt;/updated&gt;
  &lt;generator version="101277"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/deployment/server/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;dept1&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/deployment/server/dept1&lt;/id&gt;
    &lt;updated&gt;2011-07-22T10:47:20-0700&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept1" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept1" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept1/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept1" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept1/disable" rel="disable"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept1/dept1.ServerClasses" rel="serverclasses"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="disabled"&gt;1&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="whitelist.0"&gt;*.dept1.splunk.com&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;dept2&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/deployment/server/dept2&lt;/id&gt;
    &lt;updated&gt;2011-07-22T10:47:20-0700&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept2" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept2" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept2/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept2" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept2/disable" rel="disable"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept2/dept2.ServerClasses" rel="serverclasses"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="disabled"&gt;1&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="whilelist.0"&gt;*.dept2.splunk.com&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## deployment/server/{name}
{: name='deploymentservername'}

Get the configuration information for this deployment server.

	[GET] deployment/server/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view this deployment server configuration. |
|--------------------------------
| **404** | Requested deployment server does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Retrieve deployment server configuration for instance 'dept1'

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/deployment/server/dept1
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom" 
      xmlns:s="http://dev.splunk.com/ns/rest" 
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;deploymentserver&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/deployment/server&lt;/id&gt;
  &lt;updated&gt;2011-07-22T10:50:17-0700&lt;/updated&gt;
  &lt;generator version="101277"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/deployment/server/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;dept1&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/deployment/server/dept1&lt;/id&gt;
    &lt;updated&gt;2011-07-22T10:50:17-0700&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept1" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept1" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept1/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept1" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept1/disable" rel="disable"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept1/dept1.ServerClasses" rel="serverclasses"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="disabled"&gt;1&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:attributes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="optionalFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;check-new&lt;/s:item&gt;
                &lt;s:item&gt;disabled&lt;/s:item&gt;
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
        &lt;s:key name="whitelist.0"&gt;*.dept1.splunk.com&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## deployment/server/{name}
{: name='deploymentservername'}

Updates deployment server instance configuration

	[POST] deployment/server/{name}

### Parameters

check-new
: _Optional_ **Boolean** If true, this deployment server reviews the information in its configuration to find out if there is something new or updated to push out to a deployment client.

disabled
: _Optional_ **Boolean** If true, disables this deployment server.

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
| **403** | Insufficient permissions to edit this deployment server configuration. |
|--------------------------------
| **404** | Requested deployment server does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Reload configuration to check for new server class on deployment server instance dept1.

#### Request
<pre class='terminal'>
curl -k -u admin:changeme https://localhost:8089/services/deployment/server/dept1 \
	-d check-new=true \
	-d disabled=false
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom" 
      xmlns:s="http://dev.splunk.com/ns/rest" 
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;deploymentserver&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/deployment/server&lt;/id&gt;
  &lt;updated&gt;2011-07-22T10:58:02-0700&lt;/updated&gt;
  &lt;generator version="101277"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/deployment/server/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;dept1&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/deployment/server/dept1&lt;/id&gt;
    &lt;updated&gt;2011-07-22T10:58:02-0700&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept1" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept1" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept1/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept1" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept1/dept1.Clients" rel="clients"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept1/disable" rel="disable"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept1/dept1.Reload" rel="reload"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept1/dept1.ServerClasses" rel="serverclasses"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="whitelist.0"&gt;*.dept1.splunk.com&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;dept2&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/deployment/server/dept2&lt;/id&gt;
    &lt;updated&gt;2011-07-22T10:58:02-0700&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept2" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept2" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept2/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept2" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept2/disable" rel="disable"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept2/dept2.ServerClasses" rel="serverclasses"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="disabled"&gt;1&lt;/s:key&gt;
        &lt;s:key name="eai:acl"&gt;&lt;s:dict&gt;&lt;s:key name="app"&gt;system&lt;/s:key&gt;&lt;s:key name="can_change_perms"&gt;1&lt;/s:key&gt;&lt;s:key name="can_share_app"&gt;1&lt;/s:key&gt;&lt;s:key name="can_share_global"&gt;1&lt;/s:key&gt;&lt;s:key name="can_share_user"&gt;0&lt;/s:key&gt;&lt;s:key name="can_write"&gt;1&lt;/s:key&gt;&lt;s:key name="modifiable"&gt;1&lt;/s:key&gt;&lt;s:key name="owner"&gt;nobody&lt;/s:key&gt;&lt;s:key name="perms"&gt;&lt;s:dict&gt;&lt;s:key name="read"&gt;&lt;s:list&gt;&lt;s:item&gt;*&lt;/s:item&gt;&lt;/s:list&gt;&lt;/s:key&gt;&lt;s:key name="write"&gt;&lt;s:list&gt;&lt;s:item&gt;*&lt;/s:item&gt;&lt;/s:list&gt;&lt;/s:key&gt;&lt;/s:dict&gt;&lt;/s:key&gt;&lt;s:key name="sharing"&gt;system&lt;/s:key&gt;&lt;/s:dict&gt;&lt;/s:key&gt;
        &lt;s:key name="whilelist.0"&gt;*.dept2.splunk.com&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## deployment/serverclass
{: name='deploymentserverclass'}

Lists all server classes defined for a deployment server.

	[GET] deployment/serverclass

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
| **403** | Insufficient permissions to view deployment server classes. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Lists all server classes for this deploymenent server.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/deployment/serverclass
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;deploymentserverclass&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/deployment/serverclass&lt;/id&gt;
  &lt;updated&gt;2011-07-21T13:51:08-07:00&lt;/updated&gt;
  &lt;generator version="104259"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/deployment/serverclass/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;AppsForDesktops&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/deployment/serverclass/AppsForDesktops&lt;/id&gt;
    &lt;updated&gt;2011-07-21T13:51:08-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/serverclass/AppsForDesktops" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/serverclass/AppsForDesktops" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/serverclass/AppsForDesktops" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/serverclass/AppsForDesktops/disable" rel="disable"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/serverclass_status/AppsForDesktops/status" rel="status"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="blacklist"&gt;*&lt;/s:key&gt;
        &lt;s:key name="blacklist.0"&gt;*&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="filterType"&gt;blacklist&lt;/s:key&gt;
        &lt;s:key name="repositoryLocation"&gt;/home/vishalp/inst/current/etc/deployment-apps&lt;/s:key&gt;
        &lt;s:key name="whitelist"&gt;*.desktops.yourcompany.com&lt;/s:key&gt;
        &lt;s:key name="whitelist.0"&gt;*.desktops.yourcompany.com&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## deployment/serverclass
{: name='deploymentserverclass'}

Creates a server class.

	[POST] deployment/serverclass

### Parameters

blacklist
: _Optional_ **String** used to blacklist hosts for this serverclass

blacklist.
: _Optional_ **String** used to blacklist hosts for this serverclass

blacklist.0
: _Optional_ **String** Criteria used to identify deployment clients to disallow this server class

blacklist.1
: _Optional_ **String** Criteria used to identify deployment clients to disallow this server class

blacklist.2
: _Optional_ **String** Criteria used to identify deployment clients to disallow this server class

blacklist.3
: _Optional_ **String** Criteria used to identify deployment clients to disallow this server class

blacklist.4
: _Optional_ **String** Criteria used to identify deployment clients to disallow this server class

blacklist.5
: _Optional_ **String** Criteria used to identify deployment clients to disallow this server class

blacklist.6
: _Optional_ **String** Criteria used to identify deployment clients to disallow this server class

blacklist.7
: _Optional_ **String** Criteria used to identify deployment clients to disallow this server class

blacklist.8
: _Optional_ **String** Criteria used to identify deployment clients to disallow this server class

blacklist.9
: _Optional_ **String** Criteria used to identify deployment clients to disallow this server class

continueMatching
: _Optional_ **Boolean**  Controls how configuration is layered across classes and server-specific settings.<br/><br/>If true, configuration lookups continue matching server classes, beyond the first match. If false, only the first match is used. Matching is done in the order that server classes are defined. Defaults to true.<br/><br/>A serverClass can override this property and stop the matching.


endpoint
: _Optional_ **String** Specify a URL template string, which specifies the endpoint from which content can be downloaded by a deployment client. The deployment client knows how to substitute the values of the variables in the URL. Any custom URL can also be supplied here as long as it uses the specified variables.<br/><br/>This attribute does not need to be specified unless you have a very specific need, for example: to acquire deployment application files from a third-party httpd, for extremely large environments.<br/><br/>Can be overridden at the serverClass level.<br/><br/>Defaults to $deploymentServerUri$/services/streams/deployment?name=$serverClassName$:$appName$

filterType
: _Optional_ **Enum** Valid values: (whitelist &#124; blacklist)<br/><br/>Determines the order of execution of filters. If filterType is whitelist, all whitelist filters are applied first, followed by blacklist filters. If filterType is blacklist, all blacklist filters are applied first, followed by whitelist filters.<br/><br/>The whitelist setting indicates a filtering strategy that pulls in a subset:<br/><br/>* Items are not considered to match the server class  by default.
* Items that match any whitelist entry, and do not match any blacklist entry, are considered to match the server class.
* Items that match any blacklist entry are not considered to match the server class, regardless of whitelist.<br/><br/>The blacklist setting indicates a filtering strategy that rules out a subset:<br/><br/>* Items are considered to match the server class by default.
* Items that match any blacklist entry, and do not match any whitelist entry, are considered to not match the server class.
* Items that match any whitelist entry are considered to match the server class.<br/><br/>More briefly:<br/><br/>  whitelist: default no-match -> whitelists enable -> blacklists disable<br/><br/>  blacklist: default match -> blacklists disable-> whitelists enable<br/><br/>You can override this value at the serverClass and serverClass:app levels. If you specify whitelist at the global level, and then specify blacklist for an individual server class, the setting becomes blacklist for that server class, and you have to provide another filter in that server class definition to replace the one you overrode.

name
: _Required_ **String** The name of the server class.

repositoryLocation
: _Optional_ **String** The location on the deployment server to store the content that is to be deployed for this server class.<br/><br/>For example: $SPLUNK_HOME/etc/deployment-apps

targetRepositoryLocation
: _Optional_ **String** The location on the deployment client where the content to be deployed for this server class should be installed. <br/><br/>You can override this in deploymentclient.conf on the deployment client.

tmpFolder
: _Optional_ **String** Working folder used by the deployment server.<br/><br/>Defaults to $SPLUNK_HOME@OsDirSep@var@OsDirSep@run@OsDirSep@tmp

whitelist
: _Optional_ **String** list of hosts to accept for this serverclass

whitelist.
: _Optional_ **String** list of hosts to accept for this serverclass

whitelist.0
: _Optional_ **String** Criteria used to identify deployment clients to allow access to this server class

whitelist.1
: _Optional_ **String** Criteria used to identify deployment clients to allow access to this server class

whitelist.2
: _Optional_ **String** Criteria used to identify deployment clients to allow access to this server class

whitelist.3
: _Optional_ **String** Criteria used to identify deployment clients to allow access to this server class

whitelist.4
: _Optional_ **String** Criteria used to identify deployment clients to allow access to this server class

whitelist.5
: _Optional_ **String** Criteria used to identify deployment clients to allow access to this server class

whitelist.6
: _Optional_ **String** Criteria used to identify deployment clients to allow access to this server class

whitelist.7
: _Optional_ **String** Criteria used to identify deployment clients to allow access to this server class

whitelist.8
: _Optional_ **String** Criteria used to identify deployment clients to allow access to this server class

whitelist.9
: _Optional_ **String** Criteria used to identify deployment clients to allow access to this server class

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
| **403** | Insufficient permissions to create a deployment server class. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Create a new serverclass, with the name MyServerClass.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/deployment/serverclass \
	-d name=MyServerClass
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;deploymentserverclass&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/deployment/serverclass&lt;/id&gt;
  &lt;updated&gt;2011-07-21T15:41:12-07:00&lt;/updated&gt;
  &lt;generator version="104259"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/deployment/serverclass/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;AppsForDesktops&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/deployment/serverclass/AppsForDesktops&lt;/id&gt;
    &lt;updated&gt;2011-07-21T15:41:12-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/serverclass/AppsForDesktops" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/serverclass/AppsForDesktops" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/serverclass/AppsForDesktops" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/serverclass/AppsForDesktops/disable" rel="disable"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/serverclass_status/AppsForDesktops/status" rel="status"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="blacklist"&gt;*&lt;/s:key&gt;
        &lt;s:key name="blacklist.0"&gt;*&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="filterType"&gt;blacklist&lt;/s:key&gt;
        &lt;s:key name="repositoryLocation"&gt;/home/vishalp/inst/current/etc/deployment-apps&lt;/s:key&gt;
        &lt;s:key name="whitelist"&gt;*.desktops.yourcompany.com&lt;/s:key&gt;
        &lt;s:key name="whitelist.0"&gt;*.desktops.yourcompany.com&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## deployment/serverclass/{name}
{: name='deploymentserverclassname'}

Returns information about this server class.

	[GET] deployment/serverclass/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view deployment server class. |
|--------------------------------
| **404** | Deployment server class does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Return configuration details for the serverclass, MyServerClass.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/deployment/serverclass/MyServerClass
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;deploymentserverclass&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/deployment/serverclass&lt;/id&gt;
  &lt;updated&gt;2011-07-21T15:38:00-07:00&lt;/updated&gt;
  &lt;generator version="104259"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/deployment/serverclass/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;MyServerClass&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/deployment/serverclass/MyServerClass&lt;/id&gt;
    &lt;updated&gt;2011-07-21T15:38:00-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/serverclass/MyServerClass" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/serverclass/MyServerClass" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/serverclass/MyServerClass" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/serverclass/MyServerClass/disable" rel="disable"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/serverclass_status/MyServerClass/status" rel="status"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="blacklist"&gt;*&lt;/s:key&gt;
        &lt;s:key name="blacklist.0"&gt;*&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:attributes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="optionalFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;blacklist&lt;/s:item&gt;
                &lt;s:item&gt;blacklist.&lt;/s:item&gt;
                &lt;s:item&gt;blacklist.0&lt;/s:item&gt;
                &lt;s:item&gt;blacklist.1&lt;/s:item&gt;
                &lt;s:item&gt;blacklist.2&lt;/s:item&gt;
                &lt;s:item&gt;blacklist.3&lt;/s:item&gt;
                &lt;s:item&gt;blacklist.4&lt;/s:item&gt;
                &lt;s:item&gt;blacklist.5&lt;/s:item&gt;
                &lt;s:item&gt;blacklist.6&lt;/s:item&gt;
                &lt;s:item&gt;blacklist.7&lt;/s:item&gt;
                &lt;s:item&gt;blacklist.8&lt;/s:item&gt;
                &lt;s:item&gt;blacklist.9&lt;/s:item&gt;
                &lt;s:item&gt;continueMatching&lt;/s:item&gt;
                &lt;s:item&gt;endpoint&lt;/s:item&gt;
                &lt;s:item&gt;filterType&lt;/s:item&gt;
                &lt;s:item&gt;repositoryLocation&lt;/s:item&gt;
                &lt;s:item&gt;targetRepositoryLocation&lt;/s:item&gt;
                &lt;s:item&gt;tmpFolder&lt;/s:item&gt;
                &lt;s:item&gt;whitelist&lt;/s:item&gt;
                &lt;s:item&gt;whitelist.&lt;/s:item&gt;
                &lt;s:item&gt;whitelist.0&lt;/s:item&gt;
                &lt;s:item&gt;whitelist.1&lt;/s:item&gt;
                &lt;s:item&gt;whitelist.2&lt;/s:item&gt;
                &lt;s:item&gt;whitelist.3&lt;/s:item&gt;
                &lt;s:item&gt;whitelist.4&lt;/s:item&gt;
                &lt;s:item&gt;whitelist.5&lt;/s:item&gt;
                &lt;s:item&gt;whitelist.6&lt;/s:item&gt;
                &lt;s:item&gt;whitelist.7&lt;/s:item&gt;
                &lt;s:item&gt;whitelist.8&lt;/s:item&gt;
                &lt;s:item&gt;whitelist.9&lt;/s:item&gt;
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
        &lt;s:key name="filterType"&gt;blacklist&lt;/s:key&gt;
        &lt;s:key name="repositoryLocation"&gt;/home/vishalp/inst/current/etc/deployment-apps&lt;/s:key&gt;
        &lt;s:key name="whitelist"&gt;*.web.fflanda.com,*.linux.fflanda.com&lt;/s:key&gt;
        &lt;s:key name="whitelist.0"&gt;*.web.fflanda.com&lt;/s:key&gt;
        &lt;s:key name="whitelist.1"&gt;*.linux.fflanda.com&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## deployment/serverclass/{name}
{: name='deploymentserverclassname'}

Creates a new server class.

	[POST] deployment/serverclass/{name}

### Parameters

blacklist
: _Optional_ **INHERITED** INHERITED

blacklist.
: _Optional_ **INHERITED** INHERITED

blacklist.0
: _Optional_ **INHERITED** INHERITED

blacklist.1
: _Optional_ **INHERITED** INHERITED

blacklist.2
: _Optional_ **INHERITED** INHERITED

blacklist.3
: _Optional_ **INHERITED** INHERITED

blacklist.4
: _Optional_ **INHERITED** INHERITED

blacklist.5
: _Optional_ **INHERITED** INHERITED

blacklist.6
: _Optional_ **INHERITED** INHERITED

blacklist.7
: _Optional_ **INHERITED** INHERITED

blacklist.8
: _Optional_ **INHERITED** INHERITED

blacklist.9
: _Optional_ **INHERITED** INHERITED

continueMatching
: _Optional_ **INHERITED** INHERITED

endpoint
: _Optional_ **INHERITED** INHERITED

filterType
: _Optional_ **INHERITED** INHERITED

repositoryLocation
: _Optional_ **INHERITED** INHERITED

targetRepositoryLocation
: _Optional_ **INHERITED** INHERITED

tmpFolder
: _Optional_ **INHERITED** INHERITED

whitelist
: _Optional_ **INHERITED** INHERITED

whitelist.
: _Optional_ **INHERITED** INHERITED

whitelist.0
: _Optional_ **INHERITED** INHERITED

whitelist.1
: _Optional_ **INHERITED** INHERITED

whitelist.2
: _Optional_ **INHERITED** INHERITED

whitelist.3
: _Optional_ **INHERITED** INHERITED

whitelist.4
: _Optional_ **INHERITED** INHERITED

whitelist.5
: _Optional_ **INHERITED** INHERITED

whitelist.6
: _Optional_ **INHERITED** INHERITED

whitelist.7
: _Optional_ **INHERITED** INHERITED

whitelist.8
: _Optional_ **INHERITED** INHERITED

whitelist.9
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
| **403** | Insufficient permissions to edit deployment server class. |
|--------------------------------
| **404** | Deployment server class does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Set the filter type for MyServerClass to blacklist, all blacklist filters are applied first, followed by whitelist filters. It also sets filters for both the blacklist and the whitelist.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/deployment/serverclass/MyServerClass \
	-d filterType=blacklist \
	-d blacklist.0=* \
	-d whitelist.0=*.web.fflanda.com \
	-d whitelist.1=*.linux.fflanda.com
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;deploymentserverclass&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/deployment/serverclass&lt;/id&gt;
  &lt;updated&gt;2011-07-21T13:52:02-07:00&lt;/updated&gt;
  &lt;generator version="104259"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/deployment/serverclass/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;AppsForDesktops&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/deployment/serverclass/AppsForDesktops&lt;/id&gt;
    &lt;updated&gt;2011-07-21T13:52:02-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/serverclass/AppsForDesktops" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/serverclass/AppsForDesktops" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/serverclass/AppsForDesktops" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/serverclass/AppsForDesktops/disable" rel="disable"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/serverclass_status/AppsForDesktops/status" rel="status"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="blacklist"&gt;*&lt;/s:key&gt;
        &lt;s:key name="blacklist.0"&gt;*&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="filterType"&gt;blacklist&lt;/s:key&gt;
        &lt;s:key name="repositoryLocation"&gt;/home/vishalp/inst/current/etc/deployment-apps&lt;/s:key&gt;
        &lt;s:key name="whitelist"&gt;*.desktops.yourcompany.com&lt;/s:key&gt;
        &lt;s:key name="whitelist.0"&gt;*.desktops.yourcompany.com&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## deployment/tenants
{: name='deploymenttenants'}

Lists the multi-tenants configuration for this Splunk instance.

Multi-tenants configuration is a type of deployment server topology where more than one deployment server is running on the same Splunk instance, and each of those deployment servers serves content to its own set of deployment clients.

	[GET] deployment/tenants

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
| **403** | Insufficient permissions to view deployment tenants configuration. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Retrieve tentant configuration for all deployment servers hosted by the splunk instance

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/deployment/tenants
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom" 
      xmlns:s="http://dev.splunk.com/ns/rest" 
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;deploymenttenants&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/deployment/tenants&lt;/id&gt;
  &lt;updated&gt;2011-07-22T11:10:32-0700&lt;/updated&gt;
  &lt;generator version="101277"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/deployment/tenants/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;dept1&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/deployment/tenants/dept1&lt;/id&gt;
    &lt;updated&gt;2011-07-22T11:10:32-0700&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/tenants/dept1" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/tenants/dept1" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/tenants/dept1/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/tenants/dept1" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/tenants/dept1/dept1.Clients" rel="clients"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/tenants/dept1/disable" rel="disable"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/tenants/dept1/dept1.Reload" rel="reload"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/tenants/dept1/dept1.ServerClasses" rel="serverclasses"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="whitelist.0"&gt;*.dept1.splunk.com&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;dept2&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/deployment/tenants/dept2&lt;/id&gt;
    &lt;updated&gt;2011-07-22T11:10:32-0700&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/tenants/dept2" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/tenants/dept2" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/tenants/dept2/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/tenants/dept2" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/tenants/dept2/disable" rel="disable"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/tenants/dept2/dept2.ServerClasses" rel="serverclasses"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="disabled"&gt;1&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="whilelist.0"&gt;*.dept2.splunk.com&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## deployment/tenants/{name}
{: name='deploymenttenantsname'}

Lists the configuration for this deployment server in a multi-tenant configuration.

	[GET] deployment/tenants/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view the deployment tenants configuration. |
|--------------------------------
| **404** | Deployment tenants configuration does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Retrieve configuration for deployment server instance dept1

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/deployment/tenants/dept1
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:s="http://dev.splunk.com/ns/rest"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;deploymentserver&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/deployment/server&lt;/id&gt;
  &lt;updated&gt;2011-07-22T11:08:46-0700&lt;/updated&gt;
  &lt;generator version="101277"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/deployment/server/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;dept1&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/deployment/server/dept1&lt;/id&gt;
    &lt;updated&gt;2011-07-22T11:08:46-0700&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept1" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept1" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept1/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept1" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept1/dept1.Clients" rel="clients"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept1/disable" rel="disable"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept1/dept1.Reload" rel="reload"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/server/dept1/dept1.ServerClasses" rel="serverclasses"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:attributes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="optionalFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;check-new&lt;/s:item&gt;
                &lt;s:item&gt;disabled&lt;/s:item&gt;
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
        &lt;s:key name="whitelist.0"&gt;*.dept1.splunk.com&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## deployment/tenants/{name}
{: name='deploymenttenantsname'}

Updates the configuration for this deployment server in a multi-tenant configuration.

	[POST] deployment/tenants/{name}

### Parameters

check-new
: _Optional_ **Boolean** If true, this deployment server in a multi-tenant configuration reviews the information in its configuration to find out if there is something new or updated to push out to a deployment client.

disabled
: _Optional_ **Boolean** If true, disables this deployment server, which is in a multi-tenant configuration.

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
| **403** | Insufficient permissions to edit the deployment tenants configuration. |
|--------------------------------
| **404** | Deployment tenants configuration does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Get deployment server configuration for deployment server instance dept1

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/deployment/tenants/dept1 \
	-d check-new=true \
	-d disabled=false
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom" 
      xmlns:s="http://dev.splunk.com/ns/rest" 
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;deploymenttenants&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/deployment/tenants&lt;/id&gt;
  &lt;updated&gt;2011-07-22T11:39:46-0700&lt;/updated&gt;
  &lt;generator version="101277"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/deployment/tenants/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;dept1&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/deployment/tenants/dept1&lt;/id&gt;
    &lt;updated&gt;2011-07-22T11:39:46-0700&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/tenants/dept1" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/tenants/dept1" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/tenants/dept1/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/tenants/dept1" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/tenants/dept1/dept1.Clients" rel="clients"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/tenants/dept1/disable" rel="disable"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/tenants/dept1/dept1.Reload" rel="reload"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/tenants/dept1/dept1.ServerClasses" rel="serverclasses"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="whitelist.0"&gt;*.dept1.splunk.com&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;dept2&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/deployment/tenants/dept2&lt;/id&gt;
    &lt;updated&gt;2011-07-22T11:39:46-0700&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/tenants/dept2" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/tenants/dept2" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/tenants/dept2/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/tenants/dept2" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/tenants/dept2/disable" rel="disable"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/tenants/dept2/dept2.ServerClasses" rel="serverclasses"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="disabled"&gt;1&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="whilelist.0"&gt;*.dept2.splunk.com&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;dest1&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/deployment/tenants/dest1&lt;/id&gt;
    &lt;updated&gt;2011-07-22T11:39:46-0700&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/tenants/dest1" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/tenants/dest1" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/tenants/dest1/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/tenants/dest1" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/tenants/dest1/disable" rel="disable"/&gt;
    &lt;link href="/servicesNS/nobody/system/deployment/tenants/dest1/dest1.ServerClasses" rel="serverclasses"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="disabled"&gt;1&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## search/distributed/config
{: name='searchdistributedconfig'}

Lists the configuration options for the distributed search system.

	[GET] search/distributed/config

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
| **403** | Insufficient permissions to view configuration for distributed search. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Retrieves distributed search configuration.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/search/distributed/config
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;distsearch-setup&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/search/distributed/config&lt;/id&gt;
  &lt;updated&gt;2011-07-10T23:21:51-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;distributedSearch&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/search/distributed/config/distributedSearch&lt;/id&gt;
    &lt;updated&gt;2011-07-10T23:21:51-07:00&lt;/updated&gt;
    &lt;link href="/services/search/distributed/config/distributedSearch" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/search/distributed/config/distributedSearch" rel="list"/&gt;
    &lt;link href="/services/search/distributed/config/distributedSearch" rel="edit"/&gt;
    &lt;link href="/services/search/distributed/config/distributedSearch" rel="remove"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="autoAddServers"&gt;0&lt;/s:key&gt;
        &lt;s:key name="blacklistNames"/&gt;
        &lt;s:key name="blacklistURLs"/&gt;
        &lt;s:key name="checkTimedOutServersFrequency"&gt;60&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;s:key name="dist_search_enabled"&gt;1&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="heartbeatFrequency"&gt;0&lt;/s:key&gt;
        &lt;s:key name="heartbeatMcastAddr"&gt;224.0.0.37&lt;/s:key&gt;
        &lt;s:key name="heartbeatPort"&gt;8888&lt;/s:key&gt;
        &lt;s:key name="removedTimedOutServers"&gt;0&lt;/s:key&gt;
        &lt;s:key name="serverTimeout"&gt;10&lt;/s:key&gt;
        &lt;s:key name="servers"/&gt;
        &lt;s:key name="shareBundles"&gt;1&lt;/s:key&gt;
        &lt;s:key name="skipOurselves"&gt;0&lt;/s:key&gt;
        &lt;s:key name="statusTimeout"&gt;10&lt;/s:key&gt;
        &lt;s:key name="ttl"&gt;1&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## search/distributed/config/{name}
{: name='searchdistributedconfigname'}

Disables the distributed search feature.  Note that "distributedSearch" is the only valid name here.

	[DELETE] search/distributed/config/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deleted successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to delete configuration for distributed search. |
|--------------------------------
| **404** | Configuration for distributed search does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Disables the distributed search configuration.  Note that "distributedSearch" is the only valid name here.

#### Request
<pre class='terminal'>
curl -k -u admin:pass --request DELETE \
	https://localhost:8089/services/search/distributed/config/distributedSearch
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;distsearch-setup&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/search/distributed/config&lt;/id&gt;
  &lt;updated&gt;2011-07-10T23:23:17-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## search/distributed/config/{name}
{: name='searchdistributedconfigname'}

Displays configuration options.  Note that "distributedSearch" is the only valid name here.

	[GET] search/distributed/config/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view configuration for distributed search. |
|--------------------------------
| **404** | Configuration for distributed search does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Retrieves distributed search configuration.  This is identical to accessing search/distributed/config.  Note that "distributedSearch" is the only valid name here.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/search/distributed/config/distributedSearch
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>

</code></pre>

## search/distributed/config/{name}
{: name='searchdistributedconfigname'}

Update the configuration for the distributed search feature.  Note that "distributedSearch" is the only valid name here.

	[POST] search/distributed/config/{name}

### Parameters

autoAddServers
: _Optional_ **Boolean** If true, automatically add all discovered servers.

blacklistNames
: _Optional_ **String** A comma-separated list of servers that you do not want to peer with. <br/><br/>Servers are the 'server name' that is created at startup time.

blacklistURLs
: _Optional_ **String** Specify a comma separated list of server names or URIs to specify servers to blacklist.<br/><br/>You can blacklist on server name or server URI (x.x.x.x:port).

checkTimedOutServersFrequency
: _Optional_ **Number** Rechecks servers at the specified frequency (in seconds).  If this is set to 0, then no recheck occurs. Defaults to 60.<br/><br/>This attribute is ONLY relevant if removeTimedOutServers is set to true. If removeTimedOutServers is false, this attribute is ignored.


connectionTimeout
: _Optional_ **Number** Amount of time, in seconds, to use as a timeout during search peer connection establishment.

disabled
: _Optional_ **Boolean** If true, disables the distributed search.<br/><br/>Defaults to false (the distributed search is enabled).

heartbeatFrequency
: _Optional_ **Number** The period between heartbeat messages, in seconds. <br/><br/>Use 0 to disable sending of heartbeats. Defaults to 0.

heartbeatMcastAddr
: _Optional_ **String** Specify an IP address to set a multicast address where each Splunk server sends and listens for heart beat messages.<br/><br/>This allows Splunk servers to auto-discover other Splunk servers on your network. Defaults to 224.0.0.37.

heartbeatPort
: _Optional_ **String** Specify a port to set the heartbeat port where each Splunk server sends and listens for heart beat messages.<br/><br/>This allows Splunk servers to auto-discover other Splunk servers on the network. Defaults to 8888.

receiveTimeout
: _Optional_ **Number** Amount of time in seconds to use as a timeout while trying to read/receive data from a search peer.

removedTimedOutServers
: _Optional_ **Boolean** If true, removes a server connection that cannot be made within serverTimeout.<br/><br/>If false, every call to that server attempts to connect. This may result in a slow user interface.<br/><br/>Defaults to false.

sendTimeout
: _Optional_ **Number** Amount of time in seconds to use as a timeout while trying to write/send data to a search peer.

serverTimeout
: _Optional_ **Number** Deprected. Use connectionTimeout, sendTimeout, and receiveTimeout.

servers
: _Optional_ **String** Specify a comma-separated list of server to set the initial list of servers.  <br/><br/>If operating completely in autoAddServers mode (discovering all servers), there is no need to list any servers here.

shareBundles
: _Optional_ **Boolean** Indicates whether this server uses bundle replication to share search time configuration with search peers. <br/><br/>If set to false, the search head assumes that the search peers can access the correct bundles using an NFS share and have correctly configured the options listed under: "SEARCH HEAD BUNDLE MOUNTING OPTIONS."<br/><br/>Defaults to true.

skipOurselves
: _Optional_ **Boolean** If set to true, this server does NOT participate as a server in any search or other call.<br/><br/>This is used for building a node that does nothing but merge the results from other servers. <br/><br/>Defaults to false.

statusTimeout
: _Optional_ **Number** Set connection timeout when gathering a search peer's basic info (/services/server/info). Defaults to 10.<br/><br/>Note: Read/write timeouts are automatically set to twice this value.


ttl
: _Optional_ **Number** Time to live (ttl) of the heartbeat messages. Defaults to 1 (this subnet).<br/><br/>Increasing this number allows the UDP multicast packets to spread beyond the current subnet to the specified number of hops.<br/><br/>NOTE:  This only works if routers along the way are configured to pass UDP multicast packets.

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
| **403** | Insufficient permissions to edit configuration for distributed search. |
|--------------------------------
| **404** | Configuration for distributed search does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

This example changes the connection timeout period of a distributed search to 20 seconds.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/search/distributed/config/distributedSearch \
	-d connectionTimeout=20
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;distsearch-setup&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/search/distributed/config&lt;/id&gt;
  &lt;updated&gt;2011-07-10T23:23:06-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## search/distributed/peers
{: name='searchdistributedpeers'}

Returns a list of configured search peers that this search head is configured to distribute searches to.

	[GET] search/distributed/peers

### Parameters

count
: _Optional_ **Number** Maximum number of items to return.

discoveredPeersOnly
: _Optional_ **Bool** If set to true, only list peers that have been auto-discovered.

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
| **403** | Insufficient permissions to view search peer. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

This example list of configured search peers that this search head is configured to distribute searches to.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/search/distributed/peers
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;distsearch-peer&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/search/distributed/peers&lt;/id&gt;
  &lt;updated&gt;2011-07-11T18:21:48-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/search/distributed/peers/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;tiny:8090&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/search/distributed/peers/tiny%3A8090&lt;/id&gt;
    &lt;updated&gt;2011-07-11T18:21:48-07:00&lt;/updated&gt;
    &lt;link href="/services/search/distributed/peers/tiny%3A8090" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/search/distributed/peers/tiny%3A8090" rel="list"/&gt;
    &lt;link href="/services/search/distributed/peers/tiny%3A8090" rel="edit"/&gt;
    &lt;link href="/services/search/distributed/peers/tiny%3A8090" rel="remove"/&gt;
    &lt;link href="/services/search/distributed/peers/tiny%3A8090/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="build"/&gt;
        &lt;s:key name="bundle_versions"&gt;
          &lt;s:list/&gt;
        &lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="guid"/&gt;
        &lt;s:key name="is_https"&gt;1&lt;/s:key&gt;
        &lt;s:key name="licenseSignature"/&gt;
        &lt;s:key name="peerName"&gt;tiny:8090&lt;/s:key&gt;
        &lt;s:key name="peerType"&gt;configured&lt;/s:key&gt;
        &lt;s:key name="replicationStatus"&gt;Initial&lt;/s:key&gt;
        &lt;s:key name="status"&gt;Down&lt;/s:key&gt;
        &lt;s:key name="version"/&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## search/distributed/peers
{: name='searchdistributedpeers'}

Adds a new search peer.

	[POST] search/distributed/peers

### Parameters

name
: _Required_ **String** The name of the search peer.<br/><br/>Defined as hostname:port, where port is the management port.

remotePassword
: _Required_ **String** The password of the remote user.<br/><br/>This is used to authenicate with the search peer to exchange certificates.

remoteUsername
: _Required_ **String** A username with admin privileges in the search peer server.<br/><br/>This is used to exchange certificates.

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
| **403** | Insufficient permissions to create search peer. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

This example adds a new search peer.  Note that distributed search must first be enabled via the search/distributed/config endpoint.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/search/distributed/peers \
	-d name=MrT:8092 \
	-d remoteUsername=admin \
	-d remotePassword=mypass
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;distsearch-peer&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/search/distributed/peers&lt;/id&gt;
  &lt;updated&gt;2011-07-11T18:22:00-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/search/distributed/peers/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## search/distributed/peers/{name}
{: name='searchdistributedpeersname'}

Removes the distributed search peer specified by {name}.

	[DELETE] search/distributed/peers/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deleted successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to delete search peer. |
|--------------------------------
| **404** | Search peer does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

This example removes the distributed search peer hosted at MrT:8092.

#### Request
<pre class='terminal'>
curl -k -u admin:pass --request DELETE \
	https://localhost:8089/services/search/distributed/peers/MrT%3A8092
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;distsearch-peer&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/search/distributed/peers&lt;/id&gt;
  &lt;updated&gt;2011-07-11T18:24:31-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/search/distributed/peers/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## search/distributed/peers/{name}
{: name='searchdistributedpeersname'}

Returns information about the distributed search peer specified by {name}.

	[GET] search/distributed/peers/{name}

### Parameters

discoveredPeersOnly
: _Optional_ **Boolean** If true, return only auto-discovered search peers.

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view search peer. |
|--------------------------------
| **404** | Search peer does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

This example retrieves information about the search peer hosted at MrT:8092.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/search/distributed/peers/MrT%3A8092
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;distsearch-peer&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/search/distributed/peers&lt;/id&gt;
  &lt;updated&gt;2011-07-11T18:23:34-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/search/distributed/peers/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;MrT:8092&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/search/distributed/peers/MrT%3A8092&lt;/id&gt;
    &lt;updated&gt;2011-07-11T18:23:34-07:00&lt;/updated&gt;
    &lt;link href="/services/search/distributed/peers/MrT%3A8092" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/search/distributed/peers/MrT%3A8092" rel="list"/&gt;
    &lt;link href="/services/search/distributed/peers/MrT%3A8092" rel="edit"/&gt;
    &lt;link href="/services/search/distributed/peers/MrT%3A8092" rel="remove"/&gt;
    &lt;link href="/services/search/distributed/peers/MrT%3A8092/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="build"&gt;102878&lt;/s:key&gt;
        &lt;s:key name="bundle_versions"&gt;
          &lt;s:list/&gt;
        &lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:attributes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="optionalFields"&gt;
              &lt;s:list/&gt;
            &lt;/s:key&gt;
            &lt;s:key name="requiredFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;remotePassword&lt;/s:item&gt;
                &lt;s:item&gt;remoteUsername&lt;/s:item&gt;
              &lt;/s:list&gt;
            &lt;/s:key&gt;
            &lt;s:key name="wildcardFields"&gt;
              &lt;s:list/&gt;
            &lt;/s:key&gt;
          &lt;/s:dict&gt;
        &lt;/s:key&gt;
        &lt;s:key name="guid"&gt;04D30EDF-A255-47D9-8B78-4ED003AFB660&lt;/s:key&gt;
        &lt;s:key name="is_https"&gt;1&lt;/s:key&gt;
        &lt;s:key name="licenseSignature"&gt;69fc3b4aef59da9610548e84ce63b8a2&lt;/s:key&gt;
        &lt;s:key name="peerName"&gt;MrT-amrit&lt;/s:key&gt;
        &lt;s:key name="peerType"&gt;configured&lt;/s:key&gt;
        &lt;s:key name="replicationStatus"&gt;Initial&lt;/s:key&gt;
        &lt;s:key name="status"&gt;Up&lt;/s:key&gt;
        &lt;s:key name="version"&gt;20110705&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## search/distributed/peers/{name}
{: name='searchdistributedpeersname'}

Update the configuration of the distributed search peer specified by {name}.

	[POST] search/distributed/peers/{name}

### Parameters

remotePassword
: _Required_ **INHERITED** INHERITED

remoteUsername
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
| **403** | Insufficient permissions to edit search peer. |
|--------------------------------
| **404** | Search peer does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

This example updates the username and password used to authenticate against the distributed search peer hosted at MrT:8092.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/search/distributed/peers/MrT%3A8092 \
	-d remoteUsername=admin \
	-d remotePassword=pass
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;distsearch-peer&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/search/distributed/peers&lt;/id&gt;
  &lt;updated&gt;2011-07-11T18:24:11-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/search/distributed/peers/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>


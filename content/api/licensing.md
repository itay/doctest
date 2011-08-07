## licenser/groups
{: name='licensergroups'}

Lists all licenser groups.

	[GET] licenser/groups

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
| **403** | Insufficient permissions to view licenser groups. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Lists all the licenser groups for this Splunnk instance.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/licenser/groups
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;groups&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/licenser/groups&lt;/id&gt;
  &lt;updated&gt;2011-07-11T09:45:35-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;Enterprise&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/licenser/groups/Enterprise&lt;/id&gt;
    &lt;updated&gt;2011-07-11T09:45:35-07:00&lt;/updated&gt;
    &lt;link href="/services/licenser/groups/Enterprise" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/licenser/groups/Enterprise" rel="list"/&gt;
    &lt;link href="/services/licenser/groups/Enterprise" rel="edit"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="is_active"&gt;1&lt;/s:key&gt;
        &lt;s:key name="stack_ids"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;enterprise&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## licenser/groups/{name}
{: name='licensergroupsname'}

Lists a specific licenser group.  A licenser group contains one or more licenser stacks that can operate concurrently.  Only one licenser group is active at any given time

	[GET] licenser/groups/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view licenser groups. |
|--------------------------------
| **404** | Licenser groups does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Return information about the Forwarder licenser group.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/licenser/groups/Forwarder
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;groups&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/licenser/groups&lt;/id&gt;
  &lt;updated&gt;2011-07-11T09:47:18-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;Forwarder&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/licenser/groups/Forwarder&lt;/id&gt;
    &lt;updated&gt;2011-07-11T09:47:18-07:00&lt;/updated&gt;
    &lt;link href="/services/licenser/groups/Forwarder" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/licenser/groups/Forwarder" rel="list"/&gt;
    &lt;link href="/services/licenser/groups/Forwarder" rel="edit"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:attributes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="optionalFields"&gt;
              &lt;s:list/&gt;
            &lt;/s:key&gt;
            &lt;s:key name="requiredFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;is_active&lt;/s:item&gt;
              &lt;/s:list&gt;
            &lt;/s:key&gt;
            &lt;s:key name="wildcardFields"&gt;
              &lt;s:list/&gt;
            &lt;/s:key&gt;
          &lt;/s:dict&gt;
        &lt;/s:key&gt;
        &lt;s:key name="is_active"&gt;0&lt;/s:key&gt;
        &lt;s:key name="stack_ids"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;forwarder&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## licenser/groups/{name}
{: name='licensergroupsname'}

Activates specific licenser group with the side effect of deactivating the previously active one.

There can only be a single active licenser group for a given instance of Splunk.  Use this to switch between, for example, free to enterprise, or download-trial to free.

	[POST] licenser/groups/{name}

### Parameters

is_active
: _Required_ **Boolean** Active specific licenser group

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
| **403** | Insufficient permissions to edit licenser group. |
|--------------------------------
| **404** | Licenser group does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Make the Enterprise licenser group the active license group.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/licenser/groups/Enterprise \
	-d is_active=1
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;groups&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/licenser/groups&lt;/id&gt;
  &lt;updated&gt;2011-07-11T09:55:02-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## licenser/licenses
{: name='licenserlicenses'}

Lists all licenses that have been added.  Only a subset of these licenses may be active however, this is simply listing all licenses in every stack/group, regardless of which group is active

	[GET] licenser/licenses

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
| **403** | Insufficient permissions to view licenses. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

List information about all licenses for the Splunk instance.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/licenser/licenses
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;licenses&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/licenser/licenses&lt;/id&gt;
  &lt;updated&gt;2011-07-11T09:30:33-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/licenser/licenses/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;E08B . . . FA75BF&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/licenser/licenses/E08B . . . FA75BF&lt;/id&gt;
    &lt;updated&gt;2011-07-11T09:30:33-07:00&lt;/updated&gt;
    &lt;link href="/services/licenser/licenses/E08B . . . FA75BF" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/licenser/licenses/E08B . . . FA75BF" rel="list"/&gt;
    &lt;link href="/services/licenser/licenses/E08B . . . FA75BF" rel="remove"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="creation_time"&gt;1309852804&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="expiration_time"&gt;1315641604&lt;/s:key&gt;
        &lt;s:key name="features"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;Auth&lt;/s:item&gt;
            &lt;s:item&gt;FwdData&lt;/s:item&gt;
            &lt;s:item&gt;RcvData&lt;/s:item&gt;
            &lt;s:item&gt;LocalSearch&lt;/s:item&gt;
            &lt;s:item&gt;DistSearch&lt;/s:item&gt;
            &lt;s:item&gt;RcvSearch&lt;/s:item&gt;
            &lt;s:item&gt;ScheduledSearch&lt;/s:item&gt;
            &lt;s:item&gt;Alerting&lt;/s:item&gt;
            &lt;s:item&gt;DeployClient&lt;/s:item&gt;
            &lt;s:item&gt;DeployServer&lt;/s:item&gt;
            &lt;s:item&gt;SplunkWeb&lt;/s:item&gt;
            &lt;s:item&gt;SigningProcessor&lt;/s:item&gt;
            &lt;s:item&gt;SyslogOutputProcessor&lt;/s:item&gt;
            &lt;s:item&gt;AllowDuplicateKeys&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
        &lt;s:key name="group_id"&gt;Trial&lt;/s:key&gt;
        &lt;s:key name="label"&gt;Splunk Enterprise Download Trial&lt;/s:key&gt;
        &lt;s:key name="license_hash"&gt;E08B . . . FA75BF&lt;/s:key&gt;
        &lt;s:key name="max_violations"&gt;5&lt;/s:key&gt;
        &lt;s:key name="quota"&gt;524288000&lt;/s:key&gt;
        &lt;s:key name="sourcetypes"&gt;
          &lt;s:list/&gt;
        &lt;/s:key&gt;
        &lt;s:key name="stack_id"&gt;download-trial&lt;/s:key&gt;
        &lt;s:key name="status"&gt;VALID&lt;/s:key&gt;
        &lt;s:key name="type"&gt;download-trial&lt;/s:key&gt;
        &lt;s:key name="window_period"&gt;30&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## licenser/licenses
{: name='licenserlicenses'}

Add a license entitlement to this instance.

	[POST] licenser/licenses

### Parameters

name
: _Required_ **string** Path to license file on server. If the payload parameter is specified, the name parameter is ignored.

payload
: _Optional_ **string** String representation of license, encoded in xml

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
| **403** | Insufficient permissions to add a license. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Adds a Splunk license entitlement from a downloaded Splunk license file.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/licenser/licenses \
	-d name=/Users/vgenovese/downloads/Splunk_enterprise.lic
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;licenses&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/licenser/licenses&lt;/id&gt;
  &lt;updated&gt;2011-07-11T09:41:32-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/licenser/licenses/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;CF6C50 . . . 72CE6C&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/licenser/licenses/CF6C50 . . . 72CE6C&lt;/id&gt;
    &lt;updated&gt;2011-07-11T09:41:32-07:00&lt;/updated&gt;
    &lt;link href="/services/licenser/licenses/CF6C50 . . . 72CE6C" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/licenser/licenses/CF6C50 . . . 72CE6C" rel="list"/&gt;
    &lt;link href="/services/licenser/licenses/CF6C50 . . . 72CE6C" rel="remove"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="creation_time"&gt;1306168427&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="expiration_time"&gt;2147483647&lt;/s:key&gt;
        &lt;s:key name="features"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;Auth&lt;/s:item&gt;
            &lt;s:item&gt;FwdData&lt;/s:item&gt;
            &lt;s:item&gt;RcvData&lt;/s:item&gt;
            &lt;s:item&gt;LocalSearch&lt;/s:item&gt;
            &lt;s:item&gt;DistSearch&lt;/s:item&gt;
            &lt;s:item&gt;RcvSearch&lt;/s:item&gt;
            &lt;s:item&gt;ScheduledSearch&lt;/s:item&gt;
            &lt;s:item&gt;Alerting&lt;/s:item&gt;
            &lt;s:item&gt;DeployClient&lt;/s:item&gt;
            &lt;s:item&gt;DeployServer&lt;/s:item&gt;
            &lt;s:item&gt;SplunkWeb&lt;/s:item&gt;
            &lt;s:item&gt;SigningProcessor&lt;/s:item&gt;
            &lt;s:item&gt;SyslogOutputProcessor&lt;/s:item&gt;
            &lt;s:item&gt;CanBeRemoteMaster&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
        &lt;s:key name="group_id"&gt;Enterprise&lt;/s:key&gt;
        &lt;s:key name="label"&gt;Splunk Enterprise&lt;/s:key&gt;
        &lt;s:key name="license_hash"&gt;CF6C50 . . . 72CE6C&lt;/s:key&gt;
        &lt;s:key name="max_violations"&gt;5&lt;/s:key&gt;
        &lt;s:key name="quota"&gt;10737418240&lt;/s:key&gt;
        &lt;s:key name="sourcetypes"&gt;
          &lt;s:list/&gt;
        &lt;/s:key&gt;
        &lt;s:key name="stack_id"&gt;enterprise&lt;/s:key&gt;
        &lt;s:key name="status"&gt;VALID&lt;/s:key&gt;
        &lt;s:key name="type"&gt;enterprise&lt;/s:key&gt;
        &lt;s:key name="window_period"&gt;30&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## licenser/licenses/{name}
{: name='licenserlicensesname'}

Delete the license with hash corresponding to {name}.

NOTE: You cannot delete the last license out of an active group. First, deactivate the group (by switching to another group) and then perform the delete.

	[DELETE] licenser/licenses/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deleted successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to delete license. |
|--------------------------------
| **404** | License does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Deletes the specified license.
Note: The hash for the license payload has been elided for readability

#### Request
<pre class='terminal'>
curl -k -u admin:pass --request DELETE \
	https://localhost:8089/services/licenser/licenses/E4BF . . . FC639D
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom" 
  xmlns:s="http://dev.splunk.com/ns/rest" 
  xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;licenses&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/licenser/licenses&lt;/id&gt;
  &lt;updated&gt;2011-07-07T09:45:12-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/licenser/licenses/_new" rel="create"/&gt;
  &lt;opensearch:totalResults&gt;0&lt;/opensearch:totalResults&gt;
  &lt;opensearch:itemsPerPage&gt;30&lt;/opensearch:itemsPerPage&gt;
  &lt;opensearch:startIndex&gt;0&lt;/opensearch:startIndex&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## licenser/licenses/{name}
{: name='licenserlicensesname'}

List attributes of specific license.  The {name} portion of URL is actually the hash of the license payload.

	[GET] licenser/licenses/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view license. |
|--------------------------------
| **404** | License does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

This example lists the details of the Splunk Enterprise license.
Note: The hash for the license payload has been elided for readability.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://127.0.0.1:3339/services/licenser/licenses/E4BF . . . FC639D
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:s="http://dev.splunk.com/ns/rest"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;licenses&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/licenser/licenses&lt;/id&gt;
  &lt;updated&gt;2011-07-05T15:57:08-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/licenser/licenses/_new" rel="create"/&gt;
  &lt;opensearch:totalResults&gt;1&lt;/opensearch:totalResults&gt;
  &lt;opensearch:itemsPerPage&gt;30&lt;/opensearch:itemsPerPage&gt;
  &lt;opensearch:startIndex&gt;0&lt;/opensearch:startIndex&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;E4BF . . . FC639D&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/licenser/licenses/E4BF . . . FC639D&lt;/id&gt;
    &lt;updated&gt;2011-07-05T15:57:08-07:00&lt;/updated&gt;
    &lt;link href="/services/licenser/licenses/E4BF . . . FC639D" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/licenser/licenses/E4BF . . . FC639D" rel="list"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="creation_time"&gt;1300901512&lt;/s:key&gt;
        &lt;s:key name="eai:acl"&gt; . . . &lt;/s:key&gt;
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
        &lt;s:key name="expiration_time"&gt;1314811912&lt;/s:key&gt;
        &lt;s:key name="features"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;Auth&lt;/s:item&gt;
            &lt;s:item&gt;FwdData&lt;/s:item&gt;
            &lt;s:item&gt;RcvData&lt;/s:item&gt;
            &lt;s:item&gt;LocalSearch&lt;/s:item&gt;
            &lt;s:item&gt;DistSearch&lt;/s:item&gt;
            &lt;s:item&gt;RcvSearch&lt;/s:item&gt;
            &lt;s:item&gt;ScheduledSearch&lt;/s:item&gt;
            &lt;s:item&gt;Alerting&lt;/s:item&gt;
            &lt;s:item&gt;DeployClient&lt;/s:item&gt;
            &lt;s:item&gt;DeployServer&lt;/s:item&gt;
            &lt;s:item&gt;SplunkWeb&lt;/s:item&gt;
            &lt;s:item&gt;SigningProcessor&lt;/s:item&gt;
            &lt;s:item&gt;SyslogOutputProcessor&lt;/s:item&gt;
            &lt;s:item&gt;AllowDuplicateKeys&lt;/s:item&gt;
            &lt;s:item&gt;CanBeRemoteMaster&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
        &lt;s:key name="group_id"&gt;Enterprise&lt;/s:key&gt;
        &lt;s:key name="label"&gt;Splunk Internal License&lt;/s:key&gt;
        &lt;s:key name="license_hash"&gt;E4BF . . . FC639D&lt;/s:key&gt;
        &lt;s:key name="max_violations"&gt;5&lt;/s:key&gt;
        &lt;s:key name="quota"&gt;10737418240&lt;/s:key&gt;
        &lt;s:key name="sourcetypes"&gt;&lt;s:list/&gt;&lt;/s:key&gt;
        &lt;s:key name="stack_id"&gt;enterprise&lt;/s:key&gt;
        &lt;s:key name="status"&gt;VALID&lt;/s:key&gt;
        &lt;s:key name="type"&gt;enterprise&lt;/s:key&gt;
        &lt;s:key name="window_period"&gt;30&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## licenser/messages
{: name='licensermessages'}

Lists all messages/alerts/persisted warnings for this node.

	[GET] licenser/messages

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
| **403** | Insufficient permissions to view licenser messages. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

This example lists messages from the Splunk Enterprise license.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/licenser/messages
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;licensermessages&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/licenser/messages&lt;/id&gt;
  &lt;updated&gt;2011-08-02T03:50:46-07:00&lt;/updated&gt;
  &lt;generator version="105103"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;70a19a5cfe6d7c2a678089638dee7bea&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/licenser/messages/70a19a5cfe6d7c2a678089638dee7bea&lt;/id&gt;
    &lt;updated&gt;2011-08-02T03:50:46-07:00&lt;/updated&gt;
    &lt;link href="/services/licenser/messages/70a19a5cfe6d7c2a678089638dee7bea" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/licenser/messages/70a19a5cfe6d7c2a678089638dee7bea" rel="list"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="category"&gt;pool_warning_count&lt;/s:key&gt;
        &lt;s:key name="create_time"&gt;1312282230&lt;/s:key&gt;
        &lt;s:key name="description"&gt;This pool contains slave(s) with 3 warnings&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="pool_id"/&gt;
        &lt;s:key name="severity"&gt;WARN&lt;/s:key&gt;
        &lt;s:key name="slave_id"/&gt;
        &lt;s:key name="stack_id"/&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## licenser/messages/{name}
{: name='licensermessagesname'}

List specific message whose msgId corresponds to {name} component.

	[GET] licenser/messages/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view licenser messages. |
|--------------------------------
| **404** | Licenser message does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

This example lists the message for corresponding msgID.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://127.0.0.1:3339/services/licenser/messages/2702b33a1bd369ae9209a9ecf4cb39db
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:s="http://dev.splunk.com/ns/rest"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
    &lt;title&gt;licensermessages&lt;/title&gt;
    &lt;id&gt;https://127.0.0.1:3339/services/licenser/messages&lt;/id&gt;
    &lt;updated&gt;2011-05-16T21:45:17-07:00&lt;/updated&gt;
    &lt;generator version="99678"/&gt;
    &lt;author&gt;
        &lt;name&gt;Splunk&lt;/name&gt;
    &lt;/author&gt;
    &lt;opensearch:totalResults&gt;1&lt;/opensearch:totalResults&gt;
    &lt;opensearch:itemsPerPage&gt;30&lt;/opensearch:itemsPerPage&gt;
    &lt;opensearch:startIndex&gt;0&lt;/opensearch:startIndex&gt;
    &lt;s:messages/&gt;
    &lt;entry&gt;
        &lt;title&gt;2702b33a1bd369ae9209a9ecf4cb39db&lt;/title&gt;
        &lt;id&gt;https://127.0.0.1:3339/services/licenser/messages/2702b33a1bd369ae9209a9ecf4cb39db&lt;/id&gt;
        &lt;updated&gt;2011-05-16T21:45:17-07:00&lt;/updated&gt;
        &lt;link href="/services/licenser/messages/2702b33a1bd369ae9209a9ecf4cb39db" rel="alternate"/&gt;
        &lt;author&gt;
            &lt;name&gt;system&lt;/name&gt;
        &lt;/author&gt;
        &lt;link href="/services/licenser/messages/2702b33a1bd369ae9209a9ecf4cb39db" rel="list"/&gt;
        &lt;content type="text/xml"&gt;
            &lt;s:dict&gt;
                &lt;s:key name="category"&gt;license_window&lt;/s:key&gt;
                &lt;s:key name="create_time"&gt;1305607136&lt;/s:key&gt;
                &lt;s:key name="description"&gt;test warnings&lt;/s:key&gt;
                &lt;s:key name="eai:acl"&gt;. . .&lt;/s:key&gt;
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
                &lt;s:key name="pool_id"/&gt;
                &lt;s:key name="severity"&gt;WARN&lt;/s:key&gt;
                &lt;s:key name="slave_id"/&gt;
                &lt;s:key name="stack_id"/&gt;
            &lt;/s:dict&gt;
        &lt;/content&gt;
    &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## licenser/pools
{: name='licenserpools'}

Enumerates all pools.  A pool logically partitions the daily volume entitlements of a stack. You can use a pool to divide license privileges amongst multiple slaves

	[GET] licenser/pools

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
| **403** | Insufficient permissions to view licenser pools. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Lists the license pool configuration for this instance of Splunk.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/licenser/pools
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:s="http://dev.splunk.com/ns/rest"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;pools&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/licenser/pools&lt;/id&gt;
  &lt;updated&gt;2011-07-08T10:55:18-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/licenser/pools/_new" rel="create"/&gt;
  &lt;link href="/services/licenser/pools/_reload" rel="_reload"/&gt;
  &lt;opensearch:totalResults&gt;4&lt;/opensearch:totalResults&gt;
  &lt;opensearch:itemsPerPage&gt;30&lt;/opensearch:itemsPerPage&gt;
  &lt;opensearch:startIndex&gt;0&lt;/opensearch:startIndex&gt;
  &lt;s:messages/&gt;
  . . .
  &lt;entry&gt;
    &lt;title&gt;auto_generated_pool_enterprise&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/licenser/pools/auto_generated_pool_enterprise&lt;/id&gt;
    &lt;updated&gt;2011-07-08T10:55:18-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/licenser/pools/auto_generated_pool_enterprise" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/licenser/pools/auto_generated_pool_enterprise" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/licenser/pools/auto_generated_pool_enterprise/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/system/licenser/pools/auto_generated_pool_enterprise" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/system/licenser/pools/auto_generated_pool_enterprise" rel="remove"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="description"&gt;auto_generated_pool_enterprise&lt;/s:key&gt;
        &lt;s:key name="eai:acl"&gt; . . . &lt;/s:key&gt;
        &lt;s:key name="quota"&gt;MAX&lt;/s:key&gt;
        &lt;s:key name="slaves"&gt;&lt;s:list&gt;&lt;s:item&gt;*&lt;/s:item&gt;&lt;/s:list&gt;&lt;/s:key&gt;
        &lt;s:key name="slaves_usage_bytes"&gt;
          &lt;s:dict&gt;&lt;s:key name="1F3A34AE-75DA-4680-B184-5BF309843919"&gt;26445659&lt;/s:key&gt;&lt;/s:dict&gt;
        &lt;/s:key&gt;
        &lt;s:key name="stack_id"&gt;enterprise&lt;/s:key&gt;
        &lt;s:key name="used_bytes"&gt;26445659&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;auto_generated_pool_forwarder&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/licenser/pools/auto_generated_pool_forwarder&lt;/id&gt;
    &lt;updated&gt;2011-07-08T10:55:18-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/licenser/pools/auto_generated_pool_forwarder" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/licenser/pools/auto_generated_pool_forwarder" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/licenser/pools/auto_generated_pool_forwarder/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/system/licenser/pools/auto_generated_pool_forwarder" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/system/licenser/pools/auto_generated_pool_forwarder" rel="remove"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="description"&gt;auto_generated_pool_forwarder&lt;/s:key&gt;
       &lt;s:key name="eai:acl"&gt; . . . &lt;/s:key&gt;
        &lt;s:key name="quota"&gt;MAX&lt;/s:key&gt;
        &lt;s:key name="slaves"&gt;&lt;s:list&gt;&lt;s:item&gt;*&lt;/s:item&gt;&lt;/s:list&gt;&lt;/s:key&gt;
        &lt;s:key name="slaves_usage_bytes"&gt;&lt;/s:key&gt;
        &lt;s:key name="stack_id"&gt;forwarder&lt;/s:key&gt;
        &lt;s:key name="used_bytes"&gt;0&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
  . . .
&lt;/feed&gt;
</code></pre>

## licenser/pools
{: name='licenserpools'}

Create a license pool.

	[POST] licenser/pools

### Parameters

description
: _Optional_ **String** description of this pool

name
: _Required_ **String** Edit the properties of the specified pool

quota
: _Required_ **String** Defines the byte quota of this pool.<br/><br/>Valid values:<br/><br/>MAX: maximum amount allowed by the license. You can only have one pool with MAX size in a stack.<br/><br/>Number[MB&#124;GB]: Specify a specific size. For example, 552428800, or simply specify 50MB.

slaves
: _Optional_ **String** Comma-separated list of slaveids that are members of this pool, or '*' to accept all slaves.<br/><br/>You can also specify a comma-separated list guids to specify slaves that can connect to this pool.

stack_id
: _Required_ **Enum** Valid values: (download-trial &#124; enterprise &#124; forwarder &#124; free)<br/><br/>Stack ID of the stack corresponding to this pool

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
| **403** | Insufficient permissions to create licenser pools. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Create a license pool, myLicensePool, that accepts all enterprise license slaves and accepts the maximum number of bytes allowed for this license.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/licenser/pools \
	-d name=myLicensePool \
	-d quota=MAX \
	-d slaves=* \
	-d stack_id=enterprise
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:s="http://dev.splunk.com/ns/rest"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;pools&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/licenser/pools&lt;/id&gt;
  &lt;updated&gt;2011-07-08T11:31:47-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/licenser/pools/_new" rel="create"/&gt;
  &lt;link href="/services/licenser/pools/_reload" rel="_reload"/&gt;
  &lt;opensearch:totalResults&gt;0&lt;/opensearch:totalResults&gt;
  &lt;opensearch:itemsPerPage&gt;30&lt;/opensearch:itemsPerPage&gt;
  &lt;opensearch:startIndex&gt;0&lt;/opensearch:startIndex&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## licenser/pools/{name}
{: name='licenserpoolsname'}

Delete specified pool.  Deleting pools is not supported for every pool. Certain stacks have fixed pools which cannot be deleted.

	[DELETE] licenser/pools/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deleted successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to delete licenser pool. |
|--------------------------------
| **404** | Licenser pool does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Deletes the auto-generated enterprise license pool.
Typically, you delete this pool to create a new enterprise license pool.

#### Request
<pre class='terminal'>
curl -k -u admin:pass --request DELETE \
	https://localhost:8089/services/licenser/pools/auto_generated_pool_enterprise
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom" 
      xmlns:s="http://dev.splunk.com/ns/rest" 
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;pools&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/licenser/pools&lt;/id&gt;
  &lt;updated&gt;2011-07-08T11:29:26-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/licenser/pools/_new" rel="create"/&gt;
  &lt;link href="/services/licenser/pools/_reload" rel="_reload"/&gt;
  &lt;opensearch:totalResults&gt;0&lt;/opensearch:totalResults&gt;
  &lt;opensearch:itemsPerPage&gt;30&lt;/opensearch:itemsPerPage&gt;
  &lt;opensearch:startIndex&gt;0&lt;/opensearch:startIndex&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## licenser/pools/{name}
{: name='licenserpoolsname'}

Lists details of the pool specified by {name}.

A pool logically partitions the daily volume entitlements of a stack. A pool can be used to divide license privileges amongst multiple slaves

	[GET] licenser/pools/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view licenser pools. |
|--------------------------------
| **404** | Licenser pool does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Display details of the automatically generated license pool for forwarders.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/licenser/pools/auto_generated_pool_forwarder
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:s="http://dev.splunk.com/ns/rest"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;pools&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/licenser/pools&lt;/id&gt;
  &lt;updated&gt;2011-07-08T11:03:37-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/licenser/pools/_new" rel="create"/&gt;
  &lt;link href="/services/licenser/pools/_reload" rel="_reload"/&gt;
  &lt;opensearch:totalResults&gt;1&lt;/opensearch:totalResults&gt;
  &lt;opensearch:itemsPerPage&gt;30&lt;/opensearch:itemsPerPage&gt;
  &lt;opensearch:startIndex&gt;0&lt;/opensearch:startIndex&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;auto_generated_pool_forwarder&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/licenser/pools/auto_generated_pool_forwarder&lt;/id&gt;
    &lt;updated&gt;2011-07-08T11:03:37-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/licenser/pools/auto_generated_pool_forwarder" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/licenser/pools/auto_generated_pool_forwarder" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/licenser/pools/auto_generated_pool_forwarder/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/system/licenser/pools/auto_generated_pool_forwarder" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/system/licenser/pools/auto_generated_pool_forwarder" rel="remove"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="description"&gt;auto_generated_pool_forwarder&lt;/s:key&gt;
        &lt;s:key name="eai:acl"&gt; . . . &lt;/s:key&gt;
        &lt;s:key name="eai:attributes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="optionalFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;append_slaves&lt;/s:item&gt;
                &lt;s:item&gt;description&lt;/s:item&gt;
                &lt;s:item&gt;quota&lt;/s:item&gt;
                &lt;s:item&gt;slaves&lt;/s:item&gt;
              &lt;/s:list&gt;
            &lt;/s:key&gt;
            &lt;s:key name="requiredFields"&gt;
              &lt;s:list/&gt;&lt;/s:key&gt;
            &lt;s:key name="wildcardFields"&gt;
              &lt;s:list/&gt;
            &lt;/s:key&gt;
          &lt;/s:dict&gt;
        &lt;/s:key&gt;
        &lt;s:key name="quota"&gt;MAX&lt;/s:key&gt;
        &lt;s:key name="slaves"&gt;&lt;s:list&gt;&lt;s:item&gt;*&lt;/s:item&gt;&lt;/s:list&gt;&lt;/s:key&gt;
        &lt;s:key name="slaves_usage_bytes"&gt;&lt;/s:key&gt;
        &lt;s:key name="stack_id"&gt;forwarder&lt;/s:key&gt;
        &lt;s:key name="used_bytes"&gt;0&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## licenser/pools/{name}
{: name='licenserpoolsname'}

Edit properties of the pool specified by {name}.

	[POST] licenser/pools/{name}

### Parameters

append_slaves
: _Optional_ **Boolean** Flag which controls whether newly specified slaves will be appended to existing slaves list or overwritten

description
: _Optional_ **INHERITED** INHERITED

quota
: _Optional_ **INHERITED** INHERITED

slaves
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
| **403** | Insufficient permissions to edit licenser pool. |
|--------------------------------
| **404** | Licenser pool does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Modify the byte quota for the license pool, myLicensePool, to allow 50 MB.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/licenser/pools/myLicensePool \
	-d quota=50MB
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
 . . .
  &lt;entry&gt;
    &lt;title&gt;myLicensePool&lt;/title&gt;
    &lt;id&gt;https://localhost:8085/servicesNS/nobody/system/licenser/pools/myLicensePool&lt;/id&gt;
    &lt;updated&gt;2011-07-24T08:46:49-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/licenser/pools/myLicensePool" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/licenser/pools/myLicensePool" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/licenser/pools/myLicensePool/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/system/licenser/pools/myLicensePool" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/system/licenser/pools/myLicensePool" rel="remove"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="description"&gt;&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:attributes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="optionalFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;append_slaves&lt;/s:item&gt;
                &lt;s:item&gt;description&lt;/s:item&gt;
                &lt;s:item&gt;quota&lt;/s:item&gt;
                &lt;s:item&gt;slaves&lt;/s:item&gt;
              &lt;/s:list&gt;
            &lt;/s:key&gt;
            &lt;s:key name="requiredFields"&gt;
              &lt;s:list/&gt;&lt;/s:key&gt;
            &lt;s:key name="wildcardFields"&gt;
              &lt;s:list/&gt;&lt;/s:key&gt;
          &lt;/s:dict&gt;
        &lt;/s:key&gt;
        &lt;s:key name="quota"&gt;552428800&lt;/s:key&gt;
        &lt;s:key name="slaves"&gt;&lt;s:list&gt;&lt;s:item&gt;*&lt;/s:item&gt;&lt;/s:list&gt;&lt;/s:key&gt;
        &lt;s:key name="slaves_usage_bytes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="1F3A34AE-75DA-4680-B184-5BF309843919"&gt;39846322&lt;/s:key&gt;
          &lt;/s:dict&gt;
        &lt;/s:key&gt;
        &lt;s:key name="stack_id"&gt;enterprise&lt;/s:key&gt;
        &lt;s:key name="used_bytes"&gt;39846322&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
</code></pre>

## licenser/slaves
{: name='licenserslaves'}

List all slaves registered to this license master.  Any slave that attempts to connect to master is reported, regardless of whether it is allocated to a master licenser pool.

	[GET] licenser/slaves

### Parameters

count
: _Optional_ **Number** Maximum number of items to return.

offset
: _Optional_ **Number** Index for first item to return.

poolid
: _Optional_ **n/a** Do not use.

search
: _Optional_ **String** Boolean predicate to filter results.

sort_dir
: _Optional_ **Enum** Direction to sort by (asc/desc).

sort_key
: _Optional_ **String** Field to sort by.

sort_mode
: _Optional_ **Enum** Collating sequence for the sort (auto, alpha, alpha_case, num).

stackid
: _Optional_ **string** Do not use.

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view license slaves. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

This example lists all slaves to this Splunk server, which is a license master.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/licenser/slaves
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
  xmlns:s="http://dev.splunk.com/ns/rest"
  xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;slaves&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/licenser/slaves&lt;/id&gt;
  &lt;updated&gt;2011-05-17T09:37:54-07:00&lt;/updated&gt;
  &lt;generator version="99849"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;opensearch:totalResults&gt;1&lt;/opensearch:totalResults&gt;
  &lt;opensearch:itemsPerPage&gt;30&lt;/opensearch:itemsPerPage&gt;
  &lt;opensearch:startIndex&gt;0&lt;/opensearch:startIndex&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;74A43C7E-C33C-41F6-B027-E603D2C3FE68&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/licenser/slaves/74A43C7E-C33C-41F6-B027-E603D2C3FE68&lt;/id&gt;
    &lt;updated&gt;2011-05-17T09:37:54-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/licenser/slaves/74A43C7E-C33C-41F6-B027-E603D2C3FE68" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/licenser/slaves/74A43C7E-C33C-41F6-B027-E603D2C3FE68" rel="list"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="eai:acl"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="app"&gt;system&lt;/s:key&gt;
            &lt;s:key name="can_write"&gt;1&lt;/s:key&gt;
              &lt;s:key name="modifiable"&gt;0&lt;/s:key&gt;
            &lt;s:key name="owner"&gt;nobody&lt;/s:key&gt;
            &lt;s:key name="perms"&gt;
              &lt;s:dict&gt;
                &lt;s:key name="read"&gt;
                  &lt;s:list&gt;
                    &lt;s:item&gt;admin&lt;/s:item&gt;
                  &lt;/s:list&gt;
                &lt;/s:key&gt;
                &lt;s:key name="write"&gt;
                  &lt;s:list&gt;
                    &lt;s:item&gt;admin&lt;/s:item&gt;
                  &lt;/s:list&gt;
                &lt;/s:key&gt;
              &lt;/s:dict&gt;
            &lt;/s:key&gt;
            &lt;s:key name="sharing"&gt;system&lt;/s:key&gt;
          &lt;/s:dict&gt;
        &lt;/s:key&gt;
        &lt;s:key name="label"&gt;thething-vishalp&lt;/s:key&gt;
        &lt;s:key name="pool_ids"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;auto_generated_pool_enterprise&lt;/s:item&gt;
            &lt;s:item&gt;auto_generated_pool_forwarder&lt;/s:item&gt;
            &lt;s:item&gt;auto_generated_pool_free&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
        &lt;s:key name="stack_ids"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;enterprise&lt;/s:item&gt;
            &lt;s:item&gt;forwarder&lt;/s:item&gt;
            &lt;s:item&gt;free&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
        &lt;s:key name="warning_count"&gt;0&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## licenser/slaves/{name}
{: name='licenserslavesname'}

List attributes of slave specified by {name}.

	[GET] licenser/slaves/{name}

### Parameters

poolid
: _Optional_ **Do not use.** Do not use.

stackid
: _Optional_ **string** do not use

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view license slave. |
|--------------------------------
| **404** | License slave does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

This example displays the details of a specific licenser slave.
Use <pre>https://localhost:8089/services/licenser/slaves</pre> to obtain the IDs of licenser slaves.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/services/licenser/slaves/74A43C7E-C33C-41F6-B027-E603D2C3FE68
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
    xmlns:s="http://dev.splunk.com/ns/rest"
    xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;slaves&lt;/title&gt;
  &lt;id&gt;https://127.0.0.1:8282/services/licenser/slaves&lt;/id&gt;
  &lt;updated&gt;2011-05-17T09:44:10-07:00&lt;/updated&gt;
  &lt;generator version="99849"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;opensearch:totalResults&gt;1&lt;/opensearch:totalResults&gt;
  &lt;opensearch:itemsPerPage&gt;30&lt;/opensearch:itemsPerPage&gt;
  &lt;opensearch:startIndex&gt;0&lt;/opensearch:startIndex&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;74A43C7E-C33C-41F6-B027-E603D2C3FE68&lt;/title&gt;
    &lt;id&gt;https://127.0.0.1:8282/servicesNS/nobody/system/licenser/slaves/74A43C7E-C33C-41F6-B027-E603D2C3FE68&lt;/id&gt;
    &lt;updated&gt;2011-05-17T09:44:10-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/licenser/slaves/74A43C7E-C33C-41F6-B027-E603D2C3FE68" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/licenser/slaves/74A43C7E-C33C-41F6-B027-E603D2C3FE68" rel="list"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="eai:acl"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="app"&gt;system&lt;/s:key&gt;
            &lt;s:key name="can_write"&gt;1&lt;/s:key&gt;
            &lt;s:key name="modifiable"&gt;0&lt;/s:key&gt;
            &lt;s:key name="owner"&gt;nobody&lt;/s:key&gt;
            &lt;s:key name="perms"&gt;
              &lt;s:dict&gt;
                &lt;s:key name="read"&gt;
                  &lt;s:list&gt;
                    &lt;s:item&gt;admin&lt;/s:item&gt;
                  &lt;/s:list&gt;
                &lt;/s:key&gt;
                &lt;s:key name="write"&gt;
                  &lt;s:list&gt;
                    &lt;s:item&gt;admin&lt;/s:item&gt;
                  &lt;/s:list&gt;
                &lt;/s:key&gt;
              &lt;/s:dict&gt;
            &lt;/s:key&gt;
            &lt;s:key name="sharing"&gt;system&lt;/s:key&gt;
          &lt;/s:dict&gt;
        &lt;/s:key&gt;
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
        &lt;s:key name="label"&gt;thething-vishalp&lt;/s:key&gt;
        &lt;s:key name="pool_ids"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;auto_generated_pool_enterprise&lt;/s:item&gt;
            &lt;s:item&gt;auto_generated_pool_forwarder&lt;/s:item&gt;
            &lt;s:item&gt;auto_generated_pool_free&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
        &lt;s:key name="stack_ids"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;enterprise&lt;/s:item&gt;
            &lt;s:item&gt;forwarder&lt;/s:item&gt;
            &lt;s:item&gt;free&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
        &lt;s:key name="warning_count"&gt;0&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## licenser/stacks
{: name='licenserstacks'}

Enumerate all license stacks.

	[GET] licenser/stacks

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
| **403** | Insufficient permissions to view license stacks. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Displays the license stack configuration for an instance of Splunk.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/licenser/stacks
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom" xmlns:s="http://dev.splunk.com/ns/rest" xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;stacks&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/licenser/stacks&lt;/id&gt;
  &lt;updated&gt;2011-07-08T10:37:33-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;opensearch:totalResults&gt;4&lt;/opensearch:totalResults&gt;
  &lt;opensearch:itemsPerPage&gt;30&lt;/opensearch:itemsPerPage&gt;
  &lt;opensearch:startIndex&gt;0&lt;/opensearch:startIndex&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;download-trial&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/licenser/stacks/download-trial&lt;/id&gt;
    &lt;updated&gt;2011-07-08T10:37:33-07:00&lt;/updated&gt;
    &lt;link href="/services/licenser/stacks/download-trial" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/licenser/stacks/download-trial" rel="list"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="eai:acl"&gt;. . . &lt;/s:key&gt;
        &lt;s:key name="label"&gt;Splunk Enterprise Download Trial&lt;/s:key&gt;
        &lt;s:key name="quota"&gt;524288000&lt;/s:key&gt;
        &lt;s:key name="type"&gt;download-trial&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;enterprise&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/licenser/stacks/enterprise&lt;/id&gt;
    &lt;updated&gt;2011-07-08T10:37:33-07:00&lt;/updated&gt;
    &lt;link href="/services/licenser/stacks/enterprise" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/licenser/stacks/enterprise" rel="list"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="eai:acl"&gt;. . . &lt;/s:key&gt;
        &lt;s:key name="label"&gt;Splunk Internal License&lt;/s:key&gt;
        &lt;s:key name="quota"&gt;10737418240&lt;/s:key&gt;
        &lt;s:key name="type"&gt;enterprise&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;forwarder&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/licenser/stacks/forwarder&lt;/id&gt;
    &lt;updated&gt;2011-07-08T10:37:33-07:00&lt;/updated&gt;
    &lt;link href="/services/licenser/stacks/forwarder" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/licenser/stacks/forwarder" rel="list"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="eai:acl"&gt;. . . &lt;/s:key&gt;
        &lt;s:key name="label"&gt;Splunk Forwarder&lt;/s:key&gt;
        &lt;s:key name="quota"&gt;1048576&lt;/s:key&gt;
        &lt;s:key name="type"&gt;forwarder&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;free&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/licenser/stacks/free&lt;/id&gt;
    &lt;updated&gt;2011-07-08T10:37:33-07:00&lt;/updated&gt;
    &lt;link href="/services/licenser/stacks/free" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/licenser/stacks/free" rel="list"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="eai:acl"&gt;. . . &lt;/s:key&gt;
        &lt;s:key name="label"&gt;Splunk Free&lt;/s:key&gt;
        &lt;s:key name="quota"&gt;524288000&lt;/s:key&gt;
        &lt;s:key name="type"&gt;free&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## licenser/stacks/{name}
{: name='licenserstacksname'}

Retrieve details of specific license stacks.  A license stack is comprised of one or more licenses of the same "type".  The daily indexing quota of a license stack is additive, so a stack represents the aggregate entitlement for a collection of licenses.

	[GET] licenser/stacks/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view license stacks. |
|--------------------------------
| **404** | License stack does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

This example lists details of the enterprise license stack.
In this example, the enterprise license stack contains one entry.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/enterprise
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:s="http://dev.splunk.com/ns/rest"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;stacks&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/licenser/stacks&lt;/id&gt;
  &lt;updated&gt;2011-07-08T10:42:44-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;opensearch:totalResults&gt;1&lt;/opensearch:totalResults&gt;
  &lt;opensearch:itemsPerPage&gt;30&lt;/opensearch:itemsPerPage&gt;
  &lt;opensearch:startIndex&gt;0&lt;/opensearch:startIndex&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;enterprise&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/licenser/stacks/enterprise&lt;/id&gt;
    &lt;updated&gt;2011-07-08T10:42:44-07:00&lt;/updated&gt;
    &lt;link href="/services/licenser/stacks/enterprise" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/licenser/stacks/enterprise" rel="list"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="eai:acl"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="app"&gt;&lt;/s:key&gt;
            &lt;s:key name="can_write"&gt;1&lt;/s:key&gt;
            &lt;s:key name="modifiable"&gt;0&lt;/s:key&gt;
            &lt;s:key name="owner"&gt;system&lt;/s:key&gt;
            &lt;s:key name="perms"&gt;
              &lt;s:dict&gt;
                &lt;s:key name="read"&gt;
                  &lt;s:list&gt;
                    &lt;s:item&gt;admin&lt;/s:item&gt;
                    &lt;/s:list&gt;
                &lt;/s:key&gt;
                &lt;s:key name="write"&gt;
                  &lt;s:list&gt;
                    &lt;s:item&gt;admin&lt;/s:item&gt;
                  &lt;/s:list&gt;
                &lt;/s:key&gt;
              &lt;/s:dict&gt;
            &lt;/s:key&gt;
            &lt;s:key name="sharing"&gt;system&lt;/s:key&gt;
          &lt;/s:dict&gt;
        &lt;/s:key&gt;
        &lt;s:key name="eai:attributes"&gt; . . . &lt;/s:key&gt;
        &lt;s:key name="label"&gt;Splunk Internal License&lt;/s:key&gt;
        &lt;s:key name="quota"&gt;10737418240&lt;/s:key&gt;
        &lt;s:key name="type"&gt;enterprise&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>


## alerts/fired_alerts
{: name='alertsfiredalerts'}

Returns a summary view of the list of all alerts that have been fired on the server.

	[GET] alerts/fired_alerts

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
| **403** | Insufficient permissions to view fired alerts. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

This example lists all alerts fired on this server that belong to the admin user.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/-/alerts/fired_alerts
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;alerts&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/alerts/fired_alerts&lt;/id&gt;
  &lt;updated&gt;2011-07-11T19:27:22-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;-&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/admin/search/alerts/fired_alerts/-&lt;/id&gt;
    &lt;updated&gt;2011-07-11T19:27:22-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/alerts/fired_alerts/-" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/admin/search/alerts/fired_alerts/-" rel="list"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="triggered_alert_count"&gt;0&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## alerts/fired_alerts/{name}
{: name='alertsfiredalertsname'}

Deletes the record of this triggered alert.

	[DELETE] alerts/fired_alerts/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deleted successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to delete the fired alert. |
|--------------------------------
| **404** | Fired alert does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Remove this particular record of the "have_events" alert being fired on this server.  Note that the name is specially crafted, and was retrieved from the GET fired_alerts/have_events response.

#### Request
<pre class='terminal'>
curl -k -u admin:pass --request DELETE \
	https://localhost:8089/servicesNS/admin/search/alerts/fired_alerts/scheduler__admin__search_aGF2ZV9ldmVudHM_at_1310437740_5d3dfde563194ffd_1310437749
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;alerts&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/alerts/fired_alerts&lt;/id&gt;
  &lt;updated&gt;2011-07-11T19:35:25-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## alerts/fired_alerts/{name}
{: name='alertsfiredalertsname'}

Returns a list of all unexpired triggered or fired instances of this alert.

	[GET] alerts/fired_alerts/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view fired alert. |
|--------------------------------
| **404** | Fired alert does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Retrieve all instances of the "have_alert" alert being fired.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/alerts/fired_alerts/have_events
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;alerts&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/alerts/fired_alerts&lt;/id&gt;
  &lt;updated&gt;2011-07-11T19:29:46-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;scheduler__admin__search_aGF2ZV9ldmVudHM_at_1310437740_5d3dfde563194ffd_1310437749&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/admin/search/alerts/fired_alerts/scheduler__admin__search_aGF2ZV9ldmVudHM_at_1310437740_5d3dfde563194ffd_1310437749&lt;/id&gt;
    &lt;updated&gt;2011-07-11T19:29:09-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/alerts/fired_alerts/scheduler__admin__search_aGF2ZV9ldmVudHM_at_1310437740_5d3dfde563194ffd_1310437749" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;published&gt;2011-07-11T19:29:09-07:00&lt;/published&gt;
    &lt;link href="/servicesNS/admin/search/alerts/fired_alerts/scheduler__admin__search_aGF2ZV9ldmVudHM_at_1310437740_5d3dfde563194ffd_1310437749" rel="list"/&gt;
    &lt;link href="/servicesNS/admin/search/alerts/fired_alerts/scheduler__admin__search_aGF2ZV9ldmVudHM_at_1310437740_5d3dfde563194ffd_1310437749" rel="remove"/&gt;
    &lt;link href="/servicesNS/admin/search/search/jobs/scheduler__admin__search_aGF2ZV9ldmVudHM_at_1310437740_5d3dfde563194ffd" rel="job"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/searches/have_events" rel="savedsearch"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="actions"/&gt;
        &lt;s:key name="alert_type"&gt;historical&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="expiration_time"&gt;1310524149&lt;/s:key&gt;
        &lt;s:key name="savedsearch_name"&gt;have_events&lt;/s:key&gt;
        &lt;s:key name="severity"&gt;3&lt;/s:key&gt;
        &lt;s:key name="sid"&gt;scheduler__admin__search_aGF2ZV9ldmVudHM_at_1310437740_5d3dfde563194ffd&lt;/s:key&gt;
        &lt;s:key name="trigger_time"&gt;1310437749&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/commands
{: name='datacommands'}

List all python search commands.

	[GET] data/commands

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
| **403** | Insufficient permissions to view commands. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

List python search commands.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/nobody/search/data/commands
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;commandsconf&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/commands&lt;/id&gt;
  &lt;updated&gt;2011-07-07T00:52:26-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/commands/_reload" rel="_reload"/&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;bucketdir&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/commands/bucketdir&lt;/id&gt;
    &lt;updated&gt;2011-07-07T00:52:26-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/search/data/commands/bucketdir" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/search/data/commands/bucketdir" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/commands/bucketdir/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/commands/bucketdir/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="changes_colorder"&gt;1&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;s:key name="eai:appName"&gt;search&lt;/s:key&gt;
        &lt;s:key name="eai:userName"&gt;admin&lt;/s:key&gt;
        &lt;s:key name="enableheader"&gt;1&lt;/s:key&gt;
        &lt;s:key name="filename"&gt;bucketdir.py&lt;/s:key&gt;
        &lt;s:key name="generates_timeorder"&gt;0&lt;/s:key&gt;
        &lt;s:key name="generating"&gt;0&lt;/s:key&gt;
        &lt;s:key name="maxinputs"&gt;50000&lt;/s:key&gt;
        &lt;s:key name="outputheader"&gt;0&lt;/s:key&gt;
        &lt;s:key name="passauth"&gt;0&lt;/s:key&gt;
        &lt;s:key name="required_fields"&gt;*&lt;/s:key&gt;
        &lt;s:key name="requires_preop"&gt;0&lt;/s:key&gt;
        &lt;s:key name="retainsevents"&gt;0&lt;/s:key&gt;
        &lt;s:key name="streaming"&gt;0&lt;/s:key&gt;
        &lt;s:key name="supports_getinfo"&gt;0&lt;/s:key&gt;
        &lt;s:key name="supports_rawargs"&gt;1&lt;/s:key&gt;
        &lt;s:key name="type"&gt;python&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/commands/{name}
{: name='datacommandsname'}

Provide information about a specific python search command.

	[GET] data/commands/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view command. |
|--------------------------------
| **404** | Command does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Provides information about the python search command, input.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/nobody/search/data/commands/input
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;commandsconf&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/commands&lt;/id&gt;
  &lt;updated&gt;2011-07-07T00:52:26-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/commands/_reload" rel="_reload"/&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;input&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/commands/input&lt;/id&gt;
    &lt;updated&gt;2011-07-07T00:52:26-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/search/data/commands/input" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/search/data/commands/input" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/commands/input/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/commands/input/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="changes_colorder"&gt;1&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
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
              &lt;s:list/&gt;
            &lt;/s:key&gt;
          &lt;/s:dict&gt;
        &lt;/s:key&gt;
        &lt;s:key name="eai:userName"&gt;admin&lt;/s:key&gt;
        &lt;s:key name="enableheader"&gt;1&lt;/s:key&gt;
        &lt;s:key name="filename"&gt;input.py&lt;/s:key&gt;
        &lt;s:key name="generates_timeorder"&gt;0&lt;/s:key&gt;
        &lt;s:key name="generating"&gt;0&lt;/s:key&gt;
        &lt;s:key name="maxinputs"&gt;50000&lt;/s:key&gt;
        &lt;s:key name="outputheader"&gt;0&lt;/s:key&gt;
        &lt;s:key name="passauth"&gt;1&lt;/s:key&gt;
        &lt;s:key name="required_fields"&gt;*&lt;/s:key&gt;
        &lt;s:key name="requires_preop"&gt;0&lt;/s:key&gt;
        &lt;s:key name="retainsevents"&gt;0&lt;/s:key&gt;
        &lt;s:key name="streaming"&gt;0&lt;/s:key&gt;
        &lt;s:key name="supports_getinfo"&gt;0&lt;/s:key&gt;
        &lt;s:key name="supports_rawargs"&gt;1&lt;/s:key&gt;
        &lt;s:key name="type"&gt;python&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## saved/searches
{: name='savedsearches'}

Returns information on all saved searches.

	[GET] saved/searches

### Parameters

count
: _Optional_ **Number** Maximum number of items to return.

earliest_time
: _Optional_ **String** For scheduled searches display all the scheduled times starting from this time (not just the next run time)

latest_time
: _Optional_ **String** For scheduled searches display all the scheduled times until this time (not just the next run time)

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
| **403** | Insufficient permissions to view saved search. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

List all saved searched on this Splunk instance.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/saved/searches
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;savedsearch&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/saved/searches&lt;/id&gt;
  &lt;updated&gt;2011-07-13T11:56:35-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/saved/searches/_new" rel="create"/&gt;
  &lt;link href="/services/saved/searches/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;Errors in the last 24 hours&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/saved/searches/Errors%20in%20the%20last%2024%20hours&lt;/id&gt;
    &lt;updated&gt;2011-07-13T11:56:35-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/search/saved/searches/Errors%20in%20the%20last%2024%20hours" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/search/saved/searches/Errors%20in%20the%20last%2024%20hours" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/search/saved/searches/Errors%20in%20the%20last%2024%20hours/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/search/saved/searches/Errors%20in%20the%20last%2024%20hours" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/search/saved/searches/Errors%20in%20the%20last%2024%20hours/disable" rel="disable"/&gt;
    &lt;link href="/servicesNS/nobody/search/saved/searches/Errors%20in%20the%20last%2024%20hours/dispatch" rel="dispatch"/&gt;
    &lt;link href="/servicesNS/nobody/search/saved/searches/Errors%20in%20the%20last%2024%20hours/history" rel="history"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="action.email"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.email.reportServerEnabled"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.email.sendresults"/&gt;
        &lt;s:key name="action.email.to"/&gt;
        &lt;s:key name="action.populate_lookup"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.rss"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.script"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.summary_index"&gt;0&lt;/s:key&gt;
        &lt;s:key name="alert.digest_mode"&gt;1&lt;/s:key&gt;
        &lt;s:key name="alert.expires"&gt;24h&lt;/s:key&gt;
        &lt;s:key name="alert.severity"&gt;3&lt;/s:key&gt;
        &lt;s:key name="alert.suppress"/&gt;
        &lt;s:key name="alert.suppress.period"/&gt;
        &lt;s:key name="alert.track"&gt;auto&lt;/s:key&gt;
        &lt;s:key name="alert_comparator"/&gt;
        &lt;s:key name="alert_condition"/&gt;
        &lt;s:key name="alert_threshold"/&gt;
        &lt;s:key name="alert_type"&gt;always&lt;/s:key&gt;
        &lt;s:key name="cron_schedule"/&gt;
        &lt;s:key name="description"/&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;s:key name="dispatch.buckets"&gt;0&lt;/s:key&gt;
        &lt;s:key name="dispatch.earliest_time"&gt;-1d&lt;/s:key&gt;
        &lt;s:key name="dispatch.latest_time"/&gt;
        &lt;s:key name="dispatch.lookups"&gt;1&lt;/s:key&gt;
        &lt;s:key name="dispatch.max_count"&gt;500000&lt;/s:key&gt;
        &lt;s:key name="dispatch.max_time"&gt;0&lt;/s:key&gt;
        &lt;s:key name="dispatch.reduce_freq"&gt;10&lt;/s:key&gt;
        &lt;s:key name="dispatch.spawn_process"&gt;1&lt;/s:key&gt;
        &lt;s:key name="dispatch.time_format"&gt;%FT%T.%Q%:z&lt;/s:key&gt;
        &lt;s:key name="dispatch.ttl"&gt;2p&lt;/s:key&gt;
        &lt;s:key name="displayview"/&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="is_scheduled"&gt;0&lt;/s:key&gt;
        &lt;s:key name="is_visible"&gt;1&lt;/s:key&gt;
        &lt;s:key name="max_concurrent"&gt;1&lt;/s:key&gt;
        &lt;s:key name="next_scheduled_time"/&gt;
        &lt;s:key name="qualifiedSearch"&gt;search  error OR failed OR severe OR ( sourcetype=access_* ( 404 OR 500 OR 503 ) )&lt;/s:key&gt;
        &lt;s:key name="realtime_schedule"&gt;1&lt;/s:key&gt;
        &lt;s:key name="request.ui_dispatch_app"/&gt;
        &lt;s:key name="request.ui_dispatch_view"/&gt;
        &lt;s:key name="restart_on_searchpeer_add"&gt;1&lt;/s:key&gt;
        &lt;s:key name="run_on_startup"&gt;0&lt;/s:key&gt;
        &lt;s:key name="search"&gt;error OR failed OR severe OR ( sourcetype=access_* ( 404 OR 500 OR 503 ) )&lt;/s:key&gt;
        &lt;s:key name="vsid"&gt;*:75qh2fwx&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## saved/searches
{: name='savedsearches'}

Creates a saved search.

	[POST] saved/searches

### Parameters

action.email
: _Optional_ **Boolean** The state of the email action. Read-only attribute. Value ignored on POST. Use actions to specify a list of enabled actions.

action.email.auth_password
: _Optional_ **String** The password to use when authenticating with the SMTP server. Normally this value will be set when editing the email settings, however you can set a clear text password here and it will be encrypted on the next Splunk restart.<br/><br/>Defaults to empty string.

action.email.auth_username
: _Optional_ **String** The username to use when authenticating with the SMTP server. If this is empty string, no authentication is attempted. Defaults to empty string.<br/><br/>NOTE: Your SMTP server might reject unauthenticated emails.

action.email.bcc
: _Optional_ **String** BCC email address to use if action.email is enabled. 

action.email.cc
: _Optional_ **String** CC email address to use if action.email is enabled.

action.email.command
: _Optional_ **String** The search command (or pipeline) which is responsible for executing the action.<br/><br/>Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$.

action.email.format
: _Optional_ **Enum** Valid values: (plain &#124; html &#124; raw &#124; csv)<br/><br/>Specify the format of text in the email. This value also applies to any attachments.

action.email.from
: _Optional_ **String** Email address from which the email action originates.<br/><br/>Defaults to splunk@$LOCALHOST or whatever value is set in alert_actions.conf.

action.email.hostname
: _Optional_ **String** Sets the hostname used in the web link (url) sent in email actions.<br/><br/>This value accepts two forms:<br/><br/>  hostname (for example, splunkserver, splunkserver.example.com)<br/><br/>  protocol://hostname:port (for example, http://splunkserver:8000, https://splunkserver.example.com:443)<br/><br/>When this value is a simple hostname, the protocol and port which are configured within splunk are used to construct the base of the url.<br/><br/>When this value begins with 'http://', it is used verbatim. NOTE: This means the correct port must be specified if it is not the default port for http or https. This is useful in cases when the Splunk server is not aware of how to construct an externally referencable url, such as SSO environments, other proxies, or when the Splunk server hostname is not generally resolvable.<br/><br/>Defaults to current hostname provided by the operating system, or if that fails "localhost". When set to empty, default behavior is used.

action.email.inline
: _Optional_ **Boolean** Indicates whether the search results are contained in the body of the email.<br/><br/>Results can be either inline or attached to an email. See action.email.sendresults.

action.email.mailserver
: _Optional_ **String** Set the address of the MTA server to be used to send the emails.<br/><br/>Defaults to <LOCALHOST> (or whatever is set in alert_actions.conf).

action.email.maxresults
: _Optional_ **Number** Sets the global maximum number of search results to send when email.action is enabled.<br/><br/>Defaults to 100.

action.email.maxtime
: _Optional_ **Number** Valid values are Integer&#91;m&#124;s&#124;h&#124;d&#93;.<br/><br/>Specifies the maximum amount of time the execution of an email action takes before the action is aborted. Defaults to 5m.

action.email.preprocess_results
: _Optional_ **String** Search string to preprocess results before emailing them. Defaults to empty string (no preprocessing).<br/><br/>Usually the preprocessing consists of filtering out unwanted internal fields.

action.email.reportPaperOrientation
: _Optional_ **Enum** Valid values: (portrait &#124; landscape)<br/><br/>Specifies the paper orientation: portrait or landscape. Defaults to portrait.

action.email.reportPaperSize
: _Optional_ **Enum** Valid values: (letter &#124; legal &#124; ledger &#124; a2 &#124; a3 &#124; a4 &#124; a5)<br/><br/>Specifies the paper size for PDFs. Defaults to letter.

action.email.reportServerEnabled
: _Optional_ **Boolean** Indicates whether the PDF server is enabled. Defaults to false.

action.email.reportServerURL
: _Optional_ **String**  The URL of the PDF report server, if one is set up and available on the network.<br/><br/>For a default locally installed report server, the URL is http://localhost:8091/

action.email.sendpdf
: _Optional_ **Boolean** Indicates whether to create and send the results as a PDF. Defaults to false.

action.email.sendresults
: _Optional_ **Boolean** Indicates whether to attach the search results in the email.<br/><br/>Results can be either attached or inline. See action.email.inline. 

action.email.subject
: _Optional_ **String** Specifies an alternate email subject.<br/><br/>Defaults to SplunkAlert-<savedsearchname>.

action.email.to
: _Optional_ **String** A comma or semicolon separated list of recipient email addresses. Required if this search is scheduled and the email alert action is enabled.

action.email.track_alert
: _Optional_ **Boolean** Indicates whether the execution of this action signifies a trackable alert.

action.email.ttl
: _Optional_ **Number** Valid values are Integer[p].<br/><br/>Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows &lt;Integer&gt;, int is the number of scheduled periods. Defaults to 86400 (24 hours).<br/><br/>If no actions are triggered, the artifacts have their ttl determined by dispatch.ttl in savedsearches.conf.

action.email.use_ssl
: _Optional_ **Boolean** Indicates whether to use SSL when communicating with the SMTP server.<br/><br/>Defaults to false.

action.email.use_tls
: _Optional_ **Boolean** Indicates whether to use TLS (transport layer security) when communicating with the SMTP server (starttls).<br/><br/>Defaults to false.

action.populate_lookup
: _Optional_ **Boolean** The state of the populate lookup action. Read-only attribute. Value ignored on POST. Use actions to specify a list of enabled actions.

action.populate_lookup.command
: _Optional_ **String** The search command (or pipeline) which is responsible for executing the action.<br/><br/>Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$.

action.populate_lookup.hostname
: _Optional_ **String** Sets the hostname used in the web link (url) sent in alert actions.<br/><br/>This value accepts two forms:<br/><br/>  hostname (for example, splunkserver, splunkserver.example.com)<br/><br/>  protocol://hostname:port (for example, http://splunkserver:8000, https://splunkserver.example.com:443)<br/><br/>See action.email.hostname for details.

action.populate_lookup.maxresults
: _Optional_ **Number** Sets the maximum number of search results sent via alerts. Defaults to 100.

action.populate_lookup.maxtime
: _Optional_ **Number** Valid values are: Integer[m&#124;s&#124;h&#124;d]<br/><br/>Sets the maximum amount of time the execution of an action takes before the action is aborted. Defaults to 5m.

action.populate_lookup.track_alert
: _Optional_ **Boolean** Indicates whether the execution of this action signifies a trackable alert.

action.populate_lookup.ttl
: _Optional_ **Number** Valid values are Integer[p]<br/><br/>Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, then this specifies the number of scheduled periods. Defaults to 10p.<br/><br/>If no actions are triggered, the artifacts have their ttl determined by dispatch.ttl in savedsearches.conf.

action.rss
: _Optional_ **Boolean** The state of the rss action. Read-only attribute. Value ignored on POST. Use actions to specify a list of enabled actions.

action.rss.command
: _Optional_ **String** The search command (or pipeline) which is responsible for executing the action.<br/><br/>Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$.

action.rss.hostname
: _Optional_ **String** Sets the hostname used in the web link (url) sent in alert actions.<br/><br/>This value accepts two forms:<br/><br/>  hostname (for example, splunkserver, splunkserver.example.com)<br/><br/>  protocol://hostname:port (for example, http://splunkserver:8000, https://splunkserver.example.com:443)<br/><br/>See action.email.hostname for details.

action.rss.maxresults
: _Optional_ **Number** Sets the maximum number of search results sent via alerts. Defaults to 100.

action.rss.maxtime
: _Optional_ **Number** Valid values are Integer[m&#124;s&#124;h&#124;d].<br/><br/>Sets the maximum amount of time the execution of an action takes before the action is aborted. Defaults to 1m.

action.rss.track_alert
: _Optional_ **Boolean** Indicates whether the execution of this action signifies a trackable alert.

action.rss.ttl
: _Optional_ **Number** Valid values are: Integer[p]<br/><br/>Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, specifies the number of scheduled periods. Defaults to 86400 (24 hours).<br/><br/>If no actions are triggered, the artifacts have their ttl determined by dispatch.ttl in savedsearches.conf.

action.script
: _Optional_ **Boolean** The state of the script action. Read-only attribute. Value ignored on POST. Use actions to specify a list of enabled actions.

action.script.command
: _Optional_ **String** The search command (or pipeline) which is responsible for executing the action.<br/><br/>Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$.

action.script.hostname
: _Optional_ **String** Sets the hostname used in the web link (url) sent in alert actions.<br/><br/>This value accepts two forms:<br/><br/>  hostname (for example, splunkserver, splunkserver.example.com)<br/><br/>  protocol://hostname:port (for example, http://splunkserver:8000, https://splunkserver.example.com:443)<br/><br/>See action.email.hostname for details.

action.script.maxresults
: _Optional_ **Number** Sets the maximum number of search results sent via alerts. Defaults to 100.

action.script.maxtime
: _Optional_ **Number** Valid values are: Integer[m&#124;s&#124;h&#124;d]<br/><br/>Sets the maximum amount of time the execution of an action takes before the action is aborted. Defaults to 5m.

action.script.track_alert
: _Optional_ **Boolean** Indicates whether the execution of this action signifies a trackable alert.

action.script.ttl
: _Optional_ **Number** Valid values are: Integer[p]<br/><br/>Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, specifies the number of scheduled periods. Defaults to 600 (10 minutes).<br/><br/>If no actions are triggered, the artifacts have their ttl determined by dispatch.ttl in savedsearches.conf.

action.summary_index
: _Optional_ **Boolean** The state of the summary index action. Read-only attribute. Value ignored on POST. Use actions to specify a list of enabled actions.<br/><br/>Defaults to 0

action.summary_index._name
: _Optional_ **String** Specifies the name of the summary index where the results of the scheduled search are saved.<br/><br/>Defaults to "summary."

action.summary_index.command
: _Optional_ **String** The search command (or pipeline) which is responsible for executing the action.<br/><br/>Generally the command is a template search pipeline which is realized with values from the saved search. To reference saved search field values wrap them in $, for example to reference the savedsearch name use $name$, to reference the search use $search$.

action.summary_index.hostname
: _Optional_ **String** Sets the hostname used in the web link (url) sent in alert actions.<br/><br/>This value accepts two forms:<br/><br/>  hostname (for example, splunkserver, splunkserver.example.com)<br/><br/>  protocol://hostname:port (for example, http://splunkserver:8000, https://splunkserver.example.com:443)<br/><br/>See action.email.hostname for details.

action.summary_index.inline
: _Optional_ **Boolean** Determines whether to execute the summary indexing action as part of the scheduled search. <br/><br/><b>NOTE:</b> This option is considered only if the summary index action is enabled and is always executed (in other words, if <code>counttype = always</code>).<br/><br/>Defaults to true

action.summary_index.maxresults
: _Optional_ **Number** Sets the maximum number of search results sent via alerts. Defaults to 100.

action.summary_index.maxtime
: _Optional_ **Number** Valid values are: Integer[m&#124;s&#124;h&#124;d]<br/><br/>Sets the maximum amount of time the execution of an action takes before the action is aborted. Defaults to 5m.

action.summary_index.track_alert
: _Optional_ **Boolean** Indicates whether the execution of this action signifies a trackable alert.

action.summary_index.ttl
: _Optional_ **Number** Valid values are: Integer[p]<br/><br/>Specifies the minimum time-to-live in seconds of the search artifacts if this action is triggered. If p follows Integer, specifies the number of scheduled periods. Defaults to 10p.<br/><br/>If no actions are triggered, the artifacts have their ttl determined by dispatch.ttl in savedsearches.conf.

actions
: _Optional_ **String** List of enabled actions

alert.digest_mode
: _Optional_ **Boolean** Specifies whether Splunk applies the alert actions to the entire result set or on each individual result.<br/><br/>Defaults to true.


alert.expires
: _Optional_ **Number** Valid values: [number][time-unit]<br/><br/>Sets the period of time to show the alert in the dashboard. Defaults to 24h.<br/><br/>Use [number][time-unit] to specify a time. For example: 60 = 60 seconds, 1m = 1 minute, 1h = 60 minutes = 1 hour.

alert.severity
: _Optional_ **Enum** Valid values: (1 &#124; 2 &#124; 3 &#124; 4 &#124; 5 &#124; 6)<br/><br/>Sets the alert severity level.<br/><br/>Valid values are:<br/><br/>  1 DEBUG
  2 INFO
  3 WARN
  4 ERROR
  5 SEVERE
  6 FATAL

alert.suppress
: _Optional_ **Boolean** Indicates whether alert suppression is enabled for this schedules search.

alert.suppress.period
: _Optional_ **Number** Valid values: [number][time-unit]<br/><br/>Specifies the suppresion period. Only valid if <code>alert.supress</code> is enabled.<br/><br/>Use [number][time-unit] to specify a time. For example: 60 = 60 seconds, 1m = 1 minute, 1h = 60 minutes = 1 hour.

alert.track
: _Optional_ **Enum** Valid values: (true &#124; false &#124; auto)<br/><br/>Specifies whether to track the actions triggered by this scheduled search.<br/><br/>auto  - determine whether to track or not based on the tracking setting of each action, do not track scheduled searches that always trigger actions.<br/><br/>true  - force alert tracking.<br/><br/>false - disable alert tracking for this search.


alert_comparator
: _Optional_ **String** One of the following strings: greater than, less than, equal to, rises by, drops by, rises by perc, drops by perc

alert_condition
: _Optional_ **String** Contains a conditional search that is evaluated against the results of the saved search. Defaults to an empty string.<br/><br/>Alerts are triggered if the specified search yields a non-empty search result list.<br/><br/>NOTE: If you specify an alert_condition, do not set counttype, relation, or quantity.


alert_threshold
: _Optional_ **Number** The value to compare to before triggering the alert actions. Valid values are: Integer[%]?

alert_type
: _Optional_ **String** What to base the alert on, overriden by alert_condition if it is specified. Valid values are: always, custom, number of events, number of hosts, number of sources 

cron_schedule
: _Optional_ **String** Valid values: cron string<br/><br/>The cron schedule to execute this search. For example: */5 * * * *  causes the search to execute every 5 minutes.<br/><br/>cron lets you use standard cron notation to define your scheduled search interval. In particular, cron can accept this type of notation: 00,20,40 * * * *, which runs the search every hour at hh:00, hh:20, hh:40. Along the same lines, a cron of 03,23,43 * * * * runs the search every hour at hh:03, hh:23, hh:43.<br/><br/>Splunk recommends that you schedule your searches so that they are staggered over time. This  reduces system load. Running all of them every 20 minutes (*/20) means they would all launch at hh:00 (20, 40) and might slow your system every 20 minutes.

description
: _Optional_ **String** Human-readable description of this saved search. Defaults to empty string.

disabled
: _Optional_ **Boolean** Indicates if the saved search is enabled.<br/><br/>Disabled saved searches are not visible in Splunk Web.

dispatch.buckets
: _Optional_ **Number** The maximum nuber of timeline buckets.

dispatch.earliest_time
: _Optional_ **String** A time string that specifies the earliest time for this search. Can be a relative or absolute time.<br/><br/>If this value is an absolute time, use the dispatch.time_format to format the value.

dispatch.latest_time
: _Optional_ **String** A time string that specifies the latest time for this saved search. Can be a relative or absolute time.<br/><br/>If this value is an absolute time, use the dispatch.time_format to format the value.

dispatch.lookups
: _Optional_ **Boolean** Enables or disables the lookups for this search.

dispatch.max_count
: _Optional_ **Number** The maximum number of results before finalizing the search.

dispatch.max_time
: _Optional_ **Number** Indicates the maximum amount of time (in seconds) before finalizing the search.

dispatch.reduce_freq
: _Optional_ **Number** Specifies how frequently Splunk should run the MapReduce reduce phase on accumulated map values.

dispatch.rt_backfill
: _Optional_ **Boolean** Whether to back fill the real time window for this search. Parameter valid only if this is a real time search

dispatch.spawn_process
: _Optional_ **Boolean** Specifies whether Splunk spawns a new search process when this saved search is executed.

dispatch.time_format
: _Optional_ **String** A time format string that defines the time format that Splunk uses to specify the earliest and latest time.

dispatch.ttl
: _Optional_ **Number** Valid values: Integer[p]<<br/><br/>Indicates the time to live (in seconds) for the artifacts of the scheduled search, if no  actions are triggered.<br/><br/>If an action is triggered Splunk changes the ttl to that action's ttl. If multiple actions are triggered, Splunk applies the maximum ttl to the artifacts. To set the action's ttl, refer to alert_actions.conf.spec.<br/><br/>If the integer is followed by the letter 'p' Splunk interprets the ttl as a multiple of the scheduled search's period.

displayview
: _Optional_ **String** Defines the default UI view name (not label) in which to load the results. Accessibility is subject to the user having sufficient permissions.

is_scheduled
: _Optional_ **Boolean** Whether this search is to be ran on a schedule

is_visible
: _Optional_ **Boolean** Specifies whether this saved search should be listed in the visible saved search list.

max_concurrent
: _Optional_ **Number** The maximum number of concurrent instances of this search the scheduler is allowed to run.

next_scheduled_time
: _Optional_ **String** Read-only attribute. Value ignored on POST. There are some old clients who still send this value

qualifiedSearch
: _Optional_ **String** Read-only attribute. Value ignored on POST. Splunk computes this value during runtime.

realtime_schedule
: _Optional_ **Boolean** Controls the way the scheduler computes the next execution time of a scheduled search. If this value is set to 1, the scheduler bases its determination of the next scheduled search execution time on the current time.<br/><br/>If this value is set to 0, the scheduler bases its determination of the next scheduled search on the last search execution time. This is called continuous scheduling. If set to 0, the scheduler never skips scheduled execution periods. However, the execution of the saved search might fall behind depending on the scheduler's load. Use continuous scheduling whenever you enable the summary index option.<br/><br/>If set to 1, the scheduler might skip some execution periods to make sure that the scheduler is executing the searches running over the most recent time range.<br/><br/>The scheduler tries to execute searches that have realtime_schedule set to 1 before it executes searches that have continuous scheduling (realtime_schedule = 0).

request.ui_dispatch_app
: _Optional_ **String** Specifies a field used by Splunk UI to denote the app this search should be dispatched in.

request.ui_dispatch_view
: _Optional_ **String** Specifies a field used by Splunk UI to denote the view this search should be displayed in.

restart_on_searchpeer_add
: _Optional_ **Boolean** Specifies whether to restart a real-time search managed by the scheduler when a search peer becomes available for this saved search.<br/><br/>NOTE: The peer can be a newly added peer or a peer that has been down and has become available.

run_on_startup
: _Optional_ **Boolean** Indicates whether this search runs when Splunk starts. If it does not run on startup, it runs at the next scheduled time.<br/><br/>Splunk recommends that you set run_on_startup to true for scheduled searches that populate lookup tables.

search
: _Required_ **String** The search to save.

vsid
: _Optional_ **String** Defines the viewstate id associated with the UI view listed in 'displayview'.<br/><br/>Must match up to a stanza in viewstates.conf.

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
| **403** | Insufficient permissions to create saved search. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Creates a search, MySavedSearch.
URI-encode the search string if it contains any of the following characters: =, &, ?, %
Otherwise, these characters can be interpreted as part of the HTTP request.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/servicesNS/admin/search/saved/searches --data-urlencode name=MySavedSearch \
	-d search="index=_internal source=*metrics.log"
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;savedsearch&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/saved/searches&lt;/id&gt;
  &lt;updated&gt;2011-07-09T22:35:08-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/saved/searches/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/admin/search/saved/searches/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;MySavedSearch&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/admin/search/saved/searches/MySavedSearch&lt;/id&gt;
    &lt;updated&gt;2011-07-09T22:35:08-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/saved/searches/MySavedSearch" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/admin/search/saved/searches/MySavedSearch" rel="list"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/searches/MySavedSearch/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/searches/MySavedSearch" rel="edit"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/searches/MySavedSearch" rel="remove"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/searches/MySavedSearch/move" rel="move"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/searches/MySavedSearch/disable" rel="disable"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/searches/MySavedSearch/dispatch" rel="dispatch"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/searches/MySavedSearch/history" rel="history"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="action.email"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.email.auth_password"/&gt;
        &lt;s:key name="action.email.auth_username"/&gt;
        &lt;s:key name="action.email.bcc"/&gt;
        &lt;s:key name="action.email.cc"/&gt;
        &lt;s:key name="action.email.command"&gt;
&lt;![CDATA[$action.email.preprocess_results{default=""}$ | sendemail "server=$action.email.mailserver{default=localhost}$" "use_ssl=$action.email.use_ssl{default=false}$" "use_tls=$action.email.use_tls{default=false}$" "to=$action.email.to$" "cc=$action.email.cc$" "bcc=$action.email.bcc$" "from=$action.email.from{default=splunk@localhost}$" "subject=$action.email.subject{recurse=yes}$" "format=$action.email.format{default=csv}$" "sssummary=Saved Search [$name$]: $counttype$($results.count$)" "sslink=$results.url$" "ssquery=$search$" "ssname=$name$" "inline=$action.email.inline{default=False}$" "sendresults=$action.email.sendresults{default=False}$" "sendpdf=$action.email.sendpdf{default=False}$" "pdfview=$action.email.pdfview$" "searchid=$search_id$" "graceful=$graceful{default=True}$" maxinputs="$action.email.maxresults{default=10000}$" maxtime="$action.email.maxtime{default=5m}$"]]&gt;        &lt;/s:key&gt;
        &lt;s:key name="action.email.format"&gt;html&lt;/s:key&gt;
        &lt;s:key name="action.email.from"&gt;splunk&lt;/s:key&gt;
        &lt;s:key name="action.email.hostname"/&gt;
        &lt;s:key name="action.email.inline"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.email.mailserver"&gt;localhost&lt;/s:key&gt;
        &lt;s:key name="action.email.maxresults"&gt;10000&lt;/s:key&gt;
        &lt;s:key name="action.email.maxtime"&gt;5m&lt;/s:key&gt;
        &lt;s:key name="action.email.preprocess_results"/&gt;
        &lt;s:key name="action.email.reportPaperOrientation"&gt;portrait&lt;/s:key&gt;
        &lt;s:key name="action.email.reportPaperSize"&gt;letter&lt;/s:key&gt;
        &lt;s:key name="action.email.reportServerEnabled"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.email.reportServerURL"/&gt;
        &lt;s:key name="action.email.sendpdf"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.email.sendresults"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.email.subject"&gt;Splunk Alert: $name$&lt;/s:key&gt;
        &lt;s:key name="action.email.to"/&gt;
        &lt;s:key name="action.email.track_alert"&gt;1&lt;/s:key&gt;
        &lt;s:key name="action.email.ttl"&gt;86400&lt;/s:key&gt;
        &lt;s:key name="action.email.use_ssl"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.email.use_tls"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.populate_lookup"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.populate_lookup.command"&gt;copyresults dest=&amp;quot;$action.populate_lookup.dest$&amp;quot;  sid=&amp;quot;$search_id$&amp;quot;&lt;/s:key&gt;
        &lt;s:key name="action.populate_lookup.hostname"/&gt;
        &lt;s:key name="action.populate_lookup.maxresults"&gt;10000&lt;/s:key&gt;
        &lt;s:key name="action.populate_lookup.maxtime"&gt;5m&lt;/s:key&gt;
        &lt;s:key name="action.populate_lookup.track_alert"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.populate_lookup.ttl"&gt;120&lt;/s:key&gt;
        &lt;s:key name="action.rss"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.rss.command"&gt;createrss &amp;quot;path=$name$.xml&amp;quot; &amp;quot;name=$name$&amp;quot; &amp;quot;link=$results.url$&amp;quot; &amp;quot;descr=Alert trigger: $name$, results.count=$results.count$ &amp;quot; &amp;quot;count=30&amp;quot; &amp;quot;graceful=$graceful{default=1}$&amp;quot; maxtime=&amp;quot;$action.rss.maxtime{default=1m}$&amp;quot;&lt;/s:key&gt;
        &lt;s:key name="action.rss.hostname"/&gt;
        &lt;s:key name="action.rss.maxresults"&gt;10000&lt;/s:key&gt;
        &lt;s:key name="action.rss.maxtime"&gt;1m&lt;/s:key&gt;
        &lt;s:key name="action.rss.track_alert"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.rss.ttl"&gt;86400&lt;/s:key&gt;
        &lt;s:key name="action.script"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.script.command"&gt;runshellscript &amp;quot;$action.script.filename$&amp;quot; &amp;quot;$results.count$&amp;quot; &amp;quot;$search$&amp;quot; &amp;quot;$search$&amp;quot; &amp;quot;$name$&amp;quot; &amp;quot;Saved Search [$name$] $counttype$($results.count$)&amp;quot; &amp;quot;$results.url$&amp;quot; &amp;quot;$deprecated_arg$&amp;quot; &amp;quot;$search_id$&amp;quot; maxtime=&amp;quot;$action.script.maxtime{default=5m}$&amp;quot;&lt;/s:key&gt;
        &lt;s:key name="action.script.hostname"/&gt;
        &lt;s:key name="action.script.maxresults"&gt;10000&lt;/s:key&gt;
        &lt;s:key name="action.script.maxtime"&gt;5m&lt;/s:key&gt;
        &lt;s:key name="action.script.track_alert"&gt;1&lt;/s:key&gt;
        &lt;s:key name="action.script.ttl"&gt;600&lt;/s:key&gt;
        &lt;s:key name="action.summary_index"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.summary_index._name"&gt;summary&lt;/s:key&gt;
        &lt;s:key name="action.summary_index.command"&gt;
&lt;![CDATA[summaryindex spool=t uselb=t addtime=t index="$action.summary_index._name{required=yes}$" file="$name$_$#random$.stash_new" name="$name$" marker="$action.summary_index*{format=$KEY=\\\"$VAL\\\", key_regex="action.summary_index.(?!(?:command|inline|maxresults|maxtime|ttl|track_alert|(?:_.*))$)(.*)"}$"]]&gt;        &lt;/s:key&gt;
        &lt;s:key name="action.summary_index.hostname"/&gt;
        &lt;s:key name="action.summary_index.inline"&gt;1&lt;/s:key&gt;
        &lt;s:key name="action.summary_index.maxresults"&gt;10000&lt;/s:key&gt;
        &lt;s:key name="action.summary_index.maxtime"&gt;5m&lt;/s:key&gt;
        &lt;s:key name="action.summary_index.track_alert"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.summary_index.ttl"&gt;120&lt;/s:key&gt;
        &lt;s:key name="alert.digest_mode"&gt;1&lt;/s:key&gt;
        &lt;s:key name="alert.expires"&gt;24h&lt;/s:key&gt;
        &lt;s:key name="alert.severity"&gt;3&lt;/s:key&gt;
        &lt;s:key name="alert.suppress"/&gt;
        &lt;s:key name="alert.suppress.period"/&gt;
        &lt;s:key name="alert.track"&gt;auto&lt;/s:key&gt;
        &lt;s:key name="alert_comparator"/&gt;
        &lt;s:key name="alert_condition"/&gt;
        &lt;s:key name="alert_threshold"/&gt;
        &lt;s:key name="alert_type"&gt;always&lt;/s:key&gt;
        &lt;s:key name="cron_schedule"/&gt;
        &lt;s:key name="description"/&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;s:key name="dispatch.buckets"&gt;0&lt;/s:key&gt;
        &lt;s:key name="dispatch.earliest_time"/&gt;
        &lt;s:key name="dispatch.latest_time"/&gt;
        &lt;s:key name="dispatch.lookups"&gt;1&lt;/s:key&gt;
        &lt;s:key name="dispatch.max_count"&gt;500000&lt;/s:key&gt;
        &lt;s:key name="dispatch.max_time"&gt;0&lt;/s:key&gt;
        &lt;s:key name="dispatch.reduce_freq"&gt;10&lt;/s:key&gt;
        &lt;s:key name="dispatch.spawn_process"&gt;1&lt;/s:key&gt;
        &lt;s:key name="dispatch.time_format"&gt;%FT%T.%Q%:z&lt;/s:key&gt;
        &lt;s:key name="dispatch.ttl"&gt;2p&lt;/s:key&gt;
        &lt;s:key name="displayview"/&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="is_scheduled"&gt;0&lt;/s:key&gt;
        &lt;s:key name="is_visible"&gt;1&lt;/s:key&gt;
        &lt;s:key name="max_concurrent"&gt;1&lt;/s:key&gt;
        &lt;s:key name="next_scheduled_time"/&gt;
        &lt;s:key name="qualifiedSearch"&gt;search  index&lt;/s:key&gt;
        &lt;s:key name="realtime_schedule"&gt;1&lt;/s:key&gt;
        &lt;s:key name="request.ui_dispatch_app"/&gt;
        &lt;s:key name="request.ui_dispatch_view"/&gt;
        &lt;s:key name="restart_on_searchpeer_add"&gt;1&lt;/s:key&gt;
        &lt;s:key name="run_on_startup"&gt;0&lt;/s:key&gt;
        &lt;s:key name="search"&gt;index&lt;/s:key&gt;
        &lt;s:key name="vsid"/&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## saved/searches/{name}
{: name='savedsearchesname'}

Deletes this saved search.

	[DELETE] saved/searches/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deleted successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to delete saved search. |
|--------------------------------
| **404** | Saved search does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Deletes the saved search, MySavedSearch.

#### Request
<pre class='terminal'>
curl -k -u admin:pass --request DELETE \
	https://localhost:8089/servicesNS/admin/search/saved/searches/MySavedSearch
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;savedsearch&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/saved/searches&lt;/id&gt;
  &lt;updated&gt;2011-07-13T12:09:05-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/saved/searches/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/admin/search/saved/searches/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## saved/searches/{name}
{: name='savedsearchesname'}

Returns information on this saved search.

	[GET] saved/searches/{name}

### Parameters

earliest_time
: _Optional_ **String** If the search is scheduled display scheduled times starting from this time

latest_time
: _Optional_ **String** If the search is scheduled display scheduled times ending at this time

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view saved search. |
|--------------------------------
| **404** | Saved search does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Return details of the saved search, MySavedSearch, which was created in the example for the POST operation for saved/searches.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/saved/searches/MySavedSearch
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;savedsearch&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/saved/searches&lt;/id&gt;
  &lt;updated&gt;2011-07-13T11:57:54-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/saved/searches/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/admin/search/saved/searches/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;MySavedSearch&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/admin/search/saved/searches/MySavedSearch&lt;/id&gt;
    &lt;updated&gt;2011-07-13T11:57:54-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/saved/searches/MySavedSearch" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/admin/search/saved/searches/MySavedSearch" rel="list"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/searches/MySavedSearch/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/searches/MySavedSearch" rel="edit"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/searches/MySavedSearch" rel="remove"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/searches/MySavedSearch/move" rel="move"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/searches/MySavedSearch/disable" rel="disable"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/searches/MySavedSearch/dispatch" rel="dispatch"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/searches/MySavedSearch/history" rel="history"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="action.email"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.email.auth_password"/&gt;
        &lt;s:key name="action.email.auth_username"/&gt;
        &lt;s:key name="action.email.bcc"/&gt;
        &lt;s:key name="action.email.cc"/&gt;
        &lt;s:key name="action.email.command"&gt;
      &lt;![CDATA[$action.email.preprocess_results{default=""}$
      "use_tls=$action.email.use_tls{default=false}$" "to=$action.email.to$" "cc=$action.email.cc$"
      "bcc=$action.email.bcc$" "from=$action.email.from{default=splunk@localhost}$" "subject=$action.email.subject{recurse=yes}$"
      "format=$action.email.format{default=csv}$" "sssummary=Saved Search [$name$]: $counttype$($results.count$)"
      "sslink=$results.url$" "ssquery=$search$" "ssname=$name$" "inline=$action.email.inline{default=False}$"
      "sendresults=$action.email.sendresults{default=False}$" "sendpdf=$action.email.sendpdf{default=False}$"
      "pdfview=$action.email.pdfview$" "searchid=$search_id$" "graceful=$graceful{default=True}$"
      maxinputs="$action.email.maxresults{default=10000}$" maxtime="$action.email.maxtime{default=5m}$"]]&gt;
        &lt;/s:key&gt;
        &lt;s:key name="action.email.format"&gt;html&lt;/s:key&gt;
        &lt;s:key name="action.email.from"&gt;splunk&lt;/s:key&gt;
        &lt;s:key name="action.email.hostname"/&gt;
        &lt;s:key name="action.email.inline"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.email.mailserver"&gt;localhost&lt;/s:key&gt;
        &lt;s:key name="action.email.maxresults"&gt;10000&lt;/s:key&gt;
        &lt;s:key name="action.email.maxtime"&gt;5m&lt;/s:key&gt;
        &lt;s:key name="action.email.preprocess_results"/&gt;
        &lt;s:key name="action.email.reportPaperOrientation"&gt;portrait&lt;/s:key&gt;
        &lt;s:key name="action.email.reportPaperSize"&gt;letter&lt;/s:key&gt;
        &lt;s:key name="action.email.reportServerEnabled"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.email.reportServerURL"/&gt;
        &lt;s:key name="action.email.sendpdf"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.email.sendresults"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.email.subject"&gt;Splunk Alert: $name$&lt;/s:key&gt;
        &lt;s:key name="action.email.to"/&gt;
        &lt;s:key name="action.email.track_alert"&gt;1&lt;/s:key&gt;
        &lt;s:key name="action.email.ttl"&gt;86400&lt;/s:key&gt;
        &lt;s:key name="action.email.use_ssl"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.email.use_tls"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.populate_lookup"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.populate_lookup.command"&gt;
          copyresults dest=&amp;quot;$action.populate_lookup.dest$&amp;quot;  sid=&amp;quot;$search_id$&amp;quot;
        &lt;/s:key&gt;
        &lt;s:key name="action.populate_lookup.hostname"/&gt;
        &lt;s:key name="action.populate_lookup.maxresults"&gt;10000&lt;/s:key&gt;
        &lt;s:key name="action.populate_lookup.maxtime"&gt;5m&lt;/s:key&gt;
        &lt;s:key name="action.populate_lookup.track_alert"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.populate_lookup.ttl"&gt;120&lt;/s:key&gt;
        &lt;s:key name="action.rss"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.rss.command"&gt;
          createrss &amp;quot;path=$name$.xml&amp;quot; &amp;quot;name=$name$&amp;quot; &amp;quot;link=$results.url$&amp;quot;
          &amp;quot;descr=Alert trigger: $name$, results.count=$results.count$ &amp;quot; &amp;quot;count=30&amp;quot;
          &amp;quot;graceful=$graceful{default=1}$&amp;quot; maxtime=&amp;quot;$action.rss.maxtime{default=1m}$&amp;quot;
        &lt;/s:key&gt;
        &lt;s:key name="action.rss.hostname"/&gt;
        &lt;s:key name="action.rss.maxresults"&gt;10000&lt;/s:key&gt;
        &lt;s:key name="action.rss.maxtime"&gt;1m&lt;/s:key&gt;
        &lt;s:key name="action.rss.track_alert"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.rss.ttl"&gt;86400&lt;/s:key&gt;
        &lt;s:key name="action.script"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.script.command"&gt;runshellscript &amp;quot;$action.script.filename$&amp;quot;
          &amp;quot;$results.count$&amp;quot; &amp;quot;$search$&amp;quot; &amp;quot;$search$&amp;quot; &amp;quot;$name$&amp;quot;
          &amp;quot;Saved Search [$name$] $counttype$($results.count$)&amp;quot; &amp;quot;$results.url$&amp;quot;
          &amp;quot;$deprecated_arg$&amp;quot; &amp;quot;$search_id$&amp;quot;
          maxtime=&amp;quot;$action.script.maxtime{default=5m}$&amp;quot;
        &lt;/s:key&gt;
        &lt;s:key name="action.script.hostname"/&gt;
        &lt;s:key name="action.script.maxresults"&gt;10000&lt;/s:key&gt;
        &lt;s:key name="action.script.maxtime"&gt;5m&lt;/s:key&gt;
        &lt;s:key name="action.script.track_alert"&gt;1&lt;/s:key&gt;
        &lt;s:key name="action.script.ttl"&gt;600&lt;/s:key&gt;
        &lt;s:key name="action.summary_index"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.summary_index._name"&gt;summary&lt;/s:key&gt;
        &lt;s:key name="action.summary_index.command"&gt;
          &lt;![CDATA[summaryindex spool=t uselb=t addtime=t index="$action.summary_index._name{required=yes}$"
          file="$name$_$#random$.stash_new" name="$name$"
          marker="$action.summary_index*{format=$KEY=\\\"$VAL\\\",
            key_regex="action.summary_index.(?!(?:command|inline|maxresults|maxtime|ttl|track_alert|(?:_.*))$)(.*)"}$"]]&gt;
        &lt;/s:key&gt;
        &lt;s:key name="action.summary_index.hostname"/&gt;
        &lt;s:key name="action.summary_index.inline"&gt;1&lt;/s:key&gt;
        &lt;s:key name="action.summary_index.maxresults"&gt;10000&lt;/s:key&gt;
        &lt;s:key name="action.summary_index.maxtime"&gt;5m&lt;/s:key&gt;
        &lt;s:key name="action.summary_index.track_alert"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.summary_index.ttl"&gt;120&lt;/s:key&gt;
        &lt;s:key name="alert.digest_mode"&gt;1&lt;/s:key&gt;
        &lt;s:key name="alert.expires"&gt;24h&lt;/s:key&gt;
        &lt;s:key name="alert.severity"&gt;3&lt;/s:key&gt;
        &lt;s:key name="alert.suppress"/&gt;
        &lt;s:key name="alert.suppress.period"/&gt;
        &lt;s:key name="alert.track"&gt;auto&lt;/s:key&gt;
        &lt;s:key name="alert_comparator"/&gt;
        &lt;s:key name="alert_condition"/&gt;
        &lt;s:key name="alert_threshold"/&gt;
        &lt;s:key name="alert_type"&gt;always&lt;/s:key&gt;
        &lt;s:key name="cron_schedule"/&gt;
        &lt;s:key name="description"/&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;s:key name="dispatch.buckets"&gt;0&lt;/s:key&gt;
        &lt;s:key name="dispatch.earliest_time"/&gt;
        &lt;s:key name="dispatch.latest_time"/&gt;
        &lt;s:key name="dispatch.lookups"&gt;1&lt;/s:key&gt;
        &lt;s:key name="dispatch.max_count"&gt;500000&lt;/s:key&gt;
        &lt;s:key name="dispatch.max_time"&gt;0&lt;/s:key&gt;
        &lt;s:key name="dispatch.reduce_freq"&gt;10&lt;/s:key&gt;
        &lt;s:key name="dispatch.spawn_process"&gt;1&lt;/s:key&gt;
        &lt;s:key name="dispatch.time_format"&gt;%FT%T.%Q%:z&lt;/s:key&gt;
        &lt;s:key name="dispatch.ttl"&gt;2p&lt;/s:key&gt;
        &lt;s:key name="displayview"/&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:attributes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="optionalFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;action.email&lt;/s:item&gt;
                &lt;s:item&gt;action.email.auth_password&lt;/s:item&gt;
                &lt;s:item&gt;action.email.auth_username&lt;/s:item&gt;
                &lt;s:item&gt;action.email.bcc&lt;/s:item&gt;
                &lt;s:item&gt;action.email.cc&lt;/s:item&gt;
                &lt;s:item&gt;action.email.command&lt;/s:item&gt;
                &lt;s:item&gt;action.email.format&lt;/s:item&gt;
                &lt;s:item&gt;action.email.from&lt;/s:item&gt;
                &lt;s:item&gt;action.email.hostname&lt;/s:item&gt;
                &lt;s:item&gt;action.email.inline&lt;/s:item&gt;
                &lt;s:item&gt;action.email.mailserver&lt;/s:item&gt;
                &lt;s:item&gt;action.email.maxresults&lt;/s:item&gt;
                &lt;s:item&gt;action.email.maxtime&lt;/s:item&gt;
                &lt;s:item&gt;action.email.preprocess_results&lt;/s:item&gt;
                &lt;s:item&gt;action.email.reportPaperOrientation&lt;/s:item&gt;
                &lt;s:item&gt;action.email.reportPaperSize&lt;/s:item&gt;
                &lt;s:item&gt;action.email.reportServerEnabled&lt;/s:item&gt;
                &lt;s:item&gt;action.email.reportServerURL&lt;/s:item&gt;
                &lt;s:item&gt;action.email.sendpdf&lt;/s:item&gt;
                &lt;s:item&gt;action.email.sendresults&lt;/s:item&gt;
                &lt;s:item&gt;action.email.subject&lt;/s:item&gt;
                &lt;s:item&gt;action.email.to&lt;/s:item&gt;
                &lt;s:item&gt;action.email.track_alert&lt;/s:item&gt;
                &lt;s:item&gt;action.email.ttl&lt;/s:item&gt;
                &lt;s:item&gt;action.email.use_ssl&lt;/s:item&gt;
                &lt;s:item&gt;action.email.use_tls&lt;/s:item&gt;
                &lt;s:item&gt;action.populate_lookup&lt;/s:item&gt;
                &lt;s:item&gt;action.populate_lookup.command&lt;/s:item&gt;
                &lt;s:item&gt;action.populate_lookup.hostname&lt;/s:item&gt;
                &lt;s:item&gt;action.populate_lookup.maxresults&lt;/s:item&gt;
                &lt;s:item&gt;action.populate_lookup.maxtime&lt;/s:item&gt;
                &lt;s:item&gt;action.populate_lookup.track_alert&lt;/s:item&gt;
                &lt;s:item&gt;action.populate_lookup.ttl&lt;/s:item&gt;
                &lt;s:item&gt;action.rss&lt;/s:item&gt;
                &lt;s:item&gt;action.rss.command&lt;/s:item&gt;
                &lt;s:item&gt;action.rss.hostname&lt;/s:item&gt;
                &lt;s:item&gt;action.rss.maxresults&lt;/s:item&gt;
                &lt;s:item&gt;action.rss.maxtime&lt;/s:item&gt;
                &lt;s:item&gt;action.rss.track_alert&lt;/s:item&gt;
                &lt;s:item&gt;action.rss.ttl&lt;/s:item&gt;
                &lt;s:item&gt;action.script&lt;/s:item&gt;
                &lt;s:item&gt;action.script.command&lt;/s:item&gt;
                &lt;s:item&gt;action.script.hostname&lt;/s:item&gt;
                &lt;s:item&gt;action.script.maxresults&lt;/s:item&gt;
                &lt;s:item&gt;action.script.maxtime&lt;/s:item&gt;
                &lt;s:item&gt;action.script.track_alert&lt;/s:item&gt;
                &lt;s:item&gt;action.script.ttl&lt;/s:item&gt;
                &lt;s:item&gt;action.summary_index&lt;/s:item&gt;
                &lt;s:item&gt;action.summary_index._name&lt;/s:item&gt;
                &lt;s:item&gt;action.summary_index.command&lt;/s:item&gt;
                &lt;s:item&gt;action.summary_index.hostname&lt;/s:item&gt;
                &lt;s:item&gt;action.summary_index.inline&lt;/s:item&gt;
                &lt;s:item&gt;action.summary_index.maxresults&lt;/s:item&gt;
                &lt;s:item&gt;action.summary_index.maxtime&lt;/s:item&gt;
                &lt;s:item&gt;action.summary_index.track_alert&lt;/s:item&gt;
                &lt;s:item&gt;action.summary_index.ttl&lt;/s:item&gt;
                &lt;s:item&gt;actions&lt;/s:item&gt;
                &lt;s:item&gt;alert.digest_mode&lt;/s:item&gt;
                &lt;s:item&gt;alert.expires&lt;/s:item&gt;
                &lt;s:item&gt;alert.severity&lt;/s:item&gt;
                &lt;s:item&gt;alert.suppress&lt;/s:item&gt;
                &lt;s:item&gt;alert.suppress.period&lt;/s:item&gt;
                &lt;s:item&gt;alert.track&lt;/s:item&gt;
                &lt;s:item&gt;alert_comparator&lt;/s:item&gt;
                &lt;s:item&gt;alert_condition&lt;/s:item&gt;
                &lt;s:item&gt;alert_threshold&lt;/s:item&gt;
                &lt;s:item&gt;alert_type&lt;/s:item&gt;
                &lt;s:item&gt;cron_schedule&lt;/s:item&gt;
                &lt;s:item&gt;description&lt;/s:item&gt;
                &lt;s:item&gt;disabled&lt;/s:item&gt;
                &lt;s:item&gt;dispatch.buckets&lt;/s:item&gt;
                &lt;s:item&gt;dispatch.earliest_time&lt;/s:item&gt;
                &lt;s:item&gt;dispatch.latest_time&lt;/s:item&gt;
                &lt;s:item&gt;dispatch.lookups&lt;/s:item&gt;
                &lt;s:item&gt;dispatch.max_count&lt;/s:item&gt;
                &lt;s:item&gt;dispatch.max_time&lt;/s:item&gt;
                &lt;s:item&gt;dispatch.reduce_freq&lt;/s:item&gt;
                &lt;s:item&gt;dispatch.spawn_process&lt;/s:item&gt;
                &lt;s:item&gt;dispatch.time_format&lt;/s:item&gt;
                &lt;s:item&gt;dispatch.ttl&lt;/s:item&gt;
                &lt;s:item&gt;displayview&lt;/s:item&gt;
                &lt;s:item&gt;is_scheduled&lt;/s:item&gt;
                &lt;s:item&gt;is_visible&lt;/s:item&gt;
                &lt;s:item&gt;max_concurrent&lt;/s:item&gt;
                &lt;s:item&gt;next_scheduled_time&lt;/s:item&gt;
                &lt;s:item&gt;qualifiedSearch&lt;/s:item&gt;
                &lt;s:item&gt;realtime_schedule&lt;/s:item&gt;
                &lt;s:item&gt;request.ui_dispatch_app&lt;/s:item&gt;
                &lt;s:item&gt;request.ui_dispatch_view&lt;/s:item&gt;
                &lt;s:item&gt;restart_on_searchpeer_add&lt;/s:item&gt;
                &lt;s:item&gt;run_on_startup&lt;/s:item&gt;
                &lt;s:item&gt;vsid&lt;/s:item&gt;
              &lt;/s:list&gt;
            &lt;/s:key&gt;
            &lt;s:key name="requiredFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;search&lt;/s:item&gt;
              &lt;/s:list&gt;
            &lt;/s:key&gt;
            &lt;s:key name="wildcardFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;action\..*&lt;/s:item&gt;
                &lt;s:item&gt;args\..*&lt;/s:item&gt;
                &lt;s:item&gt;dispatch\..*&lt;/s:item&gt;
              &lt;/s:list&gt;
            &lt;/s:key&gt;
          &lt;/s:dict&gt;
        &lt;/s:key&gt;
        &lt;s:key name="is_scheduled"&gt;0&lt;/s:key&gt;
        &lt;s:key name="is_visible"&gt;1&lt;/s:key&gt;
        &lt;s:key name="max_concurrent"&gt;1&lt;/s:key&gt;
        &lt;s:key name="next_scheduled_time"/&gt;
        &lt;s:key name="qualifiedSearch"&gt;search  index&lt;/s:key&gt;
        &lt;s:key name="realtime_schedule"&gt;1&lt;/s:key&gt;
        &lt;s:key name="request.ui_dispatch_app"/&gt;
        &lt;s:key name="request.ui_dispatch_view"/&gt;
        &lt;s:key name="restart_on_searchpeer_add"&gt;1&lt;/s:key&gt;
        &lt;s:key name="run_on_startup"&gt;0&lt;/s:key&gt;
        &lt;s:key name="search"&gt;index&lt;/s:key&gt;
        &lt;s:key name="vsid"/&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## saved/searches/{name}
{: name='savedsearchesname'}

Updates this saved search.

	[POST] saved/searches/{name}

### Parameters

action.email
: _Optional_ **INHERITED** INHERITED

action.email.auth_password
: _Optional_ **INHERITED** INHERITED

action.email.auth_username
: _Optional_ **INHERITED** INHERITED

action.email.bcc
: _Optional_ **INHERITED** INHERITED

action.email.cc
: _Optional_ **INHERITED** INHERITED

action.email.command
: _Optional_ **INHERITED** INHERITED

action.email.format
: _Optional_ **INHERITED** INHERITED

action.email.from
: _Optional_ **INHERITED** INHERITED

action.email.hostname
: _Optional_ **INHERITED** INHERITED

action.email.inline
: _Optional_ **INHERITED** INHERITED

action.email.mailserver
: _Optional_ **INHERITED** INHERITED

action.email.maxresults
: _Optional_ **INHERITED** INHERITED

action.email.maxtime
: _Optional_ **INHERITED** INHERITED

action.email.preprocess_results
: _Optional_ **INHERITED** INHERITED

action.email.reportPaperOrientation
: _Optional_ **INHERITED** INHERITED

action.email.reportPaperSize
: _Optional_ **INHERITED** INHERITED

action.email.reportServerEnabled
: _Optional_ **INHERITED** INHERITED

action.email.reportServerURL
: _Optional_ **INHERITED** INHERITED

action.email.sendpdf
: _Optional_ **INHERITED** INHERITED

action.email.sendresults
: _Optional_ **INHERITED** INHERITED

action.email.subject
: _Optional_ **INHERITED** INHERITED

action.email.to
: _Optional_ **INHERITED** INHERITED

action.email.track_alert
: _Optional_ **INHERITED** INHERITED

action.email.ttl
: _Optional_ **INHERITED** INHERITED

action.email.use_ssl
: _Optional_ **INHERITED** INHERITED

action.email.use_tls
: _Optional_ **INHERITED** INHERITED

action.populate_lookup
: _Optional_ **INHERITED** INHERITED

action.populate_lookup.command
: _Optional_ **INHERITED** INHERITED

action.populate_lookup.hostname
: _Optional_ **INHERITED** INHERITED

action.populate_lookup.maxresults
: _Optional_ **INHERITED** INHERITED

action.populate_lookup.maxtime
: _Optional_ **INHERITED** INHERITED

action.populate_lookup.track_alert
: _Optional_ **INHERITED** INHERITED

action.populate_lookup.ttl
: _Optional_ **INHERITED** INHERITED

action.rss
: _Optional_ **INHERITED** INHERITED

action.rss.command
: _Optional_ **INHERITED** INHERITED

action.rss.hostname
: _Optional_ **INHERITED** INHERITED

action.rss.maxresults
: _Optional_ **INHERITED** INHERITED

action.rss.maxtime
: _Optional_ **INHERITED** INHERITED

action.rss.track_alert
: _Optional_ **INHERITED** INHERITED

action.rss.ttl
: _Optional_ **INHERITED** INHERITED

action.script
: _Optional_ **INHERITED** INHERITED

action.script.command
: _Optional_ **INHERITED** INHERITED

action.script.hostname
: _Optional_ **INHERITED** INHERITED

action.script.maxresults
: _Optional_ **INHERITED** INHERITED

action.script.maxtime
: _Optional_ **INHERITED** INHERITED

action.script.track_alert
: _Optional_ **INHERITED** INHERITED

action.script.ttl
: _Optional_ **INHERITED** INHERITED

action.summary_index
: _Optional_ **INHERITED** INHERITED

action.summary_index._name
: _Optional_ **INHERITED** INHERITED

action.summary_index.command
: _Optional_ **INHERITED** INHERITED

action.summary_index.hostname
: _Optional_ **INHERITED** INHERITED

action.summary_index.inline
: _Optional_ **INHERITED** INHERITED

action.summary_index.maxresults
: _Optional_ **INHERITED** INHERITED

action.summary_index.maxtime
: _Optional_ **INHERITED** INHERITED

action.summary_index.track_alert
: _Optional_ **INHERITED** INHERITED

action.summary_index.ttl
: _Optional_ **INHERITED** INHERITED

actions
: _Optional_ **INHERITED** INHERITED

alert.digest_mode
: _Optional_ **INHERITED** INHERITED

alert.expires
: _Optional_ **INHERITED** INHERITED

alert.severity
: _Optional_ **INHERITED** INHERITED

alert.suppress
: _Optional_ **INHERITED** INHERITED

alert.suppress.period
: _Optional_ **INHERITED** INHERITED

alert.track
: _Optional_ **INHERITED** INHERITED

alert_comparator
: _Optional_ **INHERITED** INHERITED

alert_condition
: _Optional_ **INHERITED** INHERITED

alert_threshold
: _Optional_ **INHERITED** INHERITED

alert_type
: _Optional_ **INHERITED** INHERITED

cron_schedule
: _Optional_ **INHERITED** INHERITED

description
: _Optional_ **INHERITED** INHERITED

disabled
: _Optional_ **INHERITED** INHERITED

dispatch.buckets
: _Optional_ **INHERITED** INHERITED

dispatch.earliest_time
: _Optional_ **INHERITED** INHERITED

dispatch.latest_time
: _Optional_ **INHERITED** INHERITED

dispatch.lookups
: _Optional_ **INHERITED** INHERITED

dispatch.max_count
: _Optional_ **INHERITED** INHERITED

dispatch.max_time
: _Optional_ **INHERITED** INHERITED

dispatch.reduce_freq
: _Optional_ **INHERITED** INHERITED

dispatch.rt_backfill
: _Optional_ **INHERITED** INHERITED

dispatch.spawn_process
: _Optional_ **INHERITED** INHERITED

dispatch.time_format
: _Optional_ **INHERITED** INHERITED

dispatch.ttl
: _Optional_ **INHERITED** INHERITED

displayview
: _Optional_ **INHERITED** INHERITED

is_scheduled
: _Optional_ **INHERITED** INHERITED

is_visible
: _Optional_ **INHERITED** INHERITED

max_concurrent
: _Optional_ **INHERITED** INHERITED

next_scheduled_time
: _Optional_ **INHERITED** INHERITED

qualifiedSearch
: _Optional_ **INHERITED** INHERITED

realtime_schedule
: _Optional_ **INHERITED** INHERITED

request.ui_dispatch_app
: _Optional_ **INHERITED** INHERITED

request.ui_dispatch_view
: _Optional_ **INHERITED** INHERITED

restart_on_searchpeer_add
: _Optional_ **INHERITED** INHERITED

run_on_startup
: _Optional_ **INHERITED** INHERITED

search
: _Required_ **INHERITED** INHERITED

vsid
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
| **403** | Insufficient permissions to edit saved search. |
|--------------------------------
| **404** | Saved search does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Update MySavedSearch to enable email action and provide email addresses for the action. (The example for the POST operation for saved/searches creates MySavedSearch.)
URI-encode the search string if it contains any of the following characters: =, &, ?, %
Otherwise, these characters can be interpreted as part of the HTTP request.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/saved/searches/MySavedSearch \
	-d actions=email \
	-d action.email.to="nobody@example.com, info@example.com" \
	-d search="my search here"
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:s="http://dev.splunk.com/ns/rest"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;savedsearch&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/saved/searches&lt;/id&gt;
  &lt;updated&gt;2011-07-26T18:20:14-04:00&lt;/updated&gt;
  &lt;generator version="104601"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/saved/searches/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/admin/search/saved/searches/_reload" rel="_reload"/&gt;
  &lt;opensearch:totalResults&gt;1&lt;/opensearch:totalResults&gt;
  &lt;opensearch:itemsPerPage&gt;30&lt;/opensearch:itemsPerPage&gt;
  &lt;opensearch:startIndex&gt;0&lt;/opensearch:startIndex&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;MySavedSearch&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/admin/search/saved/searches/MySavedSearch&lt;/id&gt;
    &lt;updated&gt;2011-07-26T18:20:14-04:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/saved/searches/MySavedSearch" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/admin/search/saved/searches/MySavedSearch" rel="list"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/searches/MySavedSearch/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/searches/MySavedSearch" rel="edit"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/searches/MySavedSearch" rel="remove"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/searches/MySavedSearch/move" rel="move"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/searches/MySavedSearch/disable" rel="disable"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/searches/MySavedSearch/dispatch" rel="dispatch"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/searches/MySavedSearch/history" rel="history"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="action.email"&gt;1&lt;/s:key&gt;
        &lt;s:key name="action.email.auth_password"&gt;&lt;/s:key&gt;
        &lt;s:key name="action.email.auth_username"&gt;&lt;/s:key&gt;
        &lt;s:key name="action.email.bcc"&gt;&lt;/s:key&gt;
        &lt;s:key name="action.email.cc"&gt;&lt;/s:key&gt;
        &lt;s:key name="action.email.command"&gt;
          &lt;![CDATA[$action.email.preprocess_results{default=""}$ |
                    sendemail "server=$action.email.mailserver{default=localhost}$" "use_ssl=$action.email.use_ssl{default=false}$"
                    "use_tls=$action.email.use_tls{default=false}$" "to=$action.email.to$" "cc=$action.email.cc$"
                    "bcc=$action.email.bcc$" "from=$action.email.from{default=splunk@localhost}$"
                    "subject=$action.email.subject{recurse=yes}$" "format=$action.email.format{default=csv}$"
                    "sssummary=Saved Search [$name$]: $counttype$($results.count$)" "sslink=$results.url$"
                    "ssquery=$search$" "ssname=$name$" "inline=$action.email.inline{default=False}$"
                    "sendresults=$action.email.sendresults{default=False}$" "sendpdf=$action.email.sendpdf{default=False}$"
                    "pdfview=$action.email.pdfview$" "searchid=$search_id$"
                    "graceful=$graceful{default=True}$" maxinputs="$action.email.maxresults{default=10000}$"
                    maxtime="$action.email.maxtime{default=5m}$"]]&gt;
        &lt;/s:key&gt;
        &lt;s:key name="action.email.format"&gt;html&lt;/s:key&gt;
        &lt;s:key name="action.email.from"&gt;splunk&lt;/s:key&gt;
        &lt;s:key name="action.email.hostname"&gt;&lt;/s:key&gt;
        &lt;s:key name="action.email.inline"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.email.mailserver"&gt;localhost&lt;/s:key&gt;
        &lt;s:key name="action.email.maxresults"&gt;10000&lt;/s:key&gt;
        &lt;s:key name="action.email.maxtime"&gt;5m&lt;/s:key&gt;
        &lt;s:key name="action.email.preprocess_results"&gt;&lt;/s:key&gt;
        &lt;s:key name="action.email.reportPaperOrientation"&gt;portrait&lt;/s:key&gt;
        &lt;s:key name="action.email.reportPaperSize"&gt;letter&lt;/s:key&gt;
        &lt;s:key name="action.email.reportServerEnabled"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.email.reportServerURL"&gt;&lt;/s:key&gt;
        &lt;s:key name="action.email.sendpdf"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.email.sendresults"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.email.subject"&gt;Splunk Alert: $name$&lt;/s:key&gt;
        &lt;s:key name="action.email.to"&gt;nobody@example.com,info@example.com&lt;/s:key&gt;
        &lt;s:key name="action.email.track_alert"&gt;1&lt;/s:key&gt;
        &lt;s:key name="action.email.ttl"&gt;86400&lt;/s:key&gt;
        &lt;s:key name="action.email.use_ssl"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.email.use_tls"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.populate_lookup"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.populate_lookup.command"&gt;copyresults dest="$action.populate_lookup.dest$"  sid="$search_id$"&lt;/s:key&gt;
        &lt;s:key name="action.populate_lookup.hostname"&gt;&lt;/s:key&gt;
        &lt;s:key name="action.populate_lookup.maxresults"&gt;10000&lt;/s:key&gt;
        &lt;s:key name="action.populate_lookup.maxtime"&gt;5m&lt;/s:key&gt;
        &lt;s:key name="action.populate_lookup.track_alert"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.populate_lookup.ttl"&gt;120&lt;/s:key&gt;
        &lt;s:key name="action.rss"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.rss.command"&gt;createrss "path=$name$.xml" "name=$name$" "link=$results.url$" "descr=Alert trigger: $name$, results.count=$results.count$ " "count=30" "graceful=$graceful{default=1}$" maxtime="$action.rss.maxtime{default=1m}$"&lt;/s:key&gt;
        &lt;s:key name="action.rss.hostname"&gt;&lt;/s:key&gt;
        &lt;s:key name="action.rss.maxresults"&gt;10000&lt;/s:key&gt;
        &lt;s:key name="action.rss.maxtime"&gt;1m&lt;/s:key&gt;
        &lt;s:key name="action.rss.track_alert"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.rss.ttl"&gt;86400&lt;/s:key&gt;
        &lt;s:key name="action.script"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.script.command"&gt;runshellscript "$action.script.filename$" "$results.count$" "$search$" "$search$" "$name$" "Saved Search [$name$] $counttype$($results.count$)" "$results.url$" "$deprecated_arg$" "$search_id$" "$results.file$" maxtime="$action.script.maxtime{default=5m}$"&lt;/s:key&gt;
        &lt;s:key name="action.script.hostname"&gt;&lt;/s:key&gt;
        &lt;s:key name="action.script.maxresults"&gt;10000&lt;/s:key&gt;
        &lt;s:key name="action.script.maxtime"&gt;5m&lt;/s:key&gt;
        &lt;s:key name="action.script.track_alert"&gt;1&lt;/s:key&gt;
        &lt;s:key name="action.script.ttl"&gt;600&lt;/s:key&gt;
        &lt;s:key name="action.summary_index"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.summary_index._name"&gt;summary&lt;/s:key&gt;
        &lt;s:key name="action.summary_index.command"&gt;&lt;![CDATA[summaryindex spool=t uselb=t addtime=t index="$action.summary_index._name{required=yes}$" file="$name$_$#random$.stash_new" name="$name$" marker="$action.summary_index*{format=$KEY=\\\"$VAL\\\", key_regex="action.summary_index.(?!(?:command|inline|maxresults|maxtime|ttl|track_alert|(?:_.*))$)(.*)"}$"]]&gt;&lt;/s:key&gt;
        &lt;s:key name="action.summary_index.hostname"&gt;&lt;/s:key&gt;
        &lt;s:key name="action.summary_index.inline"&gt;1&lt;/s:key&gt;
        &lt;s:key name="action.summary_index.maxresults"&gt;10000&lt;/s:key&gt;
        &lt;s:key name="action.summary_index.maxtime"&gt;5m&lt;/s:key&gt;
        &lt;s:key name="action.summary_index.track_alert"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.summary_index.ttl"&gt;120&lt;/s:key&gt;
        &lt;s:key name="actions"&gt;email&lt;/s:key&gt;
        &lt;s:key name="alert.digest_mode"&gt;1&lt;/s:key&gt;
        &lt;s:key name="alert.expires"&gt;24h&lt;/s:key&gt;
        &lt;s:key name="alert.severity"&gt;3&lt;/s:key&gt;
        &lt;s:key name="alert.suppress"&gt;&lt;/s:key&gt;
        &lt;s:key name="alert.suppress.period"&gt;&lt;/s:key&gt;
        &lt;s:key name="alert.track"&gt;auto&lt;/s:key&gt;
        &lt;s:key name="alert_comparator"&gt;&lt;/s:key&gt;
        &lt;s:key name="alert_condition"&gt;&lt;/s:key&gt;
        &lt;s:key name="alert_threshold"&gt;&lt;/s:key&gt;
        &lt;s:key name="alert_type"&gt;always&lt;/s:key&gt;
        &lt;s:key name="cron_schedule"&gt;&lt;/s:key&gt;
        &lt;s:key name="description"&gt;&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;s:key name="dispatch.buckets"&gt;0&lt;/s:key&gt;
        &lt;s:key name="dispatch.earliest_time"&gt;&lt;/s:key&gt;
        &lt;s:key name="dispatch.latest_time"&gt;&lt;/s:key&gt;
        &lt;s:key name="dispatch.lookups"&gt;1&lt;/s:key&gt;
        &lt;s:key name="dispatch.max_count"&gt;500000&lt;/s:key&gt;
        &lt;s:key name="dispatch.max_time"&gt;0&lt;/s:key&gt;
        &lt;s:key name="dispatch.reduce_freq"&gt;10&lt;/s:key&gt;
        &lt;s:key name="dispatch.rt_backfill"&gt;0&lt;/s:key&gt;
        &lt;s:key name="dispatch.spawn_process"&gt;1&lt;/s:key&gt;
        &lt;s:key name="dispatch.time_format"&gt;%FT%T.%Q%:z&lt;/s:key&gt;
        &lt;s:key name="dispatch.ttl"&gt;2p&lt;/s:key&gt;
        &lt;s:key name="displayview"&gt;&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="is_scheduled"&gt;0&lt;/s:key&gt;
        &lt;s:key name="is_visible"&gt;1&lt;/s:key&gt;
        &lt;s:key name="max_concurrent"&gt;1&lt;/s:key&gt;
        &lt;s:key name="next_scheduled_time"&gt;&lt;/s:key&gt;
        &lt;s:key name="qualifiedSearch"&gt;search  my seach here&lt;/s:key&gt;
        &lt;s:key name="realtime_schedule"&gt;1&lt;/s:key&gt;
        &lt;s:key name="request.ui_dispatch_app"&gt;&lt;/s:key&gt;
        &lt;s:key name="request.ui_dispatch_view"&gt;&lt;/s:key&gt;
        &lt;s:key name="restart_on_searchpeer_add"&gt;1&lt;/s:key&gt;
        &lt;s:key name="run_on_startup"&gt;0&lt;/s:key&gt;
        &lt;s:key name="search"&gt;my search here&lt;/s:key&gt;
        &lt;s:key name="vsid"&gt;&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## saved/searches/{name}/acknowledge
{: name='savedsearchesnameacknowledge'}

Acknowledge the suppression of the alerts from this saved search and resume alerting. Action available only with POST

	[POST] saved/searches/{name}/acknowledge

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Suppression was acknowledged successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **402** | The Splunk license in use has disabled this feature. |
|--------------------------------
| **403** | Insufficient permissions to acknowledge the suppression. |
|--------------------------------
| **404** | Named save search does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Acknowledge the suppression of an alert and resume alerting

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/servicesNS/admin/search/saved/searches/MyAlert/acknowledge -X POST
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom" xmlns:s="http://dev.splunk.com/ns/rest" xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;savedsearch&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/saved/searches&lt;/id&gt;
  &lt;updated&gt;2011-07-26T18:31:07-04:00&lt;/updated&gt;
  &lt;generator version="104601"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/saved/searches/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/admin/search/saved/searches/_reload" rel="_reload"/&gt;
  &lt;opensearch:totalResults&gt;0&lt;/opensearch:totalResults&gt;
  &lt;opensearch:itemsPerPage&gt;30&lt;/opensearch:itemsPerPage&gt;
  &lt;opensearch:startIndex&gt;0&lt;/opensearch:startIndex&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## saved/searches/{name}/dispatch
{: name='savedsearchesnamedispatch'}

Dispatch the saved search just like the scheduler would. Action available only through POST. The following optional arguments are accepted:
dispatch.now:    [time] dispatch the search as if it this was the current time 
dispatch.*:      any dispatch.* field of the search can be overriden
now:             [time] deprecated, same as dispatch.now use that instead
trigger_actions: [bool] whether to trigger alert actions 
force_dispatch:  [bool] should a new search be started even if another instance of this search is already running

	[POST] saved/searches/{name}/dispatch

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Dispatched the saved search successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **402** | The Splunk license in use has disabled this feature. |
|--------------------------------
| **403** | Insufficient permissions to dispatch the saved search. |
|--------------------------------
| **404** | Named save search does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Dispatch the saved search and trigger alert actions.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/servicesNS/admin/search/saved/searches/MySavedSearch/dispatch \
	-d trigger_actions=1
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;?xml version='1.0' encoding='UTF-8'?&gt;
&lt;response&gt;&lt;sid&gt;admin__admin__search__MySavedSearch_at_1311797437_d831d980832e3e89&lt;/sid&gt;&lt;/response&gt;
</code></pre>

## saved/searches/{name}/history
{: name='savedsearchesnamehistory'}

Get a list of available search jobs created from this saved search

	[GET] saved/searches/{name}/history

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Retrieved the dispatch history successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to retrieve dispatch history for this saved search. |
|--------------------------------
| **404** | Named save search does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Retrive the dispatch history of a scheduled search.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/servicesNS/admin/search/saved/searches/MySavedSearch/history
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:s="http://dev.splunk.com/ns/rest"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;MySavedSearch&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/saved/searches&lt;/id&gt;
  &lt;updated&gt;2011-07-26T18:13:20-04:00&lt;/updated&gt;
  &lt;generator version="104601"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/saved/searches/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/admin/search/saved/searches/_reload" rel="_reload"/&gt;
  &lt;opensearch:totalResults&gt;2&lt;/opensearch:totalResults&gt;
  &lt;opensearch:itemsPerPage&gt;30&lt;/opensearch:itemsPerPage&gt;
  &lt;opensearch:startIndex&gt;0&lt;/opensearch:startIndex&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;scheduler__admin__search_MySavedSearch_at_1311718380_4270ba99c46128d2&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/search/jobs/scheduler__admin__search_MySavedSearch_at_1311718380_4270ba99c46128d2&lt;/id&gt;
    &lt;updated&gt;2011-07-26T18:13:18-04:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/search/search/jobs/scheduler__admin__search_MySavedSearch_at_1311718380_4270ba99c46128d2" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;published&gt;2011-07-26T18:13:01-04:00&lt;/published&gt;
    &lt;link href="/servicesNS/nobody/search/search/jobs/scheduler__admin__search_MySavedSearch_at_1311718380_4270ba99c46128d2" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/search/search/jobs/scheduler__admin__search_MySavedSearch_at_1311718380_4270ba99c46128d2/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/search/search/jobs/scheduler__admin__search_MySavedSearch_at_1311718380_4270ba99c46128d2" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/search/search/jobs/scheduler__admin__search_MySavedSearch_at_1311718380_4270ba99c46128d2" rel="remove"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="isDone"&gt;1&lt;/s:key&gt;
        &lt;s:key name="isFinalized"&gt;0&lt;/s:key&gt;
        &lt;s:key name="isRealTimeSearch"&gt;0&lt;/s:key&gt;
        &lt;s:key name="isSaved"&gt;0&lt;/s:key&gt;
        &lt;s:key name="isScheduled"&gt;1&lt;/s:key&gt;
        &lt;s:key name="isZombie"&gt;0&lt;/s:key&gt;
        &lt;s:key name="ttl"&gt;86382&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
  &lt;entry&gt;
    &lt;title&gt;scheduler__admin__search_MySavedSearch_at_1311717060_7d9aa142eba2437b&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/search/jobs/scheduler__admin__search_MySavedSearch_at_1311717060_7d9aa142eba2437b&lt;/id&gt;
    &lt;updated&gt;2011-07-26T17:51:23-04:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/search/search/jobs/scheduler__admin__search_MySavedSearch_at_1311717060_7d9aa142eba2437b" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;published&gt;2011-07-26T17:51:01-04:00&lt;/published&gt;
    &lt;link href="/servicesNS/nobody/search/search/jobs/scheduler__admin__search_MySavedSearch_at_1311717060_7d9aa142eba2437b" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/search/search/jobs/scheduler__admin__search_MySavedSearch_at_1311717060_7d9aa142eba2437b/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/search/search/jobs/scheduler__admin__search_MySavedSearch_at_1311717060_7d9aa142eba2437b" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/search/search/jobs/scheduler__admin__search_MySavedSearch_at_1311717060_7d9aa142eba2437b" rel="remove"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="isDone"&gt;1&lt;/s:key&gt;
        &lt;s:key name="isFinalized"&gt;0&lt;/s:key&gt;
        &lt;s:key name="isRealTimeSearch"&gt;0&lt;/s:key&gt;
        &lt;s:key name="isSaved"&gt;0&lt;/s:key&gt;
        &lt;s:key name="isScheduled"&gt;1&lt;/s:key&gt;
        &lt;s:key name="isZombie"&gt;0&lt;/s:key&gt;
        &lt;s:key name="ttl"&gt;85062&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## saved/searches/{name}/suppress
{: name='savedsearchesnamesuppress'}

Check the suppression state of alerts from this saved search.

	[GET] saved/searches/{name}/suppress

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Retrieved/updated the suppression state successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to retrieve/update the suppression state. |
|--------------------------------
| **404** | Named save search does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Retrieve or update the suppression state for the given alert, MySavedSeach

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/servicesNS/admin/search/saved/searches/MySavedSearch/suppress
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom" xmlns:s="http://dev.splunk.com/ns/rest" xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;savedsearch&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/saved/searches&lt;/id&gt;
  &lt;updated&gt;2011-07-26T18:22:51-04:00&lt;/updated&gt;
  &lt;generator version="104601"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/saved/searches/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/admin/search/saved/searches/_reload" rel="_reload"/&gt;
  &lt;opensearch:totalResults&gt;1&lt;/opensearch:totalResults&gt;
  &lt;opensearch:itemsPerPage&gt;30&lt;/opensearch:itemsPerPage&gt;
  &lt;opensearch:startIndex&gt;0&lt;/opensearch:startIndex&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;MySavedSearch&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/admin/search/saved/searches/MySavedSearch&lt;/id&gt;
    &lt;updated&gt;2011-07-26T18:22:51-04:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/saved/searches/MySavedSearch" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/admin/search/saved/searches/MySavedSearch" rel="list"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/searches/MySavedSearch/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/searches/MySavedSearch" rel="edit"/&gt;
    &lt;link href="/servicesNS/admin/search/saved/searches/MySavedSearch" rel="remove"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="expiration"&gt;13811&lt;/s:key&gt;
        &lt;s:key name="suppressed"&gt;1&lt;/s:key&gt;
        &lt;s:key name="suppressionKey"&gt;admin;search;MySavedSearch;;&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## scheduled/views
{: name='scheduledviews'}

Lists all scheduled view objects

	[GET] scheduled/views

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
| **403** | Insufficient permissions to view scheduled view. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

List all scheduled views

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/scheduled/views
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom" xmlns:s="http://dev.splunk.com/ns/rest" xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;scheduledviews&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/admin/scheduledviews&lt;/id&gt;
  &lt;updated&gt;2011-07-27T16:27:55-04:00&lt;/updated&gt;
  &lt;generator version="104601"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/admin/scheduledviews/_reload" rel="_reload"/&gt;
  &lt;opensearch:totalResults&gt;1&lt;/opensearch:totalResults&gt;
  &lt;opensearch:itemsPerPage&gt;30&lt;/opensearch:itemsPerPage&gt;
  &lt;opensearch:startIndex&gt;0&lt;/opensearch:startIndex&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;_ScheduledView__MyView&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/admin/search/admin/scheduledviews/_ScheduledView__MyView&lt;/id&gt;
    &lt;updated&gt;2011-07-27T16:27:55-04:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/admin/scheduledviews/_ScheduledView__MyView" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/admin/search/admin/scheduledviews/_ScheduledView__MyView" rel="list"/&gt;
    &lt;link href="/servicesNS/admin/search/admin/scheduledviews/_ScheduledView__MyView/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/admin/search/admin/scheduledviews/_ScheduledView__MyView" rel="edit"/&gt;
    &lt;link href="/servicesNS/admin/search/admin/scheduledviews/_ScheduledView__MyView" rel="remove"/&gt;
    &lt;link href="/servicesNS/admin/search/admin/scheduledviews/_ScheduledView__MyView/move" rel="move"/&gt;
    &lt;link href="/servicesNS/admin/search/admin/scheduledviews/_ScheduledView__MyView/disable" rel="disable"/&gt;
    &lt;link href="/servicesNS/admin/search/admin/scheduledviews/_ScheduledView__MyView/dispatch" rel="dispatch"/&gt;
    &lt;link href="/servicesNS/admin/search/admin/scheduledviews/_ScheduledView__MyView/history" rel="history"/&gt;
    &lt;link href="/servicesNS/admin/search/admin/scheduledviews/_ScheduledView__MyView/notify" rel="notify"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="action.email"&gt;1&lt;/s:key&gt;
        &lt;s:key name="action.email.pdfview"&gt;MyView&lt;/s:key&gt;
        &lt;s:key name="action.email.sendpdf"&gt;1&lt;/s:key&gt;
        &lt;s:key name="action.email.sendresults"&gt;&lt;/s:key&gt;
        &lt;s:key name="action.email.to"&gt;email@example.com&lt;/s:key&gt;
        &lt;s:key name="action.email.ttl"&gt;10&lt;/s:key&gt;
        &lt;s:key name="cron_schedule"&gt;* * * * *&lt;/s:key&gt;
        &lt;s:key name="description"&gt;scheduled search for view name=MyView&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="is_scheduled"&gt;1&lt;/s:key&gt;
        &lt;s:key name="next_scheduled_time"&gt;2011-07-27 16:28:00 EDT&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## scheduled/views/{name}
{: name='scheduledviewsname'}

Delete a scheduled view

	[DELETE] scheduled/views/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deleted successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to delete scheduled view. |
|--------------------------------
| **404** | Scheduled view does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Delete MyView scheduled view

#### Request
<pre class='terminal'>
curl -k -u admin:pass --request DELETE \
	https://localhost:8089/servicesNS/admin/search/scheduled/views/MyView
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;?xml-stylesheet type="text/xml" href="/static/atom.xsl"?&gt;
&lt;feed xmlns="http://www.w3.org/2005/Atom" xmlns:s="http://dev.splunk.com/ns/rest" xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;scheduledviews&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/admin/scheduledviews&lt;/id&gt;
  &lt;updated&gt;2011-07-27T16:16:02-04:00&lt;/updated&gt;
  &lt;generator version="104601"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/admin/scheduledviews/_reload" rel="_reload"/&gt;
  &lt;opensearch:totalResults&gt;0&lt;/opensearch:totalResults&gt;
  &lt;opensearch:itemsPerPage&gt;30&lt;/opensearch:itemsPerPage&gt;
  &lt;opensearch:startIndex&gt;0&lt;/opensearch:startIndex&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## scheduled/views/{name}
{: name='scheduledviewsname'}

List one scheduled view object

	[GET] scheduled/views/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view scheduled view. |
|--------------------------------
| **404** | Scheduled view does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

View the details of the MyView scheduled view

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/scheduled/views/MyView
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:s="http://dev.splunk.com/ns/rest"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;scheduledviews&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/scheduled/views&lt;/id&gt;
  &lt;updated&gt;2011-07-27T17:12:11-04:00&lt;/updated&gt;
  &lt;generator version="104601"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/scheduled/views/_reload" rel="_reload"/&gt;
  &lt;opensearch:totalResults&gt;1&lt;/opensearch:totalResults&gt;
  &lt;opensearch:itemsPerPage&gt;30&lt;/opensearch:itemsPerPage&gt;
  &lt;opensearch:startIndex&gt;0&lt;/opensearch:startIndex&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;_ScheduledView__MyView&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/admin/search/scheduled/views/_ScheduledView__MyView&lt;/id&gt;
    &lt;updated&gt;2011-07-27T17:12:11-04:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/scheduled/views/_ScheduledView__MyView" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/admin/search/scheduled/views/_ScheduledView__MyView" rel="list"/&gt;
    &lt;link href="/servicesNS/admin/search/scheduled/views/_ScheduledView__MyView/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/admin/search/scheduled/views/_ScheduledView__MyView" rel="edit"/&gt;
    &lt;link href="/servicesNS/admin/search/scheduled/views/_ScheduledView__MyView" rel="remove"/&gt;
    &lt;link href="/servicesNS/admin/search/scheduled/views/_ScheduledView__MyView/move" rel="move"/&gt;
    &lt;link href="/servicesNS/admin/search/scheduled/views/_ScheduledView__MyView/disable" rel="disable"/&gt;
    &lt;link href="/servicesNS/admin/search/scheduled/views/_ScheduledView__MyView/dispatch" rel="dispatch"/&gt;
    &lt;link href="/servicesNS/admin/search/scheduled/views/_ScheduledView__MyView/history" rel="history"/&gt;
    &lt;link href="/servicesNS/admin/search/scheduled/views/_ScheduledView__MyView/notify" rel="notify"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="action.email"&gt;1&lt;/s:key&gt;
        &lt;s:key name="action.email.auth_password"&gt;&lt;/s:key&gt;
        &lt;s:key name="action.email.auth_username"&gt;&lt;/s:key&gt;
        &lt;s:key name="action.email.bcc"&gt;&lt;/s:key&gt;
        &lt;s:key name="action.email.cc"&gt;&lt;/s:key&gt;
        &lt;s:key name="action.email.command"&gt;
          &lt;![CDATA[$action.email.preprocess_results{default=""}$ |
                   sendemail "server=$action.email.mailserver{default=localhost}$" "use_ssl=$action.email.use_ssl{default=false}$"
                   "use_tls=$action.email.use_tls{default=false}$" "to=$action.email.to$" "cc=$action.email.cc$"
                   "bcc=$action.email.bcc$" "from=$action.email.from{default=splunk@localhost}$"
                   "subject=$action.email.subject{recurse=yes}$" "format=$action.email.format{default=csv}$"
                   "sssummary=Saved Search [$name$]: $counttype$($results.count$)" "sslink=$results.url$"
                   "ssquery=$search$" "ssname=$name$" "inline=$action.email.inline{default=False}$"
                   "sendresults=$action.email.sendresults{default=False}$" "sendpdf=$action.email.sendpdf{default=False}$"
                   "pdfview=$action.email.pdfview$" "searchid=$search_id$" "graceful=$graceful{default=True}$"
                   maxinputs="$action.email.maxresults{default=10000}$" maxtime="$action.email.maxtime{default=5m}$"]]&gt;
        &lt;/s:key&gt;
        &lt;s:key name="action.email.format"&gt;html&lt;/s:key&gt;
        &lt;s:key name="action.email.from"&gt;splunk&lt;/s:key&gt;
        &lt;s:key name="action.email.hostname"&gt;&lt;/s:key&gt;
        &lt;s:key name="action.email.inline"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.email.mailserver"&gt;localhost&lt;/s:key&gt;
        &lt;s:key name="action.email.maxresults"&gt;10000&lt;/s:key&gt;
        &lt;s:key name="action.email.maxtime"&gt;5m&lt;/s:key&gt;
        &lt;s:key name="action.email.pdfview"&gt;MyView&lt;/s:key&gt;
        &lt;s:key name="action.email.preprocess_results"&gt;&lt;/s:key&gt;
        &lt;s:key name="action.email.reportPaperOrientation"&gt;portrait&lt;/s:key&gt;
        &lt;s:key name="action.email.reportPaperSize"&gt;letter&lt;/s:key&gt;
        &lt;s:key name="action.email.reportServerEnabled"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.email.reportServerURL"&gt;&lt;/s:key&gt;
        &lt;s:key name="action.email.sendpdf"&gt;1&lt;/s:key&gt;
        &lt;s:key name="action.email.sendresults"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.email.subject"&gt;Splunk Alert: $name$&lt;/s:key&gt;
        &lt;s:key name="action.email.to"&gt;info@example.com&lt;/s:key&gt;
        &lt;s:key name="action.email.track_alert"&gt;1&lt;/s:key&gt;
        &lt;s:key name="action.email.ttl"&gt;10&lt;/s:key&gt;
        &lt;s:key name="action.email.use_ssl"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.email.use_tls"&gt;0&lt;/s:key&gt;
        &lt;s:key name="cron_schedule"&gt;* * * * *&lt;/s:key&gt;
        &lt;s:key name="description"&gt;scheduled search for view name=MyView&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:attributes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="optionalFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;description&lt;/s:item&gt;
                &lt;s:item&gt;disabled&lt;/s:item&gt;
                &lt;s:item&gt;next_scheduled_time&lt;/s:item&gt;
              &lt;/s:list&gt;
            &lt;/s:key&gt;
            &lt;s:key name="requiredFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;action.email.to&lt;/s:item&gt;
                &lt;s:item&gt;cron_schedule&lt;/s:item&gt;
                &lt;s:item&gt;is_scheduled&lt;/s:item&gt;
              &lt;/s:list&gt;
            &lt;/s:key&gt;
            &lt;s:key name="wildcardFields"&gt;
              &lt;s:list&gt;&lt;s:item&gt;action\.email.*&lt;/s:item&gt;&lt;/s:list&gt;
            &lt;/s:key&gt;
          &lt;/s:dict&gt;
        &lt;/s:key&gt;
        &lt;s:key name="is_scheduled"&gt;1&lt;/s:key&gt;
        &lt;s:key name="next_scheduled_time"&gt;2011-07-27 17:13:00 EDT&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## scheduled/views/{name}
{: name='scheduledviewsname'}

Edit a scheduled view, e.g. change schedule, enable disable schedule etc

	[POST] scheduled/views/{name}

### Parameters

action.email.to
: _Required_ **String** Comma or semicolon separated list of email addresses to send the view to

cron_schedule
: _Required_ **String** The cron schedule to use for delivering the view

description
: _Optional_ **String** User readable description of this scheduled view object

disabled
: _Optional_ **Boolean** Whether this object is enabled or disabled

is_scheduled
: _Required_ **Boolean** Whether this pdf delivery should be scheduled

next_scheduled_time
: _Optional_ **String** The next time when the view will be delivered. Ignored on edit, here only for backwards compatability

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
| **403** | Insufficient permissions to edit scheduled view. |
|--------------------------------
| **404** | Scheudled view does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Edit scheduled view to email to info@example.com every hour on the hour and update the description

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/scheduled/views/MyVew \
	-d action.email.to="info@example.com" \
	-d cron_schedule="0 * * * *" \
	-d is_scheduled=1 \
	-d description="New description"
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:s="http://dev.splunk.com/ns/rest"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;scheduledviews&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/scheduled/views&lt;/id&gt;
  &lt;updated&gt;2011-07-27T17:59:32-04:00&lt;/updated&gt;
  &lt;generator version="104601"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/scheduled/views/_reload" rel="_reload"/&gt;
  &lt;opensearch:totalResults&gt;1&lt;/opensearch:totalResults&gt;
  &lt;opensearch:itemsPerPage&gt;30&lt;/opensearch:itemsPerPage&gt;
  &lt;opensearch:startIndex&gt;0&lt;/opensearch:startIndex&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;_ScheduledView__MyView&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/admin/search/scheduled/views/_ScheduledView__MyView&lt;/id&gt;
    &lt;updated&gt;2011-07-27T17:59:32-04:00&lt;/updated&gt;
    &lt;link href="/servicesNS/admin/search/scheduled/views/_ScheduledView__MyView" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/admin/search/scheduled/views/_ScheduledView__MyView" rel="list"/&gt;
    &lt;link href="/servicesNS/admin/search/scheduled/views/_ScheduledView__MyView/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/admin/search/scheduled/views/_ScheduledView__MyView" rel="edit"/&gt;
    &lt;link href="/servicesNS/admin/search/scheduled/views/_ScheduledView__MyView" rel="remove"/&gt;
    &lt;link href="/servicesNS/admin/search/scheduled/views/_ScheduledView__MyView/move" rel="move"/&gt;
    &lt;link href="/servicesNS/admin/search/scheduled/views/_ScheduledView__MyView/disable" rel="disable"/&gt;
    &lt;link href="/servicesNS/admin/search/scheduled/views/_ScheduledView__MyView/dispatch" rel="dispatch"/&gt;
    &lt;link href="/servicesNS/admin/search/scheduled/views/_ScheduledView__MyView/history" rel="history"/&gt;
    &lt;link href="/servicesNS/admin/search/scheduled/views/_ScheduledView__MyView/notify" rel="notify"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="action.email"&gt;1&lt;/s:key&gt;
        &lt;s:key name="action.email.auth_password"&gt;&lt;/s:key&gt;
        &lt;s:key name="action.email.auth_username"&gt;&lt;/s:key&gt;
        &lt;s:key name="action.email.bcc"&gt;&lt;/s:key&gt;
        &lt;s:key name="action.email.cc"&gt;&lt;/s:key&gt;
        &lt;s:key name="action.email.command"&gt;
          &lt;![CDATA[$action.email.preprocess_results{default=""}$ |
                   sendemail "server=$action.email.mailserver{default=localhost}$" "use_ssl=$action.email.use_ssl{default=false}$"
                   "use_tls=$action.email.use_tls{default=false}$" "to=$action.email.to$" "cc=$action.email.cc$"
                   "bcc=$action.email.bcc$" "from=$action.email.from{default=splunk@localhost}$"
                   "subject=$action.email.subject{recurse=yes}$" "format=$action.email.format{default=csv}$"
                   "sssummary=Saved Search [$name$]: $counttype$($results.count$)" "sslink=$results.url$"
                   "ssquery=$search$" "ssname=$name$" "inline=$action.email.inline{default=False}$"
                   "sendresults=$action.email.sendresults{default=False}$" "sendpdf=$action.email.sendpdf{default=False}$"
                   "pdfview=$action.email.pdfview$" "searchid=$search_id$" "graceful=$graceful{default=True}$"
                   maxinputs="$action.email.maxresults{default=10000}$" maxtime="$action.email.maxtime{default=5m}$"]]&gt;
        &lt;/s:key&gt;
        &lt;s:key name="action.email.format"&gt;html&lt;/s:key&gt;
        &lt;s:key name="action.email.from"&gt;splunk&lt;/s:key&gt;
        &lt;s:key name="action.email.hostname"&gt;&lt;/s:key&gt;
        &lt;s:key name="action.email.inline"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.email.mailserver"&gt;localhost&lt;/s:key&gt;
        &lt;s:key name="action.email.maxresults"&gt;10000&lt;/s:key&gt;
        &lt;s:key name="action.email.maxtime"&gt;5m&lt;/s:key&gt;
        &lt;s:key name="action.email.pdfview"&gt;MyView&lt;/s:key&gt;
        &lt;s:key name="action.email.preprocess_results"&gt;&lt;/s:key&gt;
        &lt;s:key name="action.email.reportPaperOrientation"&gt;portrait&lt;/s:key&gt;
        &lt;s:key name="action.email.reportPaperSize"&gt;letter&lt;/s:key&gt;
        &lt;s:key name="action.email.reportServerEnabled"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.email.reportServerURL"&gt;&lt;/s:key&gt;
        &lt;s:key name="action.email.sendpdf"&gt;1&lt;/s:key&gt;
        &lt;s:key name="action.email.sendresults"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.email.subject"&gt;Splunk Alert: $name$&lt;/s:key&gt;
        &lt;s:key name="action.email.to"&gt;info@example.com&lt;/s:key&gt;
        &lt;s:key name="action.email.track_alert"&gt;1&lt;/s:key&gt;
        &lt;s:key name="action.email.ttl"&gt;10&lt;/s:key&gt;
        &lt;s:key name="action.email.use_ssl"&gt;0&lt;/s:key&gt;
        &lt;s:key name="action.email.use_tls"&gt;0&lt;/s:key&gt;
        &lt;s:key name="cron_schedule"&gt;0 * * * *&lt;/s:key&gt;
        &lt;s:key name="description"&gt;New Description&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="is_scheduled"&gt;1&lt;/s:key&gt;
        &lt;s:key name="next_scheduled_time"&gt;2011-07-27 18:00:00 EDT&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## scheduled/views/{name}/dispatch
{: name='scheduledviewsnamedispatch'}

Dispatch the scheduled search (powering the scheduled view) just like the scheduler would. Action available only through POST. The following optional arguments are accepted:"dispatch.now:    [time] dispatch the search as if it this was the current time
dispatch.*:      any dispatch.* field of the search can be overriden
now:             [time] deprecated, same as dispatch.now use that instead
trigger_actions: [bool] whether to trigger the alert actions
force_dispatch:  [bool] should a new search be started even if another instance of this search is already running

	[POST] scheduled/views/{name}/dispatch

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Dispatched the scheduled view successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **402** | The Splunk license in use has disabled this feature. |
|--------------------------------
| **403** | Insufficient permissions to dispatch a scheduled view. |
|--------------------------------
| **404** | Named view does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Dispatch the scheduled view and deliver the email (trigger the action) for MyView view

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/scheduled/views/MyView/dispatch \
	-d trigger_actions=1
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;?xml version='1.0' encoding='UTF-8'?&gt;
&lt;response&gt;&lt;sid&gt;admin__admin__search_X1NjaGVkdWxlZFZpZXdfX015Vmlldw_at_1311805021_c24ff1ea77ad714b&lt;/sid&gt;&lt;/response&gt;
</code></pre>

## scheduled/views/{name}/history
{: name='scheduledviewsnamehistory'}

Get a list of search jobs used to deliver this scheduled view

	[GET] scheduled/views/{name}/history

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Retrieved scheduled view history successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to retrieve scheduled view history. |
|--------------------------------
| **404** | Named view does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Get the delivery history of the scheduled view MyView

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/scheduled/views/MyVew/history
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:s="http://dev.splunk.com/ns/rest"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;_ScheduledView__MyView&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/scheduled/views&lt;/id&gt;
  &lt;updated&gt;2011-07-27T16:25:22-04:00&lt;/updated&gt;
  &lt;generator version="104601"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/scheduled/views/_reload" rel="_reload"/&gt;
  &lt;opensearch:totalResults&gt;1&lt;/opensearch:totalResults&gt;
  &lt;opensearch:itemsPerPage&gt;30&lt;/opensearch:itemsPerPage&gt;
  &lt;opensearch:startIndex&gt;0&lt;/opensearch:startIndex&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;scheduler__admin__search_X1NjaGVkdWxlZFZpZXdfX015Vmlldw_at_1311798300_842d7ca298ab521a&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/search/jobs/scheduler__admin__search_X1NjaGVkdWxlZFZpZXdfX015Vmlldw_at_1311798300_842d7ca298ab521a&lt;/id&gt;
    &lt;updated&gt;2011-07-27T16:25:15-04:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/search/search/jobs/scheduler__admin__search_X1NjaGVkdWxlZFZpZXdfX015Vmlldw_at_1311798300_842d7ca298ab521a" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;published&gt;2011-07-27T16:25:15-04:00&lt;/published&gt;
    &lt;link href="/servicesNS/nobody/search/search/jobs/scheduler__admin__search_X1NjaGVkdWxlZFZpZXdfX015Vmlldw_at_1311798300_842d7ca298ab521a" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/search/search/jobs/scheduler__admin__search_X1NjaGVkdWxlZFZpZXdfX015Vmlldw_at_1311798300_842d7ca298ab521a/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/search/search/jobs/scheduler__admin__search_X1NjaGVkdWxlZFZpZXdfX015Vmlldw_at_1311798300_842d7ca298ab521a" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/search/search/jobs/scheduler__admin__search_X1NjaGVkdWxlZFZpZXdfX015Vmlldw_at_1311798300_842d7ca298ab521a" rel="remove"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## search/jobs
{: name='searchjobs'}

Returns a list of current searches. 

Optional filter arguments can be passed to specify searches. The user id is implied by the authentication to the call. See the response properties for <code>/search/jobs/{search_id}</code> for descriptions of the job properties.

	[GET] search/jobs

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------

### Example

Shows an entry from the listing for all search jobs.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/search/jobs
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:s="http://dev.splunk.com/ns/rest"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;jobs&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/search/jobs&lt;/id&gt;
  &lt;updated&gt;2011-06-21T10:12:22-07:00&lt;/updated&gt;
  &lt;generator version="100492"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;opensearch:totalResults&gt;8&lt;/opensearch:totalResults&gt;
  &lt;opensearch:itemsPerPage&gt;0&lt;/opensearch:itemsPerPage&gt;
  &lt;opensearch:startIndex&gt;0&lt;/opensearch:startIndex&gt;
  &lt;entry&gt;
    &lt;title&gt;search  index=_internal (source=*/metrics.log* OR source=*\\metrics.log*) group=per_sourcetype_thruput
    &lt;id&gt;https://localhost:8089/services/search/jobs/scheduler__nobody__search_VG9wIGZpdmUgc291cmNldHlwZXM_at_1308676200_22702c154383bbe4&lt;/id&gt;
    &lt;updated&gt;2011-06-21T10:10:31.000-07:00&lt;/updated&gt;
    &lt;link href="/services/search/jobs/scheduler__nobody__search_VG9wIGZpdmUgc291cmNldHlwZXM_at_1308676200_22702c154383bbe4" rel="alternate"/&gt;
    &lt;published&gt;2011-06-21T10:10:23.000-07:00&lt;/published&gt;
    &lt;link href="/services/search/jobs/scheduler__nobody__search_VG9wIGZpdmUgc291cmNldHlwZXM_at_1308676200_22702c154383bbe4/search.log" rel="log"/&gt;
    &lt;link href="/services/search/jobs/scheduler__nobody__search_VG9wIGZpdmUgc291cmNldHlwZXM_at_1308676200_22702c154383bbe4/events" rel="events"/&gt;
    &lt;link href="/services/search/jobs/scheduler__nobody__search_VG9wIGZpdmUgc291cmNldHlwZXM_at_1308676200_22702c154383bbe4/results" rel="results"/&gt;
    &lt;link href="/services/search/jobs/scheduler__nobody__search_VG9wIGZpdmUgc291cmNldHlwZXM_at_1308676200_22702c154383bbe4/results_preview" rel="results_preview"/&gt;
    &lt;link href="/services/search/jobs/scheduler__nobody__search_VG9wIGZpdmUgc291cmNldHlwZXM_at_1308676200_22702c154383bbe4/timeline" rel="timeline"/&gt;
    &lt;link href="/services/search/jobs/scheduler__nobody__search_VG9wIGZpdmUgc291cmNldHlwZXM_at_1308676200_22702c154383bbe4/summary" rel="summary"/&gt;
    &lt;link href="/services/search/jobs/scheduler__nobody__search_VG9wIGZpdmUgc291cmNldHlwZXM_at_1308676200_22702c154383bbe4/control" rel="control"/&gt;
    &lt;author&gt;
      &lt;name&gt;splunk-system-user&lt;/name&gt;
    &lt;/author&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="cursorTime"&gt;1969-12-31T16:00:00.000-08:00&lt;/s:key&gt;
        &lt;s:key name="delegate"&gt;scheduler&lt;/s:key&gt;
        &lt;s:key name="diskUsage"&gt;73728&lt;/s:key&gt;
        &lt;s:key name="dispatchState"&gt;DONE&lt;/s:key&gt;
        &lt;s:key name="doneProgress"&gt;1.00000&lt;/s:key&gt;
        &lt;s:key name="dropCount"&gt;0&lt;/s:key&gt;
        &lt;s:key name="earliestTime"&gt;2011-06-20T10:10:00.000-07:00&lt;/s:key&gt;
        &lt;s:key name="eventAvailableCount"&gt;0&lt;/s:key&gt;
        &lt;s:key name="eventCount"&gt;1363&lt;/s:key&gt;
        &lt;s:key name="eventFieldCount"&gt;0&lt;/s:key&gt;
        &lt;s:key name="eventIsStreaming"&gt;1&lt;/s:key&gt;
        &lt;s:key name="eventIsTruncated"&gt;1&lt;/s:key&gt;
        &lt;s:key name="eventSearch"&gt;search index=_internal (source=*/metrics.log* OR source=*\\metrics.log*) group=per_sourcetype_thruput &lt;/s:key&gt;
        &lt;s:key name="eventSorting"&gt;none&lt;/s:key&gt;
        &lt;s:key name="isDone"&gt;1&lt;/s:key&gt;
        &lt;s:key name="isFailed"&gt;0&lt;/s:key&gt;
        &lt;s:key name="isFinalized"&gt;0&lt;/s:key&gt;
        &lt;s:key name="isPaused"&gt;0&lt;/s:key&gt;
        &lt;s:key name="isPreviewEnabled"&gt;0&lt;/s:key&gt;
        &lt;s:key name="isRealTimeSearch"&gt;0&lt;/s:key&gt;
        &lt;s:key name="isRemoteTimeline"&gt;0&lt;/s:key&gt;
        &lt;s:key name="isSaved"&gt;0&lt;/s:key&gt;
        &lt;s:key name="isSavedSearch"&gt;1&lt;/s:key&gt;
        &lt;s:key name="isZombie"&gt;0&lt;/s:key&gt;
        &lt;s:key name="keywords"&gt;group::per_sourcetype_thruput index::_internal source::*/metrics.log* source::*\metrics.log*&lt;/s:key&gt;
        &lt;s:key name="label"&gt;Top five sourcetypes&lt;/s:key&gt;
        &lt;s:key name="latestTime"&gt;2011-06-21T10:10:00.000-07:00&lt;/s:key&gt;
        &lt;s:key name="numPreviews"&gt;0&lt;/s:key&gt;
        &lt;s:key name="priority"&gt;5&lt;/s:key&gt;
        &lt;s:key name="remoteSearch"&gt;litsearch index=_internal ( source=*/metrics.log* OR source=*\\metrics.log* )
                group=per_sourcetype_thruput | addinfo  type=count label=prereport_events
        &lt;s:key name="reportSearch"&gt;chart  sum(kb) by series  | sort  -sum(kb)  | head  5&lt;/s:key&gt;
        &lt;s:key name="resultCount"&gt;4&lt;/s:key&gt;
        &lt;s:key name="resultIsStreaming"&gt;0&lt;/s:key&gt;
        &lt;s:key name="resultPreviewCount"&gt;4&lt;/s:key&gt;
        &lt;s:key name="runDuration"&gt;0.259000&lt;/s:key&gt;
        &lt;s:key name="scanCount"&gt;1363&lt;/s:key&gt;
        &lt;s:key name="searchEarliestTime"&gt;1308589800.000000000&lt;/s:key&gt;
        &lt;s:key name="searchLatestTime"&gt;1308676200.000000000&lt;/s:key&gt;
        &lt;s:key name="sid"&gt;scheduler__nobody__search_VG9wIGZpdmUgc291cmNldHlwZXM_at_1308676200_22702c154383bbe4&lt;/s:key&gt;
        &lt;s:key name="statusBuckets"&gt;0&lt;/s:key&gt;
        &lt;s:key name="ttl"&gt;489&lt;/s:key&gt;
        &lt;s:key name="performance"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="command.addinfo"&gt;
              &lt;s:dict&gt;
                &lt;s:key name="duration_secs"&gt;0.005&lt;/s:key&gt;
                &lt;s:key name="invocations"&gt;5&lt;/s:key&gt;
                &lt;s:key name="input_count"&gt;1363&lt;/s:key&gt;
                &lt;s:key name="output_count"&gt;1363&lt;/s:key&gt;
              &lt;/s:dict&gt;
            &lt;/s:key&gt;
            &lt;s:key name="command.chart"&gt;
              &lt;s:dict&gt;
                &lt;s:key name="duration_secs"&gt;0.003&lt;/s:key&gt;
                &lt;s:key name="invocations"&gt;1&lt;/s:key&gt;
                &lt;s:key name="input_count"&gt;100000&lt;/s:key&gt;
                &lt;s:key name="output_count"&gt;4&lt;/s:key&gt;
              &lt;/s:dict&gt;
            &lt;/s:key&gt;
            &lt;s:key name="command.convert"&gt;
              &lt;s:dict&gt;
                &lt;s:key name="duration_secs"&gt;0.006&lt;/s:key&gt;
                &lt;s:key name="invocations"&gt;5&lt;/s:key&gt;
                &lt;s:key name="input_count"&gt;1363&lt;/s:key&gt;
                &lt;s:key name="output_count"&gt;1363&lt;/s:key&gt;
              &lt;/s:dict&gt;
            &lt;/s:key&gt;
            &lt;s:key name="command.fields"&gt;
              &lt;s:dict&gt;
                &lt;s:key name="duration_secs"&gt;0.005&lt;/s:key&gt;
                &lt;s:key name="invocations"&gt;5&lt;/s:key&gt;
                &lt;s:key name="input_count"&gt;1363&lt;/s:key&gt;
                &lt;s:key name="output_count"&gt;1363&lt;/s:key&gt;
              &lt;/s:dict&gt;
            &lt;/s:key&gt;
            &lt;s:key name="command.head"&gt;
              &lt;s:dict&gt;
                &lt;s:key name="duration_secs"&gt;0.001&lt;/s:key&gt;
                &lt;s:key name="invocations"&gt;1&lt;/s:key&gt;
                &lt;s:key name="input_count"&gt;4&lt;/s:key&gt;
                &lt;s:key name="output_count"&gt;4&lt;/s:key&gt;
              &lt;/s:dict&gt;
            &lt;/s:key&gt;
            &lt;s:key name="command.presort"&gt;
              &lt;s:dict&gt;
                &lt;s:key name="duration_secs"&gt;0.001&lt;/s:key&gt;
                &lt;s:key name="invocations"&gt;1&lt;/s:key&gt;
                &lt;s:key name="input_count"&gt;4&lt;/s:key&gt;
                &lt;s:key name="output_count"&gt;4&lt;/s:key&gt;
              &lt;/s:dict&gt;
            &lt;/s:key&gt;
            &lt;s:key name="command.prestats"&gt;
              &lt;s:dict&gt;
                &lt;s:key name="duration_secs"&gt;0.014&lt;/s:key&gt;
                &lt;s:key name="invocations"&gt;5&lt;/s:key&gt;
                &lt;s:key name="input_count"&gt;1363&lt;/s:key&gt;
                &lt;s:key name="output_count"&gt;12&lt;/s:key&gt;
              &lt;/s:dict&gt;
            &lt;/s:key&gt;
            &lt;s:key name="command.search"&gt;
              &lt;s:dict&gt;
                &lt;s:key name="duration_secs"&gt;0.058&lt;/s:key&gt;
                &lt;s:key name="invocations"&gt;5&lt;/s:key&gt;
                &lt;s:key name="input_count"&gt;0&lt;/s:key&gt;
                &lt;s:key name="output_count"&gt;1363&lt;/s:key&gt;
              &lt;/s:dict&gt;
            &lt;/s:key&gt;
            &lt;s:key name="command.search.fieldalias"&gt;
              &lt;s:dict&gt;
                &lt;s:key name="duration_secs"&gt;0.003&lt;/s:key&gt;
                &lt;s:key name="invocations"&gt;3&lt;/s:key&gt;
                &lt;s:key name="input_count"&gt;1363&lt;/s:key&gt;
                &lt;s:key name="output_count"&gt;1363&lt;/s:key&gt;
              &lt;/s:dict&gt;
            &lt;/s:key&gt;
            &lt;s:key name="command.search.filter"&gt;
              &lt;s:dict&gt;
                &lt;s:key name="duration_secs"&gt;0.004&lt;/s:key&gt;
                &lt;s:key name="invocations"&gt;3&lt;/s:key&gt;
              &lt;/s:dict&gt;
            &lt;/s:key&gt;
            &lt;s:key name="command.search.index"&gt;
              &lt;s:dict&gt;
                &lt;s:key name="duration_secs"&gt;0.010&lt;/s:key&gt;
                &lt;s:key name="invocations"&gt;5&lt;/s:key&gt;
              &lt;/s:dict&gt;
            &lt;/s:key&gt;
            &lt;s:key name="command.search.kv"&gt;
              &lt;s:dict&gt;
                &lt;s:key name="duration_secs"&gt;0.011&lt;/s:key&gt;
                &lt;s:key name="invocations"&gt;3&lt;/s:key&gt;
              &lt;/s:dict&gt;
            &lt;/s:key&gt;
            &lt;s:key name="command.search.lookups"&gt;
              &lt;s:dict&gt;
                &lt;s:key name="duration_secs"&gt;0.003&lt;/s:key&gt;
                &lt;s:key name="invocations"&gt;3&lt;/s:key&gt;
                &lt;s:key name="input_count"&gt;1363&lt;/s:key&gt;
                &lt;s:key name="output_count"&gt;1363&lt;/s:key&gt;
              &lt;/s:dict&gt;
            &lt;/s:key&gt;
            &lt;s:key name="command.search.rawdata"&gt;
              &lt;s:dict&gt;
                &lt;s:key name="duration_secs"&gt;0.034&lt;/s:key&gt;
                &lt;s:key name="invocations"&gt;3&lt;/s:key&gt;
              &lt;/s:dict&gt;
            &lt;/s:key&gt;
            &lt;s:key name="command.search.tags"&gt;
              &lt;s:dict&gt;
                &lt;s:key name="duration_secs"&gt;0.005&lt;/s:key&gt;
                &lt;s:key name="invocations"&gt;5&lt;/s:key&gt;
                &lt;s:key name="input_count"&gt;1363&lt;/s:key&gt;
                &lt;s:key name="output_count"&gt;1363&lt;/s:key&gt;
              &lt;/s:dict&gt;
            &lt;/s:key&gt;
            &lt;s:key name="command.search.typer"&gt;
              &lt;s:dict&gt;
                &lt;s:key name="duration_secs"&gt;0.005&lt;/s:key&gt;
                &lt;s:key name="invocations"&gt;5&lt;/s:key&gt;
                &lt;s:key name="input_count"&gt;1363&lt;/s:key&gt;
                &lt;s:key name="output_count"&gt;1363&lt;/s:key&gt;
              &lt;/s:dict&gt;
            &lt;/s:key&gt;
            &lt;s:key name="command.sort"&gt;
              &lt;s:dict&gt;
                &lt;s:key name="duration_secs"&gt;0.001&lt;/s:key&gt;
                &lt;s:key name="invocations"&gt;1&lt;/s:key&gt;
                &lt;s:key name="input_count"&gt;4&lt;/s:key&gt;
                &lt;s:key name="output_count"&gt;4&lt;/s:key&gt;
              &lt;/s:dict&gt;
            &lt;/s:key&gt;
            &lt;s:key name="dispatch.createProviderQueue"&gt;
              &lt;s:dict&gt;
                &lt;s:key name="duration_secs"&gt;0.067&lt;/s:key&gt;
                &lt;s:key name="invocations"&gt;1&lt;/s:key&gt;
              &lt;/s:dict&gt;
            &lt;/s:key&gt;
            &lt;s:key name="dispatch.evaluate"&gt;
              &lt;s:dict&gt;
                &lt;s:key name="duration_secs"&gt;0.038&lt;/s:key&gt;
                &lt;s:key name="invocations"&gt;1&lt;/s:key&gt;
              &lt;/s:dict&gt;
            &lt;/s:key&gt;
            &lt;s:key name="dispatch.evaluate.chart"&gt;
              &lt;s:dict&gt;
                &lt;s:key name="duration_secs"&gt;0.001&lt;/s:key&gt;
                &lt;s:key name="invocations"&gt;1&lt;/s:key&gt;
              &lt;/s:dict&gt;
            &lt;/s:key&gt;
            &lt;s:key name="dispatch.evaluate.head"&gt;
              &lt;s:dict&gt;
                &lt;s:key name="duration_secs"&gt;0.001&lt;/s:key&gt;
                &lt;s:key name="invocations"&gt;1&lt;/s:key&gt;
              &lt;/s:dict&gt;
            &lt;/s:key&gt;
            &lt;s:key name="dispatch.evaluate.search"&gt;
              &lt;s:dict&gt;
                &lt;s:key name="duration_secs"&gt;0.037&lt;/s:key&gt;
                &lt;s:key name="invocations"&gt;1&lt;/s:key&gt;
              &lt;/s:dict&gt;
            &lt;/s:key&gt;
            &lt;s:key name="dispatch.evaluate.sort"&gt;
              &lt;s:dict&gt;
                &lt;s:key name="duration_secs"&gt;0.001&lt;/s:key&gt;
                &lt;s:key name="invocations"&gt;1&lt;/s:key&gt;
              &lt;/s:dict&gt;
            &lt;/s:key&gt;
            &lt;s:key name="dispatch.fetch"&gt;
              &lt;s:dict&gt;
                &lt;s:key name="duration_secs"&gt;0.126&lt;/s:key&gt;
                &lt;s:key name="invocations"&gt;6&lt;/s:key&gt;
              &lt;/s:dict&gt;
            &lt;/s:key&gt;
            &lt;s:key name="dispatch.stream.local"&gt;
              &lt;s:dict&gt;
                &lt;s:key name="duration_secs"&gt;0.070&lt;/s:key&gt;
                &lt;s:key name="invocations"&gt;5&lt;/s:key&gt;
              &lt;/s:dict&gt;
            &lt;/s:key&gt;
          &lt;/s:dict&gt;
        &lt;/s:key&gt;
        &lt;s:key name="messages"&gt;
          &lt;s:dict/&gt;
        &lt;/s:key&gt;
        &lt;s:key name="request"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="ui_dispatch_app"&gt;&lt;/s:key&gt;
            &lt;s:key name="ui_dispatch_view"&gt;&lt;/s:key&gt;
          &lt;/s:dict&gt;
        &lt;/s:key&gt;
        &lt;s:key name="eai:acl"&gt;
          &lt;s:dict&gt;
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
            &lt;s:key name="owner"&gt;nobody&lt;/s:key&gt;
            &lt;s:key name="modifiable"&gt;true&lt;/s:key&gt;
            &lt;s:key name="sharing"&gt;global&lt;/s:key&gt;
            &lt;s:key name="app"&gt;search&lt;/s:key&gt;
            &lt;s:key name="can_write"&gt;true&lt;/s:key&gt;
          &lt;/s:dict&gt;
        &lt;/s:key&gt;
        &lt;s:key name="searchProviders"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;vgenovese-mbp15.splunk.com-vgenovese&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
  . . .
&lt;/feed&gt;
</code></pre>

## search/jobs
{: name='searchjobs'}

Starts a new search, returning the search ID (<code>&lt;sid&gt;</code>).

The search parameter is a search language string that specifies the search. Often you create a search specifying just the search parameter. Use the other parameters to customize a search to specific needs.

Use the returned  (<code>&lt;sid&gt;</code>) in the following endpoints to view and manage the search:

:search/jobs/{search_id}: View the status of this search job.

:search/jobs/{search_id}/control: Execute job control commands, such as pause, cancel, preview, and others.

:search/jobs/{search_id}/events: View a set of untransformed events for the search.

:search/jobs/{search_id}/results: View results of the search.

:search/jobs/{search_id}/results_preview: Preview results of a search that has not completed

:search/jobs/{search_id}/search.log: View the log file generated by the search.

:search/jobs/{search_id}/summary: View field summary information

:search/jobs/{search_id}/timeline: View event distribution over time.

	[POST] search/jobs

### Parameters

auto_cancel
: _Optional_ **Number** If specified, the job automatically cancels after this many seconds of inactivity.  (0 means never auto-cancel)

auto_finalize_ec
: _Optional_ **Number** Auto-finalize the search after at least this many events have been processed. <br/><br/>Specify <code>0</code> to indicate no limit.

auto_pause
: _Optional_ **Number** If specified, the job automatically cancels after this many seconds of inactivity.  (0 means never auto-pause)

earliest_time
: _Optional_ **String** Specify a time string. Sets the earliest (inclusive), respectively, time bounds for the search. <br/><br/>The time string can be either a UTC time (with fractional seconds), a relative time specifier (to now) or a formatted time string. (Also see comment for the search_mode variable.)

enable_lookups
: _Optional_ **Boolean** Indicates whether lookups should be applied to events. <br/><br/>Specifying true (the default) may slow searches significantly depending on the nature of the lookups.


exec_mode
: _Optional_ **Enum** Valid values: (blocking &#124; oneshot &#124; normal)<br/><br/>If set to normal, runs an asynchronous search. <br/><br/>If set to blocking, returns the sid when the job is complete. <br/><br/>If set to oneshot, returns results in the same call.

force_bundle_replication
: _Optional_ **Boolean** Specifies whether this search should cause (and wait depending on the value of sync_bundle_replication) for bundle synchronization with all search peers.

id
: _Optional_ **String** Optional string to specify the search ID (<code>&lt:sid&gt;</code>).  If unspecified, a random ID is generated.

latest_time
: _Optional_ **String** Specify a time string. Sets the latest (exclusive), respectively, time bounds for the search. <br/><br/>The time string can be either a UTC time (with fractional seconds), a relative time specifier (to now) or a formatted time string. (Also see comment for the search_mode variable.)

max_count
: _Optional_ **Number** The number of events that can be accessible in any given status bucket. <br/><br/>Also, in transforming mode, the maximum number of results to store. Specifically, in all calls, <code>codeoffset+count <= max_count</code>.

max_time
: _Optional_ **Number** The number of seconds to run this search before finalizing. Specify <code>0</code> to never finalize.

namespace
: _Optional_ **String** The application namespace in which to restrict searches. <br/><br/>The namespace corresponds to the identifier recognized in the <code>/services/apps/local</code> endpoint. 

now
: _Optional_ **String** Specify a time string to set the absolute time used for any relative time specifier in the search. Defaults to the current system time.<br/><br/>You can specify a relative time modifier for this parameter. For example, specify <code>+2d</code> to specify the current time plus two days.<br/><br/>If you specify a relative time modifier both in this parameter and in the search string, the search string modifier takes precedence.<br/><br/>Refer to [[Documentation:Splunk:SearchReference:SearchTimeModifiers|Time modifiers for search]] for details on specifying relative time modifiers.

reduce_freq
: _Optional_ **Number** Determines how frequently to run the MapReduce reduce phase on accumulated map values.

reload_macros
: _Optional_ **Boolean** Specifies whether to reload macro definitions from <code>macros.conf</code>. <br/><br/>Default is true.

remote_server_list
: _Optional_ **String** Comma-separated list of (possibly wildcarded) servers from which raw events should be pulled. This same server list is to be used in subsearches.

required_field_list
: _Optional_ **String** Deprecated. Use rf instead. <br/><br/>A comma-separated list of required fields that, even if not referenced or used directly by the search,is still included by the events and summary endpoints.

rf
: _Optional_ **String** Adds a required field to the search. There can be multiple <code>rf</code> POST arguments to the search.<br/><br/>Consider using this form of passing the required fields to the search instead of the deprecated <code>required_field_list</code>. If both <code>rf</code> and <code>required_field_list</code> are supplied, the union of the two lists is used.

rt_blocking
: _Optional_ **Boolean**  For a realtime search, indicates if the indexer blocks if the queue for this search is full.

rt_indexfilter
: _Optional_ **Boolean** For a realtime search, indicates if the indexer prefilters events.

rt_maxblocksecs
: _Optional_ **Number** For a realtime search with rt_blocking set to true, the maximum time to block.<br/><br/>Specify <code>0</code> to indicate no limit.

rt_queue_size
: _Optional_ **Number** For a realtime search, the queue size (in events) that the indexer should use for this search.

search
: _Required_ **Search** The search language string to execute, taking results from the local and remote servers.<br/><br/>Examples:<br/><br/>  "search *"<br/><br/>  "search * | outputcsv"

search_listener
: _Optional_ **String** Registers a search state listener with the search.<br/><br/>Use the format <code>search_state;results_condition;http_method;uri;</code><br/><br/>For example: <code>search_listener=onResults;true;POST;/servicesNS/admin/search/saved/search/foobar/notify;</code>


search_mode
: _Optional_ **Enum** Valid values: (normal &#124; realtime)<br/><br/>If set to realtime, search runs over live data. A realtime search may also be indicated by earliest_time and latest_time variables starting with 'rt' even if the search_mode is set to normal or is unset. For a real-time search, if both earliest_time and latest_time are both exactly 'rt', the search represents all appropriate live data received since the start of the search. <br/><br/>Additionally, if earliest_time and/or latest_time are 'rt' followed by a relative time specifiers then a sliding window is used where the time bounds of the window are determined by the relative time specifiers and are continuously updated based on the wall-clock time.

spawn_process
: _Optional_ **Boolean** Specifies whether the search should run in a separate spawned process. Default is true.

status_buckets
: _Optional_ **Number** The most status buckets to generate.<br/><br/><code>0</code> indicates to not generate timeline information.

sync_bundle_replication
: _Optional_ **Boolean** Specifies whether this search should wait for bundle replication to complete.

time_format
: _Optional_ **String** Used to convert a formatted time string from {start,end}_time into UTC seconds. It defaults to ISO-8601.

timeout
: _Optional_ **Number** The number of seconds to keep this search after processing has stopped.

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **201** | Created successfully. |
|--------------------------------

### Example

Starts a new search, specifying the search ID (<code>&lt;sid&gt;</code>) to use.
The search string for the search parameter must be prefixed with "search." Thus, it is in the form:
search search_string
URI-encode the search string if it contains any of the following characters: =, &, ?, %
Otherwise, these characters can be interpreted as part of the HTTP request.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/servicesNS/admin/search/search/jobs --data-urlencode search="search index=_internal source=*/metrics.log" \
	-d id=mysearch_02151949
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>
&lt;response&gt;&lt;sid&gt;mysearch_02151949&lt;/sid&gt;&lt;/response&gt;
</code></pre>

## search/jobs/export
{: name='searchjobsexport'}

Performs a search identical to POST search/jobs, except the search does not create a search ID (<sid>) and the search streams results as they become available. Streaming of results is based on the search string.
 
For non-streaming searches, previews of the final results are available if preview is enabled. If preview is not enabled, it is better to use search/jobs with exec_mode=oneshot.

	[GET] search/jobs/export

### Parameters

auto_cancel
: _Optional_ **Number** Same as for POST search/jobs.

auto_finalize_ec
: _Optional_ **Number** Same as for POST search/jobs.

auto_pause
: _Optional_ **Number** Same as for POST search/jobs.

earliest_time
: _Optional_ **String** Same as for POST search/jobs.

enable_lookups
: _Optional_ **Bool** Same as for POST search/jobs.

force_bundle_replication
: _Optional_ **Bool** Same as for POST search/jobs.

id
: _Optional_ **String** Same as for POST search/jobs.

latest_time
: _Optional_ **String** Same as for POST search/jobs.

max_time
: _Optional_ **Number** Same as for POST search/jobs.

namespace
: _Optional_ **String** Same as for POST search/jobs.

now
: _Optional_ **String** Same as for POST search/jobs.

reduce_freq
: _Optional_ **Number** Same as for POST search/jobs.

reload_macros
: _Optional_ **Bool** Same as for POST search/jobs.

remote_server_list
: _Optional_ **String** Same as for POST search/jobs.

required_field_list
: _Optional_ **String** Same as for POST search/jobs.

rf
: _Optional_ **String** Same as for POST search/jobs.

rt_blocking
: _Optional_ **Bool** Same as for POST search/jobs.

rt_indexfilter
: _Optional_ **Bool** Same as for POST search/jobs.

rt_maxblocksecs
: _Optional_ **Number** Same as for POST search/jobs.

rt_queue_size
: _Optional_ **Number** Same as for POST search/jobs.

search
: _Required_ **String** Same as for POST search/jobs.

search_listener
: _Optional_ **String** Same as for POST search/jobs.

search_mode
: _Optional_ **Enum** Same as for POST search/jobs.

sync_bundle_replication
: _Optional_ **Bool** Same as for POST search/jobs.

time_format
: _Optional_ **String** Same as for POST search/jobs.

timeout
: _Optional_ **Number** Same as for POST search/jobs.

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Searched successfully. |
|--------------------------------

### Example

Performs a blocking search for the most recent event in the default index.
The search string for the search parameter must be prefixed with "search." Thus, it is in the form:
search search_string
URI-encode the search string to make sure characters such as the equals sign or path separators are interpreted correctly.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/search/jobs/export \
	-d search="search * | head 1"
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;results preview='0'&gt;
&lt;meta&gt;
&lt;fieldOrder&gt;
&lt;field&gt;_cd&lt;/field&gt;
&lt;field&gt;_indextime&lt;/field&gt;
&lt;field&gt;_raw&lt;/field&gt;
&lt;field&gt;_serial&lt;/field&gt;
&lt;field&gt;_si&lt;/field&gt;
&lt;field&gt;_sourcetype&lt;/field&gt;
&lt;field&gt;_time&lt;/field&gt;
&lt;field&gt;host&lt;/field&gt;
&lt;field&gt;index&lt;/field&gt;
&lt;field&gt;linecount&lt;/field&gt;
&lt;field&gt;source&lt;/field&gt;
&lt;field&gt;sourcetype&lt;/field&gt;
&lt;field&gt;splunk_server&lt;/field&gt;
&lt;/fieldOrder&gt;
&lt;/meta&gt;
&lt;messages&gt;
  &lt;msg type="DEBUG"&gt;base lispy: [ AND ]&lt;/msg&gt;
  &lt;msg type="DEBUG"&gt;search context: user="admin", app="search", bs-pathname="/home/amrit/splunk/etc"&lt;/msg&gt;
&lt;/messages&gt;
        &lt;result offset='0'&gt;
                &lt;field k='_cd'&gt;
                        &lt;value&gt;&lt;text&gt;0:297461&lt;/text&gt;&lt;/value&gt;
                &lt;/field&gt;
                &lt;field k='_indextime'&gt;
                        &lt;value&gt;&lt;text&gt;1310338878&lt;/text&gt;&lt;/value&gt;
                &lt;/field&gt;
                &lt;field k='_raw'&gt;&lt;v xml:space='preserve' trunc='0'&gt;Sun Jul 10 15:56:02 PDT 2011   User vishalp logged in successfully.&lt;/v&gt;&lt;/field&gt;
                &lt;field k='_serial'&gt;
                        &lt;value&gt;&lt;text&gt;0&lt;/text&gt;&lt;/value&gt;
                &lt;/field&gt;
                &lt;field k='_si'&gt;
                        &lt;value&gt;&lt;text&gt;MrT&lt;/text&gt;&lt;/value&gt;
                        &lt;value&gt;&lt;text&gt;main&lt;/text&gt;&lt;/value&gt;
                &lt;/field&gt;
                &lt;field k='_sourcetype'&gt;
                        &lt;value&gt;&lt;text&gt;web_event&lt;/text&gt;&lt;/value&gt;
                &lt;/field&gt;
                &lt;field k='_time'&gt;
                        &lt;value&gt;&lt;text&gt;2011-07-10 15:56:02.000 PDT&lt;/text&gt;&lt;/value&gt;
                &lt;/field&gt;
                &lt;field k='host'&gt;
                        &lt;value&gt;&lt;text&gt;127.0.0.1&lt;/text&gt;&lt;/value&gt;
                &lt;/field&gt;
                &lt;field k='index'&gt;
                        &lt;value&gt;&lt;text&gt;main&lt;/text&gt;&lt;/value&gt;
                &lt;/field&gt;
                &lt;field k='linecount'&gt;
                        &lt;value&gt;&lt;text&gt;1&lt;/text&gt;&lt;/value&gt;
                &lt;/field&gt;
                &lt;field k='source'&gt;
                        &lt;value&gt;&lt;text&gt;www&lt;/text&gt;&lt;/value&gt;
                &lt;/field&gt;
                &lt;field k='sourcetype'&gt;
                        &lt;value&gt;&lt;text&gt;web_event&lt;/text&gt;&lt;/value&gt;
                &lt;/field&gt;
                &lt;field k='splunk_server'&gt;
                        &lt;value&gt;&lt;text&gt;MrT&lt;/text&gt;&lt;/value&gt;
                &lt;/field&gt;
        &lt;/result&gt;
&lt;/results&gt;
</code></pre>

## search/jobs/{search_id}
{: name='searchjobssearchid'}

Deletes the search job specified by {search_id}.

{search_id} is the <code>&lt;sid&gt;</code> field returned from the GET operation for the <code>search/jobs</code> endpoint.

	[DELETE] search/jobs/{search_id}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deleted successfully. |
|--------------------------------
| **404** | Search job does not exist. |
|--------------------------------

### Example

Deletes the specified search job. The {search_id} was obtained from the <code>&lt;sid&gt;</code> field returned by the GET operation for /search/jobs.
This example uses the <code>&lt;sid&gt;</code> created for the example for the POST operation to search/jobs.

#### Request
<pre class='terminal'>
curl -k -u admin:pass --request DELETE https://localhost:8089/services/search/jobs/mysearch_02151949
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;response&gt;&lt;messages&gt;&lt;msg type='INFO'&gt;Search job cancelled.&lt;/msg&gt;&lt;/messages&gt;&lt;/response&gt;
</code></pre>

## search/jobs/{search_id}
{: name='searchjobssearchid'}

Return summary information about the search job specified by {search_id}.

You can get a search ID from the <code><sid></code> field returned from the GET operation for the <code>search/jobs</code> endpoint.

	[GET] search/jobs/{search_id}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **404** | Search job does not exist. |
|--------------------------------

### Example

Lists summary information about a search job. The {search_id} was obtained from the &lt;sid&gt; field returned by the GET operation for /search/jobs.
This example uses the search ID (<code><sid></code>) created for the example for the POST operation to search/jobs.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/search/jobs/mysearch_02151949
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;entry
       xmlns="http://www.w3.org/2005/Atom"
       xmlns:s="http://dev.splunk.com/ns/rest"
       xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;search index&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/search/jobs/mysearch_02151949&lt;/id&gt;
  &lt;updated&gt;2011-07-07T20:49:58.000-07:00&lt;/updated&gt;
  &lt;link href="/services/search/jobs/mysearch_02151949" rel="alternate"/&gt;
  &lt;published&gt;2011-07-07T20:49:57.000-07:00&lt;/published&gt;
  &lt;link href="/services/search/jobs/mysearch_02151949/search.log" rel="search.log"/&gt;
  &lt;link href="/services/search/jobs/mysearch_02151949/events" rel="events"/&gt;
  &lt;link href="/services/search/jobs/mysearch_02151949/results" rel="results"/&gt;
  &lt;link href="/services/search/jobs/mysearch_02151949/results_preview" rel="results_preview"/&gt;
  &lt;link href="/services/search/jobs/mysearch_02151949/timeline" rel="timeline"/&gt;
  &lt;link href="/services/search/jobs/mysearch_02151949/summary" rel="summary"/&gt;
  &lt;link href="/services/search/jobs/mysearch_02151949/control" rel="control"/&gt;
  &lt;author&gt;
    &lt;name&gt;admin&lt;/name&gt;
  &lt;/author&gt;
  &lt;content type="text/xml"&gt;
    &lt;s:dict&gt;
      &lt;s:key name="cursorTime"&gt;1969-12-31T16:00:00.000-08:00&lt;/s:key&gt;
      &lt;s:key name="delegate"&gt;&lt;/s:key&gt;
      &lt;s:key name="diskUsage"&gt;2174976&lt;/s:key&gt;
      &lt;s:key name="dispatchState"&gt;DONE&lt;/s:key&gt;
      &lt;s:key name="doneProgress"&gt;1.00000&lt;/s:key&gt;
      &lt;s:key name="dropCount"&gt;0&lt;/s:key&gt;
      &lt;s:key name="earliestTime"&gt;2011-07-07T11:18:08.000-07:00&lt;/s:key&gt;
      &lt;s:key name="eventAvailableCount"&gt;287&lt;/s:key&gt;
      &lt;s:key name="eventCount"&gt;287&lt;/s:key&gt;
      &lt;s:key name="eventFieldCount"&gt;6&lt;/s:key&gt;
      &lt;s:key name="eventIsStreaming"&gt;1&lt;/s:key&gt;
      &lt;s:key name="eventIsTruncated"&gt;0&lt;/s:key&gt;
      &lt;s:key name="eventSearch"&gt;search index&lt;/s:key&gt;
      &lt;s:key name="eventSorting"&gt;desc&lt;/s:key&gt;
      &lt;s:key name="isDone"&gt;1&lt;/s:key&gt;
      &lt;s:key name="isFailed"&gt;0&lt;/s:key&gt;
      &lt;s:key name="isFinalized"&gt;0&lt;/s:key&gt;
      &lt;s:key name="isPaused"&gt;0&lt;/s:key&gt;
      &lt;s:key name="isPreviewEnabled"&gt;0&lt;/s:key&gt;
      &lt;s:key name="isRealTimeSearch"&gt;0&lt;/s:key&gt;
      &lt;s:key name="isRemoteTimeline"&gt;0&lt;/s:key&gt;
      &lt;s:key name="isSaved"&gt;0&lt;/s:key&gt;
      &lt;s:key name="isSavedSearch"&gt;0&lt;/s:key&gt;
      &lt;s:key name="isZombie"&gt;0&lt;/s:key&gt;
      &lt;s:key name="keywords"&gt;index&lt;/s:key&gt;
      &lt;s:key name="label"&gt;&lt;/s:key&gt;
      &lt;s:key name="latestTime"&gt;1969-12-31T16:00:00.000-08:00&lt;/s:key&gt;
      &lt;s:key name="numPreviews"&gt;0&lt;/s:key&gt;
      &lt;s:key name="priority"&gt;5&lt;/s:key&gt;
      &lt;s:key name="remoteSearch"&gt;litsearch index | fields  keepcolorder=t "host" "index" "linecount" "source" "sourcetype" "splunk_server"&lt;/s:key&gt;
      &lt;s:key name="reportSearch"&gt;&lt;/s:key&gt;
      &lt;s:key name="resultCount"&gt;287&lt;/s:key&gt;
      &lt;s:key name="resultIsStreaming"&gt;1&lt;/s:key&gt;
      &lt;s:key name="resultPreviewCount"&gt;287&lt;/s:key&gt;
      &lt;s:key name="runDuration"&gt;1.004000&lt;/s:key&gt;
      &lt;s:key name="scanCount"&gt;287&lt;/s:key&gt;
      &lt;s:key name="sid"&gt;mysearch_02151949&lt;/s:key&gt;
      &lt;s:key name="statusBuckets"&gt;0&lt;/s:key&gt;
      &lt;s:key name="ttl"&gt;516&lt;/s:key&gt;
      &lt;s:key name="performance"&gt;
        &lt;s:dict&gt;
          &lt;s:key name="command.fields"&gt;
            &lt;s:dict&gt;
              &lt;s:key name="duration_secs"&gt;0.004&lt;/s:key&gt;
              &lt;s:key name="invocations"&gt;4&lt;/s:key&gt;
              &lt;s:key name="input_count"&gt;287&lt;/s:key&gt;
              &lt;s:key name="output_count"&gt;287&lt;/s:key&gt;
            &lt;/s:dict&gt;
          &lt;/s:key&gt;
          &lt;s:key name="command.search"&gt;
            &lt;s:dict&gt;
              &lt;s:key name="duration_secs"&gt;0.089&lt;/s:key&gt;
              &lt;s:key name="invocations"&gt;4&lt;/s:key&gt;
              &lt;s:key name="input_count"&gt;0&lt;/s:key&gt;
              &lt;s:key name="output_count"&gt;287&lt;/s:key&gt;
            &lt;/s:dict&gt;
          &lt;/s:key&gt;
          &lt;s:key name="command.search.fieldalias"&gt;
            &lt;s:dict&gt;
              &lt;s:key name="duration_secs"&gt;0.002&lt;/s:key&gt;
              &lt;s:key name="invocations"&gt;2&lt;/s:key&gt;
              &lt;s:key name="input_count"&gt;287&lt;/s:key&gt;
              &lt;s:key name="output_count"&gt;287&lt;/s:key&gt;
            &lt;/s:dict&gt;
          &lt;/s:key&gt;
          &lt;s:key name="command.search.index"&gt;
            &lt;s:dict&gt;
              &lt;s:key name="duration_secs"&gt;0.005&lt;/s:key&gt;
              &lt;s:key name="invocations"&gt;4&lt;/s:key&gt;
            &lt;/s:dict&gt;
          &lt;/s:key&gt;
          &lt;s:key name="command.search.kv"&gt;
            &lt;s:dict&gt;
              &lt;s:key name="duration_secs"&gt;0.002&lt;/s:key&gt;
              &lt;s:key name="invocations"&gt;2&lt;/s:key&gt;
            &lt;/s:dict&gt;
          &lt;/s:key&gt;
          &lt;s:key name="command.search.lookups"&gt;
            &lt;s:dict&gt;
              &lt;s:key name="duration_secs"&gt;0.002&lt;/s:key&gt;
              &lt;s:key name="invocations"&gt;2&lt;/s:key&gt;
              &lt;s:key name="input_count"&gt;287&lt;/s:key&gt;
              &lt;s:key name="output_count"&gt;287&lt;/s:key&gt;
            &lt;/s:dict&gt;
          &lt;/s:key&gt;
          &lt;s:key name="command.search.rawdata"&gt;
            &lt;s:dict&gt;
              &lt;s:key name="duration_secs"&gt;0.083&lt;/s:key&gt;
              &lt;s:key name="invocations"&gt;2&lt;/s:key&gt;
            &lt;/s:dict&gt;
          &lt;/s:key&gt;
          &lt;s:key name="command.search.tags"&gt;
            &lt;s:dict&gt;
              &lt;s:key name="duration_secs"&gt;0.004&lt;/s:key&gt;
              &lt;s:key name="invocations"&gt;4&lt;/s:key&gt;
              &lt;s:key name="input_count"&gt;287&lt;/s:key&gt;
              &lt;s:key name="output_count"&gt;287&lt;/s:key&gt;
            &lt;/s:dict&gt;
          &lt;/s:key&gt;
          &lt;s:key name="command.search.typer"&gt;
            &lt;s:dict&gt;
              &lt;s:key name="duration_secs"&gt;0.004&lt;/s:key&gt;
              &lt;s:key name="invocations"&gt;4&lt;/s:key&gt;
              &lt;s:key name="input_count"&gt;287&lt;/s:key&gt;
              &lt;s:key name="output_count"&gt;287&lt;/s:key&gt;
            &lt;/s:dict&gt;
          &lt;/s:key&gt;
          &lt;s:key name="dispatch.createProviderQueue"&gt;
            &lt;s:dict&gt;
              &lt;s:key name="duration_secs"&gt;0.059&lt;/s:key&gt;
              &lt;s:key name="invocations"&gt;1&lt;/s:key&gt;
            &lt;/s:dict&gt;
          &lt;/s:key&gt;
          &lt;s:key name="dispatch.evaluate"&gt;
            &lt;s:dict&gt;
              &lt;s:key name="duration_secs"&gt;0.037&lt;/s:key&gt;
              &lt;s:key name="invocations"&gt;1&lt;/s:key&gt;
            &lt;/s:dict&gt;
          &lt;/s:key&gt;
          &lt;s:key name="dispatch.evaluate.search"&gt;
            &lt;s:dict&gt;
              &lt;s:key name="duration_secs"&gt;0.036&lt;/s:key&gt;
              &lt;s:key name="invocations"&gt;1&lt;/s:key&gt;
            &lt;/s:dict&gt;
          &lt;/s:key&gt;
          &lt;s:key name="dispatch.fetch"&gt;
            &lt;s:dict&gt;
              &lt;s:key name="duration_secs"&gt;0.092&lt;/s:key&gt;
              &lt;s:key name="invocations"&gt;5&lt;/s:key&gt;
            &lt;/s:dict&gt;
          &lt;/s:key&gt;
          &lt;s:key name="dispatch.readEventsInResults"&gt;
            &lt;s:dict&gt;
              &lt;s:key name="duration_secs"&gt;0.110&lt;/s:key&gt;
              &lt;s:key name="invocations"&gt;1&lt;/s:key&gt;
            &lt;/s:dict&gt;
          &lt;/s:key&gt;
          &lt;s:key name="dispatch.stream.local"&gt;
            &lt;s:dict&gt;
              &lt;s:key name="duration_secs"&gt;0.089&lt;/s:key&gt;
              &lt;s:key name="invocations"&gt;4&lt;/s:key&gt;
            &lt;/s:dict&gt;
          &lt;/s:key&gt;
          &lt;s:key name="dispatch.timeline"&gt;
            &lt;s:dict&gt;
              &lt;s:key name="duration_secs"&gt;0.359&lt;/s:key&gt;
              &lt;s:key name="invocations"&gt;5&lt;/s:key&gt;
            &lt;/s:dict&gt;
          &lt;/s:key&gt;
        &lt;/s:dict&gt;
      &lt;/s:key&gt;
      &lt;s:key name="messages"&gt;
        &lt;s:dict/&gt;
      &lt;/s:key&gt;
      &lt;s:key name="request"&gt;
        &lt;s:dict&gt;
          &lt;s:key name="id"&gt;mysearch_02151949&lt;/s:key&gt;
          &lt;s:key name="search"&gt;search index&lt;/s:key&gt;
        &lt;/s:dict&gt;
      &lt;/s:key&gt;
      &lt;s:key name="eai:acl"&gt;
        &lt;s:dict&gt;
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
          &lt;s:key name="owner"&gt;admin&lt;/s:key&gt;
          &lt;s:key name="modifiable"&gt;true&lt;/s:key&gt;
          &lt;s:key name="sharing"&gt;global&lt;/s:key&gt;
          &lt;s:key name="app"&gt;search&lt;/s:key&gt;
          &lt;s:key name="can_write"&gt;true&lt;/s:key&gt;
        &lt;/s:dict&gt;
      &lt;/s:key&gt;
      &lt;s:key name="searchProviders"&gt;
        &lt;s:list&gt;
          &lt;s:item&gt;vgenovese-mbp15.splunk.com&lt;/s:item&gt;
        &lt;/s:list&gt;
      &lt;/s:key&gt;
    &lt;/s:dict&gt;
  &lt;/content&gt;
&lt;/entry&gt;
</code></pre>

## search/jobs/{search_id}/control
{: name='searchjobssearchidcontrol'}

Executes a job control command for the search specified by {search_id}.

	[POST] search/jobs/{search_id}/control

### Parameters

action
: _Required_ **Enum** Valid values: (pause &#124; unpause &#124; finalize &#124; cancel &#124; touch &#124; setttl &#124; setpriority &#124; enablepreview &#124; disablepreview)<br/><br/>The control action to execute.<br/><br/>pause:  Suspends the execution of the current search.<br/><br/>unpause:  Resumes the execution of the current search, if paused.<br/><br/>finalize:  Stops the search, and provides intermediate results to the /results endpoint.<br/><br/>cancel:  Stops the current search and deletes the result cache.<br/><br/>touch:   Extends the expiration time of the search to now + ttl<br/><br/>setttl:  Change the ttl of the search. Arguments: ttl=&lt;number&gt;<br/><br/>setpriority:  Sets the priority of the search process. Arguments: priority=&lt;0-10&gt;<br/><br/>enablepreview:  Enable preview generation (may slow search considerably).<br/><br/>disablepreview:  Disable preview generation.

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Updated successfully. |
|--------------------------------
| **403** | Insufficient permissions to edit control action for search job. |
|--------------------------------
| **404** | Search job does not exist. |
|--------------------------------

### Example

Pauses the search specified by the search ID (<code><sid></code>) mysearch_02151949.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/search/jobs/mysearch_02151949/control \
	-d action=pause
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;response&gt;&lt;messages&gt;&lt;msg type='INFO'&gt;Search job paused.&lt;/msg&gt;&lt;/messages&gt;&lt;/response&gt;
</code></pre>

## search/jobs/{search_id}/events
{: name='searchjobssearchidevents'}

Returns the events of the search specified by {search_id}. These events are the data from the search pipeline before the first "transforming" search command. This is the primary method for a client to fetch a set of UNTRANSFORMED events for the search job.

This endpoint is only valid if the status_buckets > 0 or the search has no transforming commands.



	[GET] search/jobs/{search_id}/events

### Parameters

count
: _Optional_ **Number** The maximum number of results to return. If value is set to <code>0</code>, then all available results are returned. Default value is <code>100</code>.

earliest_time
: _Optional_ **String** A time string representing the earliest (inclusive), respectively, time bounds for the results to be returned. If not specified, the range applies to all results found.

f
: _Optional_ **String** A field to return for the event set. <br/><br/>You can pass multiple <code>POST f</code> arguments if multiple field are required. If <code>field_list</code> and <code>f</code> are provided, the union of the lists is used.

field_list
: _Optional_ **String** Deprecated. Consider using <code>f</code>.<br/><br/>A comma-separated list of the fields to return for the event set.

latest_time
: _Optional_ **String** A time string representing the latest (exclusive), respectively, time bounds for the results to be returned. If not specified, the range applies to all results found.

max_lines
: _Optional_ **Number** The maximum lines that any single event's _raw field should contain. <br/><br/>Specify <code>0</code> to specify no limit.

offset
: _Optional_ **Number** The first result (inclusive) from which to begin returning data. <br/><br/>This value is 0-indexed. Default value is 0. <br/><br/>In 4.1+, negative offsets are allowed and are added to <code>count</code> to compute the absolute offset (for example, <code>offset=-1</code> is the last available offset. Offsets in the results are always absolute and never negative.

output_mode
: _Optional_ **Enum** Valid values: (csv &#124; raw &#124; xml &#124; json)<br/><br/>Specifies what format the output should be returned in.

output_time_format
: _Optional_ **String** Formats a UTC time. Defaults to what is specified in <code>time_format</code>.

search
: _Optional_ **String** The post processing search to apply to results. Can be any valid search language string.

segmentation
: _Optional_ **String** The type of segmentation to perform on the data. This incudes an option to perform k/v segmentation.


time_format
: _Optional_ **String** Expression to convert a formatted time string from {start,end}_time into UTC seconds. <br/><br/>It defaults to %m/%d/%Y:%H:%M:%S

truncation_mode
: _Optional_ **String** Specifies how "max_lines" should be achieved.<br/><br/>Valid values are {<code>abstract</code>, <code>truncate</code>}. Default value is <code>abstract</code>.

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **204** | Search was found, but events are not yet ready.  Retry request. |
|--------------------------------
| **404** | Search job does not exist. |
|--------------------------------

### Example

Returns a set of untransformed events, listing the fields arch, build, connectionType and date_hour in the default XML format.
This example returns three sets of results. By default, this endpoint returns 100 sets of events.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/search/jobs/1312313809.20/events --get \
	-d f=arch \
	-d f=build \
	-d f=connectionType \
	-d r \
	-d count=3
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;results preview='0'&gt;
&lt;meta&gt;
&lt;fieldOrder&gt;
&lt;field&gt;arch&lt;/field&gt;
&lt;field&gt;build&lt;/field&gt;
&lt;field&gt;connectionType&lt;/field&gt;
&lt;field&gt;date_hour&lt;/field&gt;
&lt;/fieldOrder&gt;
&lt;/meta&gt;
	&lt;result offset='0'&gt;
		&lt;field k='arch'&gt;
			&lt;value&gt;&lt;text&gt;i686&lt;/text&gt;&lt;/value&gt;
		&lt;/field&gt;
		&lt;field k='build'&gt;
			&lt;value&gt;&lt;text&gt;98164&lt;/text&gt;&lt;/value&gt;
		&lt;/field&gt;
		&lt;field k='connectionType'&gt;
			&lt;value&gt;&lt;text&gt;cooked&lt;/text&gt;&lt;/value&gt;
		&lt;/field&gt;
		&lt;field k='date_hour'&gt;
			&lt;value&gt;&lt;text&gt;19&lt;/text&gt;&lt;/value&gt;
		&lt;/field&gt;
	&lt;/result&gt;
	&lt;result offset='1'&gt;
		&lt;field k='arch'&gt;
			&lt;value&gt;&lt;text&gt;i686&lt;/text&gt;&lt;/value&gt;
		&lt;/field&gt;
		&lt;field k='build'&gt;
			&lt;value&gt;&lt;text&gt;98164&lt;/text&gt;&lt;/value&gt;
		&lt;/field&gt;
		&lt;field k='connectionType'&gt;
			&lt;value&gt;&lt;text&gt;cooked&lt;/text&gt;&lt;/value&gt;
		&lt;/field&gt;
		&lt;field k='date_hour'&gt;
			&lt;value&gt;&lt;text&gt;19&lt;/text&gt;&lt;/value&gt;
		&lt;/field&gt;
	&lt;/result&gt;
	&lt;result offset='2'&gt;
		&lt;field k='arch'&gt;
			&lt;value&gt;&lt;text&gt;i686&lt;/text&gt;&lt;/value&gt;
		&lt;/field&gt;
		&lt;field k='build'&gt;
			&lt;value&gt;&lt;text&gt;98164&lt;/text&gt;&lt;/value&gt;
		&lt;/field&gt;
		&lt;field k='connectionType'&gt;
			&lt;value&gt;&lt;text&gt;cooked&lt;/text&gt;&lt;/value&gt;
		&lt;/field&gt;
		&lt;field k='date_hour'&gt;
			&lt;value&gt;&lt;text&gt;19&lt;/text&gt;&lt;/value&gt;
		&lt;/field&gt;
	&lt;/result&gt;
&lt;/results&gt;
</code></pre>

## search/jobs/{search_id}/results
{: name='searchjobssearchidresults'}

Returns the results of the search specified by {search_id}. This is the table that exists after all processing from the search pipeline has completed.

This is the primary method for a client to fetch a set of TRANSFORMED events. If the dispatched search does not include a transforming command, the effect is the same as get_events, however with fewer options.

	[GET] search/jobs/{search_id}/results

### Parameters

count
: _Optional_ **Number** The maximum number of results to return. If value is set to <code>0</code>, then all available results are returned.

f
: _Optional_ **String** A field to return for the event set. <br/><br/>You can pass multiple <code>POST f</code> arguments if multiple field are required. If <code>field_list</code> and <code>f</code> are provided the union of the lists is used.

field_list
: _Optional_ **String** Specify a comma-separated list of the fields to return for the event set.

offset
: _Optional_ **Number** The first result (inclusive) from which to begin returning data. <br/><br/>This value is 0-indexed. Default value is 0. <br/><br/>In 4.1+, negative offsets are allowed and are added to <code>count</code> to compute the absolute offset (for example, <code>offset=-1</code> is the last available offset). <br/><br/>Offsets in the results are always absolute and never negative.

output_mode
: _Optional_ **Enum** Valid values: (csv &#124; raw &#124; xml &#124; json)<br/><br/>Specifies what format the output should be returned in.

search
: _Optional_ **String** The post processing search to apply to results. Can be any valid search language string.

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **204** | Search was found, but events are not yet ready.  Retry request. |
|--------------------------------
| **404** | Search job does not exist. |
|--------------------------------

### Example

Returns a set of transformed events for the search, listing the fields index, source, and sourcetype in JSON format.
This example returns three sets of results. By default, this endpoint returns 100 sets of events.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/search/jobs/mysearch_02151949/results --get \
	-d f=index \
	-d f=source \
	-d f=sourcetype \
	-d count=3 \
	-d output_mode=json
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
[
	{
		"index": "os",
		"source": "lsof",
		"sourcetype": "lsof"
	},
	{
		"index": "os",
		"source": "lsof",
		"sourcetype": "lsof"
	},
	{
		"index": "os",
		"source": "lsof",
		"sourcetype": "lsof"
	}
]
</code></pre>

## search/jobs/{search_id}/results_preview
{: name='searchjobssearchidresultspreview'}

Returns the intermediate preview results of the search specified by {search_id}. When the job is complete, this gives the same response as /search/jobs/{search_id}/results.

This endpoint is only valid if preview is enabled. 

	[GET] search/jobs/{search_id}/results_preview

### Parameters

count
: _Optional_ **Number** The maximum number of results to return. <br/><br/>If value is set to <code>0</code>, then all available results are returned.

f
: _Optional_ **String** A field to return for the event set. <br/><br/>You can pass multiple <code>POST f</code> arguments if multiple field are required. If <code>field_list</code> and <code>f</code> are provided the union of the lists is used.

field_list
: _Optional_ **String** Specify a comma-separated list of the fields to return for the event set.

offset
: _Optional_ **Number** The first result (inclusive) from which to begin returning data. <br/><br/>This value is 0-indexed. Default value is 0. <br/><br/>In 4.1+, negative offsets are allowed and are added to <code>count</code> to compute the absolute offset (for example, <code>offset=-1</code> is the last available offset). <br/><br/>Offsets in the results are always absolute and never negative.

output_mode
: _Optional_ **String** Specifies what format the output should be returned in.<br/><br/>Valid values are:<br/><br/>  csv
  raw
  xml
  json


search
: _Optional_ **String** The post processing search to apply to results. Can be any valid search language string.

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **204** | Search was found, but events are not yet ready.  Retry request. |
|--------------------------------
| **404** | Search job does not exist. |
|--------------------------------

### Example

Returns preview results for the search, listing the fields index, source, and sourcetype in JSON format.
This example returns three sets of results. By default, this endpoint returns 100 sets of events.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/services/search/jobs/mysearch_02151949/results_preview --get \
	-d f=index \
	-d f=source \
	-d f=sourcetype \
	-d count=3 \
	-d output_mode=json
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
[
	{
		"index": "os",
		"source": "lsof",
		"sourcetype": "lsof"
	},
	{
		"index": "os",
		"source": "lsof",
		"sourcetype": "lsof"
	},
	{
		"index": "os",
		"source": "lsof",
		"sourcetype": "lsof"
	}
]
</code></pre>

## search/jobs/{search_id}/search.log
{: name='searchjobssearchidsearch.log'}

Returns the search.log for the search job specified by {search_id}.

	[GET] search/jobs/{search_id}/search.log

### Parameters

attachment
: _Optional_ **Boolean** If true, returns search.log as an attachment. Otherwise, streams search.log.

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **204** | Search was found, but events are not yet ready.  Retry request. |
|--------------------------------
| **404** | Search log does not exist. |
|--------------------------------

### Example

Returns the search log for the search specified by mysearch_02151949.
Only a few lines  of the search log are listed in the response.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/search/jobs/mysearch_02151949/search.log
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
07-07-2011 21:36:22.066 INFO  ApplicationManager - Found application directory: /Applications/splunk4.3/etc/apps/user-prefs
07-07-2011 21:36:22.066 INFO  ApplicationManager - Initialized at least 12 applications: /Applications/splunk4.3/etc/apps
07-07-2011 21:36:22.066 INFO  ApplicationManager - Found 5 application(s) that might have global exports
07-07-2011 21:36:22.073 INFO  dispatchRunner - initing LicenseMgr in search process: nonPro=0
07-07-2011 21:36:22.074 INFO  LicenseMgr - Initing LicenseMgr
07-07-2011 21:36:22.075 INFO  ServerConfig - My GUID is "1F3A34AE-75DA-4680-B184-5BF309843919".
07-07-2011 21:36:22.075 INFO  ServerConfig - My hostname is "ombroso-mbp15.local".
07-07-2011 21:36:22.076 INFO  SSLCommon - added zlib compression
07-07-2011 21:36:22.077 INFO  ServerConfig - Default output queue for file-based input: parsingQueue.
07-07-2011 21:36:22.077 INFO  LMConfig - serverName=ombroso-mbp15.splunk.com guid=1F3A34AE-75DA-4680-B184-5BF309843919 
07-07-2011 21:36:22.077 INFO  LMConfig - connection_timeout=30
07-07-2011 21:36:22.077 INFO  LMConfig - send_timeout=30
07-07-2011 21:36:22.077 INFO  LMConfig - receive_timeout=30
. . .
</code></pre>

## search/jobs/{search_id}/summary
{: name='searchjobssearchidsummary'}

Returns "getFieldsAndStats" output of the so-far-read events.

This endpoint is only valid when status_buckets > 0. To guarantee a set of fields in the summary, when creating the search, use the <code>required_fields_list</code> or <code>rf</code> parameters.

	[GET] search/jobs/{search_id}/summary

### Parameters

earliest_time
: _Optional_ **String** Time string representing the earliest (inclusive), respectively, time bounds for the search. <br/><br/>The time string can be either a UTC time (with fractional seconds), a relative time specifier (to now) or a formatted time string. (Also see comment for the search_mode variable.)

f
: _Optional_ **String** A field to return for the event set.<br/><br/>You can pass multiple <code>POST f</code> arguments if multiple field are required. If <code>field_list</code> and <code>f</code> are provided, the union of the lists is used.

field_list
: _Optional_ **String** Deprecated. Consider using <code>f</code>.<br/><br/>A comma-separated list of the fields to return for the event set.

latest_time
: _Optional_ **String** Time string representing the latest (exclusive), respectively, time bounds for the search. <br/><br/>The time string can be either a UTC time (with fractional seconds), a relative time specifier (to now) or a formatted time string. (Also see comment for the search_mode variable.) 

min_freq
: _Optional_ **Number** For each key, the fraction of results this key must occur in to be displayed.<br/><br/>Express the fraction as a number between 0 and 1.

output_time_format
: _Optional_ **String** Formats a UTC time. Defaults to what is specified in <code>time_format</code>.

search
: _Optional_ **String** Specifies a substring that all returned events should contain either in one of their values or tags.

time_format
: _Optional_ **String** Expression to convert a formatted time string from {start,end}_time into UTC seconds.
It defaults to %m/%d/%Y:%H:%M:%S

top_count
: _Optional_ **Number** For each key, specfies how many of the most frequent items to return.

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **403** | Insufficient permissions to view summary for search job. |
|--------------------------------
| **404** | Summary for search job does not exist. |
|--------------------------------

### Example

Returns the field summary information that is usually used to populate the fields picker in the default search view.  This examples returns the summary in XML format for only the fields source, sourcetype, and host.  For each field, also return the 5 most common values for the field.  The summary information is over the entire timerange of the search.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/search/jobs/mytestsid/summary --get \
	-d f=source \
	-d f=sourcetype \
	-d f=host \
	-d top_count=5
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;?xml version='1.0' encoding='UTF-8'?&gt;
&lt;summary earliest_time='1969-12-31T16:00:00.000-08:00' latest_time='1969-12-31T16:00:00.464-08:00' duration='0' c='150375'&gt;
	&lt;field k='host' c='150375' nc='0' dc='1' exact='1'&gt;
		&lt;modes&gt;
			&lt;value c='150375' exact='1'&gt;&lt;text&gt;tiny&lt;/text&gt;&lt;/value&gt;		&lt;/modes&gt;
	&lt;/field&gt;
	&lt;field k='source' c='150375' nc='0' dc='13' exact='1'&gt;
		&lt;modes&gt;
			&lt;value c='136107' exact='1'&gt;&lt;text&gt;/mnt/scsi/steveyz/splunksi/var/log/splunk/metrics.log&lt;/text&gt;&lt;/value&gt;			&lt;value c='6682' exact='1'&gt;&lt;text&gt;/mnt/scsi/steveyz/splunksi/var/log/splunk/splunkd_access.log&lt;/text&gt;&lt;/value&gt;			&lt;value c='4656' exact='1'&gt;&lt;text&gt;/mnt/scsi/steveyz/splunksi/var/log/splunk/scheduler.log&lt;/text&gt;&lt;/value&gt;			&lt;value c='1714' exact='1'&gt;&lt;text&gt;/mnt/scsi/steveyz/splunksi/var/log/splunk/web_access.log&lt;/text&gt;&lt;/value&gt;			&lt;value c='937' exact='1'&gt;&lt;text&gt;/mnt/scsi/steveyz/splunksi/var/log/splunk/splunkd.log&lt;/text&gt;&lt;/value&gt;		&lt;/modes&gt;
	&lt;/field&gt;
	&lt;field k='sourcetype' c='150375' nc='0' dc='10' exact='1'&gt;
		&lt;modes&gt;
			&lt;value c='137053' exact='1'&gt;&lt;text&gt;splunkd&lt;/text&gt;&lt;/value&gt;			&lt;value c='6682' exact='1'&gt;&lt;text&gt;splunkd_access&lt;/text&gt;&lt;/value&gt;			&lt;value c='4656' exact='1'&gt;&lt;text&gt;scheduler&lt;/text&gt;&lt;/value&gt;			&lt;value c='1714' exact='1'&gt;&lt;text&gt;splunk_web_access&lt;/text&gt;&lt;/value&gt;			&lt;value c='193' exact='1'&gt;&lt;text&gt;splunk_web_service&lt;/text&gt;&lt;/value&gt;		&lt;/modes&gt;
	&lt;/field&gt;
&lt;/summary&gt;
</code></pre>

## search/jobs/{search_id}/timeline
{: name='searchjobssearchidtimeline'}

Returns event distribution over time of the so-far-read untransformed events.

This endpoint is only valid when status_buckets > 0. To guarantee a set of fields in the summary, when creating the search, use the <code>required_fields_list</code> or <code>rf</code> parameters.

	[GET] search/jobs/{search_id}/timeline

### Parameters

output_time_format
: _Optional_ **String** Formats a UTC time. Defaults to what is specified in <code>time_format</code>.

time_format
: _Optional_ **String** Expression to convert a formatted time string from {start,end}_time into UTC seconds. <br/><br/>It defaults to %m/%d/%Y:%H:%M:%S

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **204** | Search was found, but events are not yet ready.  Retry request. |
|--------------------------------
| **404** | Timeline for search job does not exist. |
|--------------------------------

### Example

Get the information usually used to populate the timeline, which is basically just a breakdown of the event distribution over time.  Render times using the splunk server's locale time format

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/search/jobs/mytestsid/timeline --get \
	-d time_format="%c"
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;timeline c='150397' cursor='1312308000'&gt;
&lt;bucket c='7741' a='7741' t='1312308000.000' d='3600' f='1' etz='-25200' ltz='-25200'&gt;Tue Aug  2 11:00:00 2011&lt;/bucket&gt;
&lt;bucket c='7894' a='7894' t='1312311600.000' d='3600' f='1' etz='-25200' ltz='-25200'&gt;Tue Aug  2 12:00:00 2011&lt;/bucket&gt;
&lt;bucket c='7406' a='7406' t='1312315200.000' d='3600' f='1' etz='-25200' ltz='-25200'&gt;Tue Aug  2 13:00:00 2011&lt;/bucket&gt;
&lt;bucket c='6097' a='6097' t='1312318800.000' d='3600' f='1' etz='-25200' ltz='-25200'&gt;Tue Aug  2 14:00:00 2011&lt;/bucket&gt;
&lt;bucket c='6072' a='6072' t='1312322400.000' d='3600' f='1' etz='-25200' ltz='-25200'&gt;Tue Aug  2 15:00:00 2011&lt;/bucket&gt;
&lt;bucket c='6002' a='6002' t='1312326000.000' d='3600' f='1' etz='-25200' ltz='-25200'&gt;Tue Aug  2 16:00:00 2011&lt;/bucket&gt;
&lt;bucket c='6004' a='6004' t='1312329600.000' d='3600' f='1' etz='-25200' ltz='-25200'&gt;Tue Aug  2 17:00:00 2011&lt;/bucket&gt;
&lt;bucket c='5994' a='5994' t='1312333200.000' d='3600' f='1' etz='-25200' ltz='-25200'&gt;Tue Aug  2 18:00:00 2011&lt;/bucket&gt;
&lt;bucket c='6037' a='6037' t='1312336800.000' d='3600' f='1' etz='-25200' ltz='-25200'&gt;Tue Aug  2 19:00:00 2011&lt;/bucket&gt;
&lt;bucket c='6021' a='6021' t='1312340400.000' d='3600' f='1' etz='-25200' ltz='-25200'&gt;Tue Aug  2 20:00:00 2011&lt;/bucket&gt;
&lt;bucket c='6051' a='6051' t='1312344000.000' d='3600' f='1' etz='-25200' ltz='-25200'&gt;Tue Aug  2 21:00:00 2011&lt;/bucket&gt;
&lt;bucket c='6006' a='6006' t='1312347600.000' d='3600' f='1' etz='-25200' ltz='-25200'&gt;Tue Aug  2 22:00:00 2011&lt;/bucket&gt;
&lt;bucket c='6041' a='6041' t='1312351200.000' d='3600' f='1' etz='-25200' ltz='-25200'&gt;Tue Aug  2 23:00:00 2011&lt;/bucket&gt;
&lt;bucket c='5993' a='5993' t='1312354800.000' d='3600' f='1' etz='-25200' ltz='-25200'&gt;Wed Aug  3 00:00:00 2011&lt;/bucket&gt;
&lt;bucket c='6040' a='6040' t='1312358400.000' d='3600' f='1' etz='-25200' ltz='-25200'&gt;Wed Aug  3 01:00:00 2011&lt;/bucket&gt;
&lt;bucket c='5993' a='5993' t='1312362000.000' d='3600' f='1' etz='-25200' ltz='-25200'&gt;Wed Aug  3 02:00:00 2011&lt;/bucket&gt;
&lt;bucket c='6061' a='6061' t='1312365600.000' d='3600' f='1' etz='-25200' ltz='-25200'&gt;Wed Aug  3 03:00:00 2011&lt;/bucket&gt;
&lt;bucket c='5995' a='5995' t='1312369200.000' d='3600' f='1' etz='-25200' ltz='-25200'&gt;Wed Aug  3 04:00:00 2011&lt;/bucket&gt;
&lt;bucket c='5988' a='5988' t='1312372800.000' d='3600' f='1' etz='-25200' ltz='-25200'&gt;Wed Aug  3 05:00:00 2011&lt;/bucket&gt;
&lt;bucket c='6042' a='6042' t='1312376400.000' d='3600' f='1' etz='-25200' ltz='-25200'&gt;Wed Aug  3 06:00:00 2011&lt;/bucket&gt;
&lt;bucket c='5998' a='5998' t='1312380000.000' d='3600' f='1' etz='-25200' ltz='-25200'&gt;Wed Aug  3 07:00:00 2011&lt;/bucket&gt;
&lt;bucket c='6055' a='6055' t='1312383600.000' d='3600' f='1' etz='-25200' ltz='-25200'&gt;Wed Aug  3 08:00:00 2011&lt;/bucket&gt;
&lt;bucket c='5997' a='5997' t='1312387200.000' d='3600' f='1' etz='-25200' ltz='-25200'&gt;Wed Aug  3 09:00:00 2011&lt;/bucket&gt;
&lt;bucket c='5994' a='5994' t='1312390800.000' d='3600' f='1' etz='-25200' ltz='-25200'&gt;Wed Aug  3 10:00:00 2011&lt;/bucket&gt;
&lt;bucket c='875' a='875' t='1312394400.000' d='3600' f='1' etz='-25200' ltz='-25200'&gt;Wed Aug  3 11:00:00 2011&lt;/bucket&gt;
&lt;/timeline&gt;
</code></pre>

## search/parser
{: name='searchparser'}

Parses Splunk search language and returns semantic map.

	[GET] search/parser

### Parameters

enable_lookups
: _Optional_ **Boolean** If <code>true</code>, reverse lookups are done to expand the search expression.

output_mode
: _Optional_ **String** Specify output formatting. Select from either:<br/><br/>  xml:  XML formatting
  json: JSON formatting


parse_only
: _Optional_ **Boolean** If true, disables expansion of search due evaluation of subsearches, time term expansion, lookups, tags, eventtypes, sourcetype alias.

q
: _Required_ **String** The search string to parse.

reload_macros
: _Optional_ **Boolean** If true, reload macro definitions from macros.conf.


### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------

### Example

Returns the semantic map for the specified search string in JSON format.
In the q parameter, the search operator, search, is prefixed to the search string.
For this example, --get prevents the operation from being interpreted as a POST operation.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/search/parser --get \
	-d output_mode=json \
	-d q="search index=os sourcetype=cpu"
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
{
	"remoteSearch": "litsearch  | fields  keepcolorder=t \"host\" \"index\" \"linecount\" \"source\" \"sourcetype\" \"splunk_server\"",
	"remoteTimeOrdered": true,
	"eventsSearch": "search ",
	"eventsTimeOrdered": true,
	"eventsStreaming": true,
	"reportsSearch": "",
	"commands": [
		{
			"command": "search",
			"rawargs": "",
			"pipeline": "streaming",
			"args": {
				"search": [""],
			}
			"isGenerating": true,
			"streamType": "SP_STREAM",
		},
	]
}
</code></pre>

## search/timeparser
{: name='searchtimeparser'}

Returns a lookup table of time arguments to absolute timestamps.

	[GET] search/timeparser

### Parameters

now
: _Optional_ **String** The time to use as current time for relative time identifiers. <br/><br/>Can itself either be a relative time (from the real "now" time) or an absolute time in the format specified by <code>time_format</code>.


output_time_format
: _Optional_ **String** Used to format a UTC time. Defaults to the value of <code>time_format</code>.

time
: _Required_ **String** The time argument to parse. <br/><br/>Acceptable inputs are either a relative time identifier or an absolute time. Multiple time arguments can be passed by specifying multiple time parameters.


time_format
: _Optional_ **String** The format (<code>strftime</code>) of the absolute time format passed in time. <br/><br/>This field is not used if a relative time identifier is provided. For absolute times, the default value is the ISO-8601 format.


### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **204** | No timeparser arguments given. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------

### Example

Returns a lookup table of absolute timestamps for the supplied time parameters.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/search/timeparser --get \
	-d time=-12h \
	-d time=-24h
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;response&gt;
	&lt;dict&gt;
		&lt;key name="-12h"&gt;2011-07-06T21:54:23.000-07:00&lt;/key&gt;
		&lt;key name="-24h"&gt;2011-07-06T09:54:23.000-07:00&lt;/key&gt;
	&lt;/dict&gt;
&lt;/response&gt;
</code></pre>

## search/typeahead
{: name='searchtypeahead'}

Returns a list of words or descriptions for possible auto-complete terms.

count is a required parameter to specify how many descriptions to list. prefix is a required parameter to specify a string for terms in your index.

	[GET] search/typeahead

### Parameters

count
: _Required_ **Number** The number of counts to return for this term.

output_mode
: _Optional_ **String** Format for the output. Select from either:<br/><br/>  xml:  XML format
  json:  JSON format


prefix
: _Required_ **String** The term for which to return typeahead results.

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **204** | No Content. The server successfully processed the request, but is not returning any content. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **403** | Insufficient permissions to view typeahead results. |
|--------------------------------
| **405** | Invalid method (only GET is supported). |
|--------------------------------

### Example

Returns 3 typeahead terms for the string "source," displaying the results in JSON format.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/search/typeahead --get \
	-d count=3 \
	-d prefix=source \
	-d output_mode=json
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
[
	{
		"content": "source=\"cpu\"",
		"count": "181",
		"operator": "false"
	},
	{
		"content": "source=\"df\"",
		"count": "19",
		"operator": "false"
	},
	{
		"content": "source=\"hardware\"",
		"count": "1",
		"operator": "false"
	}
]
</code></pre>


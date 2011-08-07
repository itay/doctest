<a name='dataoutputstcpdefault'/>

## data/outputs/tcp/default

Returns the current tcpout properties.

	[GET] data/outputs/tcp/default

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
| **403** | Insufficient permissions to view outputs. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Retrieves the default TCP output settings.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/data/outputs/tcp/default
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;tcpout-default&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/data/outputs/tcp/default&lt;/id&gt;
  &lt;updated&gt;2011-07-10T22:38:23-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/data/outputs/tcp/default/_new" rel="create"/&gt;
  &lt;link href="/services/data/outputs/tcp/default/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;tcpout&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/data/outputs/tcp/default/tcpout&lt;/id&gt;
    &lt;updated&gt;2011-07-10T22:38:23-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/data/outputs/tcp/default/tcpout" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/data/outputs/tcp/default/tcpout" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/outputs/tcp/default/tcpout/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/outputs/tcp/default/tcpout" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/outputs/tcp/default/tcpout" rel="remove"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/outputs/tcp/default/tcpout/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="autoLB"&gt;1&lt;/s:key&gt;
        &lt;s:key name="defaultGroup"&gt;spacecake_9998&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="forwardedindex.0.whitelist"&gt;.*&lt;/s:key&gt;
        &lt;s:key name="forwardedindex.1.blacklist"&gt;_.*&lt;/s:key&gt;
        &lt;s:key name="forwardedindex.2.whitelist"&gt;_audit&lt;/s:key&gt;
        &lt;s:key name="forwardedindex.filter.disable"&gt;0&lt;/s:key&gt;
        &lt;s:key name="indexAndForward"&gt;0&lt;/s:key&gt;
        &lt;s:key name="maxQueueSize"&gt;500KB&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/outputs/tcp/default

Configures global tcpout properties.

	[POST] data/outputs/tcp/default

### Parameters

blockOnQueueFull
: _Optional_ **Boolean** If disabled, data destined for forwarders will be thrown away if no forwarders in the group are reachable.

defaultGroup
: _Optional_ **String** Comma-separated list of one or more target group names, specified later in [tcpout:<target_group>] stanzas of outputs.conf.spec file.<br/><br/>The forwarder sends all data to the specified groups. If you don't want to forward data automatically, don't set this attribute. Can be overridden by an inputs.conf _TCP_ROUTING setting, which in turn can be overridden by a props.conf/transforms.conf modifier.<br/><br/>Starting with 4.2, this attribute is no longer required.

disabled
: _Optional_ **Boolean** Disables default tcpout settings

dropEventsOnQueueFull
: _Optional_ **Number** If set to a positive number, wait the specified number of seconds before throwing out all new events until the output queue has space. Defaults to -1 (do not drop events).<br/><br/>CAUTION: Do not set this value to a positive integer if you are monitoring files.<br/><br/>Setting this to -1 or 0 causes the output queue to block when it gets full, whih causes further blocking up the processing chain. If any target group's queue is blocked, no more data reaches any other target group.<br/><br/>Using auto load-balancing is the best way to minimize this condition, because, in that case, multiple receivers must be down (or jammed up) before queue blocking can occur.

heartbeatFrequency
: _Optional_ **Number** How often (in seconds) to send a heartbeat packet to the receiving server.<br/><br/>Heartbeats are only sent if sendCookedData=true. Defaults to 30 seconds.

indexAndForward
: _Optional_ **Boolean** Specifies whether to index all data locally, in addition to forwarding it. Defaults to false.<br/><br/>This is known as an "index-and-forward" configuration. This attribute is only available for heavy forwarders. It is available only at the top level [tcpout] stanza in outputs.conf. It cannot be overridden in a target group.

maxQueueSize
: _Optional_ **Number** Specify an integer or integer[KB|MB|GB].<br/><br/>Sets the maximum size of the forwarder's output queue. It also sets the maximum size of the wait queue to 3x this value, if you have enabled indexer acknowledgment (useACK=true).<br/><br/>Although the wait queue and the output queues are both configured by this attribute, they are separate queues. The setting determines the maximum size of the queue's in-memory (RAM) buffer.<br/><br/>For heavy forwarders sending parsed data, maxQueueSize is the maximum number of events. Since events are typically much shorter than data blocks, the memory consumed by the queue on a parsing forwarder will likely be much smaller than on a non-parsing forwarder, if you use this version of the setting.<br/><br/>If specified as a lone integer (for example, maxQueueSize=100), maxQueueSize indicates the maximum number of queued events (for parsed data) or blocks of data (for unparsed data). A block of data is approximately 64KB. For non-parsing forwarders, such as universal forwarders, that send unparsed data, maxQueueSize is the maximum number of data blocks.<br/><br/>If specified as an integer followed by KB, MB, or GB (for example, maxQueueSize=100MB), maxQueueSize indicates the maximum RAM allocated to the queue buffer. Defaults to 500KB (which means a maximum size of 500KB for the output queue and 1500KB for the wait queue, if any).

name
: _Required_ **String** Configuration to be edited.  The only valid value is "tcpout".

sendCookedData
: _Optional_ **Boolean** If true, events are cooked (have been processed by Splunk). If false, events are raw and untouched prior to sending. Defaults to true.<br/><br/>Set to false if you are sending to a third-party system.

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
| **403** | Insufficient permissions to create output. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Can be used to edit default forwarding settings just as with POSTing to data/outputs/tcp/default/{name}.  Note that this action does not create a new entry, and that "tcpout" is the only valid name to specify here.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/data/outputs/tcp/default/tcpout \
	-d 'defaultGroup=west_coast_indexers'
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>

</code></pre>

<a name='dataoutputstcpdefaultname'/>

## data/outputs/tcp/default/{name}

Disable the default forwarding settings.

	[DELETE] data/outputs/tcp/default/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deleted successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to disable forwarding settings. |
|--------------------------------
| **404** | Forwarding settings do not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Disables the default forwarding settings stanza.  Note that "tcpout" is the only valid name here.

#### Request
<pre class='terminal'>
curl -k -u admin:pass --request DELETE \
	https://localhost:8089/services/data/outputs/tcp/default/tcpout
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:s="http://dev.splunk.com/ns/rest"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;tcpout-default&lt;/title&gt;
  &lt;id&gt;https://localhost:8085/services/data/outputs/tcp/default&lt;/id&gt;
  &lt;updated&gt;2011-07-19T20:09:02-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/data/outputs/tcp/default/_new" rel="create"/&gt;
  &lt;link href="/services/data/outputs/tcp/default/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## data/outputs/tcp/default/{name}

Retrieve the named configuration.  The only valid name here is "tcpout".

	[GET] data/outputs/tcp/default/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view forwaring settings. |
|--------------------------------
| **404** | Forwarding settings do not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Retrieves the default forwarding settings.  This is identical to retrieving data/outputs/tcp/default.  Note that "tcpout" is the only valid name to retrieve at this endpoint.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/data/outputs/tcp/default/tcpout
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>

</code></pre>

## data/outputs/tcp/default/{name}

Configure global forwarding properties.

	[POST] data/outputs/tcp/default/{name}

### Parameters

blockOnQueueFull
: _Optional_ **INHERITED** INHERITED

defaultGroup
: _Optional_ **INHERITED** INHERITED

disabled
: _Optional_ **INHERITED** INHERITED

dropEventsOnQueueFull
: _Optional_ **INHERITED** INHERITED

heartbeatFrequency
: _Optional_ **INHERITED** INHERITED

indexAndForward
: _Optional_ **INHERITED** INHERITED

maxQueueSize
: _Optional_ **INHERITED** INHERITED

sendCookedData
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
| **403** | Insufficient permissions to edit forwarding settings. |
|--------------------------------
| **404** | Forwarding settings do not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Increases the default heartbeat frequency to 60 seconds.  Note that "tcpout" is the only valid name to edit at this endpoint.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/data/outputs/tcp/default/tcpout \
	-d heartbeatFrequency=60
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;tcpout-default&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/data/outputs/tcp/default&lt;/id&gt;
  &lt;updated&gt;2011-07-10T22:43:53-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/data/outputs/tcp/default/_new" rel="create"/&gt;
  &lt;link href="/services/data/outputs/tcp/default/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

<a name='dataoutputstcpgroup'/>

## data/outputs/tcp/group

Returns configuration information about target groups. 

	[GET] data/outputs/tcp/group

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
| **403** | Insufficient permissions to view group. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Display the list of output groups configured to send data via Splunk's cooked format.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/data/outputs/tcp/group
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;tcpout-group&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/data/outputs/tcp/group&lt;/id&gt;
  &lt;updated&gt;2011-07-10T22:21:07-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/data/outputs/tcp/group/_new" rel="create"/&gt;
  &lt;link href="/services/data/outputs/tcp/group/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;spacecake_9998&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/data/outputs/tcp/group/spacecake_9998&lt;/id&gt;
    &lt;updated&gt;2011-07-10T22:21:07-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/data/outputs/tcp/group/spacecake_9998" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/data/outputs/tcp/group/spacecake_9998" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/outputs/tcp/group/spacecake_9998/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/outputs/tcp/group/spacecake_9998" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/outputs/tcp/group/spacecake_9998" rel="remove"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="method"&gt;autobalance&lt;/s:key&gt;
        &lt;s:key name="servers"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;spacecake:9998&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/outputs/tcp/group

Configures a group of one or more data forwarding destinations.

	[POST] data/outputs/tcp/group

### Parameters

autoLB
: _Optional_ **Boolean** If set to true, forwarder performs automatic load balancing. In automatic mode, the forwarder selects a new indexer every autoLBFrequency seconds. If the connection to the current indexer is lost, the forwarder selects a new live indexer to forward data to.<br/><br/>Do not alter the default setting, unless you have some overriding need to use round-robin load balancing. Round-robin load balancing (autoLB=false) was previously the default load balancing method. Starting with release 4.2, however, round-robin load balancing has been deprecated, and the default has been changed to automatic load balancing (autoLB=true).

blockOnQueueFull
: _Optional_ **Boolean** If disabled, data destined for forwarders will be thrown away if no forwarders in the group are reachable.

compressed
: _Optional_ **Boolean** If true, forwarder sends compressed data.<br/><br/>If set to true, the receiver port must also have compression turned on.

disabled
: _Optional_ **Boolean** If true, disables the group.

dropEventsOnQueueFull
: _Optional_ **Number** If set to a positive number, wait the specified number of seconds before throwing out all new events until the output queue has space. Defaults to -1 (do not drop events).<br/><br/>CAUTION: Do not set this value to a positive integer if you are monitoring files.<br/><br/>Setting this to -1 or 0 causes the output queue to block when it gets full, which causes further blocking up the processing chain. If any target group's queue is blocked, no more data reaches any other target group.<br/><br/>Using auto load-balancing is the best way to minimize this condition, because, in that case, multiple receivers must be down (or jammed up) before queue blocking can occur.

heartbeatFrequency
: _Optional_ **Number** How often (in seconds) to send a heartbeat packet to the group.<br/><br/>Heartbeats are only sent if sendCookedData=true. Defaults to 30 seconds.

maxQueueSize
: _Optional_ **Number** Specify either an integer or integer[KB&#124;MB&#124;GB].<br/><br/>Sets the maximum size of the forwarder's output queue. It also sets the maximum size of the wait queue to 3x this value, if you have enabled indexer acknowledgment (useACK=true).<br/><br/>Although the wait queue and the output queues are both configured by this attribute, they are separate queues. The setting determines the maximum size of the queue's in-memory (RAM) buffer.<br/><br/>For heavy forwarders sending parsed data, maxQueueSize is the maximum number of events. Since events are typically much shorter than data blocks, the memory consumed by the queue on a parsing forwarder will likely be much smaller than on a non-parsing forwarder, if you use this version of the setting.<br/><br/>If specified as a lone integer (for example, maxQueueSize=100), maxQueueSize indicates the maximum number of queued events (for parsed data) or blocks of data (for unparsed data). A block of data is approximately 64KB. For non-parsing forwarders, such as universal forwarders, that send unparsed data, maxQueueSize is the maximum number of data blocks.<br/><br/>If specified as an integer followed by KB, MB, or GB (for example, maxQueueSize=100MB), maxQueueSize indicates the maximum RAM allocated to the queue buffer. Defaults to 500KB (which means a maximum size of 500KB for the output queue and 1500KB for the wait queue, if any).

method
: _Optional_ **Enum** Valid values: (tcpout &#124; syslog &#124; httpout)<br/><br/>Specifies the type of output processor.

name
: _Required_ **String** The name of the group of receivers.

sendCookedData
: _Optional_ **Boolean** If true, send cooked events (events that have been processed by Splunk).<br/><br/>If false, events are raw and untouched prior to sending. Set to false if you are sending to a third-party system.<br/><br/>Defaults to true.

servers
: _Required_ **String** Comma-separated list of servers to include in the group.

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
| **403** | Insufficient permissions to create group. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Creates an auto-load balanced forwarding configuration consisting of two Splunk receivers.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/data/outputs/tcp/group \
	-d name=lan_receivers \
	-d method=autobalance \
	-d servers=10.3.3.3:9997,10.4.4.4:9997
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;tcpout-group&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/data/outputs/tcp/group&lt;/id&gt;
  &lt;updated&gt;2011-07-10T22:21:23-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/data/outputs/tcp/group/_new" rel="create"/&gt;
  &lt;link href="/services/data/outputs/tcp/group/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

<a name='dataoutputstcpgroupname'/>

## data/outputs/tcp/group/{name}

Deletes the target group specified by {name}.

	[DELETE] data/outputs/tcp/group/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deleted successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to delete group. |
|--------------------------------
| **404** | Group does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Removes the lan_receivers forwarding configuration.

#### Request
<pre class='terminal'>
curl -k -u admin:pass --request DELETE \
	https://localhost:8089/services/data/outputs/tcp/group/lan_receivers
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;tcpout-group&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/data/outputs/tcp/group&lt;/id&gt;
  &lt;updated&gt;2011-07-10T22:32:47-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/data/outputs/tcp/group/_new" rel="create"/&gt;
  &lt;link href="/services/data/outputs/tcp/group/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## data/outputs/tcp/group/{name}

Returns configuration information about the target group specified by {name}.

	[GET] data/outputs/tcp/group/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view group. |
|--------------------------------
| **404** | Group does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Displays the configuration for the newly created forwarder configuration.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/data/outputs/tcp/group/lan_receivers
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;tcpout-group&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/data/outputs/tcp/group&lt;/id&gt;
  &lt;updated&gt;2011-07-10T22:23:10-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/data/outputs/tcp/group/_new" rel="create"/&gt;
  &lt;link href="/services/data/outputs/tcp/group/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;lan_receivers&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/data/outputs/tcp/group/lan_receivers&lt;/id&gt;
    &lt;updated&gt;2011-07-10T22:23:10-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/data/outputs/tcp/group/lan_receivers" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/data/outputs/tcp/group/lan_receivers" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/outputs/tcp/group/lan_receivers/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/outputs/tcp/group/lan_receivers" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/outputs/tcp/group/lan_receivers" rel="remove"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="autoLB"&gt;1&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:attributes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="optionalFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;autoLB&lt;/s:item&gt;
                &lt;s:item&gt;blockOnQueueFull&lt;/s:item&gt;
                &lt;s:item&gt;compressed&lt;/s:item&gt;
                &lt;s:item&gt;disabled&lt;/s:item&gt;
                &lt;s:item&gt;dropEventsOnQueueFull&lt;/s:item&gt;
                &lt;s:item&gt;heartbeatFrequency&lt;/s:item&gt;
                &lt;s:item&gt;maxPersistentQueueSizeInMegs&lt;/s:item&gt;
                &lt;s:item&gt;maxQueueSize&lt;/s:item&gt;
                &lt;s:item&gt;method&lt;/s:item&gt;
                &lt;s:item&gt;persistentQueuePath&lt;/s:item&gt;
                &lt;s:item&gt;sendCookedData&lt;/s:item&gt;
                &lt;s:item&gt;usePersistentQueue&lt;/s:item&gt;
              &lt;/s:list&gt;
            &lt;/s:key&gt;
            &lt;s:key name="requiredFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;servers&lt;/s:item&gt;
              &lt;/s:list&gt;
            &lt;/s:key&gt;
            &lt;s:key name="wildcardFields"&gt;
              &lt;s:list/&gt;
            &lt;/s:key&gt;
          &lt;/s:dict&gt;
        &lt;/s:key&gt;
        &lt;s:key name="method"&gt;autobalance&lt;/s:key&gt;
        &lt;s:key name="servers"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;10.3.3.3:9997&lt;/s:item&gt;
            &lt;s:item&gt;10.4.4.4:9997&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/outputs/tcp/group/{name}

Updates the configuration of the target group.

	[POST] data/outputs/tcp/group/{name}

### Parameters

autoLB
: _Optional_ **INHERITED** INHERITED

blockOnQueueFull
: _Optional_ **INHERITED** INHERITED

compressed
: _Optional_ **INHERITED** INHERITED

disabled
: _Optional_ **INHERITED** INHERITED

dropEventsOnQueueFull
: _Optional_ **INHERITED** INHERITED

heartbeatFrequency
: _Optional_ **INHERITED** INHERITED

maxQueueSize
: _Optional_ **INHERITED** INHERITED

method
: _Optional_ **INHERITED** INHERITED

sendCookedData
: _Optional_ **INHERITED** INHERITED

servers
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
| **403** | Insufficient permissions to edit group. |
|--------------------------------
| **404** | Group does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Sets the memory buffer for the new forwarding group to 1 megabyte.  Note that the servers must be re-specified in this edit.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/data/outputs/tcp/group/lan_receivers \
	-d maxQueueSize=1024KB \
	-d servers=10.3.3.3:9997,10.4.4.4:9997
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;tcpout-group&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/data/outputs/tcp/group&lt;/id&gt;
  &lt;updated&gt;2011-07-10T22:26:02-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/data/outputs/tcp/group/_new" rel="create"/&gt;
  &lt;link href="/services/data/outputs/tcp/group/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

<a name='dataoutputstcpserver'/>

## data/outputs/tcp/server

Lists existing forwarded servers.

	[GET] data/outputs/tcp/server

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
| **403** | Insufficient permissions to view forwarded servers. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Retrieves the list of forwarding targets that have been defined.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/data/outputs/tcp/server
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;tcpout-server&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/data/outputs/tcp/server&lt;/id&gt;
  &lt;updated&gt;2011-07-10T21:34:59-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/data/outputs/tcp/server/_new" rel="create"/&gt;
  &lt;link href="/services/data/outputs/tcp/server/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;spacecake:9998&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/data/outputs/tcp/server/spacecake%3A9998&lt;/id&gt;
    &lt;updated&gt;2011-07-10T21:34:59-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/data/outputs/tcp/server/spacecake%3A9998" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/data/outputs/tcp/server/spacecake%3A9998" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/outputs/tcp/server/spacecake%3A9998/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/outputs/tcp/server/spacecake%3A9998" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/outputs/tcp/server/spacecake%3A9998" rel="remove"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/outputs/tcp/server/spacecake%3A9998/allconnections" rel="allconnections"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/outputs/tcp/server/spacecake%3A9998/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="destHost"&gt;spacecake.splunk.com&lt;/s:key&gt;
        &lt;s:key name="destIp"&gt;10.1.1.73&lt;/s:key&gt;
        &lt;s:key name="destPort"&gt;9998&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="method"&gt;autobalance&lt;/s:key&gt;
        &lt;s:key name="sourcePort"&gt;8085&lt;/s:key&gt;
        &lt;s:key name="status"&gt;connect_fail&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/outputs/tcp/server

Creates a new forwarder output.

	[POST] data/outputs/tcp/server

### Parameters

backoffAtStartup
: _Optional_ **Number** Sets in seconds how long to wait to retry the first time a retry is needed. Compare to initialBackoff.

disabled
: _Optional_ **Boolean** If true, disables the forwarder.

initialBackoff
: _Optional_ **Number** Sets how long, in seconds, to wait to retry every time after the first retry. Compare to backoffAtStartup.

maxBackoff
: _Optional_ **Number** Specifies the number of times in seconds before reaching the maximum backoff frequency.

maxNumberOfRetriesAtHighestBackoff
: _Optional_ **Number** Specifies the number of times the system should retry after reaching the highest back-off period, before stopping completely. -1 (default value) means to try forever.<br/><br/>Caution: Splunk recommends that you not change this from the default, or the forwarder will completely stop forwarding to a downed URI at some point.


method
: _Optional_ **Enum** Valid values: (clone &#124; balance &#124; autobalance)<br/><br/>The data distribution method used when two or more servers exist in the same forwarder group.  

name
: _Required_ **String** <host>:<port> of the Splunk receiver. <host> can be either an ip address or server name. <port> is the that port that the Splunk receiver is listening on.

sslAltNameToCheck
: _Optional_ **String** The alternate name to match in the remote server's SSL certificate.

sslCertPath
: _Optional_ **String** Path to the client certificate. If specified, connection uses SSL.

sslCipher
: _Optional_ **String** SSL Cipher in the form ALL:!aNULL:!eNULL:!LOW:!EXP:RC4+RSA:+HIGH:+MEDIUM

sslCommonNameToCheck
: _Optional_ **String** Check the common name of the server's certificate against this name.<br/><br/>If there is no match, assume that Splunk is not authenticated against this server. You must specify this setting if sslVerifyServerCert is true.

sslPassword
: _Optional_ **String** The password associated with the CAcert.<br/><br/>The default Splunk CAcert uses the password "password."

sslRootCAPath
: _Optional_ **String** The path to the root certificate authority file (optional).

sslVerifyServerCert
: _Optional_ **Boolean**  If true, make sure that the server you are connecting to is a valid one (authenticated). Both the common name and the alternate name of the server are then checked for a match.

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
| **403** | Insufficient permissions to create a forwarded server. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Creates a new data output directing data to port 9997 on the host "tiny".

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/data/outputs/tcp/server \
	-d name=tiny:9997
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;tcpout-server&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/data/outputs/tcp/server&lt;/id&gt;
  &lt;updated&gt;2011-07-10T21:35:13-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/data/outputs/tcp/server/_new" rel="create"/&gt;
  &lt;link href="/services/data/outputs/tcp/server/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

<a name='dataoutputstcpservername'/>

## data/outputs/tcp/server/{name}

Deletes the configuration for the forwarded server specified by {name}.

	[DELETE] data/outputs/tcp/server/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deleted successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to delete forwarded server configuration. |
|--------------------------------
| **404** | Forwarded server does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Remove the configuration forwarding data to host tiny's port 9997.

#### Request
<pre class='terminal'>
curl -k -u admin:pass --request DELETE \
	https://localhost:8089/services/data/outputs/tcp/server/tiny:9997
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;tcpout-server&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/data/outputs/tcp/server&lt;/id&gt;
  &lt;updated&gt;2011-07-10T21:35:41-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/data/outputs/tcp/server/_new" rel="create"/&gt;
  &lt;link href="/services/data/outputs/tcp/server/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## data/outputs/tcp/server/{name}

Lists information aobut the forwarded server specified by {name}.

	[GET] data/outputs/tcp/server/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view forwarded server. |
|--------------------------------
| **404** | Forwarded server does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Retrieve configuration details for the output configured to port 9997 on host "tiny".

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/data/outputs/tcp/server/tiny:9997
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;tcpout-server&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/data/outputs/tcp/server&lt;/id&gt;
  &lt;updated&gt;2011-07-10T21:35:24-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/data/outputs/tcp/server/_new" rel="create"/&gt;
  &lt;link href="/services/data/outputs/tcp/server/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;tiny:9997&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/data/outputs/tcp/server/tiny%3A9997&lt;/id&gt;
    &lt;updated&gt;2011-07-10T21:35:24-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/data/outputs/tcp/server/tiny%3A9997" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/data/outputs/tcp/server/tiny%3A9997" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/outputs/tcp/server/tiny%3A9997/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/outputs/tcp/server/tiny%3A9997" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/outputs/tcp/server/tiny%3A9997" rel="remove"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/outputs/tcp/server/tiny%3A9997/allconnections" rel="allconnections"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/outputs/tcp/server/tiny%3A9997/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:attributes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="optionalFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;backoffAtStartup&lt;/s:item&gt;
                &lt;s:item&gt;disabled&lt;/s:item&gt;
                &lt;s:item&gt;initialBackoff&lt;/s:item&gt;
                &lt;s:item&gt;maxBackoff&lt;/s:item&gt;
                &lt;s:item&gt;maxNumberOfRetriesAtHighestBackoff&lt;/s:item&gt;
                &lt;s:item&gt;method&lt;/s:item&gt;
                &lt;s:item&gt;sslAltNameToCheck&lt;/s:item&gt;
                &lt;s:item&gt;sslCertPath&lt;/s:item&gt;
                &lt;s:item&gt;sslCipher&lt;/s:item&gt;
                &lt;s:item&gt;sslCommonNameToCheck&lt;/s:item&gt;
                &lt;s:item&gt;sslPassword&lt;/s:item&gt;
                &lt;s:item&gt;sslRootCAPath&lt;/s:item&gt;
                &lt;s:item&gt;sslVerifyServerCert&lt;/s:item&gt;
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
        &lt;s:key name="method"&gt;autobalance&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/outputs/tcp/server/{name}

Configures the forwarded server specified by {name}.

	[POST] data/outputs/tcp/server/{name}

### Parameters

backoffAtStartup
: _Optional_ **INHERITED** INHERITED

disabled
: _Optional_ **INHERITED** INHERITED

initialBackoff
: _Optional_ **INHERITED** INHERITED

maxBackoff
: _Optional_ **INHERITED** INHERITED

maxNumberOfRetriesAtHighestBackoff
: _Optional_ **INHERITED** INHERITED

method
: _Optional_ **INHERITED** INHERITED

sslAltNameToCheck
: _Optional_ **INHERITED** INHERITED

sslCertPath
: _Optional_ **INHERITED** INHERITED

sslCipher
: _Optional_ **INHERITED** INHERITED

sslCommonNameToCheck
: _Optional_ **INHERITED** INHERITED

sslPassword
: _Optional_ **INHERITED** INHERITED

sslRootCAPath
: _Optional_ **INHERITED** INHERITED

sslVerifyServerCert
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
| **403** | Insufficient permissions to edit configuratin for forwarded server. |
|--------------------------------
| **404** | Forwarded server does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

For the forwarding configuration pointed to port 9997 on tiny, adjust the reconnect behavior to wait longer before attempting another connection.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/data/outputs/tcp/server/tiny:9997 \
	-d initialBackoff=10
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;tcpout-server&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/data/outputs/tcp/server&lt;/id&gt;
  &lt;updated&gt;2011-07-10T21:35:33-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/data/outputs/tcp/server/_new" rel="create"/&gt;
  &lt;link href="/services/data/outputs/tcp/server/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

<a name='dataoutputstcpservernameallconnections'/>

## data/outputs/tcp/server/{name}/allconnections

List current connections to forwarded server specified by {name} 

	[GET] data/outputs/tcp/server/{name}/allconnections

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed connections successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to list ouput connections. |
|--------------------------------
| **404** | Output server does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

List existing connections to forwarded server listening at localhost:9997

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/services/data/outputs/tcp/server/localhost%3A9997/allconnections
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom" 
      xmlns:s="http://dev.splunk.com/ns/rest" 
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;tcpout-server&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/data/outputs/tcp/server&lt;/id&gt;
  &lt;updated&gt;2011-07-15T15:15:12-0700&lt;/updated&gt;
  &lt;generator version="101277"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/data/outputs/tcp/server/_new" rel="create"/&gt;
  &lt;link href="/services/data/outputs/tcp/server/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;localhost:9997&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/data/outputs/tcp/server/localhost%3A9997&lt;/id&gt;
    &lt;updated&gt;2011-07-15T15:15:12-0700&lt;/updated&gt;
    &lt;link href="/services/data/outputs/tcp/server/localhost%3A9997" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/data/outputs/tcp/server/localhost%3A9997" rel="list"/&gt;
    &lt;link href="/services/data/outputs/tcp/server/localhost%3A9997/_reload" rel="_reload"/&gt;
    &lt;link href="/services/data/outputs/tcp/server/localhost%3A9997" rel="edit"/&gt;
    &lt;link href="/services/data/outputs/tcp/server/localhost%3A9997" rel="remove"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="destHost"&gt;localhost&lt;/s:key&gt;
        &lt;s:key name="destIp"&gt;127.0.0.1&lt;/s:key&gt;
        &lt;s:key name="destPort"&gt;9997&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="sourcePort"&gt;8089&lt;/s:key&gt;
        &lt;s:key name="status"&gt;connect_done&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

<a name='dataoutputstcpsyslog'/>

## data/outputs/tcp/syslog

Provides access to syslog data forwarding configurations.

	[GET] data/outputs/tcp/syslog

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
| **403** | Insufficient permissions to view configuration of forwarded servers. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Retrieves the list of forwarding targets via syslog that have been defined.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/data/outputs/tcp/syslog
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom" 
      xmlns:s="http://dev.splunk.com/ns/rest" 
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;syslog&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/data/outputs/tcp/syslog&lt;/id&gt;
  &lt;updated&gt;2011-07-21T22:16:11-0700&lt;/updated&gt;
  &lt;generator version="101277"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/data/outputs/tcp/syslog/_new" rel="create"/&gt;
  &lt;opensearch:totalResults&gt;1&lt;/opensearch:totalResults&gt;
  &lt;opensearch:itemsPerPage&gt;30&lt;/opensearch:itemsPerPage&gt;
  &lt;opensearch:startIndex&gt;0&lt;/opensearch:startIndex&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;west_coast_servers&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/data/outputs/tcp/syslog/west_coast_servers&lt;/id&gt;
    &lt;updated&gt;2011-07-21T22:16:11-0700&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/data/outputs/tcp/syslog/west_coast_servers" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/data/outputs/tcp/syslog/west_coast_servers" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/outputs/tcp/syslog/west_coast_servers" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/outputs/tcp/syslog/west_coast_servers" rel="remove"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="disabled"&gt;1&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="server"&gt;syslogservers.splunk.com:514&lt;/s:key&gt;
        &lt;s:key name="type"&gt;tcp&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/outputs/tcp/syslog

Configures a forwarder to send data in standard syslog format.

	[POST] data/outputs/tcp/syslog

### Parameters

disabled
: _Optional_ **Boolean** If true, disables global syslog settings.

name
: _Required_ **String** Name of the forwarder to send data in standard syslog format.

priority
: _Optional_ **integer** Sets syslog priority value.

server
: _Optional_ **String** host:port of the server where syslog data should be sent

timestampformat
: _Optional_ **String** Format of timestamp to add at start of the events to be forwarded.

type
: _Optional_ **String** Protocol to use to send syslog data. Valid values: (tcp | udp ).

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
| **403** | Insufficient permissions to configure a forwarded server. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Create a new group for forwarding using syslog.

#### Request
<pre class='terminal'>
curl -k -u admin:changeme https://localhost:8089/services/data/outputs/tcp/syslog \
	-d name=east_coast_servers \
	-d server=east.splunk.com:514
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom" 
      xmlns:s="http://dev.splunk.com/ns/rest" 
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;syslog&lt;/title&gt;
  &lt;id&gt;https://localhost:22090/services/data/outputs/tcp/syslog&lt;/id&gt;
  &lt;updated&gt;2011-07-21T23:00:26-07:00&lt;/updated&gt;
  &lt;generator version="104359"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/data/outputs/tcp/syslog/_new" rel="create"/&gt;
  &lt;opensearch:totalResults&gt;0&lt;/opensearch:totalResults&gt;
  &lt;opensearch:itemsPerPage&gt;30&lt;/opensearch:itemsPerPage&gt;
  &lt;opensearch:startIndex&gt;0&lt;/opensearch:startIndex&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

<a name='dataoutputstcpsyslogname'/>

## data/outputs/tcp/syslog/{name}

Deletes the configuration for the forwarder specified by {name} that sends data in syslog format.

	[DELETE] data/outputs/tcp/syslog/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deleted successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to delete forwarded server configuration. |
|--------------------------------
| **404** | Forwarded server configuration does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Remove the configuration for forwarding data to host syslog group west_coast_servers

#### Request
<pre class='terminal'>
curl -k -u admin:pass --request DELETE \
	https://localhost:8089/services/data/outputs/tcp/syslog/west_coast_servers
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom" 
      xmlns:s="http://dev.splunk.com/ns/rest" 
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;syslog&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/data/outputs/tcp/syslog&lt;/id&gt;
  &lt;updated&gt;2011-07-21T22:20:52-0700&lt;/updated&gt;
  &lt;generator version="101277"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/data/outputs/tcp/syslog/_new" rel="create"/&gt;
  &lt;opensearch:totalResults&gt;0&lt;/opensearch:totalResults&gt;
  &lt;opensearch:itemsPerPage&gt;30&lt;/opensearch:itemsPerPage&gt;
  &lt;opensearch:startIndex&gt;0&lt;/opensearch:startIndex&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## data/outputs/tcp/syslog/{name}

Returns configuration information for the forwarder specified by {name} that sends data in standard syslog format.

	[GET] data/outputs/tcp/syslog/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view forwarded server configuration. |
|--------------------------------
| **404** | Forwarded server does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Retrieve configuration details for the syslog output configured for group west_coast_servers

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/data/outputs/tcp/syslog/west_coast_servers
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom" 
      xmlns:s="http://dev.splunk.com/ns/rest" 
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;syslog&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/data/outputs/tcp/syslog&lt;/id&gt;
  &lt;updated&gt;2011-07-21T22:30:33-0700&lt;/updated&gt;
  &lt;generator version="101277"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/data/outputs/tcp/syslog/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;west_coast_servers&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/data/outputs/tcp/syslog/west_coast_servers&lt;/id&gt;
    &lt;updated&gt;2011-07-21T22:30:33-0700&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/data/outputs/tcp/syslog/west_coast_servers" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/data/outputs/tcp/syslog/west_coast_servers" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/outputs/tcp/syslog/west_coast_servers" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/outputs/tcp/syslog/west_coast_servers" rel="remove"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="disabled"&gt;1&lt;/s:key&gt;
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
        &lt;s:key name="server"&gt;syslogservers.splunk.com:514&lt;/s:key&gt;
        &lt;s:key name="type"&gt;tcp&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/outputs/tcp/syslog/{name}

Updates the configuration of the forwarder specified by {name} that sends data in syslog format.

	[POST] data/outputs/tcp/syslog/{name}

### Parameters

disabled
: _Optional_ **INHERITED** INHERITED

priority
: _Optional_ **INHERITED** INHERITED

server
: _Optional_ **INHERITED** INHERITED

timestampformat
: _Optional_ **INHERITED** INHERITED

type
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
| **403** | Insufficient permissions to edit forwarded server configuration. |
|--------------------------------
| **404** | Forwarded server does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

For forwarding group west_coast_servers, modify type to udp

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/data/outputs/tcp/syslog/west_coast_servers \
	-d type=udp
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom" 
      xmlns:s="http://dev.splunk.com/ns/rest" 
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;syslog&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/data/outputs/tcp/syslog&lt;/id&gt;
  &lt;updated&gt;2011-07-21T22:53:23-07:00&lt;/updated&gt;
  &lt;generator version="104359"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/data/outputs/tcp/syslog/_new" rel="create"/&gt;
  &lt;opensearch:totalResults&gt;0&lt;/opensearch:totalResults&gt;
  &lt;opensearch:itemsPerPage&gt;30&lt;/opensearch:itemsPerPage&gt;
  &lt;opensearch:startIndex&gt;0&lt;/opensearch:startIndex&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>


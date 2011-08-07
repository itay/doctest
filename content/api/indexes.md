## data/indexes
{: name='dataindexes'}

Lists the recognized indexes on the server.

	[GET] data/indexes

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

summarize
: _Optional_ **Bool** If true, leaves out certain index details in order to provide a faster response.

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | OK |
|--------------------------------
| **400** | TO DO: provide the rest of the status codes |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view indexes. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Lists the indexes on this Splunk instance.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/data/indexes
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;indexes&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/data/indexes&lt;/id&gt;
  &lt;updated&gt;2011-07-11T18:09:22-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/data/indexes/_new" rel="create"/&gt;
  &lt;link href="/services/data/indexes/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;_audit&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/system/data/indexes/_audit&lt;/id&gt;
    &lt;updated&gt;2011-07-11T18:09:22-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/system/data/indexes/_audit" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/system/data/indexes/_audit" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/indexes/_audit/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/indexes/_audit" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/system/data/indexes/_audit/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="assureUTF8"&gt;0&lt;/s:key&gt;
        &lt;s:key name="blockSignSize"&gt;0&lt;/s:key&gt;
        &lt;s:key name="blockSignatureDatabase"&gt;_blocksignature&lt;/s:key&gt;
        &lt;s:key name="coldPath"&gt;$SPLUNK_DB/audit/colddb&lt;/s:key&gt;
        &lt;s:key name="coldPath_expanded"&gt;/home/amrit/temp/curl/splunk/var/lib/splunk/audit/colddb&lt;/s:key&gt;
        &lt;s:key name="coldToFrozenDir"/&gt;
        &lt;s:key name="coldToFrozenScript"/&gt;
        &lt;s:key name="compressRawdata"&gt;1&lt;/s:key&gt;
        &lt;s:key name="currentDBSizeMB"&gt;1&lt;/s:key&gt;
        &lt;s:key name="defaultDatabase"&gt;main&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="enableRealtimeSearch"&gt;1&lt;/s:key&gt;
        &lt;s:key name="frozenTimePeriodInSecs"&gt;188697600&lt;/s:key&gt;
        &lt;s:key name="homePath"&gt;$SPLUNK_DB/audit/db&lt;/s:key&gt;
        &lt;s:key name="homePath_expanded"&gt;/home/amrit/temp/curl/splunk/var/lib/splunk/audit/db&lt;/s:key&gt;
        &lt;s:key name="indexThreads"&gt;auto&lt;/s:key&gt;
        &lt;s:key name="isInternal"&gt;1&lt;/s:key&gt;
        &lt;s:key name="lastInitTime"&gt;1310432962.424512&lt;/s:key&gt;
        &lt;s:key name="maxConcurrentOptimizes"&gt;3&lt;/s:key&gt;
        &lt;s:key name="maxDataSize"&gt;auto&lt;/s:key&gt;
        &lt;s:key name="maxHotBuckets"&gt;3&lt;/s:key&gt;
        &lt;s:key name="maxHotIdleSecs"&gt;0&lt;/s:key&gt;
        &lt;s:key name="maxHotSpanSecs"&gt;7776000&lt;/s:key&gt;
        &lt;s:key name="maxMemMB"&gt;5&lt;/s:key&gt;
        &lt;s:key name="maxMetaEntries"&gt;1000000&lt;/s:key&gt;
        &lt;s:key name="maxRunningProcessGroups"&gt;20&lt;/s:key&gt;
        &lt;s:key name="maxTime"&gt;2011-07-10T22:20:53-0700&lt;/s:key&gt;
        &lt;s:key name="maxTotalDataSizeMB"&gt;500000&lt;/s:key&gt;
        &lt;s:key name="maxWarmDBCount"&gt;300&lt;/s:key&gt;
        &lt;s:key name="memPoolMB"&gt;auto&lt;/s:key&gt;
        &lt;s:key name="minRawFileSyncSecs"&gt;disable&lt;/s:key&gt;
        &lt;s:key name="minTime"&gt;2011-07-10T14:33:00-0700&lt;/s:key&gt;
        &lt;s:key name="partialServiceMetaPeriod"&gt;0&lt;/s:key&gt;
        &lt;s:key name="quarantineFutureSecs"&gt;2592000&lt;/s:key&gt;
        &lt;s:key name="quarantinePastSecs"&gt;77760000&lt;/s:key&gt;
        &lt;s:key name="rawChunkSizeBytes"&gt;131072&lt;/s:key&gt;
        &lt;s:key name="rotatePeriodInSecs"&gt;60&lt;/s:key&gt;
        &lt;s:key name="serviceMetaPeriod"&gt;25&lt;/s:key&gt;
        &lt;s:key name="suppressBannerList"/&gt;
        &lt;s:key name="sync"&gt;0&lt;/s:key&gt;
        &lt;s:key name="syncMeta"&gt;1&lt;/s:key&gt;
        &lt;s:key name="thawedPath"&gt;$SPLUNK_DB/audit/thaweddb&lt;/s:key&gt;
        &lt;s:key name="thawedPath_expanded"&gt;/home/amrit/temp/curl/splunk/var/lib/splunk/audit/thaweddb&lt;/s:key&gt;
        &lt;s:key name="throttleCheckPeriod"&gt;15&lt;/s:key&gt;
        &lt;s:key name="totalEventCount"&gt;230&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/indexes
{: name='dataindexes'}

Creates a new index with the given name.

	[POST] data/indexes

### Parameters

assureUTF8
: _Optional_ **Boolean** Verifies that all data retreived from the index is proper UTF8.<br/><br/>Will degrade indexing performance when enabled (set to true).<br/><br/>Can only be set globally

blockSignSize
: _Optional_ **Number** Controls how many events make up a block for block signatures.<br/><br/>If this is set to 0, block signing is disabled for this index.<br/><br/>A recommended value is 100.

coldPath
: _Optional_ **String** An absolute path that contains the colddbs for the index. The path must be readable and writable. Cold databases are opened as needed when searching. May be defined in terms of a volume definition (see volume section below).<br/><br/>Required. Splunk will not start if an index lacks a valid coldPath.

coldToFrozenDir
: _Optional_ **String** Destination path for the frozen archive. Use as an alternative to a coldToFrozenScript. Splunk automatically puts frozen buckets in this directory.<br/><br/>Bucket freezing policy is as follows:
* New style buckets (4.2 and on): removes all files but the rawdata
:To thaw, run <pre>splunk rebuild <bucket dir></pre> on the bucket, then move to the thawed directory
* Old style buckets (Pre-4.2): gzip all the .data and .tsidx files
:To thaw, gunzip the zipped files and move the bucket into the thawed directory<br/><br/>If both coldToFrozenDir and coldToFrozenScript are specified, coldToFrozenDir takes precedence

coldToFrozenScript
: _Optional_ **String** Path to the archiving script.<br/><br/>If your script requires a program to run it (for example, python), specify the program followed by the path. The script must be in $SPLUNK_HOME/bin or one of its subdirectories.<br/><br/>Splunk ships with an example archiving script in $SPLUNK_HOME/bin called coldToFrozenExample.py. Splunk DOES NOT recommend using this example script directly. It uses a default path, and if modified in place any changes will be overwritten on upgrade.<br/><br/>Splunk recommends copying the example script to a new file in bin and modifying it for your system.  Most importantly, change the default archive path to an existing directory that fits your needs.<br/><br/>If your new script in bin/ is named myColdToFrozen.py, set this key to the following:<br/><br/>  coldToFrozenScript = "$SPLUNK_HOME/bin/python" "$SPLUNK_HOME/bin/myColdToFrozen.py"<br/><br/>By default, the example script has two possible behaviors when archiving:
* For buckets created from version 4.2 and on, it removes all files except for rawdata. To thaw: cd to the frozen bucket and type <code>splunk rebuild .</code>, then copy the bucket to thawed for that index.  We recommend using the coldToFrozenDir parameter unless you need to perform a more advanced operation upon freezing buckets.
* For older-style buckets, we simply gzip all the .tsidx files. To thaw: cd to the frozen bucket and unzip the tsidx files, then copy the bucket to thawed for that index

compressRawdata
: _Optional_ **Boolean** This parameter is ignored. The splunkd process always compresses raw data.

frozenTimePeriodInSecs
: _Optional_ **Number** Number of seconds after which indexed data rolls to frozen.  Defaults to 188697600 (6 years).<br/><br/>Freezing data means it is removed from the index.  If you need to archive your data, refer to coldToFrozenDir and coldToFrozenScript parameter documentation.

homePath
: _Optional_ **String** An absolute path that contains the hot and warm buckets for the index.<br/><br/>Required. Splunk will not start if an index lacks a valid homePath.<br/><br/>CAUTION: Path MUST be readable and writable.

maxConcurrentOptimizes
: _Optional_ **Number** The number of concurrent optimize processes that can run against a hot bucket.<br/><br/>This number should be increased if instructed by Splunk Support.  Typically the default value should suffice.


maxDataSize
: _Optional_ **Number** The maximum size in MB for a hot DB to reach before a roll to warm is triggered. Specifying "auto" or "auto_high_volume" causes Splunk to autotune this parameter (recommended).Use "auto_high_volume" for high volume indexes (such as the main index); otherwise, use "auto".  A "high volume index" would typically be considered one that gets over 10GB of data per day.
* "auto" sets the size to 750MB.
* "auto_high_volume" sets the size to 10GB on 64-bit, and 1GB on 32-bit systems.<br/><br/>Although the maximum value you can set this is 1048576 MB, which corresponds to 1 TB, a reasonable number ranges anywhere from 100 - 50000. Any number outside this range should be approved by Splunk Support before proceeding.<br/><br/>If you specify an invalid number or string, maxDataSize will be auto tuned.<br/><br/>NOTE: The precise size of your warm buckets may vary from maxDataSize, due to post-processing and timing issues with the rolling policy.

maxHotBuckets
: _Optional_ **Number** Maximum hot buckets that can exist per index. Defaults to 3.<br/><br/>When maxHotBuckets is exceeded, Splunk rolls the least recently used (LRU) hot bucket to warm. Both normal hot buckets and quarantined hot buckets count towards this total. This setting operates independently of maxHotIdleSecs, which can also cause hot buckets to roll.

maxHotIdleSecs
: _Optional_ **Number** "Maximum life, in seconds, of a hot bucket. Defaults to 0.<br/><br/>If a hot bucket exceeds maxHotIdleSecs, Splunk rolls it to warm. This setting operates independently of maxHotBuckets, which can also cause hot buckets to roll. A value of 0 turns off the idle check (equivalent to INFINITE idle time).

maxHotSpanSecs
: _Optional_ **Number** Upper bound of target maximum timespan of hot/warm buckets in seconds. Defaults to 7776000 seconds (90 days).<br/><br/>NOTE: f you set this too small, you can get an explosion of hot/warm buckets in the filesystem. The system sets a lower bound implicitly for this parameter at 3600, but this is an advanced parameter that should be set with care and understanding of the characteristics of your data.

maxMemMB
: _Optional_ **Number** The amount of memory, expressed in MB, to allocate for buffering a single tsidx file into memory before flushing to disk.  Defaults to 5. The default is recommended for all environments.<br/><br/>IMPORTANT:  Calculate this number carefully. Setting this number incorrectly may have adverse effects on your systems memory and/or splunkd stability/performance.

maxMetaEntries
: _Optional_ **Number** Sets the maximum number of unique lines in .data files in a bucket, which may help to reduce memory consumption. If set to 0, this setting is ignored (it is treated as infinite).<br/><br/>If exceeded, a hot bucket is rolled to prevent further increase. If your buckets are rolling due to Strings.data hitting this limit, the culprit may be the <code>punct</code> field in your data.  If you don't use punct, it may be best to simply disable this (see props.conf.spec in $SPLUNK_HOME/etc/system/README).<br/><br/>There is a small time delta between when maximum is exceeded and bucket is rolled. This means a bucket may end up with epsilon more lines than specified, but this is not a major concern unless excess is significant.

maxRunningProcessGroups
: _Optional_ **Number** The indexer fires off helper processes like splunk-optimize, recover-metadata, and others. This parameter controls how many processes the indexer fires off at any given time.<br/><br/><b>CAUTION:</b> This is an advanced parameter, do NOT set this unless instructed by Splunk Support.

maxTotalDataSizeMB
: _Optional_ **Number** The maximum size of an index (in MB). If an index grows larger than the maximum size, the oldest data is frozen.

maxWarmDBCount
: _Optional_ **Number** The maximum number of warm buckets. If this number is exceeded, the warm bucket/s with the lowest value for their latest times will be moved to cold.

minRawFileSyncSecs
: _Optional_ **Number** Specify an integer (or "disable") for this parameter.<br/><br/>This parameter sets how frequently splunkd forces a filesystem sync while compressing journal slices.<br/><br/>During this interval, uncompressed slices are left on disk even after they are compressed. Then splunkd forces a filesystem sync of the compressed journal and removes the accumulated uncompressed files.<br/><br/>If 0 is specified, splunkd forces a filesystem sync after every slice completes compressing. Specifying "disable" disables syncing entirely: uncompressed slices are removed as soon as compression is complete.<br/><br/><b>NOTE:</b> Some filesystems are very inefficient at performing sync operations, so only enable this if you are sure it is needed

name
: _Required_ **String** The name of the index to create.

partialServiceMetaPeriod
: _Optional_ **Number** Related to serviceMetaPeriod.  If set, it enables metadata sync every <integer> seconds, but only for records where the sync can be done efficiently in-place, without requiring a full re-write of the metadata file.  Records that require full re-write are be sync'ed at serviceMetaPeriod.<br/><br/><code>partialServiceMetaPeriod</code> specifies, in seconds, how frequently it should sync.  Zero means that this feature is turned off and serviceMetaPeriod is the only time when metadata sync happens.<br/><br/>If the value of partialServiceMetaPeriod is greater than serviceMetaPeriod, this setting has no effect.<br/><br/>By default it is turned off (zero).

quarantineFutureSecs
: _Optional_ **Number** Events with timestamp of <code>quarantineFutureSecs</code> newer than "now" are dropped into quarantine bucket. Defaults to 2592000 (30 days).<br/><br/>This is a mechanism to prevent main hot buckets from being polluted with fringe events.

quarantinePastSecs
: _Optional_ **Number** Events with timestamp of <code>quarantinePastSecs</code> older than "now" are dropped into quarantine bucket. Defaults to 77760000 (900 days).<br/><br/>This is a mechanism to prevent the main hot buckets from being polluted with fringe events.

rawChunkSizeBytes
: _Optional_ **Number** Target uncompressed size in bytes for individual raw slice in the rawdata journal of the index. Defaults to 131072 (128KB). 0 is not a valid value. If 0 is specified, <code>rawChunkSizeBytes</code> is set to the default value.<br/><br/>NOTE: rawChunkSizeBytes only specifies a target chunk size. The actual chunk size may be slightly larger by an amount proportional to an individual event size.<br/><br/>WARNING: This is an advanced parameter. Only change it if you are instructed to do so by Splunk Support.

rotatePeriodInSecs
: _Optional_ **Number** How frequently (in seconds) to check if a new hot bucket needs to be created. Also, how frequently to check if there are any warm/cold buckets that should be rolled/frozen.

serviceMetaPeriod
: _Optional_ **Number** Defines how frequently metadata is synced to disk, in seconds. Defaults to 25 (seconds).<br/><br/>You may want to set this to a higher value if the sum of your metadata file sizes is larger than many tens of megabytes, to avoid the hit on I/O in the indexing fast path.

suppressBannerList
: _Optional_ **String** Specify a comma-separated list of indexes. This parameter suppresses index missing warning banner messages for the specified indexes. Defaults to empty.

syncMeta
: _Optional_ **Boolean** When <code>true</code>, a sync operation is called before file descriptor is closed on metadata file updates. This functionality improves integrity of metadata files, especially in regards to operating system crashes/machine failures.<br/><br/><b>Note</b>: Do not change this parameter without the input of a Splunk Support.

thawedPath
: _Optional_ **String** An absolute path that contains the thawed (resurrected) databases for the index.<br/><br/>Cannot be defined in terms of a volume definition.<br/><br/>Required. Splunk will not start if an index lacks a valid <code>thawedPath</codePath>.<br/><br/>

throttleCheckPeriod
: _Optional_ **Number** Defines how frequently Splunk checks for index throttling condition, in seconds. Defaults to 15 (seconds).<br/><br/><b>Note</b>: Do not change this parameter without the input of a Splunk Support.

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **201** | Index created successfully; followed by header:

<code>Location: /services/data/indexes/{name}</code> |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **402** | The Splunk license in use has disabled this feature. |
|--------------------------------
| **403** | Insufficient permissions to create index. |
|--------------------------------
| **409** | The index name already exists. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

The following example creates an index named Shadow.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/data/indexes \
	-d name=Shadow
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>
&lt;?xml-stylesheet type="text/xml" href="/static/atom.xsl"?&gt;
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:s="http://dev.splunk.com/ns/rest"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;indexes&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/admin/search/data/indexes&lt;/id&gt;
  &lt;updated&gt;2011-05-13T13:09:27-07:00&lt;/updated&gt;
  &lt;generator version="98392"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/admin/search/data/indexes/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/admin/search/data/indexes/_reload" rel="_reload"/&gt;
  &lt;opensearch:totalResults&gt;1&lt;/opensearch:totalResults&gt;
  &lt;opensearch:itemsPerPage&gt;30&lt;/opensearch:itemsPerPage&gt;
  &lt;opensearch:startIndex&gt;0&lt;/opensearch:startIndex&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;shadow&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/indexes/shadow&lt;/id&gt;
    &lt;updated&gt;2011-05-13T13:09:27-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/search/data/indexes/shadow" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/search/data/indexes/shadow" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/indexes/shadow/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/indexes/shadow" rel="edit"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="assureUTF8"&gt;0&lt;/s:key&gt;
        &lt;s:key name="blockSignSize"&gt;0&lt;/s:key&gt;
        &lt;s:key name="blockSignatureDatabase"&gt;_blocksignature&lt;/s:key&gt;
        &lt;s:key name="coldPath"&gt;$SPLUNK_DB/shadow/colddb&lt;/s:key&gt;
        &lt;s:key name="coldPath_expanded"&gt;/Applications/splunk/var/lib/splunk/shadow/colddb&lt;/s:key&gt;
        &lt;s:key name="coldToFrozenDir"&gt;&lt;/s:key&gt;
        &lt;s:key name="coldToFrozenScript"&gt;&lt;/s:key&gt;
        &lt;s:key name="compressRawdata"&gt;1&lt;/s:key&gt;
        &lt;s:key name="currentDBSizeMB"&gt;1&lt;/s:key&gt;
        &lt;s:key name="defaultDatabase"&gt;main&lt;/s:key&gt;
        &lt;s:key name="eai:acl"&gt;. . .&lt;/s:key&gt;
        &lt;s:key name="enableRealtimeSearch"&gt;1&lt;/s:key&gt;
        &lt;s:key name="frozenTimePeriodInSecs"&gt;188697600&lt;/s:key&gt;
        &lt;s:key name="homePath"&gt;$SPLUNK_DB/shadow/db&lt;/s:key&gt;
        &lt;s:key name="homePath_expanded"&gt;/Applications/splunk/var/lib/splunk/shadow/db&lt;/s:key&gt;
        &lt;s:key name="indexThreads"&gt;auto&lt;/s:key&gt;
        &lt;s:key name="isInternal"&gt;0&lt;/s:key&gt;
        &lt;s:key name="lastInitTime"&gt;1305317367.331268&lt;/s:key&gt;
        &lt;s:key name="maxConcurrentOptimizes"&gt;3&lt;/s:key&gt;
        &lt;s:key name="maxDataSize"&gt;auto&lt;/s:key&gt;
        &lt;s:key name="maxHotBuckets"&gt;3&lt;/s:key&gt;
        &lt;s:key name="maxHotIdleSecs"&gt;0&lt;/s:key&gt;
        &lt;s:key name="maxHotSpanSecs"&gt;7776000&lt;/s:key&gt;
        &lt;s:key name="maxMemMB"&gt;5&lt;/s:key&gt;
        &lt;s:key name="maxMetaEntries"&gt;1000000&lt;/s:key&gt;
        &lt;s:key name="maxTime"&gt;&lt;/s:key&gt;
        &lt;s:key name="maxTotalDataSizeMB"&gt;500000&lt;/s:key&gt;
        &lt;s:key name="maxWarmDBCount"&gt;300&lt;/s:key&gt;
        &lt;s:key name="memPoolMB"&gt;auto&lt;/s:key&gt;
        &lt;s:key name="minRawFileSyncSecs"&gt;disable&lt;/s:key&gt;
        &lt;s:key name="minTime"&gt;&lt;/s:key&gt;
        &lt;s:key name="partialServiceMetaPeriod"&gt;0&lt;/s:key&gt;
        &lt;s:key name="quarantineFutureSecs"&gt;2592000&lt;/s:key&gt;
        &lt;s:key name="quarantinePastSecs"&gt;77760000&lt;/s:key&gt;
        &lt;s:key name="rawChunkSizeBytes"&gt;131072&lt;/s:key&gt;
        &lt;s:key name="rotatePeriodInSecs"&gt;60&lt;/s:key&gt;
        &lt;s:key name="serviceMetaPeriod"&gt;25&lt;/s:key&gt;
        &lt;s:key name="suppressBannerList"&gt;&lt;/s:key&gt;
        &lt;s:key name="sync"&gt;0&lt;/s:key&gt;
        &lt;s:key name="syncMeta"&gt;1&lt;/s:key&gt;
        &lt;s:key name="thawedPath"&gt;$SPLUNK_DB/shadow/thaweddb&lt;/s:key&gt;
        &lt;s:key name="thawedPath_expanded"&gt;/Applications/splunk/var/lib/splunk/shadow/thaweddb&lt;/s:key&gt;
        &lt;s:key name="throttleCheckPeriod"&gt;15&lt;/s:key&gt;
        &lt;s:key name="totalEventCount"&gt;0&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/indexes/{name}
{: name='dataindexesname'}

Retrieves information about the named index.

	[GET] data/indexes/{name}

### Parameters

summarize
: _Optional_ **Bool** If true, leaves out certain index details in order to provide a faster response.

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view index. |
|--------------------------------
| **404** | Index does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Lists information about the Shadow index.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/nobody/search/data/indexes/shadow
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;indexes&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/indexes&lt;/id&gt;
  &lt;updated&gt;2011-08-01T12:25:34-07:00&lt;/updated&gt;
  &lt;generator version="105103"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/indexes/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/indexes/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;shadow&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/indexes/shadow&lt;/id&gt;
    &lt;updated&gt;2011-08-01T11:47:55-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/search/data/indexes/shadow" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/search/data/indexes/shadow" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/indexes/shadow/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/indexes/shadow" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/indexes/shadow/disable" rel="disable"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="assureUTF8"&gt;0&lt;/s:key&gt;
        &lt;s:key name="blockSignSize"&gt;0&lt;/s:key&gt;
        &lt;s:key name="blockSignatureDatabase"&gt;_blocksignature&lt;/s:key&gt;
        &lt;s:key name="bloomfilterTotalSizeKB"&gt;0&lt;/s:key&gt;
        &lt;s:key name="coldPath"&gt;$SPLUNK_DB/shadow/colddb&lt;/s:key&gt;
        &lt;s:key name="coldPath_expanded"&gt;/home/amrit/bin/splunk-current/var/lib/splunk/shadow/colddb&lt;/s:key&gt;
        &lt;s:key name="coldToFrozenDir"/&gt;
        &lt;s:key name="coldToFrozenScript"/&gt;
        &lt;s:key name="compressRawdata"&gt;1&lt;/s:key&gt;
        &lt;s:key name="currentDBSizeMB"&gt;1&lt;/s:key&gt;
        &lt;s:key name="defaultDatabase"&gt;main&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:attributes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="optionalFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;assureUTF8&lt;/s:item&gt;
                &lt;s:item&gt;blockSignSize&lt;/s:item&gt;
                &lt;s:item&gt;coldToFrozenDir&lt;/s:item&gt;
                &lt;s:item&gt;coldToFrozenScript&lt;/s:item&gt;
                &lt;s:item&gt;compressRawdata&lt;/s:item&gt;
                &lt;s:item&gt;frozenTimePeriodInSecs&lt;/s:item&gt;
                &lt;s:item&gt;maxConcurrentOptimizes&lt;/s:item&gt;
                &lt;s:item&gt;maxDataSize&lt;/s:item&gt;
                &lt;s:item&gt;maxHotBuckets&lt;/s:item&gt;
                &lt;s:item&gt;maxHotIdleSecs&lt;/s:item&gt;
                &lt;s:item&gt;maxHotSpanSecs&lt;/s:item&gt;
                &lt;s:item&gt;maxMemMB&lt;/s:item&gt;
                &lt;s:item&gt;maxMetaEntries&lt;/s:item&gt;
                &lt;s:item&gt;maxRunningProcessGroups&lt;/s:item&gt;
                &lt;s:item&gt;maxTotalDataSizeMB&lt;/s:item&gt;
                &lt;s:item&gt;maxWarmDBCount&lt;/s:item&gt;
                &lt;s:item&gt;minRawFileSyncSecs&lt;/s:item&gt;
                &lt;s:item&gt;partialServiceMetaPeriod&lt;/s:item&gt;
                &lt;s:item&gt;quarantineFutureSecs&lt;/s:item&gt;
                &lt;s:item&gt;quarantinePastSecs&lt;/s:item&gt;
                &lt;s:item&gt;rawChunkSizeBytes&lt;/s:item&gt;
                &lt;s:item&gt;rotatePeriodInSecs&lt;/s:item&gt;
                &lt;s:item&gt;serviceMetaPeriod&lt;/s:item&gt;
                &lt;s:item&gt;suppressBannerList&lt;/s:item&gt;
                &lt;s:item&gt;syncMeta&lt;/s:item&gt;
                &lt;s:item&gt;throttleCheckPeriod&lt;/s:item&gt;
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
        &lt;s:key name="enableRealtimeSearch"&gt;1&lt;/s:key&gt;
        &lt;s:key name="frozenTimePeriodInSecs"&gt;188697600&lt;/s:key&gt;
        &lt;s:key name="homePath"&gt;$SPLUNK_DB/shadow/db&lt;/s:key&gt;
        &lt;s:key name="homePath_expanded"&gt;/home/amrit/bin/splunk-current/var/lib/splunk/shadow/db&lt;/s:key&gt;
        &lt;s:key name="indexThreads"&gt;auto&lt;/s:key&gt;
        &lt;s:key name="isInternal"&gt;0&lt;/s:key&gt;
        &lt;s:key name="lastInitTime"&gt;1312226552.102920&lt;/s:key&gt;
        &lt;s:key name="maxConcurrentOptimizes"&gt;3&lt;/s:key&gt;
        &lt;s:key name="maxDataSize"&gt;auto&lt;/s:key&gt;
        &lt;s:key name="maxHotBuckets"&gt;3&lt;/s:key&gt;
        &lt;s:key name="maxHotIdleSecs"&gt;0&lt;/s:key&gt;
        &lt;s:key name="maxHotSpanSecs"&gt;7776000&lt;/s:key&gt;
        &lt;s:key name="maxMemMB"&gt;5&lt;/s:key&gt;
        &lt;s:key name="maxMetaEntries"&gt;1000000&lt;/s:key&gt;
        &lt;s:key name="maxRunningProcessGroups"&gt;20&lt;/s:key&gt;
        &lt;s:key name="maxTime"/&gt;
        &lt;s:key name="maxTotalDataSizeMB"&gt;500000&lt;/s:key&gt;
        &lt;s:key name="maxWarmDBCount"&gt;300&lt;/s:key&gt;
        &lt;s:key name="memPoolMB"&gt;auto&lt;/s:key&gt;
        &lt;s:key name="minRawFileSyncSecs"&gt;disable&lt;/s:key&gt;
        &lt;s:key name="minTime"/&gt;
        &lt;s:key name="numBloomfilters"&gt;0&lt;/s:key&gt;
        &lt;s:key name="numHotBuckets"&gt;0&lt;/s:key&gt;
        &lt;s:key name="numWarmBuckets"&gt;0&lt;/s:key&gt;
        &lt;s:key name="partialServiceMetaPeriod"&gt;0&lt;/s:key&gt;
        &lt;s:key name="quarantineFutureSecs"&gt;2592000&lt;/s:key&gt;
        &lt;s:key name="quarantinePastSecs"&gt;77760000&lt;/s:key&gt;
        &lt;s:key name="rawChunkSizeBytes"&gt;131072&lt;/s:key&gt;
        &lt;s:key name="rotatePeriodInSecs"&gt;60&lt;/s:key&gt;
        &lt;s:key name="serviceMetaPeriod"&gt;25&lt;/s:key&gt;
        &lt;s:key name="suppressBannerList"/&gt;
        &lt;s:key name="sync"&gt;0&lt;/s:key&gt;
        &lt;s:key name="syncMeta"&gt;1&lt;/s:key&gt;
        &lt;s:key name="thawedPath"&gt;$SPLUNK_DB/shadow/thaweddb&lt;/s:key&gt;
        &lt;s:key name="thawedPath_expanded"&gt;/home/amrit/bin/splunk-current/var/lib/splunk/shadow/thaweddb&lt;/s:key&gt;
        &lt;s:key name="throttleCheckPeriod"&gt;15&lt;/s:key&gt;
        &lt;s:key name="totalEventCount"&gt;0&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## data/indexes/{name}
{: name='dataindexesname'}

Updates the data index specified by <code>{name}</code> with information specified with index attributes.

	[POST] data/indexes/{name}

### Parameters

assureUTF8
: _Optional_ **INHERITED** INHERITED

blockSignSize
: _Optional_ **INHERITED** INHERITED

coldToFrozenDir
: _Optional_ **INHERITED** INHERITED

coldToFrozenScript
: _Optional_ **INHERITED** INHERITED

compressRawdata
: _Optional_ **INHERITED** INHERITED

frozenTimePeriodInSecs
: _Optional_ **INHERITED** INHERITED

maxConcurrentOptimizes
: _Optional_ **INHERITED** INHERITED

maxDataSize
: _Optional_ **INHERITED** INHERITED

maxHotBuckets
: _Optional_ **INHERITED** INHERITED

maxHotIdleSecs
: _Optional_ **INHERITED** INHERITED

maxHotSpanSecs
: _Optional_ **INHERITED** INHERITED

maxMemMB
: _Optional_ **INHERITED** INHERITED

maxMetaEntries
: _Optional_ **INHERITED** INHERITED

maxRunningProcessGroups
: _Optional_ **INHERITED** INHERITED

maxTotalDataSizeMB
: _Optional_ **INHERITED** INHERITED

maxWarmDBCount
: _Optional_ **INHERITED** INHERITED

minRawFileSyncSecs
: _Optional_ **INHERITED** INHERITED

partialServiceMetaPeriod
: _Optional_ **INHERITED** INHERITED

quarantineFutureSecs
: _Optional_ **INHERITED** INHERITED

quarantinePastSecs
: _Optional_ **INHERITED** INHERITED

rawChunkSizeBytes
: _Optional_ **INHERITED** INHERITED

rotatePeriodInSecs
: _Optional_ **INHERITED** INHERITED

serviceMetaPeriod
: _Optional_ **INHERITED** INHERITED

suppressBannerList
: _Optional_ **INHERITED** INHERITED

syncMeta
: _Optional_ **INHERITED** INHERITED

throttleCheckPeriod
: _Optional_ **INHERITED** INHERITED

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Properties for the index were updated successfully. |
|--------------------------------
| **400** | Some arguments were invalid |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **402** | The Splunk license in use has disabled this feature. |
|--------------------------------
| **403** | Insufficient permissions to edit index. |
|--------------------------------
| **404** | The specified index was not found. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Unspecified error |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

The following example updates the maximum size of the index named "Shadow", setting the size at 400000 MB.
This index was created in the example for the POST operation for this endpoint.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	-d maxTotalDataSizeMB=400000 https://localhost:8089/servicesNS/nobody/search/data/indexes/shadow
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;?xml-stylesheet type="text/xml" href="/static/atom.xsl"?&gt;
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:s="http://dev.splunk.com/ns/rest"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;indexes&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/indexes&lt;/id&gt;
  &lt;updated&gt;2011-05-16T12:20:06-07:00&lt;/updated&gt;
  &lt;generator version="98392"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/data/indexes/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/data/indexes/_reload" rel="_reload"/&gt;
  &lt;opensearch:totalResults&gt;1&lt;/opensearch:totalResults&gt;
  &lt;opensearch:itemsPerPage&gt;30&lt;/opensearch:itemsPerPage&gt;
  &lt;opensearch:startIndex&gt;0&lt;/opensearch:startIndex&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;shadow&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/data/indexes/shadow&lt;/id&gt;
    &lt;updated&gt;2011-05-16T12:18:56-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/search/data/indexes/shadow" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/search/data/indexes/shadow" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/indexes/shadow/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/search/data/indexes/shadow" rel="edit"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="assureUTF8"&gt;0&lt;/s:key&gt;
        &lt;s:key name="blockSignSize"&gt;0&lt;/s:key&gt;
        &lt;s:key name="blockSignatureDatabase"&gt;_blocksignature&lt;/s:key&gt;
        &lt;s:key name="coldPath"&gt;$SPLUNK_DB/shadow/colddb&lt;/s:key&gt;
        &lt;s:key name="coldPath_expanded"&gt;/Applications/splunk4.3/var/lib/splunk/shadow/colddb&lt;/s:key&gt;
        &lt;s:key name="coldToFrozenDir"&gt;&lt;/s:key&gt;
        &lt;s:key name="coldToFrozenScript"&gt;&lt;/s:key&gt;
        &lt;s:key name="compressRawdata"&gt;1&lt;/s:key&gt;
        &lt;s:key name="currentDBSizeMB"&gt;1&lt;/s:key&gt;
        &lt;s:key name="defaultDatabase"&gt;main&lt;/s:key&gt;
        &lt;s:key name="eai:acl"&gt;. . .&lt;/s:key&gt;
        &lt;s:key name="enableRealtimeSearch"&gt;1&lt;/s:key&gt;
        &lt;s:key name="frozenTimePeriodInSecs"&gt;188697600&lt;/s:key&gt;
        &lt;s:key name="homePath"&gt;$SPLUNK_DB/shadow/db&lt;/s:key&gt;
        &lt;s:key name="homePath_expanded"&gt;/Applications/splunk4.3/var/lib/splunk/shadow/db&lt;/s:key&gt;
        &lt;s:key name="indexThreads"&gt;auto&lt;/s:key&gt;
        &lt;s:key name="isInternal"&gt;0&lt;/s:key&gt;
        &lt;s:key name="lastInitTime"&gt;1305573611.118477&lt;/s:key&gt;
        &lt;s:key name="maxConcurrentOptimizes"&gt;3&lt;/s:key&gt;
        &lt;s:key name="maxDataSize"&gt;auto&lt;/s:key&gt;
        &lt;s:key name="maxHotBuckets"&gt;3&lt;/s:key&gt;
        &lt;s:key name="maxHotIdleSecs"&gt;0&lt;/s:key&gt;
        &lt;s:key name="maxHotSpanSecs"&gt;7776000&lt;/s:key&gt;
        &lt;s:key name="maxMemMB"&gt;5&lt;/s:key&gt;
        &lt;s:key name="maxMetaEntries"&gt;1000000&lt;/s:key&gt;
        &lt;s:key name="maxTime"&gt;&lt;/s:key&gt;
        &lt;s:key name="maxTotalDataSizeMB"&gt;400000&lt;/s:key&gt;
        &lt;s:key name="maxWarmDBCount"&gt;300&lt;/s:key&gt;
        &lt;s:key name="memPoolMB"&gt;auto&lt;/s:key&gt;
        &lt;s:key name="minRawFileSyncSecs"&gt;disable&lt;/s:key&gt;
        &lt;s:key name="minTime"&gt;&lt;/s:key&gt;
        &lt;s:key name="partialServiceMetaPeriod"&gt;0&lt;/s:key&gt;
        &lt;s:key name="quarantineFutureSecs"&gt;2592000&lt;/s:key&gt;
        &lt;s:key name="quarantinePastSecs"&gt;77760000&lt;/s:key&gt;
        &lt;s:key name="rawChunkSizeBytes"&gt;131072&lt;/s:key&gt;
        &lt;s:key name="rotatePeriodInSecs"&gt;60&lt;/s:key&gt;
        &lt;s:key name="serviceMetaPeriod"&gt;25&lt;/s:key&gt;
        &lt;s:key name="suppressBannerList"&gt;&lt;/s:key&gt;
        &lt;s:key name="sync"&gt;0&lt;/s:key&gt;
        &lt;s:key name="syncMeta"&gt;1&lt;/s:key&gt;
        &lt;s:key name="thawedPath"&gt;$SPLUNK_DB/shadow/thaweddb&lt;/s:key&gt;
        &lt;s:key name="thawedPath_expanded"&gt;/Applications/splunk4.3/var/lib/splunk/shadow/thaweddb&lt;/s:key&gt;
        &lt;s:key name="throttleCheckPeriod"&gt;15&lt;/s:key&gt;
        &lt;s:key name="totalEventCount"&gt;0&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>


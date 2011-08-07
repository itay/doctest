## apps/appinstall
{: name='appsappinstall'}

Installs a Splunk app from a local file or from a URL.

	[POST] apps/appinstall

### Parameters

name
: _Required_ **String** Specifies the app to install. Can be either a path to the app on a local disk or a URL to an app, such as the apps available from Splunkbase.

update
: _Optional_ **Boolean** If true, installs an update to an app, overwriting the existing app folder.

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
| **403** | Insufficient permissions to install app. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

This example installs the basketball app from a local file. The file was downloaded an app from splunkbase.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/apps/appinstall/ \
	-d name=/Users/vgenovese/Downloads/basketball.tar
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>
&lt;?xml-stylesheet type="text/xml" href="/static/atom.xsl"?&gt;
&lt;feed xmlns="http://www.w3.org/2005/Atom" 
  xmlns:s="http://dev.splunk.com/ns/rest" 
  xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/apps/appinstall&lt;/id&gt;
  &lt;updated&gt;2011-05-31T14:37:32-07:00&lt;/updated&gt;
  &lt;generator version="100492"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/apps/appinstall/_new" rel="create"/&gt;
  &lt;opensearch:totalResults&gt;1&lt;/opensearch:totalResults&gt;
  &lt;opensearch:itemsPerPage&gt;30&lt;/opensearch:itemsPerPage&gt;
  &lt;opensearch:startIndex&gt;0&lt;/opensearch:startIndex&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;Installed&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/apps/appinstall/Installed&lt;/id&gt;
    &lt;updated&gt;2011-05-31T14:37:32-07:00&lt;/updated&gt;
    &lt;link href="/services/apps/appinstall/Installed" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/apps/appinstall/Installed" rel="list"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="eai:acl"&gt;
        . . .
        &lt;/s:key&gt;
        &lt;s:key name="location"&gt;/Applications/splunk4.3/etc/apps/basketball&lt;/s:key&gt;
        &lt;s:key name="name"&gt;basketball&lt;/s:key&gt;
        &lt;s:key name="source_location"&gt;/Users/vgenovese/Downloads/basketball.tar&lt;/s:key&gt;
        &lt;s:key name="status"&gt;installed&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## apps/apptemplates
{: name='appsapptemplates'}

Lists app templates that are used to create apps from the Mangager interface in Splunk Web.

An app templates is valid as the "template" argument to POST to /services/apps/local. The app templates can be found by enumerating $SPLUNK_HOME/share/splunk/app_templates. Adding a new template takes effect without restarting splunkd or SplunkWeb.

	[GET] apps/apptemplates

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
| **403** | Insufficient permissions to view app templates. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Lists available app templates that can be used to create a new app.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/apps/apptemplates
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title/&gt;
  &lt;id&gt;https://localhost:8089/services/apps/apptemplates&lt;/id&gt;
  &lt;updated&gt;2011-07-08T01:19:34-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;barebones&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/apps/apptemplates/barebones&lt;/id&gt;
    &lt;updated&gt;2011-07-08T01:19:34-07:00&lt;/updated&gt;
    &lt;link href="/services/apps/apptemplates/barebones" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/apps/apptemplates/barebones" rel="list"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="lol"&gt;wut&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## apps/apptemplates/{name}
{: name='appsapptemplatesname'}

Retrieves information about a specific app template.

This call is rarely used, as all the information is provided by the apps/templates endpoint, which does not require an explicit name.

	[GET] apps/apptemplates/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view app template. |
|--------------------------------
| **404** | app template does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

List information about the barebones app template.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/apps/apptemplates/barebones
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title/&gt;
  &lt;id&gt;https://localhost:8089/services/apps/apptemplates&lt;/id&gt;
  &lt;updated&gt;2011-07-08T01:19:35-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;barebones&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/apps/apptemplates/barebones&lt;/id&gt;
    &lt;updated&gt;2011-07-08T01:19:35-07:00&lt;/updated&gt;
    &lt;link href="/services/apps/apptemplates/barebones" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/apps/apptemplates/barebones" rel="list"/&gt;
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
        &lt;s:key name="lol"&gt;wut&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## apps/local
{: name='appslocal'}

Returns information on all locally-installed apps.

Splunkbase can correlate locally-installed apps with the same app on Splunkbase to notify users about app updates.

	[GET] apps/local

### Parameters

count
: _Optional_ **Number** Maximum number of items to return.

offset
: _Optional_ **Number** Index for first item to return.

refresh
: _Optional_ **Boolean** Scan for new apps and reload any objects those new apps contain.

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
| **403** | Insufficient permissions to view local apps. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Return all locally installed apps for this Splunk instance.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/apps/local
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;localapps&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/apps/local&lt;/id&gt;
  &lt;updated&gt;2011-07-11T19:14:48-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/apps/local/_new" rel="create"/&gt;
  &lt;link href="/services/apps/local/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;dstestapp&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/apps/local/dstestapp&lt;/id&gt;
    &lt;updated&gt;2011-07-11T19:14:48-07:00&lt;/updated&gt;
    &lt;link href="/services/apps/local/dstestapp" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/apps/local/dstestapp" rel="list"/&gt;
    &lt;link href="/services/apps/local/dstestapp/_reload" rel="_reload"/&gt;
    &lt;link href="/services/apps/local/dstestapp" rel="edit"/&gt;
    &lt;link href="/services/apps/local/dstestapp" rel="remove"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="author"&gt;Greg Albrecht (gba@splunk.com)&lt;/s:key&gt;
        &lt;s:key name="check_for_updates"&gt;1&lt;/s:key&gt;
        &lt;s:key name="configured"&gt;0&lt;/s:key&gt;
        &lt;s:key name="description"&gt;If you see this app then your deployment client is working correctly.&lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="label"&gt;Deployment Server Test App&lt;/s:key&gt;
        &lt;s:key name="manageable"&gt;1&lt;/s:key&gt;
        &lt;s:key name="state_change_requires_restart"&gt;0&lt;/s:key&gt;
        &lt;s:key name="version"&gt;69.420&lt;/s:key&gt;
        &lt;s:key name="visible"&gt;1&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## apps/local
{: name='appslocal'}

Creates a new application.

	[POST] apps/local

### Parameters

author
: _Optional_ **String** For apps you intend to post to Splunkbase, enter the username of your splunk.com account.<br/><br/>For internal-use-only apps, include your full name and/or contact info (for example, email).

description
: _Optional_ **String** Short explanatory string displayed underneath the app's title in Launcher.<br/><br/>Typically, short descriptions of 200 characters are more effective.

label
: _Optional_ **String** Defines the name of the app shown in the Splunk GUI and Launcher.<br/><br/>* Must be between 5 and 80 characters.
* Must not include "Splunk For" prefix.<br/><br/>Examples of good labels:
    IMAP
    SQL Server Integration Services
    FISMA Compliance

manageable
: _Optional_ **Boolean**  Indicates that the Splunk Manager can manage the app.

name
: _Required_ **String** Name of the application to create. The name you select becomes the name of the folder on disk that contains the app.

template
: _Optional_ **Enum** Valid values: (barebones &#124; sample_app)<br/><br/>Indicates the app template to use when creating the app.<br/><br/>Specify either of the following:<br/><br/>  barebones - contains basic framework for an app
  sample_app - contains example views and searches<br/><br/>You can also specify any valid app template you may have previously added.

visible
: _Optional_ **Boolean**  Indicates if the app is visible and navigable from the UI.<br/><br/>Visible apps require at least 1 view that is available from the UI

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
| **403** | Insufficient permissions to create local app. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

This example creates a new application, "myApp," based on sample_app template.
The application appears as "My Application" in Splunk Web, is navigable in Splunk Web, and is managed by the Splunk Manager.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/apps/local \
	-d name=myApp \
	-d label="My Application" \
	-d manageable=1 \
	-d template=sample_app \
	-d visible=1
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title/&gt;
  &lt;id&gt;https://localhost:8089/services/apps/local&lt;/id&gt;
  &lt;updated&gt;2011-07-11T19:15:35-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/apps/local/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;Created&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/apps/local/Created&lt;/id&gt;
    &lt;updated&gt;2011-07-11T19:15:35-07:00&lt;/updated&gt;
    &lt;link href="/services/apps/local/Created" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/apps/local/Created" rel="list"/&gt;
    &lt;link href="/services/apps/local/Created" rel="edit"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="name"&gt;myApp&lt;/s:key&gt;
        &lt;s:key name="template"&gt;sample_app&lt;/s:key&gt;
        &lt;s:key name="url"&gt;http://mrt:8001/app/myApp&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## apps/local/{name}
{: name='appslocalname'}

Removes the locally installed app with the name specified by {name}.

After deleting an app, there might also be some manual cleanup. See "Uninstall an app" in the "Meet Splunk Web and Splunk apps" section of the Splunk Admin manual.

	[DELETE] apps/local/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deleted successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to delete local app. |
|--------------------------------
| **404** | Local app does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

This example removes the locally installed app, myApp.
After deleting the app, you can use the GET operation for /apps/local to confirm that the app is no longer installed.

#### Request
<pre class='terminal'>
curl -k -u admin:pass --request DELETE https://localhost:8089/services/apps/local/myApp
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;localapps&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/apps/local&lt;/id&gt;
  &lt;updated&gt;2011-07-11T19:16:36-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/apps/local/_new" rel="create"/&gt;
  &lt;link href="/services/apps/local/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## apps/local/{name}
{: name='appslocalname'}

Returns information about the locally installed app with the name specified by {name}.

	[GET] apps/local/{name}

### Parameters

refresh
: _Optional_ **Boolean** Reloads the objects contained in the locally installed app with the name specified by {name}.

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view local app. |
|--------------------------------
| **404** | Local app does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Returns information about the locally installed Splunk search app.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/apps/local/search
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;localapps&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/apps/local&lt;/id&gt;
  &lt;updated&gt;2011-07-11T19:15:49-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/apps/local/_new" rel="create"/&gt;
  &lt;link href="/services/apps/local/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;search&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/apps/local/search&lt;/id&gt;
    &lt;updated&gt;2011-07-11T19:15:49-07:00&lt;/updated&gt;
    &lt;link href="/services/apps/local/search" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/apps/local/search" rel="list"/&gt;
    &lt;link href="/services/apps/local/search/_reload" rel="_reload"/&gt;
    &lt;link href="/services/apps/local/search" rel="edit"/&gt;
    &lt;link href="/services/apps/local/search" rel="remove"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="author"&gt;Splunk&lt;/s:key&gt;
        &lt;s:key name="check_for_updates"&gt;1&lt;/s:key&gt;
        &lt;s:key name="configured"&gt;1&lt;/s:key&gt;
        &lt;s:key name="description"&gt;
&lt;![CDATA[The Search app is Splunk's default interface for searching and analyzing IT data. It allows you to index data into Splunk, add knowledge, build reports, and create alerts. The Search app can be used across many areas of IT including application management, operations management, security, and compliance.]]&gt;        &lt;/s:key&gt;
        &lt;s:key name="disabled"&gt;0&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:attributes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="optionalFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;author&lt;/s:item&gt;
                &lt;s:item&gt;check_for_updates&lt;/s:item&gt;
                &lt;s:item&gt;description&lt;/s:item&gt;
                &lt;s:item&gt;label&lt;/s:item&gt;
                &lt;s:item&gt;manageable&lt;/s:item&gt;
                &lt;s:item&gt;version&lt;/s:item&gt;
                &lt;s:item&gt;visible&lt;/s:item&gt;
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
        &lt;s:key name="label"&gt;Search&lt;/s:key&gt;
        &lt;s:key name="manageable"&gt;1&lt;/s:key&gt;
        &lt;s:key name="state_change_requires_restart"&gt;0&lt;/s:key&gt;
        &lt;s:key name="version"&gt;4.3&lt;/s:key&gt;
        &lt;s:key name="visible"&gt;1&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## apps/local/{name}
{: name='appslocalname'}

Updates the app specified by {name}.

	[POST] apps/local/{name}

### Parameters

author
: _Optional_ **INHERITED** INHERITED

check_for_updates
: _Optional_ **Boolean** If set to true, Splunk checks Splunkbase for updates to this app.

description
: _Optional_ **INHERITED** INHERITED

label
: _Optional_ **INHERITED** INHERITED

manageable
: _Optional_ **INHERITED** INHERITED

version
: _Optional_ **version string** Specifies the version for the app. Each release of an app must change the version number.<br/><br/>Version numbers are a number followed by a sequence of numbers or dots. Pre-release versions can append a space and a single-word suffix like "beta2". Examples:<br/><br/>   1.2
   11.0.34
   2.0 beta
   1.3 beta2
   1.0 b2
   12.4 alpha
   11.0.34.234.254

visible
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
| **403** | Insufficient permissions to edit local app. |
|--------------------------------
| **404** | Local app does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

This example updates the label of the app MyApp. MyApp was created for the example to the POST operation of apps/local.
The application now appears as "My Killer App" in Splunk Web.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/apps/local/myApp \
	-d label="My Killer App"
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title/&gt;
  &lt;id&gt;https://localhost:8089/services/apps/local&lt;/id&gt;
  &lt;updated&gt;2011-07-11T19:16:08-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/apps/local/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## apps/local/{name}/setup
{: name='appslocalnamesetup'}

Returns any set up information for the app specified by {name}..

	[GET] apps/local/{name}/setup

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Set up information returned successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to setup app. |
|--------------------------------
| **404** | App does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Returns information about the setup script for the unix app.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/apps/local/unix/setup
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;localapps&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/apps/local&lt;/id&gt;
  &lt;updated&gt;2011-07-13T11:24:35-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/apps/local/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;unix&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/unix/apps/local/unix&lt;/id&gt;
    &lt;updated&gt;2011-07-13T11:24:35-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/unix/apps/local/unix" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;nobody&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/unix/apps/local/unix/setup" rel="edit"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="/admin/script/.%252Fbin%252Fcpu.sh/enabled"&gt;1&lt;/s:key&gt;
        &lt;s:key name="/admin/script/.%252Fbin%252Fcpu.sh/interval"&gt;30&lt;/s:key&gt;
        &lt;s:key name="/admin/script/.%252Fbin%252Fdf.sh/enabled"&gt;1&lt;/s:key&gt;
        &lt;s:key name="/admin/script/.%252Fbin%252Fdf.sh/interval"&gt;300&lt;/s:key&gt;
        &lt;s:key name="/admin/script/.%252Fbin%252Fhardware.sh/enabled"&gt;1&lt;/s:key&gt;
        &lt;s:key name="/admin/script/.%252Fbin%252Fhardware.sh/interval"&gt;36000&lt;/s:key&gt;
        &lt;s:key name="/admin/script/.%252Fbin%252Finterfaces.sh/enabled"&gt;1&lt;/s:key&gt;
        &lt;s:key name="/admin/script/.%252Fbin%252Finterfaces.sh/interval"&gt;60&lt;/s:key&gt;
        &lt;s:key name="/admin/script/.%252Fbin%252Fiostat.sh/enabled"&gt;1&lt;/s:key&gt;
        &lt;s:key name="/admin/script/.%252Fbin%252Fiostat.sh/interval"&gt;60&lt;/s:key&gt;
        &lt;s:key name="/admin/script/.%252Fbin%252Flastlog.sh/enabled"&gt;1&lt;/s:key&gt;
        &lt;s:key name="/admin/script/.%252Fbin%252Flastlog.sh/interval"&gt;300&lt;/s:key&gt;
        &lt;s:key name="/admin/script/.%252Fbin%252Flsof.sh/enabled"&gt;1&lt;/s:key&gt;
        &lt;s:key name="/admin/script/.%252Fbin%252Flsof.sh/interval"&gt;600&lt;/s:key&gt;
        &lt;s:key name="/admin/script/.%252Fbin%252Fnetstat.sh/enabled"&gt;1&lt;/s:key&gt;
        &lt;s:key name="/admin/script/.%252Fbin%252Fnetstat.sh/interval"&gt;60&lt;/s:key&gt;
        &lt;s:key name="/admin/script/.%252Fbin%252FopenPorts.sh/enabled"&gt;1&lt;/s:key&gt;
        &lt;s:key name="/admin/script/.%252Fbin%252FopenPorts.sh/interval"&gt;300&lt;/s:key&gt;
        &lt;s:key name="/admin/script/.%252Fbin%252Fpackage.sh/enabled"&gt;1&lt;/s:key&gt;
        &lt;s:key name="/admin/script/.%252Fbin%252Fpackage.sh/interval"&gt;3600&lt;/s:key&gt;
        &lt;s:key name="/admin/script/.%252Fbin%252Fprotocol.sh/enabled"&gt;1&lt;/s:key&gt;
        &lt;s:key name="/admin/script/.%252Fbin%252Fprotocol.sh/interval"&gt;60&lt;/s:key&gt;
        &lt;s:key name="/admin/script/.%252Fbin%252Fps.sh/enabled"&gt;1&lt;/s:key&gt;
        &lt;s:key name="/admin/script/.%252Fbin%252Fps.sh/interval"&gt;30&lt;/s:key&gt;
        &lt;s:key name="/admin/script/.%252Fbin%252Frlog.sh/enabled"&gt;1&lt;/s:key&gt;
        &lt;s:key name="/admin/script/.%252Fbin%252Frlog.sh/interval"&gt;60&lt;/s:key&gt;
        &lt;s:key name="/admin/script/.%252Fbin%252Ftime.sh/enabled"&gt;1&lt;/s:key&gt;
        &lt;s:key name="/admin/script/.%252Fbin%252Ftime.sh/interval"&gt;21600&lt;/s:key&gt;
        &lt;s:key name="/admin/script/.%252Fbin%252Ftop.sh/enabled"&gt;1&lt;/s:key&gt;
        &lt;s:key name="/admin/script/.%252Fbin%252Ftop.sh/interval"&gt;60&lt;/s:key&gt;
        &lt;s:key name="/admin/script/.%252Fbin%252FusersWithLoginPrivs.sh/enabled"&gt;1&lt;/s:key&gt;
        &lt;s:key name="/admin/script/.%252Fbin%252FusersWithLoginPrivs.sh/interval"&gt;3600&lt;/s:key&gt;
        &lt;s:key name="/admin/script/.%252Fbin%252Fvmstat.sh/enabled"&gt;1&lt;/s:key&gt;
        &lt;s:key name="/admin/script/.%252Fbin%252Fvmstat.sh/interval"&gt;60&lt;/s:key&gt;
        &lt;s:key name="/admin/script/.%252Fbin%252Fwho.sh/enabled"&gt;1&lt;/s:key&gt;
        &lt;s:key name="/admin/script/.%252Fbin%252Fwho.sh/interval"&gt;150&lt;/s:key&gt;
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
                &lt;s:item&gt;.*&lt;/s:item&gt;
              &lt;/s:list&gt;
            &lt;/s:key&gt;
          &lt;/s:dict&gt;
        &lt;/s:key&gt;
        &lt;s:key name="eai:setup"&gt;
&lt;![CDATA[&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;SetupInfo&gt;
  &lt;block title="Welcome to the Splunk for nix App"&gt;
    &lt;text&gt;The Splunk for nix app provides some sample searches and reports to boot-strap your use of Splunk for Unix host management. 
	       To work, it needs certain inputs enabled. These system metrics drive the sample dashboards.
	       Please review and confirm the inputs below before proceeding.&lt;/text&gt;
  &lt;/block&gt;
  &lt;block title="CPU Stats (sar / mpstat / etc.)" endpoint="admin/script" entity=".%252Fbin%252Fcpu.sh"&gt;
    &lt;input field="interval" id="/admin/script/.%252Fbin%252Fcpu.sh/interval"&gt;
      &lt;label&gt;Polling Interval (sec)&lt;/label&gt;
      &lt;type&gt;text&lt;/type&gt;
    &lt;/input&gt;
    &lt;input field="enabled" id="/admin/script/.%252Fbin%252Fcpu.sh/enabled"&gt;
      &lt;label&gt;Enable&lt;/label&gt;
      &lt;type&gt;bool&lt;/type&gt;
    &lt;/input&gt;
  &lt;/block&gt;
 . . .
  &lt;block title="Time Query (date, ntpdate -q)" endpoint="admin/script" entity=".%252Fbin%252Ftime.sh"&gt;
    &lt;input field="interval" id="/admin/script/.%252Fbin%252Ftime.sh/interval"&gt;
      &lt;label&gt;Polling Interval (sec)&lt;/label&gt;
      &lt;type&gt;text&lt;/type&gt;
    &lt;/input&gt;
    &lt;input field="enabled" id="/admin/script/.%252Fbin%252Ftime.sh/enabled"&gt;
      &lt;label&gt;Enable&lt;/label&gt;
      &lt;type&gt;bool&lt;/type&gt;
    &lt;/input&gt;
  &lt;/block&gt;
  &lt;block title="Linux Audit Log (/var/log/audit/audit.log | ausearch)" endpoint="admin/script" entity=".%252Fbin%252Frlog.sh"&gt;
    &lt;input field="interval" id="/admin/script/.%252Fbin%252Frlog.sh/interval"&gt;
      &lt;label&gt;Polling Interval (sec)&lt;/label&gt;
      &lt;type&gt;text&lt;/type&gt;
    &lt;/input&gt;
    &lt;input field="enabled" id="/admin/script/.%252Fbin%252Frlog.sh/enabled"&gt;
      &lt;label&gt;Enable&lt;/label&gt;
      &lt;type&gt;bool&lt;/type&gt;
    &lt;/input&gt;
  &lt;/block&gt;
  &lt;block title="Warning"&gt;
    &lt;text&gt;Submitting this form can take a long time.  Please be patient and wait for it to complete before navigating away from this page.&lt;/text&gt;
  &lt;/block&gt;
&lt;/SetupInfo&gt;
]]&gt;        &lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## apps/local/{name}/update
{: name='appslocalnameupdate'}

Returns any update information available for the app specified by {name}.

	[GET] apps/local/{name}/update

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Update information for the app was returned successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to update app. |
|--------------------------------
| **404** | App does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Returns update information for the Splunk Deployment Monitior app.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/apps/local/SplunkDeploymentMonitor/update
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;localapps&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/apps/local&lt;/id&gt;
  &lt;updated&gt;2011-07-13T11:27:41-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/apps/local/_new" rel="create"/&gt;
  &lt;link href="/services/apps/local/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;SplunkDeploymentMonitor&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/apps/local/SplunkDeploymentMonitor&lt;/id&gt;
    &lt;updated&gt;2011-07-13T11:27:41-07:00&lt;/updated&gt;
    &lt;link href="/services/apps/local/SplunkDeploymentMonitor" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/apps/local/SplunkDeploymentMonitor" rel="list"/&gt;
    &lt;link href="/services/apps/local/SplunkDeploymentMonitor/_reload" rel="_reload"/&gt;
    &lt;link href="/services/apps/local/SplunkDeploymentMonitor" rel="edit"/&gt;
    &lt;link href="/services/apps/local/SplunkDeploymentMonitor" rel="remove"/&gt;
    &lt;link href="/services/apps/local/SplunkDeploymentMonitor/update" rel="update"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="update.appurl"&gt;
          https://splunkbase.splunk.com/api/apps:download/Splunk+Deployment+Monitor/4.2.2/SplunkDeploymentMonitor_for_4.2.2.tgz
        &lt;/s:key&gt;
        &lt;s:key name="update.checksum"&gt;039fc2a1bac2da5c056b7340c98ab168&lt;/s:key&gt;
        &lt;s:key name="update.checksum.type"&gt;md5&lt;/s:key&gt;
        &lt;s:key name="update.homepage"&gt;https://splunkbase.splunk.com/apps/Splunk+Deployment+Monitor&lt;/s:key&gt;
        &lt;s:key name="update.implicit_id_required"&gt;1&lt;/s:key&gt;
        &lt;s:key name="update.name"&gt;Splunk Deployment Monitor&lt;/s:key&gt;
        &lt;s:key name="update.size"&gt;31845&lt;/s:key&gt;
        &lt;s:key name="update.version"&gt;4.2.2&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>


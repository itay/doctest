---
title: How to use the Splunk REST API
---

# How to use the Splunk REST API

## HTTP operations supported

Splunk supports HTTP GET, POST, and DELETE operations for creating and running searches and for accessing and managing Splunk resources.

## REST API examples

The Splunk REST API Reference examples use [cURL](http://curl.haxx.se/) to illustrate REST access to Splunk resources. The following request creates an index:

<pre class="terminal">
curl -k -u admin:pass -d name=Shadow https://localhost:8089/services/data/indexes
</pre>

These are the parameters we use in the `cURL` invocation above:

* `-k` Explicitly allow curl to perform insecure SSL connections and transfers.
* `-u` Specify &lt;User:Password&gt; for the request.
* `-d` For passing arguments in POST operations

However, you can use [wget](http://www.gnu.org/s/wget/), [libcurl](http://curl.haxx.se/libcurl/c/) or any other method to access the REST API. Here is the same request using wget:

<pre class="terminal">
wget -q -O - --user=admin --password=pass --no-check-certificate   \
     https://localhost:8089/services/data/indexes --post-data="name=Shadow"
</pre>

These are the parameters we use in the `wget` invocation above:

* `-q` quiet
* `-O -` output to standard out
* `--user` --password` specify user and password
* `--no-check-certificate` Explicitly allow insecure SSL connections and transfers
* `--post-data` For passing arguments in POST operations

## Atom Feed response
With few exceptions, the Splunk responses are returned in in the [Atom Syndication Format](http://xml.resource.org/public/rfc/html/rfc4287.html), also known as an Atom Feed.  The Atom Feed contains a series of entries, each entry corresponds to a Splunk resource and contains information about the resource. 

For example, this GET operation and response lists the users on a Splunk instance:


<pre class="terminal">
curl -k -u admin:pass https://localhost:8089/services/authentication/users
</pre>

The response is a list of users:

    <feed xmlns="http://www.w3.org/2005/Atom"
          xmlns:s="http://dev.splunk.com/ns/rest"
          xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/">
      <title>users</title>
      <id>https://localhost:8085/services/authentication/users</id>
      <updated>2011-07-19T10:54:01-07:00</updated>
      <generator version="102824"/>
      <author>
        <name>Splunk</name>
      </author>
      <link href="/services/authentication/users/_new" rel="create"/>
      <!-- opensearch nodes elided for brevity. -->
      <s:messages/>
      <entry>
        <title>admin</title>
        <id>https://localhost:8085/services/authentication/users/admin</id>
        <updated>2011-07-19T10:54:01-07:00</updated>
        <link href="/services/authentication/users/admin" rel="alternate"/>
        <author>
          <name>system</name>
        </author>
        <link href="/services/authentication/users/admin" rel="list"/>
        <link href="/services/authentication/users/admin" rel="edit"/>
        <content type="text/xml">
          <s:dict>
            <s:key name="defaultApp">launcher</s:key>
            <s:key name="defaultAppIsUserOverride">1</s:key>
            <s:key name="defaultAppSourceRole">system</s:key>
            <!-- eai:acl nodes elided for brevity. -->
            <s:key name="email">changeme@example.com</s:key>
            <s:key name="password">********</s:key>
            <s:key name="realname">Administrator</s:key>
            <s:key name="roles">
              <s:list>
                <s:item>admin</s:item>
              </s:list></s:key>
            <s:key name="type">Splunk</s:key>
            <s:key name="tz"></s:key>
          </s:dict>
        </content>
      </entry>
      <entry>
        <title>splunker</title>
        <id>https://localhost:8085/services/authentication/users/splunker</id>
        <updated>2011-07-19T10:54:01-07:00</updated>
        <link href="/services/authentication/users/splunker" rel="alternate"/>
        <author>
          <name>system</name>
        </author>
        <link href="/services/authentication/users/splunker" rel="list"/>
        <link href="/services/authentication/users/splunker" rel="edit"/>
        <link href="/services/authentication/users/splunker" rel="remove"/>
        <content type="text/xml">
          <s:dict>
            <s:key name="defaultApp">launcher</s:key>
            <s:key name="defaultAppIsUserOverride">0</s:key>
            <s:key name="defaultAppSourceRole">system</s:key>
            <!-- eai:acl nodes elided for brevity. -->
            <s:key name="email"></s:key>
            <s:key name="password">********</s:key>
            <s:key name="realname"></s:key>
            <s:key name="roles">
              <s:list>
                <s:item>user</s:item>
              </s:list>
            </s:key>
            <s:key name="type">Splunk</s:key>
            <s:key name="tz"></s:key>
          </s:dict>
        </content>
      </entry>
    </feed>

**Note**: For some search endpoints, you can specify a response in JSON or CSV formats. There are also some endpoints, such as <code>auth/login</code>, that return a response in simple XML.

## Open search nodes and access control lists

In the example response above, the Open Search and Access Control List (ACL) nodes have been elided for brevity. These nodes are present in most responses, but typically are not essential to understand the endpoint.

Use the Open Search section of the response if you are paging the response. The ACL nodes define permissions for accessing the endpoint.

The Splunk API Reference Manual elides the Open Search and ACL nodes from the example responses.

## Operation parameters

Many operations have required and optional parameters. The Splunk REST API Reference lists all available parameters, default values if available, and a description. Required parameters are indicated with a check.

## GET parameter list

Most GET operations have a standard set of parameters for returning information from an endpoint.

|---------------+---------+-----------+---------+-------------|
| Name          | Type    | Required  | Default | Description |
|:--------------|:--------|:----------|:--------|:------------|
| **count**     | Number  | false     | 30      | Indicates the maximum number of entries to return. To return all entries, specify 0. |
|---------------+---------+-----------+---------+-------------|
| **offset**    | Number  | false     | 0       | Index of the first entry to return. |
|---------------+---------+-----------+---------+-------------|
| **search**    | String  | false     |         | Boolean predicate to filter results. |
|---------------+---------+-----------+---------+-------------|
| **sort_dir**  | Enum    | false     | asc     | Valid values: (asc &#124; desc) <br/><br/>Indicates whether to sort the entries returned in ascending or descending order. |
|---------------+---------+-----------+---------+-------------|
| **sort_key**  | String  | false     | name    | Field to sort by. |
|---------------+---------+-----------+---------+-------------|
| **sort_mode** | Enum    | false     | auto    | Valid values: (auto &#124; alpha &#124; alpha_case &#124; num) <br/><br/>Indicates the collating sequence for sorting the returned entries. |
|---------------+---------+-----------+---------+-------------|

## URI-encoding of endpoints
For some operations, endpoints must be specially URI-encoded before they can be used to access Splunk resources. 

### Pathnames in endpoint
Typically parameters that specify a path or URL as part of the endpoint require URI-encoding. For example, consider the GET operation for this endpoint:

<code>/services/data/inputs/monitor/{name}</code>

To access this endpoint with the value of "/var/log" for {name}, specify the following URI-encoding:

<pre class="terminal">
curl -k -u admin:pass https://localhost:8089/services/data/inputs/monitor/%252Fvar%252Flog
</pre>

Alternatively, you can access the endpoint by quoting the value for {name}:

<pre class="terminal">
curl -k -u admin:pass https://localhost:8085/services/data/inputs/monitor/?"var/log"
</pre>

### `search` parameter

Endpoints that specify a search string as a POST parameter require URI-encoding if the search string contains the following characters: =, &, ?, %

Those characters are otherwise interpreted as part of the HTTP request.

For example:

<pre class="terminal">
curl -k -u admin:pass https://localhost:8089/services/saved/searches     \
     --data-urlencode name=MySavedSearch -d search="index=_internal source=*metrics.log"
</pre>

## Response status

The Splunk REST API Reference lists response codes for each operation. In some error cases, the response body contains additional descriptive information about the corresponding error.

Here are some typical status codes returned.

| Status Code       | Description                                                                                   |
|:------------------|:----------------------------------------------------------------------------------------------|
| **200**           | Operation successful.                                                                         |
|----
| **201**           | Created successfully.                                                                         |
|----
| **204**           | Successful, but no content was returned. |
|----
| **400**           | Request error.  See response body for explanation. |
|----
| **401**           | Authentication failure: must pass valid credentials with request. Session may have timed out. |
|----
| **402**           | The Splunk license in use has disabled this feature. |
|----
| **403**           | Insufficient permissions to view/edit/create/disable/delete. |
|----
| **404**           | Object does not exist. |
|----
| **405**           | Method Not Allowed (for example, supports GET but not POST) | 
|----
| **409**           | Request error: this operation is invalid for this item.  See response body for explanation. |
|----
| **500**           | Internal server error.  See response body for details. |
|----
| **503**           | This feature has been disabled in Splunk configuration files. |
|----

## Authentication

Before you can access Splunk resources, you must authenticate yourself to the splunkd server, using your username and password for the Splunk instance. 

splunkd supports token-based authentication using the standard HTTPAuthorization header. This is the recommended method for most programmatic accesses against the API.

Obtain a session key at the /services/auth/login endpoint:

<pre class="terminal">
curl -k -u admin:pass  https://localhost:8089/services/auth/login   \
     -d username=admin -d password=pass
</pre>

The response is a session key:

    <response>
      <sessionKey>192fd3e46a31246da7ea7f109e7f95fd</sessionKey>
    </response>

Insert the session key into the Authorization header of every subsequent request, as follows: <br/>
<code>Authorization: Splunk 192fd3e46a31246da7ea7f109e7f95fd</code>
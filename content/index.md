---
title: About the Splunk REST API
---

# About the Splunk REST API

## Splunk's API is RESTful 

Splunk's API is RESTful, which means it uses HTTP requests to interact with resources within Splunk. Both Splunk Web and the Splunk CLI use Splunk’s REST API to communicate with a Splunk instance. You can use the REST API to configure and manage a Splunk instance, create and run searches in Splunk, or create your own applications that interact with Splunk.

You can use any language or tool that supports HTTP calls to access the Splunk REST API. 

**Note**: The Splunk REST API Reference examples use [cURL](http://curl.haxx.se/) to illustrate REST access to Splunk resources. However, you can use [wget](http://www.gnu.org/s/wget/), [libcurl](http://curl.haxx.se/libcurl/c/) or any other method to access the REST API.


## Accessing Splunk resources

Splunk resources are identified as URLs that map to endpoints. You can access the resources using a web browser, curl or other command line tools, or through program language tools.

splunkd is the server for the REST API endpoints. The Splunk REST API Reference  categorizes and lists the endpoints available for development. 

You can view the endpoints available in a Splunk instance using a web browser pointing to  the Splunk management port.

	https://localhost:8089/services

For example, the following curl command creates a search:

<pre class="terminal">curl -u admin:pass -k https://localhost:8089/services/search/jobs -d "search=search *"</pre>

**Note**: 8089 is the default Splunk management port. The management port in your Splunk installation may vary. Examples in this reference use the default managment port.

## API differences between Splunk 4.3 and Splunk 4.2
This preview version of the Splunk REST API Reference contains endpoints that are found in Splunk 4.3. 

All endpoints in Slunk 4.3 are available in Splunk 4.2, but the following endpoints have been implemented differently:

### Endpoints available in Splunk 4.2 but at a deprecated URL

`/directory` (Splunk 4.3) <br/>
`/admin/directory` (Splunk 4.2)

Provides access to user configurable objects

`storage/passwords` (Splunk 4.3) <br/>
`admin/passwords` (Splunk 4.2)

Allows for management of secure credentials 

### Parameters to endpoints available only in Splunk 4.3
`authentication/users` (`tz` parameter)

In Splunk 4.3 only, this endpoint contains the `tz` parameter to configure the timezone for a user.
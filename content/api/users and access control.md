<a name='authlogin'/>

## auth/login

Returns a session key to be used when making REST calls to splunkd.

	[POST] auth/login

### Parameters

password
: _Optional_ **String** The password for the user specified with <code>username</code>.

username
: _Optional_ **String** The Splunk account username.

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Authenticated successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------

### Example

Return a session key for the admin user that can be used in future request operations.

#### Request
<pre class='terminal'>
curl -k -u admin:pass  https://localhost:8089/services/auth/login \
	-d username=admin \
	-d password=pass
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;response&gt;
  &lt;sessionKey&gt;192fd3e46a31246da7ea7f109e7f95fd&lt;/sessionKey&gt;
&lt;/response&gt;
</code></pre>

<a name='authenticationauthtokens'/>

## authentication/auth-tokens

Does nothing.  Is a placeholder for potential future information.

	[GET] authentication/auth-tokens

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
| **403** | Insufficient permissions to view auth-tokens. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Simply returns successfully, with a mostly empty XML feed.  This action is reserved for potential future usage.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/authentication/auth-tokens
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;auth-tokens&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/authentication/auth-tokens&lt;/id&gt;
  &lt;updated&gt;2011-07-19T19:44:28-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/authentication/auth-tokens/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## authentication/auth-tokens

Creates an authentication token

	[POST] authentication/auth-tokens

### Parameters

name
: _Required_ **String** This is a special key, always being "_create"

nonce
: _Required_ **String** An alphanumeric string representing a unique identifier for this request

peername
: _Optional_ **String** The name of the splunk server requesting this token

sig
: _Required_ **String** A cryptographic signature of the "userid", "username", "nonce", and "ts" arguments

ts
: _Required_ **Number** The unix time at which the signature was created

userid
: _Required_ **String** The name of the user requesting this token

username
: _Required_ **String** The name of the user requesting this token

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
| **403** | Insufficient permissions to create auth-tokens. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Creates an authentication token.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/authentication/auth-tokens \
	-d name=_create \
	-d nonce=787ab24cbd6ba0f295821bb7f41a138d \
	-d sig=VRoD6rNqJUisbWwTtF%2BQZbDsS%2BDRZpLR60Q3oIywqqvo2fzIgFF1yfhLGRyPtBtBg4A63gjL2SuQC9Xf1yXomB56poCaTZ74fmBIgGsszu5WNHxTgIK7apjxKmPFS9I%2Bmf4lUzrl82M7dnED1t8kRuzsZYNLl20fzy6NiEabn1g= \
	-d peername=marklar-staging \
	-d ts=1310276274 \
	-d userid=splunk-system-user \
	-d username=splunk-system-user
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;auth-tokens&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/authentication/auth-tokens&lt;/id&gt;
  &lt;updated&gt;2011-07-15T15:03:45-07:00&lt;/updated&gt;
  &lt;generator version="103645"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/authentication/auth-tokens/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;splunk-system-user&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/authentication/auth-tokens/splunk-system-user&lt;/id&gt;
    &lt;updated&gt;2011-07-15T15:03:45-07:00&lt;/updated&gt;
    &lt;link href="/services/authentication/auth-tokens/splunk-system-user" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/authentication/auth-tokens/splunk-system-user" rel="list"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="splunk-system-user"&gt;8a63fccda33279c887094318d0b0j503&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

<a name='authenticationcurrentcontext'/>

## authentication/current-context

Lists one item named "context" which contains the name of the current user

	[GET] authentication/current-context

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
| **403** | Insufficient permissions to view current-context. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Retrieves the username of the authenticated session owner.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/authentication/current-context
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;current-context&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/authentication/current-context&lt;/id&gt;
  &lt;updated&gt;2011-07-10T23:28:20-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;context&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/authentication/current-context/context&lt;/id&gt;
    &lt;updated&gt;2011-07-10T23:28:20-07:00&lt;/updated&gt;
    &lt;link href="/services/authentication/current-context/context" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/authentication/current-context/context" rel="list"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="username"&gt;admin&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

<a name='authenticationcurrentcontextname'/>

## authentication/current-context/{name}

Displays an item (always named "context") that contains the name of the current user.

	[GET] authentication/current-context/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view current-context. |
|--------------------------------
| **404** | current-context does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Identical to retrieving authentication/current-context.  Note that "context" is the only valid name here.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/authentication/current-context/context
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>

</code></pre>

<a name='authenticationhttpauthtokens'/>

## authentication/httpauth-tokens

List all currently active session tokens

	[GET] authentication/httpauth-tokens

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
| **403** | Insufficient permissions to view httpauth-tokens. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

List the active session tokens for this Splunk instance.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/authentication/httpauth-tokens
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;httpauth-tokens&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/authentication/httpauth-tokens&lt;/id&gt;
  &lt;updated&gt;2011-07-12T13:51:56-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;795fc961f9cee34da3401cbe68f08659&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/authentication/httpauth-tokens/795fc961f9cee34da3401cbe68f08659&lt;/id&gt;
    &lt;updated&gt;2011-07-12T13:51:56-07:00&lt;/updated&gt;
    &lt;link href="/services/authentication/httpauth-tokens/795fc961f9cee34da3401cbe68f08659" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/authentication/httpauth-tokens/795fc961f9cee34da3401cbe68f08659" rel="list"/&gt;
    &lt;link href="/services/authentication/httpauth-tokens/795fc961f9cee34da3401cbe68f08659" rel="remove"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="authString"&gt;795fc961f9cee34da3401cbe68f08659&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="searchId"/&gt;
        &lt;s:key name="timeAccessed"&gt;Tue Jul 12 13:51:56 2011&lt;/s:key&gt;
        &lt;s:key name="userName"&gt;admin&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

<a name='authenticationhttpauthtokensname'/>

## authentication/httpauth-tokens/{name}

End the session associated with this token

	[DELETE] authentication/httpauth-tokens/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deleted successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to delete httpauth-token. |
|--------------------------------
| **404** | httpauth-token does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

End the session by deleting the session token.

#### Request
<pre class='terminal'>
curl -k -u admin:pass --request DELETE \
	https://localhost:8089/services/authentication/httpauth-tokens/ddc919fd970184455f6c21819d5b1c82
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;httpauth-tokens&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/authentication/httpauth-tokens&lt;/id&gt;
  &lt;updated&gt;2011-07-12T13:57:08-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## authentication/httpauth-tokens/{name}

Get information about a specific session token

	[GET] authentication/httpauth-tokens/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view httpauth-tokens. |
|--------------------------------
| **404** | httpauth-token does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Get information about the specified session token.

#### Request
<pre class='terminal'>
curl -k -u admin:pass \
	https://localhost:8089/services/authentication/httpauth-tokens/ddc919fd970184455f6c21819d5b1c82
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;httpauth-tokens&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/authentication/httpauth-tokens&lt;/id&gt;
  &lt;updated&gt;2011-07-12T13:54:44-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;ddc919fd970184455f6c21819d5b1c82&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/authentication/httpauth-tokens/ddc919fd970184455f6c21819d5b1c82&lt;/id&gt;
    &lt;updated&gt;2011-07-12T13:54:44-07:00&lt;/updated&gt;
    &lt;link href="/services/authentication/httpauth-tokens/ddc919fd970184455f6c21819d5b1c82" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/authentication/httpauth-tokens/ddc919fd970184455f6c21819d5b1c82" rel="list"/&gt;
    &lt;link href="/services/authentication/httpauth-tokens/ddc919fd970184455f6c21819d5b1c82" rel="remove"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="authString"&gt;ddc919fd970184455f6c21819d5b1c82&lt;/s:key&gt;
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
        &lt;s:key name="searchId"/&gt;
        &lt;s:key name="timeAccessed"&gt;Tue Jul 12 13:50:29 2011&lt;/s:key&gt;
        &lt;s:key name="userName"&gt;splunk-system-user&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

<a name='authenticationusers'/>

## authentication/users

Returns a list of all the users registered on the server.

	[GET] authentication/users

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
| **403** | Insufficient permissions to view users. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Returns a list of all users registered on this Splunk instance.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/authentication/users
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;users&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/authentication/users&lt;/id&gt;
  &lt;updated&gt;2011-07-08T14:07:58-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/authentication/users/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;admin&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/authentication/users/admin&lt;/id&gt;
    &lt;updated&gt;2011-07-08T14:07:58-07:00&lt;/updated&gt;
    &lt;link href="/services/authentication/users/admin" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/authentication/users/admin" rel="list"/&gt;
    &lt;link href="/services/authentication/users/admin" rel="edit"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="defaultApp"&gt;launcher&lt;/s:key&gt;
        &lt;s:key name="defaultAppIsUserOverride"&gt;0&lt;/s:key&gt;
        &lt;s:key name="defaultAppSourceRole"&gt;system&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="email"&gt;changeme@example.com&lt;/s:key&gt;
        &lt;s:key name="password"&gt;********&lt;/s:key&gt;
        &lt;s:key name="realname"&gt;Administrator&lt;/s:key&gt;
        &lt;s:key name="roles"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;admin&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
        &lt;s:key name="type"&gt;Splunk&lt;/s:key&gt;
        &lt;s:key name="tz"/&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## authentication/users

Creates a new user.

	[POST] authentication/users

### Parameters

createrole
: _Optional_ **String** The name of a role to create for the user. After creating the role, you can later edit that role to specify what access that user has to Splunk.

defaultApp
: _Optional_ **String** Specify a default app for the user.<br/><br/>The default app specified here overrieds the default app inherited from the user's roles.

email
: _Optional_ **String** Specify an email address for the user.

name
: _Required_ **String** The Splunk username for the user to login to splunk.<br/><br/>usernames must be unique on the system.

password
: _Required_ **String** The user's password.

realname
: _Optional_ **String** A full name to associate with the user.

roles
: _Optional_ **String** A role to assign to this user. To assign multiple roles, send them in separate 'roles' arguments.

tz
: _Optional_ **String** Timezone to use when displaying dates for this user.

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
| **403** | Insufficient permissions to create user. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Creates the user named splunker, setting the password to changeme and setting the role to user.
After creating the role, perform the GET operation on /authentication/users/splunker to see details about the user.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/authentication/users \
	-d name=splunker \
	-d password=changeme \
	-d roles=user
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;users&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/authentication/users&lt;/id&gt;
  &lt;updated&gt;2011-07-08T14:08:17-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/authentication/users/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages&gt;
    &lt;s:msg type="WARN"&gt;This user will be disabled after the Enterprise Trial License expires&lt;/s:msg&gt;
  &lt;/s:messages&gt;
&lt;/feed&gt;
</code></pre>

<a name='authenticationusersname'/>

## authentication/users/{name}

Removes the user from the system.

	[DELETE] authentication/users/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deleted successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to delete user. |
|--------------------------------
| **404** | User does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Deletes the splunker user.
The example for the POST operation for /authentication/users creates the splunker user.

#### Request
<pre class='terminal'>
curl -k -u admin:pass --request DELETE https://localhost:8089/services/authentication/users/splunker
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;users&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/authentication/users&lt;/id&gt;
  &lt;updated&gt;2011-07-08T14:08:59-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/authentication/users/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## authentication/users/{name}

Returns information about the user.

	[GET] authentication/users/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view user. |
|--------------------------------
| **404** | User does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Return information about the admin user.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/authentication/users/admin
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;users&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/authentication/users&lt;/id&gt;
  &lt;updated&gt;2011-07-08T14:08:34-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/authentication/users/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;admin&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/authentication/users/admin&lt;/id&gt;
    &lt;updated&gt;2011-07-08T14:08:34-07:00&lt;/updated&gt;
    &lt;link href="/services/authentication/users/admin" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/authentication/users/admin" rel="list"/&gt;
    &lt;link href="/services/authentication/users/admin" rel="edit"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="defaultApp"&gt;launcher&lt;/s:key&gt;
        &lt;s:key name="defaultAppIsUserOverride"&gt;0&lt;/s:key&gt;
        &lt;s:key name="defaultAppSourceRole"&gt;system&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:attributes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="optionalFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;defaultApp&lt;/s:item&gt;
                &lt;s:item&gt;email&lt;/s:item&gt;
                &lt;s:item&gt;password&lt;/s:item&gt;
                &lt;s:item&gt;realname&lt;/s:item&gt;
                &lt;s:item&gt;roles&lt;/s:item&gt;
                &lt;s:item&gt;tz&lt;/s:item&gt;
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
        &lt;s:key name="email"&gt;changeme@example.com&lt;/s:key&gt;
        &lt;s:key name="password"&gt;********&lt;/s:key&gt;
        &lt;s:key name="realname"&gt;Administrator&lt;/s:key&gt;
        &lt;s:key name="roles"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;admin&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
        &lt;s:key name="type"&gt;Splunk&lt;/s:key&gt;
        &lt;s:key name="tz"/&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## authentication/users/{name}

Update information about the user specified by {name}.

	[POST] authentication/users/{name}

### Parameters

defaultApp
: _Optional_ **INHERITED** INHERITED

email
: _Optional_ **INHERITED** INHERITED

password
: _Optional_ **INHERITED** INHERITED

realname
: _Optional_ **INHERITED** INHERITED

roles
: _Optional_ **INHERITED** INHERITED

tz
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
| **403** | Insufficient permissions to edit user. |
|--------------------------------
| **404** | User does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Changes the defaultApp for the user splunker to the Splunk launcher app.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/authentication/users/splunker \
	-d defaultApp=launcher
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;users&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/authentication/users&lt;/id&gt;
  &lt;updated&gt;2011-07-08T14:08:53-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/authentication/users/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;splunker&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/authentication/users/splunker&lt;/id&gt;
    &lt;updated&gt;2011-07-08T14:08:53-07:00&lt;/updated&gt;
    &lt;link href="/services/authentication/users/splunker" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/authentication/users/splunker" rel="list"/&gt;
    &lt;link href="/services/authentication/users/splunker" rel="edit"/&gt;
    &lt;link href="/services/authentication/users/splunker" rel="remove"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="defaultApp"&gt;launcher&lt;/s:key&gt;
        &lt;s:key name="defaultAppIsUserOverride"&gt;1&lt;/s:key&gt;
        &lt;s:key name="defaultAppSourceRole"&gt;system&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="email"/&gt;
        &lt;s:key name="password"&gt;********&lt;/s:key&gt;
        &lt;s:key name="realname"/&gt;
        &lt;s:key name="roles"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;user&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
        &lt;s:key name="type"&gt;Splunk&lt;/s:key&gt;
        &lt;s:key name="tz"/&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

<a name='authorizationcapabilities'/>

## authorization/capabilities

List all system capabiilities

	[GET] authorization/capabilities

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
| **403** | Insufficient permissions to view capabilities. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Lists all capabilities known to Splunk.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/authorization/capabilities
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;capabilities&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/authorization/capabilities&lt;/id&gt;
  &lt;updated&gt;2011-07-10T23:32:25-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;capabilities&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/authorization/capabilities/capabilities&lt;/id&gt;
    &lt;updated&gt;2011-07-10T23:32:25-07:00&lt;/updated&gt;
    &lt;link href="/services/authorization/capabilities/capabilities" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/authorization/capabilities/capabilities" rel="list"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="capabilities"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;admin_all_objects&lt;/s:item&gt;
            &lt;s:item&gt;change_authentication&lt;/s:item&gt;
            &lt;s:item&gt;change_own_password&lt;/s:item&gt;
            &lt;s:item&gt;delete_by_keyword&lt;/s:item&gt;
            &lt;s:item&gt;edit_deployment_client&lt;/s:item&gt;
            &lt;s:item&gt;edit_deployment_server&lt;/s:item&gt;
            &lt;s:item&gt;edit_dist_peer&lt;/s:item&gt;
            &lt;s:item&gt;edit_forwarders&lt;/s:item&gt;
            &lt;s:item&gt;edit_httpauths&lt;/s:item&gt;
            &lt;s:item&gt;edit_input_defaults&lt;/s:item&gt;
            &lt;s:item&gt;edit_monitor&lt;/s:item&gt;
            &lt;s:item&gt;edit_roles&lt;/s:item&gt;
            &lt;s:item&gt;edit_scripted&lt;/s:item&gt;
            &lt;s:item&gt;edit_search_server&lt;/s:item&gt;
            &lt;s:item&gt;edit_server&lt;/s:item&gt;
            &lt;s:item&gt;edit_splunktcp&lt;/s:item&gt;
            &lt;s:item&gt;edit_splunktcp_ssl&lt;/s:item&gt;
            &lt;s:item&gt;edit_tcp&lt;/s:item&gt;
            &lt;s:item&gt;edit_udp&lt;/s:item&gt;
            &lt;s:item&gt;edit_user&lt;/s:item&gt;
            &lt;s:item&gt;edit_web_settings&lt;/s:item&gt;
            &lt;s:item&gt;get_metadata&lt;/s:item&gt;
            &lt;s:item&gt;get_typeahead&lt;/s:item&gt;
            &lt;s:item&gt;indexes_edit&lt;/s:item&gt;
            &lt;s:item&gt;license_edit&lt;/s:item&gt;
            &lt;s:item&gt;license_tab&lt;/s:item&gt;
            &lt;s:item&gt;list_deployment_client&lt;/s:item&gt;
            &lt;s:item&gt;list_forwarders&lt;/s:item&gt;
            &lt;s:item&gt;list_httpauths&lt;/s:item&gt;
            &lt;s:item&gt;list_inputs&lt;/s:item&gt;
            &lt;s:item&gt;request_remote_tok&lt;/s:item&gt;
            &lt;s:item&gt;rest_apps_management&lt;/s:item&gt;
            &lt;s:item&gt;rest_apps_view&lt;/s:item&gt;
            &lt;s:item&gt;rest_properties_get&lt;/s:item&gt;
            &lt;s:item&gt;rest_properties_set&lt;/s:item&gt;
            &lt;s:item&gt;restart_splunkd&lt;/s:item&gt;
            &lt;s:item&gt;rtsearch&lt;/s:item&gt;
            &lt;s:item&gt;schedule_search&lt;/s:item&gt;
            &lt;s:item&gt;search&lt;/s:item&gt;
            &lt;s:item&gt;use_file_operator&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

<a name='authorizationcapabilitiesname'/>

## authorization/capabilities/{name}

List a particular system capability name. This does not list any further information besides the name.

	[GET] authorization/capabilities/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view capabilities. |
|--------------------------------
| **404** | Capability does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Identical to accessing authorization/capabilities.  Note that "capabilities" is the only valid name here.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/authorization/capabilities/capabilities
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>

</code></pre>

<a name='authorizationroles'/>

## authorization/roles

Lists all roles and the permissions for each role.

	[GET] authorization/roles

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
| **403** | Insufficient permissions to view roles. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Lists all the roles defined for this Splunk instance.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/authorization/roles
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;roles&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/authorization/roles&lt;/id&gt;
  &lt;updated&gt;2011-07-08T13:52:32-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/authorization/roles/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;admin&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/authorization/roles/admin&lt;/id&gt;
    &lt;updated&gt;2011-07-08T13:52:32-07:00&lt;/updated&gt;
    &lt;link href="/services/authorization/roles/admin" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/authorization/roles/admin" rel="list"/&gt;
    &lt;link href="/services/authorization/roles/admin" rel="edit"/&gt;
    &lt;link href="/services/authorization/roles/admin" rel="remove"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="capabilities"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;admin_all_objects&lt;/s:item&gt;
            &lt;s:item&gt;change_authentication&lt;/s:item&gt;
            &lt;s:item&gt;edit_deployment_client&lt;/s:item&gt;
            &lt;s:item&gt;edit_deployment_server&lt;/s:item&gt;
            &lt;s:item&gt;edit_dist_peer&lt;/s:item&gt;
            &lt;s:item&gt;edit_forwarders&lt;/s:item&gt;
            &lt;s:item&gt;edit_httpauths&lt;/s:item&gt;
            &lt;s:item&gt;edit_input_defaults&lt;/s:item&gt;
            &lt;s:item&gt;edit_monitor&lt;/s:item&gt;
            &lt;s:item&gt;edit_roles&lt;/s:item&gt;
            &lt;s:item&gt;edit_scripted&lt;/s:item&gt;
            &lt;s:item&gt;edit_search_server&lt;/s:item&gt;
            &lt;s:item&gt;edit_server&lt;/s:item&gt;
            &lt;s:item&gt;edit_splunktcp&lt;/s:item&gt;
            &lt;s:item&gt;edit_splunktcp_ssl&lt;/s:item&gt;
            &lt;s:item&gt;edit_tcp&lt;/s:item&gt;
            &lt;s:item&gt;edit_udp&lt;/s:item&gt;
            &lt;s:item&gt;edit_user&lt;/s:item&gt;
            &lt;s:item&gt;edit_web_settings&lt;/s:item&gt;
            &lt;s:item&gt;indexes_edit&lt;/s:item&gt;
            &lt;s:item&gt;license_edit&lt;/s:item&gt;
            &lt;s:item&gt;license_tab&lt;/s:item&gt;
            &lt;s:item&gt;list_deployment_client&lt;/s:item&gt;
            &lt;s:item&gt;list_forwarders&lt;/s:item&gt;
            &lt;s:item&gt;list_httpauths&lt;/s:item&gt;
            &lt;s:item&gt;rest_apps_management&lt;/s:item&gt;
            &lt;s:item&gt;restart_splunkd&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
        &lt;s:key name="defaultApp"/&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="imported_capabilities"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;change_own_password&lt;/s:item&gt;
            &lt;s:item&gt;get_metadata&lt;/s:item&gt;
            &lt;s:item&gt;get_typeahead&lt;/s:item&gt;
            &lt;s:item&gt;list_inputs&lt;/s:item&gt;
            &lt;s:item&gt;request_remote_tok&lt;/s:item&gt;
            &lt;s:item&gt;rest_apps_view&lt;/s:item&gt;
            &lt;s:item&gt;rest_properties_get&lt;/s:item&gt;
            &lt;s:item&gt;rest_properties_set&lt;/s:item&gt;
            &lt;s:item&gt;rtsearch&lt;/s:item&gt;
            &lt;s:item&gt;schedule_search&lt;/s:item&gt;
            &lt;s:item&gt;search&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
        &lt;s:key name="imported_roles"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;power&lt;/s:item&gt;
            &lt;s:item&gt;user&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
        &lt;s:key name="imported_rtSrchJobsQuota"&gt;20&lt;/s:key&gt;
        &lt;s:key name="imported_srchDiskQuota"&gt;500&lt;/s:key&gt;
        &lt;s:key name="imported_srchFilter"/&gt;
        &lt;s:key name="imported_srchIndexesAllowed"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;*&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
        &lt;s:key name="imported_srchIndexesDefault"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;main&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
        &lt;s:key name="imported_srchJobsQuota"&gt;10&lt;/s:key&gt;
        &lt;s:key name="imported_srchTimeWin"&gt;-1&lt;/s:key&gt;
        &lt;s:key name="rtSrchJobsQuota"&gt;100&lt;/s:key&gt;
        &lt;s:key name="srchDiskQuota"&gt;10000&lt;/s:key&gt;
        &lt;s:key name="srchFilter"&gt;*&lt;/s:key&gt;
        &lt;s:key name="srchIndexesAllowed"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;*&lt;/s:item&gt;
            &lt;s:item&gt;_*&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
        &lt;s:key name="srchIndexesDefault"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;main&lt;/s:item&gt;
            &lt;s:item&gt;os&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
        &lt;s:key name="srchJobsQuota"&gt;50&lt;/s:key&gt;
        &lt;s:key name="srchTimeWin"&gt;0&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## authorization/roles

Create a user role.

	[POST] authorization/roles

### Parameters

capabilities
: _Optional_ **String** Specify a comma-separated list of capabilities to assign to this role.<br/><br/>Roles inherit all capabilities from imported roles<br/><br/>Capabilities available are:<br/><br/>  admin_all_objects
  change_authentication
  change_own_password
  delete_by_keyword
  edit_deployment_client
  edit _depoyment_server
  edit_dist_peer
  edit_forwarders
  edit_httpauths
  edit_input_defaults
  edit_monitor
  edit_scripted
  edit_search_server
  edit_splunktcp
  edit_splunktcp_ssl
  edit_tcp
  edit_udp
  edit_web_settings
  get_metadata
  get_typeahead
  indexes_edit
  license_edit
  license_tab
  list_deployment_client
  list_forwarders
  list_httpauths
  list_inputs
  request_remote_tok
  rest_apps_management
  rest_apps_view
  rest_properties_get
  rest_properties_set
  restart_splunkd
  rtsearch
  schedule_search
  search
  use_file_operator

defaultApp
: _Optional_ **String** Specify the name of the app to use as the default app for the role.A user-specific default app will override this.<br/><br/>The name you specify is the name of the folder containing the app.

imported_roles
: _Optional_ **String** Specify a comma-separated list of roles their associated capabilities that should be imported. By default a role imports no other roles. <br/><br/>Importing other roles also imports the other aspects of that role, such as capabilities and allowed indexes to search. If you specify multiple roles, this role inherits from the parent with the broadest permissions.<br/><br/>Default Splunk roles are:<br/><br/>  admin
  can_delete
  power
  user<br/><br/>You can specify additional roles that have been created.

name
: _Required_ **String** The name of the user role to create.

rtSrchJobsQuota
: _Optional_ **Number** Specify the maximum number of concurrent real time search jobs for this role.<br/><br/>This count is independent from the normal search jobs limit.

srchDiskQuota
: _Optional_ **Number** Specifies the maximum disk space in MB that can be used by a user's search jobs. For example, 100 limits this role to 100 MB total.

srchFilter
: _Optional_ **String** Specify a search string that restricts the scope of searches run by this role. Search results for this role only show events that also match the search string you specify.   In the case that a user has multiple roles with different search filters, they are combined with an OR.<br/><br/>The search string can include source, host, index, eventtype, sourcetype, search fields, *, OR and, AND. <br/><br/>Example: "host=web* OR source=/var/log/*"<br/><br/>Note: You can also use the srchIndexesAllowed and srchIndexesDefault parameters to limit the search on indexes.

srchIndexesAllowed
: _Optional_ **String** Comma-separated list of indexes this role has permissions to search.  These may be wildcarded, but the index name must begin with an underscore to match internal indexes.<br/><br/>Search indexes available by default from Splunk include:<br/><br/>  All internal indexes
  All non-internal indexes
  _audit
  _blocksignature
  _internal
  _thefishbucket
  history
  main<br/><br/>You can also specify other search indexes that have been added to the server.

srchIndexesDefault
: _Optional_ **String** Comma-separated list of search indexes that searches for this role default to when no index is specified.  These may be wildcarded, but the index name must begin with an underscore to match internal indexes.<br/><br/>A user with this role can search other indexes using "index= " <br/><br/>For example, "index=special_index".<br/><br/>Search indexes available by default from Splunk include:<br/><br/>  All internal indexes
  All non-internal indexes
  _audit
  _blocksignature
  _internal
  _thefishbucket
  history
  main
  other search indexes that have been added to the server<br/><br/>These indexes can be wildcarded, with the exception that '*' does not match internal indexes. To match internal indexes, start with '_'. All internal indexes are represented by '_*'.

srchJobsQuota
: _Optional_ **Number** The maximum number of concurrent searches a user with this role is allowed to run. In the event of many roles per user, the maximum of these quotas is applied.

srchTimeWin
: _Optional_ **Number** Maximum time span of a search, in seconds.
 
By default, searches are not limited to any specific time window. To override any search time windows from imported roles, set srchTimeWin to '0', as the 'admin' role does.

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
| **403** | Insufficient permissions to create role. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Creates a new role, SplunkUser that imports the capabilities of the user role and sets the defaultApp to the Splunk search app.
After creating the role, perform the GET operation on /authorization/roles/SplunkUser to verify that the role was created.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/authorization/roles \
	-d name=SplunkUser \
	-d imported_roles=user \
	-d defaultApp=search
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;roles&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/authorization/roles&lt;/id&gt;
  &lt;updated&gt;2011-07-08T13:52:47-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/authorization/roles/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages&gt;
    &lt;s:msg type="WARN"&gt;This role will be disabled after the Enterprise Trial License expires&lt;/s:msg&gt;
  &lt;/s:messages&gt;
&lt;/feed&gt;
</code></pre>

<a name='authorizationrolesname'/>

## authorization/roles/{name}

Deletes the role specified by {name}.

	[DELETE] authorization/roles/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deleted successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to delete role. |
|--------------------------------
| **404** | Role does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Deletes the SplunkUser role created in the POST example for /authorization/roles.
After deleting the role, run the GET operation for /authorization/roles to verify that the role has been deleted.

#### Request
<pre class='terminal'>
curl -k -u admin:pass --request DELETE \
	https://localhost:8089/services/authorization/roles/SplunkUser
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;roles&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/authorization/roles&lt;/id&gt;
  &lt;updated&gt;2011-07-08T13:53:06-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/authorization/roles/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## authorization/roles/{name}

Lists the permissions for the role specified by {name}.

	[GET] authorization/roles/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view role. |
|--------------------------------
| **404** | Role does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

List the permissions for the SplunkUser role created for the POST operation example for /authorization/roles.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/authorization/roles/SplunkUser
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;roles&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/authorization/roles&lt;/id&gt;
  &lt;updated&gt;2011-07-08T13:52:57-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/authorization/roles/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;splunkuser&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/services/authorization/roles/splunkuser&lt;/id&gt;
    &lt;updated&gt;2011-07-08T13:52:57-07:00&lt;/updated&gt;
    &lt;link href="/services/authorization/roles/splunkuser" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;system&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/services/authorization/roles/splunkuser" rel="list"/&gt;
    &lt;link href="/services/authorization/roles/splunkuser" rel="edit"/&gt;
    &lt;link href="/services/authorization/roles/splunkuser" rel="remove"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="capabilities"&gt;
          &lt;s:list/&gt;
        &lt;/s:key&gt;
        &lt;s:key name="defaultApp"&gt;search&lt;/s:key&gt;
        &lt;!-- eai:acl nodes elided for brevity. --&gt;
        &lt;s:key name="eai:attributes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="optionalFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;capabilities&lt;/s:item&gt;
                &lt;s:item&gt;defaultApp&lt;/s:item&gt;
                &lt;s:item&gt;imported_roles&lt;/s:item&gt;
                &lt;s:item&gt;rtSrchJobsQuota&lt;/s:item&gt;
                &lt;s:item&gt;srchDiskQuota&lt;/s:item&gt;
                &lt;s:item&gt;srchFilter&lt;/s:item&gt;
                &lt;s:item&gt;srchIndexesAllowed&lt;/s:item&gt;
                &lt;s:item&gt;srchIndexesDefault&lt;/s:item&gt;
                &lt;s:item&gt;srchJobsQuota&lt;/s:item&gt;
                &lt;s:item&gt;srchTimeWin&lt;/s:item&gt;
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
        &lt;s:key name="imported_capabilities"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;change_own_password&lt;/s:item&gt;
            &lt;s:item&gt;get_metadata&lt;/s:item&gt;
            &lt;s:item&gt;get_typeahead&lt;/s:item&gt;
            &lt;s:item&gt;list_inputs&lt;/s:item&gt;
            &lt;s:item&gt;request_remote_tok&lt;/s:item&gt;
            &lt;s:item&gt;rest_apps_view&lt;/s:item&gt;
            &lt;s:item&gt;rest_properties_get&lt;/s:item&gt;
            &lt;s:item&gt;rest_properties_set&lt;/s:item&gt;
            &lt;s:item&gt;search&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
        &lt;s:key name="imported_roles"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;user&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
        &lt;s:key name="imported_rtSrchJobsQuota"&gt;6&lt;/s:key&gt;
        &lt;s:key name="imported_srchDiskQuota"&gt;100&lt;/s:key&gt;
        &lt;s:key name="imported_srchFilter"/&gt;
        &lt;s:key name="imported_srchIndexesAllowed"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;*&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
        &lt;s:key name="imported_srchIndexesDefault"&gt;
          &lt;s:list&gt;
            &lt;s:item&gt;main&lt;/s:item&gt;
          &lt;/s:list&gt;
        &lt;/s:key&gt;
        &lt;s:key name="imported_srchJobsQuota"&gt;3&lt;/s:key&gt;
        &lt;s:key name="imported_srchTimeWin"&gt;-1&lt;/s:key&gt;
        &lt;s:key name="rtSrchJobsQuota"&gt;0&lt;/s:key&gt;
        &lt;s:key name="srchDiskQuota"&gt;0&lt;/s:key&gt;
        &lt;s:key name="srchFilter"/&gt;
        &lt;s:key name="srchIndexesAllowed"&gt;
          &lt;s:list/&gt;
        &lt;/s:key&gt;
        &lt;s:key name="srchIndexesDefault"&gt;
          &lt;s:list/&gt;
        &lt;/s:key&gt;
        &lt;s:key name="srchJobsQuota"&gt;0&lt;/s:key&gt;
        &lt;s:key name="srchTimeWin"&gt;-1&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## authorization/roles/{name}

Updates the role specified by {name}.

	[POST] authorization/roles/{name}

### Parameters

capabilities
: _Optional_ **INHERITED** INHERITED

defaultApp
: _Optional_ **INHERITED** INHERITED

imported_roles
: _Optional_ **INHERITED** INHERITED

rtSrchJobsQuota
: _Optional_ **INHERITED** INHERITED

srchDiskQuota
: _Optional_ **INHERITED** INHERITED

srchFilter
: _Optional_ **INHERITED** INHERITED

srchIndexesAllowed
: _Optional_ **INHERITED** INHERITED

srchIndexesDefault
: _Optional_ **INHERITED** INHERITED

srchJobsQuota
: _Optional_ **INHERITED** INHERITED

srchTimeWin
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
| **403** | Insufficient permissions to edit role. |
|--------------------------------
| **404** | Role does not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Updates the SplunkUser role to change the default application to launcher. The SplunkUser role is created in the example for the POST operation for /authorization/roles.
After updating the role, run the GET operation for /authorization/roles/SplunkUser to see the updated default application.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/authorization/roles/SplunkUser \
	-d defaultApp=launcher
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;roles&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/authorization/roles&lt;/id&gt;
  &lt;updated&gt;2011-07-08T13:53:02-07:00&lt;/updated&gt;
  &lt;generator version="102807"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/authorization/roles/_new" rel="create"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

<a name='storagepasswords'/>

## storage/passwords

List available credentials

	[GET] storage/passwords

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
| **403** | Insufficient permissions to view credentials. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Lists stored credentials, showing the clear text and encrypted password.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/services/storage/passwords
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:s="http://dev.splunk.com/ns/rest"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;passwords&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/services/storage/passwords&lt;/id&gt;
  &lt;updated&gt;2011-07-05T21:39:56-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/services/storage/passwords/_new" rel="create"/&gt;
  &lt;link href="/services/storage/passwords/_reload" rel="_reload"/&gt;
  &lt;opensearch:totalResults&gt;1&lt;/opensearch:totalResults&gt;
  &lt;opensearch:itemsPerPage&gt;30&lt;/opensearch:itemsPerPage&gt;
  &lt;opensearch:startIndex&gt;0&lt;/opensearch:startIndex&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;:splunker:&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/storage/passwords/%3Asplunker%3A&lt;/id&gt;
    &lt;updated&gt;2011-07-05T21:39:56-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/search/storage/passwords/%3Asplunker%3A" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/search/storage/passwords/%3Asplunker%3A" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/search/storage/passwords/%3Asplunker%3A/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/search/storage/passwords/%3Asplunker%3A" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/search/storage/passwords/%3Asplunker%3A" rel="remove"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="clear_password"&gt;changeme&lt;/s:key&gt;
        &lt;s:key name="eai:acl"&gt; . . .&lt;/s:key&gt;
        &lt;s:key name="encr_password"&gt;$1$oPmwi5i6DcNz&lt;/s:key&gt;
        &lt;s:key name="password"&gt;********&lt;/s:key&gt;
        &lt;s:key name="realm"&gt;&lt;/s:key&gt;
        &lt;s:key name="username"&gt;splunker&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## storage/passwords

Create/edit new credentials

	[POST] storage/passwords

### Parameters

name
: _Required_ **String** Username for the credentials

password
: _Required_ **String** The password for the credentials - this is the only part of the credentials that will be stored securely

realm
: _Optional_ **String** The credential realm

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
| **403** | Insufficient permissions to create credentials. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Creates stored credentials for the user, splunker.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/nobody/search/storage/passwords \
	-d name=splunker \
	-d password=changeme
</pre>
<p></p>

#### Response
<%= headers 201 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:s="http://dev.splunk.com/ns/rest"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;passwords&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/storage/passwords&lt;/id&gt;
  &lt;updated&gt;2011-07-05T21:39:41-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/storage/passwords/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/storage/passwords/_reload" rel="_reload"/&gt;
  &lt;opensearch:totalResults&gt;1&lt;/opensearch:totalResults&gt;
  &lt;opensearch:itemsPerPage&gt;30&lt;/opensearch:itemsPerPage&gt;
  &lt;opensearch:startIndex&gt;0&lt;/opensearch:startIndex&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;:splunker:&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/storage/passwords/%3Asplunker%3A&lt;/id&gt;
    &lt;updated&gt;2011-07-05T21:39:41-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/search/storage/passwords/%3Asplunker%3A" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/search/storage/passwords/%3Asplunker%3A" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/search/storage/passwords/%3Asplunker%3A/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/search/storage/passwords/%3Asplunker%3A" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/search/storage/passwords/%3Asplunker%3A" rel="remove"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="clear_password"&gt;changeme&lt;/s:key&gt;
        &lt;s:key name="eai:acl"&gt; . . &lt;/s:key&gt;
        &lt;s:key name="encr_password"&gt;$1$oPmwi5i6DcNz&lt;/s:key&gt;
        &lt;s:key name="password"&gt;********&lt;/s:key&gt;
        &lt;s:key name="realm"&gt;&lt;/s:key&gt;
        &lt;s:key name="username"&gt;splunker&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

<a name='storagepasswordsname'/>

## storage/passwords/{name}

Delete the identified credentials

	[DELETE] storage/passwords/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Deleted successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to delete credentials. |
|--------------------------------
| **404** | Credentials do not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Deletes the stored credentials for the user, splunker.

#### Request
<pre class='terminal'>
curl -k -u admin:pass --request DELETE \
	https://localhost:8089/servicesNS/nobody/search/storage/passwords/:splunker:
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"
      xmlns:s="http://dev.splunk.com/ns/rest"&gt;
  &lt;title&gt;passwords&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/storage/passwords&lt;/id&gt;
  &lt;updated&gt;2011-07-12T14:48:50-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/storage/passwords/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/storage/passwords/_reload" rel="_reload"/&gt;
  &lt;!-- opensearch nodes elided for brevity. --&gt;
  &lt;s:messages/&gt;
&lt;/feed&gt;
</code></pre>

## storage/passwords/{name}

List only the credentials identified by the given id

	[GET] storage/passwords/{name}

### Status Codes

| Status Code       | Description |
|:------------------|:------------|
| **200** | Listed successfully. |
|--------------------------------
| **400** | Request error.  See response body for details. |
|--------------------------------
| **401** | Authentication failure: must pass valid credentials with request. |
|--------------------------------
| **403** | Insufficient permissions to view credentials. |
|--------------------------------
| **404** | Credentials do not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------

### Example

Lists stored credentials for the user splunker.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/nobody/search/storage/passwords/splunker
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:s="http://dev.splunk.com/ns/rest"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;passwords&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/storage/passwords&lt;/id&gt;
  &lt;updated&gt;2011-07-05T21:50:10-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/storage/passwords/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/storage/passwords/_reload" rel="_reload"/&gt;
  &lt;opensearch:totalResults&gt;1&lt;/opensearch:totalResults&gt;
  &lt;opensearch:itemsPerPage&gt;30&lt;/opensearch:itemsPerPage&gt;
  &lt;opensearch:startIndex&gt;0&lt;/opensearch:startIndex&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;:splunker:&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/storage/passwords/%3Asplunker%3A&lt;/id&gt;
    &lt;updated&gt;2011-07-05T21:50:10-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/search/storage/passwords/%3Asplunker%3A" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/search/storage/passwords/%3Asplunker%3A" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/search/storage/passwords/%3Asplunker%3A/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/search/storage/passwords/%3Asplunker%3A" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/search/storage/passwords/%3Asplunker%3A" rel="remove"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="clear_password"&gt;changeme&lt;/s:key&gt;
        &lt;s:key name="eai:acl"&gt; . . . &lt;/s:key&gt;
        &lt;s:key name="eai:attributes"&gt;
          &lt;s:dict&gt;
            &lt;s:key name="optionalFields"&gt;
              &lt;s:list/&gt;
            &lt;/s:key&gt;
            &lt;s:key name="requiredFields"&gt;
              &lt;s:list&gt;
                &lt;s:item&gt;password&lt;/s:item&gt;
              &lt;/s:list&gt;
            &lt;/s:key&gt;
            &lt;s:key name="wildcardFields"&gt;
              &lt;s:list/&gt;
            &lt;/s:key&gt;
          &lt;/s:dict&gt;
        &lt;/s:key&gt;
        &lt;s:key name="encr_password"&gt;$1$oPmwi5i6DcNz&lt;/s:key&gt;
        &lt;s:key name="password"&gt;********&lt;/s:key&gt;
        &lt;s:key name="realm"&gt;&lt;/s:key&gt;
        &lt;s:key name="username"&gt;splunker&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>

## storage/passwords/{name}

Edit the identified credentials.

	[POST] storage/passwords/{name}

### Parameters

password
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
| **403** | Insufficient permissions to edit credentials. |
|--------------------------------
| **404** | Credentials do not exist. |
|--------------------------------
| **409** | Request error: this operation is invalid for this item.  See response body for details. |
|--------------------------------
| **500** | Internal server error.  See response body for details. |
|--------------------------------
| **503** | This feature has been disabled in Splunk configuration files. |
|--------------------------------

### Example

Change the stored credentials for the user splunker, by setting the password to pass.

#### Request
<pre class='terminal'>
curl -k -u admin:pass https://localhost:8089/servicesNS/nobody/search/storage/passwords/splunker \
	-d password=pass
</pre>
<p></p>

#### Response
<%= headers 200 %>
<pre class='highlight'><code class='language-xml'>
&lt;feed xmlns="http://www.w3.org/2005/Atom"
      xmlns:s="http://dev.splunk.com/ns/rest"
      xmlns:opensearch="http://a9.com/-/spec/opensearch/1.1/"&gt;
  &lt;title&gt;passwords&lt;/title&gt;
  &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/storage/passwords&lt;/id&gt;
  &lt;updated&gt;2011-07-05T21:54:31-07:00&lt;/updated&gt;
  &lt;generator version="102824"/&gt;
  &lt;author&gt;
    &lt;name&gt;Splunk&lt;/name&gt;
  &lt;/author&gt;
  &lt;link href="/servicesNS/nobody/search/storage/passwords/_new" rel="create"/&gt;
  &lt;link href="/servicesNS/nobody/search/storage/passwords/_reload" rel="_reload"/&gt;
  &lt;opensearch:totalResults&gt;1&lt;/opensearch:totalResults&gt;
  &lt;opensearch:itemsPerPage&gt;30&lt;/opensearch:itemsPerPage&gt;
  &lt;opensearch:startIndex&gt;0&lt;/opensearch:startIndex&gt;
  &lt;s:messages/&gt;
  &lt;entry&gt;
    &lt;title&gt;:splunker:&lt;/title&gt;
    &lt;id&gt;https://localhost:8089/servicesNS/nobody/search/storage/passwords/%3Asplunker%3A&lt;/id&gt;
    &lt;updated&gt;2011-07-05T21:54:31-07:00&lt;/updated&gt;
    &lt;link href="/servicesNS/nobody/search/storage/passwords/%3Asplunker%3A" rel="alternate"/&gt;
    &lt;author&gt;
      &lt;name&gt;admin&lt;/name&gt;
    &lt;/author&gt;
    &lt;link href="/servicesNS/nobody/search/storage/passwords/%3Asplunker%3A" rel="list"/&gt;
    &lt;link href="/servicesNS/nobody/search/storage/passwords/%3Asplunker%3A/_reload" rel="_reload"/&gt;
    &lt;link href="/servicesNS/nobody/search/storage/passwords/%3Asplunker%3A" rel="edit"/&gt;
    &lt;link href="/servicesNS/nobody/search/storage/passwords/%3Asplunker%3A" rel="remove"/&gt;
    &lt;content type="text/xml"&gt;
      &lt;s:dict&gt;
        &lt;s:key name="clear_password"&gt;pass&lt;/s:key&gt;
        &lt;s:key name="eai:acl"&gt; . . . &lt;/s:key&gt;
        &lt;s:key name="encr_password"&gt;$1$s/Cilqo=&lt;/s:key&gt;
        &lt;s:key name="password"&gt;********&lt;/s:key&gt;
        &lt;s:key name="realm"&gt;&lt;/s:key&gt;
        &lt;s:key name="username"&gt;splunker&lt;/s:key&gt;
      &lt;/s:dict&gt;
    &lt;/content&gt;
  &lt;/entry&gt;
&lt;/feed&gt;
</code></pre>


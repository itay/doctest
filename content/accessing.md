---
title: Accessing Splunk resources
---

# Accessing Splunk resources

## Splunk's layering of resources

Splunk takes a layering approach for access to resources. This layering approach is necessary to account for permissions to view apps, system files, and other resources by users throughout a Splunk installation.

Splunk implements this layering approach through configuration files and an order of precedence that determines access to the resources defined therein.

Splunk REST API namespace endpoints, as described later in this section, provide access to resources based on this layering approach. This is important when viewing, creating, updating, or deleting resources to make sure you are accessing the correct resources for a user's namespace.

### Search-time resources

Generally speaking, resources that affect search activities have an app/user context. 

The order or precedence in the app/user context is:

* Settings specific to a user
* Settings specific to the current app
* Settings globally-visible from other apps
* System-wide settings

This layering enables users access to not only resources specific to them but also to apps and system-wide settings.

The order of precedence also accounts for different resources with the same name. For example, a user can have a saved search with the same name as a saved search at the system level.

Examples of search-time resources include:

* /saved/searches (saved searches)
* /data/props/extractions (field extractions)

### Index-time resources

For some resources there is no user/app context. These are resources that affect data input, indexing, or deployment activities. In this case, the order of precedence is:

* Local system settings
* Settings for all apps
* Default system settings

Because there is no user/app context, user-specific settings are ignored. Access to resources is based on the capabilities defined in the Splunk-defined role for a user. For example, /data/inputs/monitor looks the same to all users who can access it based on their Splunk role.

Examples of these resources include:

* /data/indexes (indexes)
* /data/inputs/monitors (monitor inputs)

## Accessing resources with the Splunk REST API 

When using the Splunk REST API, use the <code>/servicesNS/*</code> endpoints to ensure that you specify the correct user/app context for the resource:

<code>https://{Splunk server}:{management port}/servicesNS/{user}/{app}/*</code>

### Search-time resources

For example, from the Splunk default management port, the following GET operation returns saved searches accessible by the admin user from within the search app context. It does not, however, list saved searches private to the admin user in another app, such as the launcher app.

<pre class="terminal">curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search/saved/searches</pre>

### Index-time resources

For index-time resources, access through the Splunk REST API is still through a user/app context. For example, the following POST operation creates an index:

<pre class="terminal">
curl -k -u admin:pass https://localhost:8089/servicesNS/nobody/search/data/indexes   \
        -d name=Shadow
</pre>

Here, Splunk uses the user "nobody" to indicate that there is no specific user for this context. The search app is accessible by all users.

Access is through the Splunk admin user credentials. The admin user, through its admin role, has the capabilities to create and edit indexes.

Access through the credentials of a user (with a user role) cannot create an index.

## /services/* endpoints

Splunk resources can also be accessed through the services endpoints:

 <code>https://{Splunk server}:{management port}/services/*</code>

For example, the following GET operation returns all services available to the admin user:

<pre class="terminal">
curl -k -u admin:pass https://localhost:8089/services/
</pre>

When processing a request to a services/* endpoint, Splunk processes the request using the user/app context of the current user. The following are equivalent:

<pre class="terminal">
curl -k -u {user}:{pw} https://localhost:8089/services/
curl -k -u {user}:{pw} https://localhost:8089/servicesNS/{user}/{default app}
</pre>

The preceding GET operation is equivalent to:

<pre class="terminal">
curl -k -u admin:pass https://localhost:8089/servicesNS/admin/search
</pre>

However, for create, update, and delete operations (POST, {name} POST, {name} DELETE), you should use the /servicesNS/* endpoints to make sure you access resources with the correct user/app context. 

# Sphinx plugin for Server Density

Returns all sphinx stats properly.

Uses the new MySQL protocol via the mysql command line client which must be installed. Take care to configure correctly as it may just show you MySQL's status otherwise.

Requires Python 2.7+

For the web-based plugin configuration we currently use these graphs:

Running
* running

Connections
* connections

Queries
* queries
* dist_queries

Query Times
* query_wall
* avg_query_wall
* dist_wall
* avg_dist_wall
* dist_local
* avg_dist_local
* dist_wait
* avg_dist_wait

Commands
* command_search
* command_excerpt
* command_update
* command_keywords
* command_persist
* command_status
* command_flushattrs

Agents
* agent_connect
* agent_retry

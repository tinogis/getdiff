# README

Simple script to retrieve a Pull Request diff file from github with curl
through github API.

```sh
$> getdiff -u username https://github.com/owner/repo/pull/prnumber.diff
```

All parameters except url are passed directly to curl

# WHY THIS SCRIPT?

Former github API allowed Basic Authentication style retrieving from portal:

```sh
$> curl -u user https://github.com/owner/repo/pull/prnumber.diff
```

You can't download diff files this way now.

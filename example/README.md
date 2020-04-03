# pulumi-google-analytics Example

This folder contains an example that uses pulumi-google-analytics.

### Setup

1. Create a Python virtualenv, activate it, and install the pip project from the parent folder:

```
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip3 install -e ..
```
2. Create the required stacks

```
$ pulumi stack init dev
```

3. Configure variables

```
$ pulumi config set aws:region <region>
$ pulumi config set google_api_key_file <google-api-key-file>
$ pulumi config set ga_account_id <google-analytics-manager-account-id>
```

4. Edit ```__main__.py``` file acordingly.

###  Deploy

```
$ pulumi up
```


### Clean up

Destroy the stack and google tag manager resources.

```
$ pulumi destroy
$ pulumi stack rm
```

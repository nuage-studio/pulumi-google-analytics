[![Deploy](https://get.pulumi.com/new/button.svg)](https://app.pulumi.com/new)

# pulumi-google-analytics

This project contains a pip packaged named `pulumi-google-analytics` which allows Google Analytics resources to be managed in Pulumi.

An example Pulumi program which uses this package is present in the `example` folder.

## Setup

* Install the package into your Pulumi project using `pip`

```
$ pip install pulumi-google-analytics
```

* Set your Google credentials in your stack config:

```
$ pulumi config set aws:region <region>
$ pulumi config set google_api_key_file <google-api-key-file>
$ pulumi config set ga_account_id <google-analytics-manager-account-id>
```


## Directory structure

```
.
├── example
│   ├── __main__.py
│   ├── Pulumi.yaml
│   └── README.md
├── pulumi_google_analytics
│   └── dynamic_providers
│       ├── web_property_provider.py
│       ├── web_property.py
│       └── service.py
├── README.md
├── requirements.txt
└── setup.py
```

# Getting started

You need Python 3 (preferably 3.8) installed to start working on this project.

In order to install your virtualenv, just go to the root of the project and:
```bash
make install
```

# IDE

Nuage recommends [Visual Studio Code](https://code.visualstudio.com/download) to work on this project, and some default settings have been configured in the [.vscode/settings.json](.vscode/settings.json).

These settings merely enforce the code-quality guidelines defined below, but if you use another IDE it's probably worth taking a quick look at it to ensure compliance with the standard.

By default, we recommend:
1. Putting your virtualenv in a `venv` folder at the project root
2. Using a `.env` file to define your environment variables (cf. [python-dotenv](https://pypi.org/project/python-dotenv/))

# Code quality

This project has opinionated code-quality requirements:
- Code formatter: [black](https://black.readthedocs.io/en/stable/)
- Code linter: [pylint](https://www.pylint.org)
- Code style guidelines: [flake8](https://flake8.pycqa.org/en/latest/)

All of these tools are enforced at the commit-level via [pre-commit](https://pre-commit.com)

You can run the following command to apply code-quality to your project at any point:
```bash
make quality
```

Code quality configuration files:
- IDE-agnostic coding style settings are set in the [.editorconfig](.editorconfig) file
- Python-related settings are set in the [setup.cfg](setup.cfg) file
- Pre-commit-related settings are set in the [.pre-commit-config.yaml](.pre-commit-config.yaml) file
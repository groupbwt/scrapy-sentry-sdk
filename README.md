# scrapy-sentry-sdk
A Scrapy extension for integration of Sentry SDK to Scrapy projects.

This package provides a Scrapy extension for convenient initialization of Sentry SDK.

## Installation

```shell script
pip install scrapy_sentry_sdk
```

## Usage

To use the extension add the following to you project `settings.py`:

```python
# Send exceptions to Sentry
# replace SENTRY_DSN by you own DSN
SENTRY_DSN = "XXXXXXXXXX"

# Optionally, additional configuration options can be provided
SENTRY_CLIENT_OPTIONS = {
    "release": "you-project@version"  # these correspond to the sentry_sdk.init kwargs
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
EXTENSIONS = {
    'scrapy_sentry_sdk.extensions.SentryLogging': 1,  # Load SentryLogging extension before others
}
```

## Configuration

Currently, this extension uses two Scrapy settings keys:

- `SENTRY_DSN`: your project DSN (string, required)
- `SENTRY_CLIENT_OPTIONS`: additional SDK options (dict, optional)

More details on configuring the SDK can be found in [Sentry documentation](https://docs.sentry.io/platforms/python/).

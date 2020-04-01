# scrapy-sentry-sdk
A Scrapy extension for integration of Sentry SDK to Scrapy projects.

This package provides a Scrapy extension for convenient initialization of Sentry SDK.

To use it, first install the package:

```shell script
pip install scrapy_sentry_sdk
```

The add the following to you project's `settings.py`:

```python
# Send exceptions to Sentry
# replace SENTRY_DSN by you own DSN
SENTRY_DSN = "XXXXXXXXXX"

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
EXTENSIONS = {
    'scrapy_sentry_sdk.extensions.SentryLogging': 1,  # Load SentryLogging extension before others
}
```

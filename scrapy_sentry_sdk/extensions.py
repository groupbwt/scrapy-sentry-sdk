# -*- coding: utf-8 -*-
import sentry_sdk
from scrapy.exceptions import NotConfigured


class SentryLogging(object):
    """
    Send exceptions and errors to Sentry.
    """

    @classmethod
    def from_crawler(cls, crawler):
        sentry_dsn = crawler.settings.get('SENTRY_DSN', None)
        if sentry_dsn is None:
            raise NotConfigured("No SENTRY_DSN configured")

        ext = cls()
        sentry_sdk.init(sentry_dsn)
        return ext

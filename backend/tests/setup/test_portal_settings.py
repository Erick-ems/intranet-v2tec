"""Portal settings tests."""

from plone import api

import pytest


class TestPortalSettings:
    """Test that Portal configuration is correctly done."""

    @pytest.mark.parametrize(
        "key,expected",
        [
            ["plone.site_title", "Intranet da V2Tec"],
            ["plone.email_from_name", "Intranet da V2Tec"],
            ["plone.smtp_host", "localhost"],
            ["plone.smtp_port", 25],
            ["plone.twitter_username", "plone"],
        ],
    )
    def test_setting(self, portal, key: str, expected: str | int):
        """Test registry setting."""
        value = api.portal.get_registry_record(key)
        assert value == expected

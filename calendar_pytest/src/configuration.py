"""
Configuration specific to Calendar API tests.
"""

from common.configuration import config as common_config


class CalendarConfig:
    """Calendar API specific configuration."""

    @staticmethod
    def get_api_key() -> str:
        """Get Calendarific API key."""
        return common_config.get_calendarific_api_key()

    @staticmethod
    def get_base_url() -> str:
        """Get Calendarific base URL."""
        return common_config.get_base_url()

    # Default test parameters
    DEFAULT_COUNTRY = "US"
    DEFAULT_YEAR = 2019

    # Valid country codes for testing
    VALID_COUNTRY_CODES = [
        ("ss", "south_sudan"),
        ("es", "spain"),
        ("tz", "tanzania"),
        ("tg", "togo"),
        ("uk", "united_kingdom"),
        ("us", "united_states"),
        ("me", "montenegro"),
    ]


# Singleton instance
calendar_config = CalendarConfig()

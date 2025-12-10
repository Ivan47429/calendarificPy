import pytest
import logging
from calendar_pytest.src.requests import CalendarApiClient
from common.helpers import setup_logger


@pytest.fixture(scope="session", autouse=True)
def configure_logging():
    setup_logger("common", logging.INFO)
    setup_logger("calendar_pytest", logging.INFO)


@pytest.fixture(scope="function")
def calendar_api_client():
    client = CalendarApiClient()
    yield client
    client.close()


@pytest.fixture(scope="session")
def calendar_api_client_session():
    client = CalendarApiClient()
    yield client
    client.close()

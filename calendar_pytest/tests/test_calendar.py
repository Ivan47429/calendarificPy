import pytest
from calendar_pytest.src.requests import CalendarApiClient
from calendar_pytest.src.configuration import calendar_config
from common.constants import HTTP_OK
from common.helpers import extract_json_safely


class TestCalendarApi:
   
    @pytest.fixture
    def api_client(self):
        client = CalendarApiClient()
        yield client
        client.close()

    @pytest.mark.parametrize(
        "country_code",
        [
            pytest.param("ss", id="south_sudan"),
            pytest.param("es", id="spain"),
            pytest.param("tz", id="tanzania"),
            pytest.param("tg", id="togo"),
            pytest.param("uk", id="united_kingdom"),
            pytest.param("us", id="united_states"),
            pytest.param("me", id="montenegro"),
        ]
    )
    def test_get_holidays_returns_200(self, api_client, country_code):
        year = calendar_config.DEFAULT_YEAR
        response = api_client.get_holidays(country=country_code, year=year)

        assert response.status_code == HTTP_OK, \
            f"Expected status code {HTTP_OK} for country '{country_code}', but got {response.status_code}"

    @pytest.mark.parametrize(
        "country_code",
        [
            pytest.param("ss", id="south_sudan"),
            pytest.param("es", id="spain"),
            pytest.param("tz", id="tanzania"),
            pytest.param("tg", id="togo"),
            pytest.param("uk", id="united_kingdom"),
            pytest.param("us", id="united_states"),
            pytest.param("me", id="montenegro"),
        ]
    )
    def test_get_holidays_response_structure(self, api_client, country_code):
        year = calendar_config.DEFAULT_YEAR
        response = api_client.get_holidays(country=country_code, year=year)

        # Validate response is valid JSON with expected structure
        json_data = extract_json_safely(response)

        assert "meta" in json_data, \
            f"Response missing 'meta' field for country '{country_code}'"
        assert "response" in json_data, \
            f"Response missing 'response' field for country '{country_code}'"

        # Validate meta contains code field
        assert "code" in json_data["meta"], \
            f"Meta missing 'code' field for country '{country_code}'"
        assert json_data["meta"]["code"] == HTTP_OK, \
            f"Meta code mismatch for country '{country_code}'"

        # Validate response contains holidays array
        assert "holidays" in json_data["response"], \
            f"Response missing 'holidays' field for country '{country_code}'"
        assert isinstance(json_data["response"]["holidays"], list), \
            f"Holidays is not a list for country '{country_code}'"


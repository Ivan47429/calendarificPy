
from typing import Dict, Any, Optional
import requests
from requests import Response

from common.configuration import config
from common.constants import DEFAULT_TIMEOUT
from common.helpers import log_request, log_response, extract_json_safely
from calendar_pytest.src.models import CalendarificApiResponse


class CalendarApiClient:

    def __init__(self, api_key: Optional[str] = None, base_url: Optional[str] = None):
        self.api_key = api_key or config.get_calendarific_api_key()
        self.base_url = base_url or config.get_base_url()
        self.session = requests.Session()

    def get_holidays(
        self,
        country: str,
        year: int,
        additional_params: Optional[Dict[str, Any]] = None
    ) -> Response:
        endpoint = f"{self.base_url}/holidays"
        params = {
            "api_key": self.api_key,
            "country": country,
            "year": year
        }

        if additional_params:
            params.update(additional_params)

        log_request("GET", endpoint, params=params)
        response = self.session.get(endpoint, params=params, timeout=DEFAULT_TIMEOUT)
        log_response(response)

        return response

    def get_holidays_as_model(
        self,
        country: str,
        year: int,
        additional_params: Optional[Dict[str, Any]] = None
    ) -> CalendarificApiResponse:
        response = self.get_holidays(country, year, additional_params)
        response.raise_for_status()
        json_data = extract_json_safely(response)
        return CalendarificApiResponse.from_dict(json_data)

    def close(self) -> None:
        self.session.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

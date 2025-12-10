import logging
from typing import Any, Dict
from requests import Response


def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


def log_request(method: str, url: str, **kwargs) -> None:
    logger = logging.getLogger(__name__)
    logger.info(f"Request: {method.upper()} {url}")
    if kwargs.get('params'):
        logger.debug(f"Params: {kwargs['params']}")
    if kwargs.get('json'):
        logger.debug(f"Body: {kwargs['json']}")


def log_response(response: Response) -> None:
    logger = logging.getLogger(__name__)
    logger.info(f"Response: {response.status_code} - {response.reason}")
    logger.debug(f"Response Body: {response.text[:200]}...")


def validate_status_code(response: Response, expected_code: int) -> bool:
    return response.status_code == expected_code


def extract_json_safely(response: Response) -> Dict[str, Any]:
    try:
        return response.json()
    except ValueError as e:
        raise ValueError(f"Failed to parse JSON from response: {e}")

from dataclasses import dataclass
from typing import Any, Dict, List


@dataclass
class Country:
    id: str
    name: str
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Country':
        """Create Country instance from dictionary."""
        return cls(
            id=data['id'],
            name=data['name']
        )


@dataclass
class DateTime:
    """DateTime details model."""
    year: int
    month: int
    day: int

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'DateTime':
        """Create DateTime instance from dictionary."""
        return cls(
            year=data['year'],
            month=data['month'],
            day=data['day']
        )


@dataclass
class Date:
    """Date information model."""
    iso: str
    datetime: DateTime

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Date':
        """Create Date instance from dictionary."""
        return cls(
            iso=data['iso'],
            datetime=DateTime.from_dict(data['datetime'])
        )


@dataclass
class Holiday:
    """Holiday information model."""
    name: str
    description: str
    country: Country
    date: Date
    type: List[str]
    primary_type: str
    canonical_url: str
    urlid: str
    locations: str
    states: str

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Holiday':
        """Create Holiday instance from dictionary."""
        return cls(
            name=data['name'],
            description=data['description'],
            country=Country.from_dict(data['country']),
            date=Date.from_dict(data['date']),
            type=data['type'],
            primary_type=data['primary_type'],
            canonical_url=data['canonical_url'],
            urlid=data['urlid'],
            locations=data['locations'],
            states=data['states']
        )


@dataclass
class HolidaysResponse:
    """Holidays response data model."""
    holidays: List[Holiday]

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'HolidaysResponse':
        """Create HolidaysResponse instance from dictionary."""
        return cls(
            holidays=[Holiday.from_dict(h) for h in data['holidays']]
        )


@dataclass
class CalendarificApiResponse:
    """Complete Calendarific API response model."""
    meta: Dict[str, int]
    response: HolidaysResponse

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'CalendarificApiResponse':
        """Create CalendarificApiResponse instance from dictionary."""
        return cls(
            meta=data['meta'],
            response=HolidaysResponse.from_dict(data['response'])
        )

    @property
    def status_code(self) -> int:
        """Get status code from meta."""
        return self.meta['code']

    @property
    def holidays(self) -> List[Holiday]:
        """Get list of holidays."""
        return self.response.holidays

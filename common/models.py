from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class ApiMeta:
    """Common API metadata model."""
    code: int

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ApiMeta':
        """Create ApiMeta instance from dictionary."""
        return cls(code=data['code'])

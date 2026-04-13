from dataclasses import dataclass, field
from datetime import datetime, date, timedelta
from typing import ClassVar

from app.services.util import (generate_unique_id, date_lower_than_today_error,
    reservation_not_found_error, guest_not_found_error, room_not_available_error,
    room_not_found_error, room_already_exists_error)


# TODO: Implement Guest class here

@dataclass
class Guest:
    REGULAR = "regular"
    VIP = "vip"
    name: str
    email: str
    type_: str = REGULAR

    def __str__(self):
        return f"Guest {self.name} ({self.email}) of type {self.type_}"


# TODO: Implement Reservation class here


# TODO: Implement Room class here


# TODO: Implement Hotel class here


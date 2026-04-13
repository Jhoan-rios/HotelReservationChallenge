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
@dataclass
class Reservation:
    guest_name: str
    description: str
    check_in: date
    check_out: date
    guests: list[Guest] = field(default_factory=list)
    id: str = field(default_factory=generate_unique_id)

    def add_guest(self, name: str, email: str, type_: str = Guest.REGULAR):
        guest = Guest(name=name, email=email, type_=type_)
        self.guests.append(guest)

    def delete_guest(self, guest_index: int):
        if 0 <= guest_index < len(self.guests):
            del self.guests[guest_index]
        else:
            guest_not_found_error()

    def __len__(self):
        return (self.check_out - self.check_in).days

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"Guest: {self.guest_name}\n"
            f"Description: {self.description}\n"
            f"Dates: {self.check_in} - {self.check_out}"
        )


# TODO: Implement Room class here

    class Room:
        def __init__(self, number: int, type_: str, price_per_night):
            self.number: int = number
            self.type_: str = type_
            self.price_per_night: float = price_per_night
            self.available: dict[date, str | None] = {}

        def _init_availability(self):
            today = datetime.now().date()

            for i in range(365):
                dia_actual = today + timedelta(days=i)
                self.available[dia_actual] = None

        def book(self, reservation_id:str, check_in: date, check_out: date):
            pass


# TODO: Implement Hotel class here
class Hotel:

    def __init__(self):
        self.rooms: dict[int, Room] = {}
        self.reservations: dict[str, Reservation] = {}

    def add_room(self, number: int, type_: str, price_per_night: float):
        if number in self.rooms:
            room_already_exists_error()
        else:
            self.rooms[number] = Room(number, type_, price_per_night)

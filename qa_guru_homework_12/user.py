import dataclasses
from datetime import date


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile_number: str
    date_of_birth: date
    subject: str
    hobbies: str
    picture: str
    street_address: str
    city_address: str
    state_address: str

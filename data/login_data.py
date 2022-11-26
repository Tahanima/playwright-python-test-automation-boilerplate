from data.base_data import BaseData
from dataclasses import dataclass


@dataclass
class LoginData(BaseData):
    username: str = ' '
    password: str = ' '
    error_message: str = ' '

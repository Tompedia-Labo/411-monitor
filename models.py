from dataclasses import dataclass

@dataclass
class CameraAuth:
    url: str
    user: str
    password: str

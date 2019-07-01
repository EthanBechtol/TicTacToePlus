from dataclasses import dataclass


@dataclass
class PlayerTimer:
    character: str
    timer: float
    start_time: float

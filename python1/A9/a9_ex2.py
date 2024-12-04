class Time:
    def __init__(self, hours: int, minutes: int, seconds: int):
        if not isinstance(hours, int) or not isinstance(minutes, int) or not isinstance(seconds, int):
            raise TypeError("Hours, minutes, and seconds must be integers.")
        if hours < 0 or hours > 23:
            raise ValueError("hours must be between 0 and 23")
        if minutes < 0 or minutes > 59:
            raise ValueError("minutes must be between 0 and 59")
        if seconds < 0 or seconds > 59:
            raise ValueError("seconds must be between 0 and 59")
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def to_seconds(self) -> int:
        """Returns the total number of seconds represented by the Time object."""
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    @classmethod
    def from_seconds(cls, total_seconds: int) -> "Time":
        """Creates a Time object from the total number of seconds."""
        if not isinstance(total_seconds, int):
            raise TypeError("total_seconds must be an integer.")
        if total_seconds < 0 or total_seconds > 86399:
            raise ValueError("total_seconds must be between 0 and 86399 inclusive.")
        hours = total_seconds // 3600
        remaining = total_seconds % 3600
        minutes = remaining // 60
        seconds = remaining % 60
        return cls(hours, minutes, seconds)

    def __repr__(self) -> str:
        return f"Time(hours={self.hours}, minutes={self.minutes}, seconds={self.seconds})"

    def __str__(self) -> str:
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Time):
            return NotImplemented
        return (self.hours, self.minutes, self.seconds) == (other.hours, other.minutes, other.seconds)

    def __lt__(self, other) -> bool:
        if not isinstance(other, Time):
            return NotImplemented
        return self.to_seconds() < other.to_seconds()

    def __add__(self, other):
        if isinstance(other, Time):
            total_seconds = self.to_seconds() + other.to_seconds()
            if total_seconds > 86399:
                raise ValueError("Resulting time exceeds 23:59:59")
            return Time.from_seconds(total_seconds)
        elif isinstance(other, int):
            total_seconds = self.to_seconds() + other
            if total_seconds < 0 or total_seconds > 86399:
                raise ValueError("Resulting time must be between 00:00:00 and 23:59:59")
            return Time.from_seconds(total_seconds)
        return NotImplemented

    def __radd__(self, other):
        # Support int + Time
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Time):
            difference = self.to_seconds() - other.to_seconds()
            return difference
        elif isinstance(other, int):
            total_seconds = self.to_seconds() - other
            if total_seconds < 0:
                raise ValueError("Resulting time cannot be negative")
            return Time.from_seconds(total_seconds)
        return NotImplemented

    def __int__(self) -> int:
        return self.to_seconds()
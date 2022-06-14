from dataclasses import dataclass
from typing import List


def in_allowed_range(input):
    return 0 < input < 1000

@dataclass
class Stats:
    """Data stats entity."""
    stats: List[int]

    def less(self, value):
        """Get how many values are lower than the provided value.
        Args:
            value (int): Value to compare to.
        Returns:
            value (int): Quantity of numbers lower than value.
        Raises:
            ValueError
        """
        if not in_allowed_range(value):
            raise ValueError(f'Invalid input')
        try:
            key = self.stats[value]
        except KeyError:
            raise ValueError(f'Invalid key: {value}')

        return key["lesser"]

    def greater(self, value):
        """Get how many values are greater than the provided value.
        Args:
            value (int): Value to compare to.
        Returns:
            value (int): Quantity of numbers higher than value.
        Raises:
            ValueError
        """
        if not in_allowed_range(value):
            raise ValueError(f'Invalid input')
        try:
            key = self.stats[value]
        except KeyError:
            raise ValueError(f'Invalid key: {value}')

        return key["greater"]

    def between(self, start, end):
        """Get how many values are between start and end.
        Args:
            start (int): Starting value.
            end (int): End value.
        Returns:
            value (int): Quantity of numbers within range.
        Raises:
            ValueError
        """
        if not in_allowed_range(start) or not in_allowed_range(end):
            raise ValueError(f'Invalid input')
        if start == end:
            raise ValueError("Start must be different from end")
        try:
            start = self.stats[start]
        except KeyError:
            raise ValueError(f'Invalid key: {start}')

        try:
            end = self.stats[end]
        except KeyError:
            raise ValueError(f'Invalid key: {start}')

        return end["count"] + (end["lesser"] - start["lesser"])



class DataCapture:
    """Data capture entity"""

    def __init__(self):
        self.storage = {}

    def _is_build_ready(self):
        return bool(self.storage)

    def add(self, value):
        """Adds a value to storage.
        Args:
            value (int): Value to be added.
        Returns:
            None
        Raises:
            KeyError
        """
        try:
            self.storage[value] += 1
        except KeyError:
            self.storage[value] = 1

    def build_stats(self):
        """Compute stats about the stored values.
        Args:
            None
        Returns:
            stats (Stats): Stats object.
        Raises:
            ValueError
        """
        if not self._is_build_ready():
            raise ValueError("Data capture is empty!")

        stats = {}
        lesser, greater = 0, 0
        keys = sorted(list(self.storage.keys()))

        for key in keys:
            value = self.storage[key]
    
            stats[key] = {}
            stats[key]["count"] = value
            stats[key]["lesser"] = lesser
            lesser += value

        for key in reversed(keys):
            value = self.storage[key]
    
            stats[key]["greater"] = greater
            greater += value
        return Stats(stats)

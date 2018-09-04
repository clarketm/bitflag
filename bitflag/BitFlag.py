"""BitFlag module"""

from functools import reduce


class BitFlag:
    """
    BitFlag class.

    :param str options:
    :ivar int flags:
    """

    def __init__(self, *options: str):
        self.flags = 0
        self._options = options
        for i, v in enumerate(options):
            setattr(self, v, 2 ** i)

    def __repr__(self):
        return "BitFlag(" + f"flags={self.flags:0{len(self._options)}b}, " + ", ".join(f"{k}={v}" for k, v in self.items()) + ")"

    def __str__(self):
        return f"flags={self.flags:0{len(self._options)}b}, " + ", ".join(f"{k}={v}" for k, v in self.items())

    def __int__(self):
        return self.flags

    def __len__(self):
        return len(self._options)

    def __getitem__(self, item):
        try:
            index = int(item)
            return self._options[index]
        except ValueError:
            return self.has(item)

    def keys(self):
        return self._options

    def values(self):
        return [self.has(f) for f in self._options]

    def items(self):
        return [(f, self.has(f)) for f in self._options]

    @property
    def flags(self) -> int:
        return self._flags

    @flags.setter
    def flags(self, value: int) -> None:
        self._flags = value

    def mask(self, *options: str):
        """
        Create a mask for the current bit flags.

        :param str options:
        :return init: flags
        """
        return reduce(lambda a, b: a | getattr(self, b), options, 0)

    def has(self, *options: str) -> bool:
        """
        Check if one or more bit flags have been set.

        :param str options:
        :return init: flags
        """
        return bool(self.flags & self.mask(*options))

    def set(self, *options: str) -> int:
        """
        Set one or more bit flags.

        :param str options:
        :return init: flags
        """
        self.flags |= self.mask(*options)
        return self.flags

    def unset(self, *options: str) -> int:
        """
        Unset one or more bit flags.

        :param str options:
        :return init: flags
        """
        self.flags &= ~(self.mask(*options))
        return self.flags

    def toggle(self, *options: str) -> int:
        """
        Toggle one or more bit flags.

        :param str options:
        :return init: flags
        """
        self.flags ^= self.mask(*options)
        return self.flags

    def reset(self) -> int:
        """
        Reset (unset) all bit flags.

        :return init: flags
        """
        self.flags &= 0
        return self.flags

    def flip(self) -> int:
        """
        Flip all bit flags.

        :return init: flags
        """
        self.flags = ~(self.flags)
        return self.flags

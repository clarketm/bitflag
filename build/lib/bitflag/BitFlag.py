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
        for i, v in enumerate(options):
            setattr(self, v, 2 ** i)

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

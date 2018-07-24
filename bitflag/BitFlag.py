from functools import reduce


class BitFlag:
    def __init__(self, *options):
        self.flags = 0
        for i, v in enumerate(options):
            setattr(self, v, 2**i)

    @property
    def flags(self):
        return self._flags

    @flags.setter
    def flags(self, value):
        self._flags = value

    def mask(self, *options):
        return reduce(lambda a, b: a | getattr(self, b), options, 0)

    def has(self, *options):
        return bool(self.flags & self.mask(*options))

    def set(self, *options):
        self.flags |= self.mask(*options)
        return self.flags

    def unset(self, *options):
        self.flags &= ~(self.mask(*options))
        return self.flags

    def toggle(self, *options):
        self.flags ^= self.mask(*options)
        return self.flags

    def reset(self, *options):
        self.flags &= 0
        return self.flags

    def flip(self, *options):
        self.flags = ~(self.flags)
        return self.flags


if __name__ == '__main__':
    f = BitFlag('a', 'b')
    f.set('a')
    print(f.has('a'))
    print(f.has('b'))

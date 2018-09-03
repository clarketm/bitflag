# [BitFlag](https://pypi.org/project/bitflag/)

[![PyPi release](https://img.shields.io/pypi/v/bitflag.svg)](https://pypi.org/project/bitflag/)

A simple bit flag class for Python 🐍.

## Installation

```bash
$ pip install bitflag
```

## Usage

```python

# 1. import the "BitFlag" class.
from bitflag import BitFlag

# 2. initialize a BitFlag instance with any number of string, flag arguments.
bf = BitFlag("flagA", "flagB", "flagC")

# 3. run operations on those bit flags!

# set – Set one or more bit flags.
bf.set("flagB", "flagC")

# unset – Unset one or more bit flags.
bf.unset("flagB")

# has – Check if one or more bit flags have been set.
bf.has("flagC")

# toggle – Toggle one or more bit flags.
bf.toggle("flagA", "flagB", "flagC")

# reset – Reset (unset) all bit flags.
bf.reset()

# flip – Flip all bit flags.
bf.flip()

# keys - iterate over flag keys.
for k in bf.keys():
    print(k)

# values - iterate over flag values.
for v in bf.values():
    print(v)

# items - iterate over flag keys and values.
for k,v in bf.items():
    print(k, v)

# str - informal string representation.
str(bf)

# repr - formal string representation.
repr(bf)

# int - integer representation.
int(bf)

```

## License

MIT &copy; [**Travis Clarke**](https://blog.travismclarke.com/)

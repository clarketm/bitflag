# [BitFlag](https://pypi.org/project/bitflag/)

A bit flag class for python.

<br>

## Installation

```bash
$ pip install bitflag
```

<br>

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

```

<br>

## License

MIT &copy; [**Travis Clarke**](https://blog.travismclarke.com/)

# vim: expandtab tabstop=4 shiftwidth=4

from pathlib import Path
from random import choice
from string import ascii_letters, digits
from tempfile import gettempdir

def make_rand_name(length: int=15) -> str:
    return choice(ascii_letters) + ''.join([choice(ascii_letters+digits) for i in range(length-1)])

def TemporaryPath() -> Path:
    return Path(gettempdir()).joinpath(make_rand_name())

# The original implementation attempted to make TemporaryPath and
# TemporaryPathContext one and the same, but it turns out that
# pathlib.Path is difficult to subclass in a sustainable way.

class TemporaryPathContext:
    def __enter__(self) -> Path:
        self.path = TemporaryPath()  # pylint: disable=W0201
        self.path.touch()
        return self.path

    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:
        self.path.unlink()

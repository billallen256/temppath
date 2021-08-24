# vim: expandtab tabstop=4 shiftwidth=4

from pathlib import Path
from random import choice
from string import ascii_letters, digits
from tempfile import gettempdir

def make_rand_name(length: int=15) -> str:
    '''
    Returns a random string of alphanumeric characters.
    Always starts with a letter, not a number.
    '''
    return choice(ascii_letters) + ''.join([choice(ascii_letters+digits) for i in range(length-1)])

def TemporaryPath() -> Path:
    '''
    Returns a pathlib.Path in the system-defined temporary directory.
    '''
    return Path(gettempdir()).joinpath(make_rand_name())

# The original implementation attempted to make TemporaryPath and
# TemporaryPathContext one and the same, but it turns out that
# pathlib.Path is difficult to subclass in a sustainable way.

class TemporaryPathContext:
    '''
    Context manager that provides a TemporaryPath then deletes it
    once the context ends.
    '''
    def __enter__(self) -> Path:
        self.path = TemporaryPath()  # pylint: disable=W0201
        self.path.touch()
        return self.path

    def __exit__(self, exc_type, exc_value, exc_traceback) -> None:
        self.path.unlink()

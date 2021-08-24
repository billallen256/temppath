# temppath

Provides a quick way to get a `pathlib.Path` file in the system-defined
temporary space.  `temppath` does _not_ wrap `tempfile.NamedTemporaryFile`,
as that automatically deletes on close, and does not allow the same file to be
written, closed, then read [in Windows](https://docs.python.org/3/library/tempfile.html#tempfile.NamedTemporaryFile)
, which is inconsistent with the Unix implementation.  Since `temppath`
provides `pathlib.Path` objects, this is not an issue.

## Usage

There is a nice context manager, which will remove the path for you.

```python
from temppath import TemporaryPath

with TemporaryPath() as t:
    t.write_text('the quick brown fox jumps over the lazy dog')
    ...
    do_something_awesome()

# The file is removed when you leave the `with` context.
```

You also have the option to just clean it up yourself if you need more control.

```python
from temppath import TemporaryPath

t = TemporaryPath()
t.write_text('the quick brown fox jumps over the lazy dog')
...
do_something_awesome()
...
t.unlink()
```

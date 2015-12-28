# Python REPL Drop

Function to drop into a python repl real quick.
The cool thing about this is that globals and local variables from the caller function are available in the repl.
Press `^D` to return control to the program.

Copy the `interact` function from `repldrop.py` and happy REPLing!

```python
def interact():
    """Drop to an interactive REPL."""
    import code, inspect
    frame = inspect.currentframe()
    prevlocals = frame.f_back.f_locals
    replvars = globals().copy()
    replvars.update(prevlocals)
    code.InteractiveConsole(locals=replvars).interact()
```

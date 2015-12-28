def interact():
    """Drop to an interactive REPL."""
    import code, inspect
    frame = inspect.currentframe()
    prevlocals = frame.f_back.f_locals
    replvars = globals().copy()
    replvars.update(prevlocals)
    code.InteractiveConsole(locals=replvars).interact()


EXAMPLE_GLOBAL_VAR = {"a": "b"}

def foo(n):
    """An example function for debugging."""
    if n == 0:
        return
    a = n + 1
    b = 2 * a
    if n == 1:
        interact()
    foo(n-1)


if __name__ == "__main__":
    foo(5)
    print "done."

"""
$ python repldrop.py
Python 2.7.10 (default, Dec  5 2015, 03:33:07)
[GCC 5.2.1 20151010] on linux2
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> EXAMPLE_GLOBAL_VAR
{'a': 'b'}
>>> b
4
>>> n
1
>>> ^D
done.
"""

def interact():
    """Drop to an interactive REPL."""
    import code, inspect
    frame = inspect.currentframe()
    prevlocals = frame.f_back.f_locals
    replvars = globals().copy()
    replvars.update(prevlocals)
    code.InteractiveConsole(locals=replvars).interact()

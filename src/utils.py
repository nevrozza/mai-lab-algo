def require(condition, msg: str | None = None):
    if not condition:
        raise ValueError(msg)

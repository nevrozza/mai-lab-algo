def require(condition, msg: str | None = None):
    if not condition:
        raise ValueError(msg)


def is_num(num: str) -> bool:
    try:
        float(num)
        return True
    except ValueError:
        return False


def is_int(num: str) -> bool:
    try:
        return int(num) == float(num)
    except ValueError:
        return False

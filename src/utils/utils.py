def require(condition, msg: str | None = None):
    if not condition:
        raise ValueError(msg)


def is_num(num: str) -> bool:
    try:
        float(num)
        return True
    except ValueError:
        return False


def is_int(num: str, base=10) -> bool:
    try:
        return int(num, base=base) == float(num)
    except ValueError:
        return False

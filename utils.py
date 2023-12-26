def str_to_felt(text):
    b_text = bytes(text, "ascii")
    return int.from_bytes(b_text, "big")

def to_uint(a):
    """Takes in value, returns uint256-ish tuple."""
    return (a & ((1 << 128) - 1), a >> 128)

def long_str_to_array(text):
    res = []
    for tok in text:
        res.append(str_to_felt(tok))
    return res

def long_str_to_print_array(text):
    res = []
    for tok in text:
        res.append(str_to_felt(tok))
    return ' '.join(res)

def decimal_to_hex(decimal: int):
    return hex(decimal)

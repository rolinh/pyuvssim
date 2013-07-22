def clamp(x, mini=0, maxi=255):
    """Clamp the given value regarding mini/maxi."""
    return int(max(mini, min(x, maxi)))

def yuv2rgb(y, u, v):
    """Turn y, u and v components into r, g, b values."""

    c = y - 16
    d = u - 128
    e = v - 128

    r = clamp((298 * c + 409 * e + 128) >> 8)
    g = clamp((298 * c - 100 * d - 208 * e + 128) >> 8)
    b = clamp((298 * c + 516 * d + 128) >> 8)

    return r, g, b

def bytes2human(n, format="%(value)i%(symbol)s"):
    """
    >>> bytes2human(10000)
    '9K'
    >>> bytes2human(100001221)
    '95M'
    """
    symbols = ('B', 'K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols[1:]):
        prefix[s] = 1 << (i+1)*10
    for symbol in reversed(symbols[1:]):
        if n >= prefix[symbol]:
            value = float(n) / prefix[symbol]
            return format % locals()
    return format % dict(symbol=symbols[0], value=n)

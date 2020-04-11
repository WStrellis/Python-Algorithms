def addBinaryStrings(a, b):
    x = int(a or '0', 2)
    z = int(b or '0', 2)
    return f"{x + z:0b}"

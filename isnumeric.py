def isNumber(s):
    """
    :type s: str
    :rtype: bool
    """
    for ch in s:
        if not ch.isdigit():
            return False
    return True

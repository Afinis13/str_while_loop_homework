def main(s):
    """
    A variable of type str is given. Find and return how many consonant letters there are.
    Args:
        s: str
        consonant: other than vowels(a, e, i, o, u)
    Returns:
        int: return answer
    """
    s=0
    a=0

    while a<len(s):
        if s[a].count("a","e","i","o","u"):
            s+=1
            a+=1
    return s

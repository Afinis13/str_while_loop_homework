def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    s=0
    a=0
    while a<=len(s):
          if  s[a].isalpha():
            s+=1
            a+=1
    return s
    
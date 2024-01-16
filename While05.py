def main(s):
    """
    A variable of type str is given. Find how many lowercase letters there are and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    s=0
    a=0
    while a<=len(s):
          if s[a].islower():
            s+=1
            a+=1
    return 

    
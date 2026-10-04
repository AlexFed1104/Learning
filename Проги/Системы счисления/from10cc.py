def from10cc(num, numsys):
    try:
        ans = []
    k = 0
    n = 0
    while num >= numsys:
        k = num % numsys
        num = num // numsys
        n = k
        if k == 10:
            n = "A"
        elif n == 11:
            n ="B"
        elif k == 12:
            n ="C"
        elif k == 13:
            n ="D"
        elif k == 14:
            n ="E"
        elif k == 15:
            n ="F"
        ans.insert(0, str(n))
    k = num % numsys
    num = num // numsys
    n = k
    if k == 10:
        n = "A"
    elif n == 11:
        n ="B"
    elif k == 12:
        n ="C"
    elif k == 13:
        n ="D"
    elif k == 14:
        n ="E"
    elif k == 15:
        n ="F"
    ans.insert(0, str(n))
    return "".join(ans)
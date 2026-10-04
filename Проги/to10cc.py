def to10cc(num, numsys):
    power = 0
    ans = 0
    digits = []
    numb = list(str(num))
    for a in numb:
        if a.upper() == "A":
            a = 10
        elif a.upper() == "B":
            a = 11
        elif a.upper() == "C":
            a = 12
        elif a.upper() == "D":
            a = 13
        elif a.upper() == "E":
            a = 14
        elif a.upper() == "F":
            a = 15
        digits.append(int(a))
    digits.reverse()
    for i in digits:
        ans += i*(numsys**power)
        power += 1
    return ans
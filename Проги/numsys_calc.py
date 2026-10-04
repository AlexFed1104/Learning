from from10cc import from10cc
from to10cc import to10cc
a = input("1: ")
asys = int(input("sys: "))
b = input("2: ")
bsys = int(input("sys: "))
act = input("action: ")
ans = int(input("ans sys: "))
if act == "+":
    print(from10cc((to10cc(a,asys)+to10cc(b,bsys)), ans))
elif act == "-":
    print(from10cc((to10cc(a,asys)-to10cc(b,bsys)), ans))
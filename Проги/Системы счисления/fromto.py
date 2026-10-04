from from10cc import from10cc
from to10cc import to10cc
num = input("Число: ")
sys = int(input("Система счисления (из): "))
tarsys = int(input("Перевести в: "))
print(from10cc(to10cc(num,sys), tarsys))
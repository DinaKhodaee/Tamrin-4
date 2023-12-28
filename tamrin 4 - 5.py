from pyfiglet import Figlet
f = Figlet(font="standard")
print(f.renderText("Dina Khodaee"))

n1 = int(input("Enter you first num: "))
n2 = int(input("Enter you second num: "))

if n1 > n2:
    kmm = n1
else:
    kmm = n2
while kmm % n1 != 0 or kmm % n2 != 0:
    kmm += 1
print("kmm", n1, "va", n2, "=", kmm)
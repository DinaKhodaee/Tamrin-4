from pyfiglet import Figlet
f = Figlet(font="standard")
print(f.renderText("Dina Khodaee"))

sec = int(input("Enter your time by second: "))
h = sec // 3600
m = (sec % 3600) // 60
secc = sec % 60
print(h, ":", m, ":", secc)
from pyfiglet import Figlet
f = Figlet(font="standard")
print(f.renderText("Dina Khodaee"))

h = int(input("Enter your time by hour: "))
m = int(input("Enter your time by minute: "))
sec = h*3600 + m*60
print("Your time by second: ", sec)
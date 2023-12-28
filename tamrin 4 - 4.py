from pyfiglet import Figlet
f = Figlet(font="standard")
print(f.renderText("Dina Khodaee"))

num = int(input("Enter the nuber: "))
if num > 0:
    print("Yes! It's factorial.")
else: 
    print("No! It's not.")
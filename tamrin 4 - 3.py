from pyfiglet import Figlet
f = Figlet(font="standard")
print(f.renderText("Dina Khodaee"))

fib = [0, 1]
f = int(input("Enter the number of Fibonacci: "))
for i in range (f):
   ffib = fib[i] + fib[i+1]
   fib.append(ffib)
print(fib)
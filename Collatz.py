# Programm Code für Collatz Problem
a = input("Number input")
i = 0

while a != 1:
  if int(a) % 2 == 1:
    a = int(a) * 3 + 1
    i += 1
    print("Number: " + str(a))
  
  elif int(a) % 2 == 0:
    a = int(a) / 2
    i += 1
    print("Number: " + str(a))

print("The number has been calculated " + str(i) + " times")

# Programm Code für Collatz Problem

a = input("Zahl eingeben")
i = 0

if len(str(a)) > 20:
  print("Eine Zahl mit mehr als 22 Ziffern zeigt nur Errors ;)")
  a = 1



while a != 1:
  if int(a) % 2 == 1:
    a = int(a) * 3 + 1
    i += 1
    print("Zahl: " + str(a))
  
  elif int(a) % 2 == 0:
    a = int(a) / 2
    i += 1
    print("Zahl: " + str(a))

print("Es wurden " + str(i) + " Rechnungen durchgeführt")

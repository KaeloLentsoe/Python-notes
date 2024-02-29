Asparagus = 30.54
Beetroot = 1.45
Broccoli = 14.43
Garlic = 35.81
Potatoes = 2.04

print ("Enter the amount of Asparagus(kg):")
aspa = float(input())
print ("Enter the amount of Beetroot(kg):")
beet = float(input())
print ("Enter the amount of Broccoli(kg):")
broc = float(input())
print ("Enter the amount of Garlic(kg):")
garl = float(input())
print ("Enter the amount of Potatoes(kg):")
pota = float(input())

aspa = aspa * Asparagus
beet = beet * Beetroot
b = (((broc * Broccoli) * 20)/ 100)
broc = (broc * Broccoli) - b
garl = garl * Garlic
p = (((pota * Potatoes) * 30) / 100)
pota = (pota * Potatoes) - p

total = aspa + beet + broc + garl + pota
print ("The total the store has to pay:R", total)
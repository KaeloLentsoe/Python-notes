# Albasini Dam in Limpopo water application 

# Constants
MEGALITRE_CAPACITY = 1000000

# The user input 
millilitres_released = float(input("Amount of water released: "))

# Convert millilitre to litres 
litres_released = millilitres_released / 1000

# Calculating remaining litres
litres_remaining = MEGALITRE_CAPACITY / 1000 - litres_released

# Calculating percentage of water left 
percentage_left = (litres_remaining / (MEGALITRE_CAPACITY / 1000)) * 100

# Pring result 
print("/nConservation Report: ")
print(f"Amoount of water released: {litres_remaining:.2f} litres")
print(f"Amount of water left: {litres_remaining:.2f} litres")
print(f"Percentage: {percentage_left:.2f}%")
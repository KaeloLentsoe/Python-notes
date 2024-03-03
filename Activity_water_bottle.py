# A water bottle company application

# User input 
liters_of_water = float(input("Enter the number of liters of water: "))

# Calculating the number of bottles and remaining water
bottles_filled = int (liters_of_water // 0.5)
remaining_water = liters_of_water % 0.5

# Print the result 
print(f"You can fill {bottles_filled} bottles of water.")
print(f"You will have {remaining_water:.2f} liters of remaining.")
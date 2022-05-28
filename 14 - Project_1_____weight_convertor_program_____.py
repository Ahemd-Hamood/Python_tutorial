print("Weight Convertor to Pounds or Kilograms ")
weight = int(input("Please Enter Weight: "))
measurement = input("Select either (L) for Pounds or (K) for Kilograms: ")

# >> convert pound to Kilograms
if measurement.upper() == "L":
    result = weight * 0.45
    print(f"You're {result} Kilos")
elif measurement.upper() == "K":
    result = weight / 0.45
    print(f"You're {result} Pounds")
else:
    "Please Select either (L) for Pounds or (K) for Kilograms"


# output 1:
# Weight Convertor to Pounds or Kilograms
# Please Enter Weight: 72
# Select either (L) for Pounds or (K) for Kilograms: k
# You're 160.0 Pounds

# output 2:
# Weight Convertor to Pounds or Kilograms
# Please Enter Weight: 160
# Select either (L) for Pounds or (K) for Kilograms: l
# You're 72.0 Kilos

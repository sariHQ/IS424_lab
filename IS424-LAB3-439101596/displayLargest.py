



displayLargest = []

for i in range(10):
    number = int(input(f"--------------------\nPlease enter value {i+1}: "))
    displayLargest.append(number)

displayLargest.sort()

largest = displayLargest[-1]
print(f"--------------------\n\nThe largest number is ----->", largest)
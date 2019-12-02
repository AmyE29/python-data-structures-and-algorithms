numbers = [89, 2354, 3546, 23, 10, -923, 823, -12]
 
# Get list length
x= len(numbers)
 
# i goes from 0 to the middle
for i in range(int( x/2 )):
    # Swap first and last numbers, second and second to last, etc, until you reach the middle
    n = numbers[i]
    # The first 4 numbers become the last 4 numbers
    numbers[i] = numbers[x - i - 1]
    # Then reverse the second half
    numbers[x - i - 1] = n
 
# print the reversed numbers
print(numbers)

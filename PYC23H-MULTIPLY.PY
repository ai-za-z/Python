def tuple_product(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

numbers = (2, 3, 4, 5)
result = tuple_product(numbers)
print(f"The product of the numbers in the tuple is: {result}")
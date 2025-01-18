def square_it_out(start, end):
    squares = []
    even_squares = []
    odd_squares = []

    for num in range(start, end + 1):
        square = num * num
        squares.append(square)

        if square % 2 == 0:
            even_squares.append(square)
        else:
            odd_squares.append(square)

    return even_squares, odd_squares

start = int(input())
end = int(input())

even_squares, odd_squares = square_it_out(start, end)

print(even_squares)
print(odd_squares)
size = int(raw_input ("Type Size "))
innersize = size - 2

for i in range(size):
    for j in range(innersize):
        inner = ('*' + ' ' * innersize + '*' +"/n")
    square = '*' * size
    print square, inner



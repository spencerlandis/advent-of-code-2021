with open('./03_binary/input.txt', 'r') as file:
    lines = file.readlines()
    total = len(lines)
    line_length = len(lines[0])
    counts = [0 for i in range(line_length-1)]
    for line in lines:
        for i in range(line_length-1):
            counts[i] += int(line[i])
    gamma = ''
    epsilon = ''

    for i in range(line_length-1):
        if counts[i] > total / 2:
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    
    print(int(gamma, 2) * int(epsilon, 2))
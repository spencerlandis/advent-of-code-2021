with open('./02_dive/input.txt', 'r') as file:
    commands = file.readlines()
    x = 0
    y = 0
    for command in commands:
        split = command.split()
        direction = split[0]
        distance = int(split[1])
        if direction == 'forward':
            x += distance
        elif direction == 'down':
            y += distance
        else:
            y -= distance
    print(x * y)
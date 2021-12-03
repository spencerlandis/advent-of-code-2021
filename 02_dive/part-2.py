with open('./02_dive/input.txt', 'r') as file:
    commands = file.readlines()
    x = 0
    y = 0
    aim = 0
    for command in commands:
        split = command.split()
        direction = split[0]
        distance = int(split[1])
        if direction == 'forward':
            x += distance
            y += aim * distance
        elif direction == 'down':
            aim += distance
        else:
            aim -= distance
    print(x * y)
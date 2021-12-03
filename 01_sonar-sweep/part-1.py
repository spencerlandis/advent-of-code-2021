with open('./01_sonar-sweep/input.txt', 'r') as file:
    count = 0
    values = [int(x) for x in file.readlines()]
    previous = values.pop(0)
    while len(values) > 0:
        current = values.pop(0)
        if current > previous:
            count += 1
        previous = current
    print(count)
with open('./01_sonar-sweep/input.txt', 'r') as file:
    count = 0
    values = [int(x) for x in file.readlines()]
    previous = sum(values[0:3])
    for i in range(1, len(values) - 2):
        current = sum(values[i: i+3])
        if current > previous:
            count += 1
        previous = current
    print(count)
def filter_lines(lines, position, bigger_share=True):
    filtered_sum = sum([int(line[position]) for line in lines])
    winning_bit = '1' if filtered_sum >= (len(lines) / 2.0) else '0'
    if not bigger_share:
        winning_bit = '1' if filtered_sum < (len(lines) / 2.0) else '0'
    return [x for x in lines if x[position] == winning_bit]

with open('./03_binary/input.txt', 'r') as file:
    oxygen = file.readlines()
    co = [x for x in oxygen]

    position = 0
    while len(oxygen) > 1:
        oxygen = filter_lines(oxygen, position, True)
        position += 1

    position = 0
    while len(co) > 1:
        co = filter_lines(co, position, False)
        position += 1

    print(int(oxygen[0], 2) * int(co[0], 2))
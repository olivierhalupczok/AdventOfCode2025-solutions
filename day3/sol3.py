with open("./day3/input3.txt") as f:
    lines = f.read().strip().split('\n')

def find_maximal_joltage(lineChars: list[int], depth=1, current_accumulator=''):
    current_line_chars = lineChars[:len(lineChars) - depth + 1]
    # print(f'lc: {lineChars} ||| clc: {current_line_chars} ||| d: {depth} ||| ca: {current_accumulator}') # DEBUG
    if depth == 1:
        return current_accumulator + str(max(lineChars))
    else:
        maxJoltage = max(current_line_chars)
        index = lineChars.index(maxJoltage)
        return find_maximal_joltage(lineChars[index+1:], depth - 1, current_accumulator + str(maxJoltage))

def main(line):
    lineChars = [int(x) for x in line.strip()]
    return find_maximal_joltage(lineChars, 12)

results: list[str] = []
for line in lines:
    results.append(main(line))

print(sum([int(result) for result in results]))
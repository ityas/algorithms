a = int(input())
b = int(input())
c = int(input())
d = int(input())

if c == d:
    print(f'\t{c}')
else:
    nums = ''
    for elem in range(c, d+1):
        nums += f'\t{elem}'
    print(nums)

for left_num in range(a, b+1):
    line = f'{left_num}\t'
    for top_num in range(c, d+1):
        line += f'{left_num * top_num}\t'
    print(line)

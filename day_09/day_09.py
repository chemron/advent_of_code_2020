# https://adventofcode.com/2020/day/9

def is_valid(lst, target):
    for i, i_val in enumerate(lst):
        for j_val in lst[i:]:
            if i_val + j_val == target:
                return True
    return False


def get_set(lst, target):
    def update():
        global set
        global s_sum
        set = lst[left:right]
        s_sum = sum(set)
    # find a contiguous set in lst that sum to target

    # split into sub lists without any numbers >= target
    left = 0
    right = 2
    update()
    while s_sum != target:
        while s_sum < target:
            right += 1
            update()
        while s_sum > target:
            # set must be at least length 2
            if left + 2 == right:
                right += 1
            left += 1
            update()

    return(set)


f = open('input.txt', 'r')

numbers = f.read().split()
numbers = list(map(int, numbers))

# length of preamble
p_length = 25


# get invalid number
invalid = None
for i in range(p_length, len(numbers)):
    sub_list = numbers[i-p_length:i]
    target = numbers[i]
    if not is_valid(sub_list, target):
        invalid = target
        break

# now get set:
set = get_set(numbers, invalid)
print(f'invalid = {invalid}')
print(f'set = {set}')
print(f'weakness = {max(set) + min(set)}')

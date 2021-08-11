# https://adventofcode.com/2020/day/8

def run_to_loop(visited, acc_lst, instructions):
    # run program until loop is reached
    i = visited[-1]
    acc = acc_lst[-1]
    no_loop = True
    while no_loop and i < len(instructions):

        # opperation and argument
        opp, arg = instructions[i]

        if opp == 'acc':
            acc += int(arg)
            i += 1
        elif opp == 'jmp':
            i += int(arg)
        elif opp == 'nop':
            i += 1
        else:
            raise NameError(f'{opp} is not a valid operation.')

        if i in visited:
            no_loop = False
        else:
            # log start of next instruction
            visited.append(i)
            acc_lst.append(acc)

    return i, acc, visited, acc_lst


f = open('input.txt', 'r')
instructions = f.read().split('\n')[:-1]
f.close()

instructions = [instruction.split() for instruction in instructions]
# instructions completed:
visited = [0]
# accumulator after each instruction:
acc_lst = [0]
i = 0
acc = 0
change = None
last_opp = None
i, acc, visited, acc_lst = run_to_loop(visited, acc_lst, instructions)
# index of visited which needs to be changed
v_change_index = len(visited)
# index of instructions that needs to be changed
i_change_index = None
while i < len(instructions):
    # need to remove an earlier instruction
    v_change_index -= 1
    # change one instruction
    changed = False
    while not changed:
        i_change_index = visited[v_change_index]
        last_opp = instructions[i_change_index][0]
        if last_opp == 'jmp':
            change = 'nop'
            changed = True
        elif last_opp == 'nop':
            change = 'jmp'
            changed = True
        else:
            v_change_index -= 1
    # change instruction
    instructions[i_change_index][0] = change
    i, acc, visited, acc_lst = run_to_loop(visited[:v_change_index + 1],
                                           acc_lst[:v_change_index + 1],
                                           instructions)
    # change instruction back
    instructions[i_change_index][0] = last_opp

print(f'Instruction changed: {i_change_index}')
print(f'Instructions done: {visited}')
print(f'Final accumulator value: {acc_lst[-1]}')

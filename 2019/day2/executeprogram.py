# opcodes
ADD = 1
MULTIPLY = 2
HALT = 99


def execute_program(program):
    memory = program.copy()
    running = True
    pointer = 0

    while running:
        opcode = memory[pointer]

        if (opcode == ADD):
            value_one_index = memory[pointer + 1]
            value_two_index = memory[pointer + 2]
            result_index = memory[pointer + 3]

            memory[result_index] = memory[value_one_index] + memory[value_two_index]
            pointer += 4

        elif (opcode == MULTIPLY):
            value_one_index = memory[pointer + 1]
            value_two_index = memory[pointer + 2]
            result_index = memory[pointer + 3]

            memory[result_index] = memory[value_one_index] * memory[value_two_index]
            pointer += 4

        elif (opcode == HALT):
            running = False

        else:
            raise ValueError("An unknown opcode was read: {}".format(opcode))

    return memory[0]

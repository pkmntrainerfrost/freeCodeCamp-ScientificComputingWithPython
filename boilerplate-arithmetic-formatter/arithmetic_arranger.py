def arithmetic_arranger(problems,answers=False):

    if len(problems) > 5:
        return "Error: Too many problems."

    rows = ["" for i in range(4)]

    for problem_index, problem in enumerate(problems):
        operator = problem.split(" ")[1]
        operands = [problem.split(" ")[0],problem.split(" ")[2]]

        if operator != "+" and operator != "-":
            return "Error: Operator must be '+' or '-'."
        
        length = 0

        for operand in operands:
            if not operand.isnumeric():
                return "Error: Numbers must only contain digits."
            if len(operand) > 4:
                return "Error: Numbers cannot be more than four digits."
            if len(operand) > length:
                length = len(operand)

        if answers:
            if operator == "+":
                answer = str(int(operands[0]) + int(operands[1]))
            else:
                answer = str(int(operands[0]) - int(operands[1]))
            rows[3] += f"{' '*(2+length-len(answer))}{answer}"

        rows[0] += f"{' '*(2+(length-len(operands[0])))}{operands[0]}"
        rows[1] += f"{operator}{' '*(1+length-len(operands[1]))}{operands[1]}"
        rows[2] += f"{'-'*(2+length)}"

        if problem_index < (len(problems)-1):
            for row_num, row in enumerate(rows):
                rows[row_num] = f"{row}{' '*4}"

    arranged_problems = ""

    for row_num, row in enumerate(rows):
        arranged_problems += row
        if row_num < 3:
            arranged_problems += "\n"

    return arranged_problems

print(arithmetic_arranger(["1 + 9","50 - 35"],True))
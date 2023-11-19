# more compact solution

def decode(instructions: str) -> str:
    answer = ""
    for code in instructions.split():
        if code == "nl":
            answer += "\n"
        elif "sp" in code:
            answer += int(code[:-2]) * " "
        elif "bS" in code:
            answer += int(code[:-2]) * "\\"
        elif "sQ" in code:
            answer += int(code[:-2]) * "'"
        else:
            answer += int(code[:-1]) * code[-1]
    return answer

if __name__ == "__main__":
    instructions = ""
    print(answer)

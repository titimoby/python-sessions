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


def run_test(test_name: str):
    answer = ""
    with open(f"{test_name}-input.txt", "r") as input:
        instructions = input.read()
        answer = decode(instructions)
    target = ""
    with open(f"{test_name}-output.txt", "r") as input:
        target = input.read()

    if answer != target:
        print("There are difference(s) between your answer and what was expected")
        print("----- Your answer -----")
        print(answer)
        print("----- Expected result -----")
        print(target)
        assert False
    else:
        print("Well done!")
        print(answer)


if __name__ == "__main__":
    names = ["cat", "spider", "flamingo"]
    for name in names:
        run_test(f"../tests-data/{name}")

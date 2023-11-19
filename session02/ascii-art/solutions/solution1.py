# Raw solution


def decode(instructions: str) -> str:
    answer = ""
    for line in instructions.split(" "):
        answer += decode_line(line)
    return answer


def decode_line(line: str) -> str:
    howmany = ""
    char = ""
    for current in line:
        if len(howmany) == len(line) - 1:
            char = current
            break
        else:
            if current.isdigit():
                howmany += current
            else:
                if line[-2:] == "sp":
                    char = " "
                    break
                elif line[-2:] == "bS":
                    char = "\\"
                    break
                elif line[-2:] == "sQ":
                    char = "'"
                    break
                elif line[-2:] == "nl":
                    howmany = "1"
                    char = "\n"
                    break
    return int(howmany) * char


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

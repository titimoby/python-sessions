# Code in this function what needs to be done
def decode(instructions: str) -> str:
    pass


# This code is here and below to test if your solution solves the problem
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
        run_test(f"./tests-data/{name}")

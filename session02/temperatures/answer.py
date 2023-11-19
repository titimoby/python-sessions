def find_closest_to_zero(n: str, values: str) -> str:
    pass


def run_test(test_name: str):
    answer = ""
    with open(f"{test_name}-input.txt", "r") as input:
        n = input.readline()
        values = input.readline()
        answer = find_closest_to_zero(n, values)
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
    names = ["simple", "negatifs", "empty", "complexe", "choix", "choix2"]
    for name in names:
        run_test(f"./tests-data/{name}")

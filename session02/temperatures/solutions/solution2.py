def find_closest_to_zero(n: str, values: str) -> str:
    nb_values = int(n)
    if nb_values == 0:
        return "0"
    else:
        closestToZero = 5527

        for i in values.split():
            t = int(i)
            if abs(t) < abs(closestToZero) or t == abs(closestToZero):
                closestToZero = t

        return f"{closestToZero}"


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
        run_test(f"../tests-data/{name}")

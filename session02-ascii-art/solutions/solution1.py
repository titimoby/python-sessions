# Raw solution

def decode_instructions(instructions: str) -> str:
    answer = ""
    for code in t.split(" "):
        answer += decode(code)
    return answer

def decode(code: str) -> str:
    howmany = ""
    char = ""
    for current in code:
        if len(howmany) == len(code) - 1:
            char = current
            break
        else:
            if current.isdigit():
                howmany += current
            else:
                if code[-2:] == "sp":
                    char = " "
                    break
                elif code[-2:] == "bS":
                    char = "\\"
                    break
                elif code[-2:] == "sQ":
                    char = "'"
                    break
                elif code[-2:] == "nl":
                    howmany = "1"
                    char = "\n"
                    break
    return int(howmany) * char




print(answer)

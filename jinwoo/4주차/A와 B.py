S = input()
T = input()


def solve(string):
    if len(S) == len(string):
        if S == string:
            return 1
        return 0
    if string[-1] == "A":
        return solve(string[:-1])
    elif string[-1] == "B":
        return solve(string[:-1][::-1])
    return 0


print(solve(T))

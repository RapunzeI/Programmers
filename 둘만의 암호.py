import string
def solution(s, skip, index):
    answer = []
    alph = "abcdefghijklmnopqrstuvwxyz"

    for i in skip:
        alph = alph.replace(i, "")

    for i in s:
        new_index = index + alph.index(i)
        if len(alph) <= new_index:
            answer.append(alph[new_index % len(alph)])
        else:
            answer.append(alph[new_index])
    answer = "".join(answer)
    return answer

print(solution("aukks", "wbqd", 29))
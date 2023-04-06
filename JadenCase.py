def solution(s):
    answer = []

    s = s.split(' ')

    for i in s:
        if i != '' and ord(i[0]) > 65:
            i = i.capitalize()
        answer.append(i.capitalize())

    return " ".join(answer)

print(solution("  3people unFollowed me"))
print(solution("for the last week"))
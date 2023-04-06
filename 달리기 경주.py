def solution(players, callings):
    answer = []
    dict = {}
    seq = {}

    for i, j in enumerate(players):
        dict[i] = j
        seq[j] = i
    
    for player in callings:
        before = dict[seq[player] - 1]

        seq[before] += 1 
        seq[player] -= 1 
        dict[seq[before]] = before
        dict[seq[player]] = player
        
    answer = sorted(seq, key=lambda x:seq[x])
    return answer

print(solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]))

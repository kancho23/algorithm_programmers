#1번 풀이
def solution(participant, completion):
    answer = ""
    # 정렬해서 배열한다
    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break

    if answer == "":
        answer = participant[-1]

    return answer

#2번 풀이
def solution(participant, completion):
    hashDict = {}
    sumHash = 0

    for part in participant:
        hashDict[hash(part)] = part
        sumHash += hash(part)
        #part는 사람 이름
        #hash(part)는 그 사람한테 해당되는 숫자(value)

    for comp in completion:
        sumHash -= hash(comp)
        #comp라는 사람이름의, 해당되는 숫자를 뺌

    return hashDict[sumHash]
    #달리지 않은 사람의 숫자는 sumHash이고,
    #이를 다시 hashDict[]에 넣으면, 사람 이름이 튀어나온다.

#3번 풀이
import collections
def solution(participant, completion):
    #리스트를 가지고 counter를 생성하면, key가 이름이고 value가 count인 딕셔너리 반환
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


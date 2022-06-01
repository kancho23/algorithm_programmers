#1번 풀이(최적화 안됨)
def dfs(s, numbers, visited, lst):
    if s != "": lst.append(s)

    for i in range(len(numbers)):
        if visited[i] == False:
            visited[i] = True
            # if s != "": lst.append(s)
            dfs(s + numbers[i], numbers, visited, lst)
            visited[i] = False


def solution(numbers):
    lst = []
    visited = [False] * len(numbers)

    dfs("", numbers, visited, lst)

    # 겹치지 않는 list 제작
    result = list(set(lst))
    for l in result:
        if len(l) != 1:
            for o in range(len(l)):
                if l[o] == '0':
                    new_l = l.replace('0', '', 1) #왜 'l[o]',''는 안되는지?
                    result[result.index(l)] = new_l
                else:
                    break
    result = list(set(result))
    answer = len(result)

    # 소수 개수 세기
    for j in result:
        if int(j) == 0 or int(j) == 1:  # 소수 불가능
            answer -= 1

        else:
            for k in range(2, int(j)):
                if int(j) % k == 0:  # 소수 아님
                    answer -= 1
                    break

    return answer

#2번 풀이(최적화됨)
def dfs(s, numbers, visited, lst):
    if s != "" and s not in lst:
        lst.append(s)

    for i in range(len(numbers)):
        if visited[i] == False and s + numbers[i] != "0":
            visited[i] = True
            dfs(s + numbers[i], numbers, visited, lst)
            visited[i] = False


def solution(numbers):
    lst = []
    visited = [False] * len(numbers)

    dfs("", numbers, visited, lst)

    # 겹치지 않는 list 제작
    lst = list(set(lst))
    answer = len(lst)

    # 소수 개수 세기
    for j in lst:
        if int(j) == 0 or int(j) == 1:  # 소수 불가능
            answer -= 1

        else:
            for k in range(2, int(int(j) ** 0.5 + 1)):
                if int(j) % k == 0:  # 소수 아님
                    answer -= 1
                    break

    return answer
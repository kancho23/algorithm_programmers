# This is a sample Python script.
def solution(citations):
    citations.sort()
    # [0,1,2,5,6]
    # 임의 숫자 이상의, 개수 세기
    # 임의 숫자 <= 개수 일때, answer 갱신

    cnt = 0
    for i in range(citations[len(citations) - 1]):
        cnt += citations.count(citations[len(citations) - 1] - i)
        if citations[len(citations) - 1] - i <= cnt:
            answer = citations[len(citations) - 1] - i
            break

    return answer


def solution(citations):
    citations.sort()
    answer = 0
    # [0,1,2,5,6]
    # 임의 숫자 이상의, 개수 세기
    # 임의 숫자 <= 개수 일때, answer 갱신

    cnt = 0
    for i in range(citations[len(citations) - 1]):
        cnt += citations.count(citations[len(citations) - 1] - i)
        if citations[len(citations) - 1] - i <= cnt:
            answer = citations[len(citations) - 1] - i
            break

    return answer

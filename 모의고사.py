def solution(answers):
    # 각자 푸는 방식 배열로 뮨자개수
    in_1 = [1, 2, 3, 4, 5]*2000
    in_2 = [2, 1, 2, 3, 2, 4, 2, 5]*1250
    in_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*1000

    cnt = [0, 0, 0]
    # answer 돌면서, answer_cnt 하나씩 올림
    for i in range(len(answers)):
        if answers[i] == in_1[i]:
            cnt[0] += 1
        if answers[i] == in_2[i]:
            cnt[1] += 1
        if answers[i] == in_3[i]:
            cnt[2] += 1

    max_cnt = max(cnt)
    # 아무도 못맞췄을 때
    answer = []
    for j in range(len(cnt)):
        if cnt[j] == max_cnt:
            answer.append(j+1)

    return answer

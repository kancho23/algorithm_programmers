# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#1차 풀이
def solution(phone_book):
    # len이 작은것만 접두사가 될 수 있다
    answer = ""
    phone_book.sort()
    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            # 시작자리 다르면 break
            if phone_book[i][0] != phone_book[j][0]:
                break
            else:
                if phone_book[i] in phone_book[j]:
                    answer = False
                    break

    if answer == "":
        answer = True
    # 하나라도 접두사가 발견되면 loop를 멈춥니다
    return(answer)

#2차 풀이
def solution(phone_book):
    phone_book.sort()

    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False

    return True

#3차 풀이
def solution(phone_book):
    answer = True
    dic = {}
    for p in phone_book:
        dic[p] = 1

    for p in phone_book:
        tmp = ""
        for num in p:
            tmp += num
            if tmp in dic and tmp!= p :
                answer = False

    return answer

phone_book = 	["123", "456", "789"]
solution(phone_book)

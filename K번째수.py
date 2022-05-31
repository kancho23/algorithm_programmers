# This is a sample Python script.

def solution(array, commands):
    answer = []
    for i in commands:
        #i=[2,5,3]
        array_i=[]
        array_i = array[i[0]-1:i[1]]
        array_i.sort()
        answer.append(array_i[i[2]-1])
    return answer

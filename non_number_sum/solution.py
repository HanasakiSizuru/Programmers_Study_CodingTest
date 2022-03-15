def solution(numbers):
    nlist = [0,1,2,3,4,5,6,7,8,9]
    answer = 0
    for n in nlist:
        if n not in numbers:
            answer += n
    return answer

def main():
    ns = [1,2,3,4,6,7,8,0]
    print(solution(ns))

    ns = [5,8,4,0,6,7,9]
    print(solution(ns))
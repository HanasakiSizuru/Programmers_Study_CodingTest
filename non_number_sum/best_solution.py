def solution(numbers):
    return 45 - sum(numbers)

def main():
    ns = [1,2,3,4,6,7,8,0]
    print(solution(ns))

    ns = [5,8,4,0,6,7,9]
    print(solution(ns))

main()
#재귀문으로 하려 했으나 최대 재귀 깊이(1000)을 초과하는 값이 나올 것이므로 반복문으로 만듦
def solution(n):
    list124 = ['1','2','4']
    answer = ""
    while (n>0):
        answer = list124[(n%3)-1] + answer
        n = (n-1) // 3
    return answer

def main():
    n = 100
    print(solution(n))

main()

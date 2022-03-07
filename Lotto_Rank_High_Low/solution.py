def solution(lottos, win_nums):
    answer = 0
    rank = [6,6,5,4,3,2,1]
    cnt0 = lottos.count(0)
    
    for lotto in lottos:
        if lotto in win_nums:
            answer += 1

            
    return rank[answer+cnt0], rank[answer]

def main():
    #예시1
    lottos = [44,1,0,0,31,25]
    win_nums = [31,10,45,1,6,19]
    result = solution(lottos,win_nums)
    print(result)
    #예시2
    lottos = [0,0,0,0,0,0]
    win_nums = [38,19,20,40,15,25]
    result = solution(lottos,win_nums)
    print(result)
    #예시3
    lottos = [45,4,35,20,3,9]
    win_nums = [20,9,3,45,4,35]
    result = solution(lottos,win_nums)
    print(result)

main()
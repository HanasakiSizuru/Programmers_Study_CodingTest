def solution(lottos, win_nums):
    answer = [0,0]
    correct = [0,0]
    for lotto in lottos:
        if lotto == 0:
            correct[0] += 1
        else :
            for wnum in win_nums:
                if lotto == wnum:
                    correct[0] += 1
                    correct[1] += 1
    pos = 0
    for cnum in correct:
        if cnum == 2:
            answer[pos] = 5
        elif cnum == 3:
            answer[pos] = 4
        elif cnum == 4:
            answer[pos] = 3
        elif cnum == 5:
            answer[pos] = 2
        elif cnum == 6:
            answer[pos] = 1
        else:
            answer[pos] = 6
        pos += 1

    return answer

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
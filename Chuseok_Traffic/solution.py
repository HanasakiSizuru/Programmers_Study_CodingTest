def solution(lines):

    time_list = [["" for _ in range(2)] for _ in range(len(lines))]
    lcnt = 0
    for line in lines:
        sline = line.split()
        sline[2].replace('s','')
        
        lcnt += 1
        
    answer = 0
    return answer

def main():
    lines = [
        "2016-09-15 01:00:04.001 2.0s",
        "2016-09-15 01:00:07.000 2s"
        ]
    print(solution(lines))
    
    lines = [
        "2016-09-15 01:00:04.002 2.0s",
        "2016-09-15 01:00:07.000 2s"
        ]
    print(solution(lines))

    lines = [
        "2016-09-15 20:59:57.421 0.351s",
        "2016-09-15 20:59:58.233 1.181s",
        "2016-09-15 20:59:58.299 0.8s",
        "2016-09-15 20:59:58.688 1.041s",
        "2016-09-15 20:59:59.591 1.412s",
        "2016-09-15 21:00:00.464 1.466s",
        "2016-09-15 21:00:00.741 1.581s",
        "2016-09-15 21:00:00.748 2.31s",
        "2016-09-15 21:00:00.966 0.381s",
        "2016-09-15 21:00:02.066 2.62s"
        ]
    print(solution(lines))

main()
def solution(absolutes, signs):
    for i in range(len(absolutes)):
        if signs[i] == False:
            absolutes[i] -= 2*absolutes[i]
    return sum(absolutes)

def main():
    abs = [4,7,12]
    signs = [True,False,True]
    print(solution(abs,signs))

    abs = [1,2,3]
    signs = [False,False,True]
    print(solution(abs,signs))

main()
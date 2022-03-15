def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))

def main():
    abs = [4,7,12]
    signs = [True,False,True]
    print(solution(abs,signs))

    abs = [1,2,3]
    signs = [False,False,True]
    print(solution(abs,signs))

main()
def solution(new_id):
    check = new_id
    while(True):
        # 1.소문자로 치환    
        new_id = new_id.lower()
        # 2.지정된 문자 외 제거
        new_id = new_id.translate(str.maketrans('~!@#$%^&*()=+[{]}:?,<>/',' '*23)).replace(' ','')
        # 3. '.'이 여러개면 하나만 표시
        while(new_id.find('..')!=-1):
            new_id = new_id.replace('..','.')

        # 4. 처음과 끝이 '.'이면 제거
        if new_id.startswith('.'):
            new_id = new_id[1:]
        if new_id.endswith('.'):
            new_id = new_id[:-1]
        # 5. 빈문자열이면 a반환
        if new_id == '':
            new_id = 'a'

        # 6. 길이가 16이상이면 처음15개만, 2자 이하면 마지막 문자를 반복해 3으로 만듦
        if len(new_id) >= 16:
            new_id = new_id[0:15]
        length = len(new_id)
        while len(new_id) <= 2:
            new_id = new_id + new_id[-1]
        # 7. 한 바퀴 테스트 끝난 후 처음 값과 같다면 반환. 그렇지 않으면 바뀐 값을 저장하고 한 바퀘 더 돌아서 체크
        if(check == new_id):
            return new_id
        else:
            check = new_id

def main():
    new_id = "...!@BaT#*..y.abcdefghijklm"
    print(solution(new_id))
    new_id = "z-+.^."
    print(solution(new_id))
    new_id = "=.="
    print(solution(new_id))
    new_id = "123_.def"
    print(solution(new_id))
    new_id = "abcdefghijklmn.p"
    print(solution(new_id))

main()

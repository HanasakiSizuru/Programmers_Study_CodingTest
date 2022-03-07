def solution(new_id):

    allow = ['[a-z]','[0-9]','-','_','.']
    
    # 1.소문자로 치환    
    new_id.lower()
    
    # 2.지정된 문자 외 제거
    for i in range(new_id.length()):
        if new_id[i] not in allow:
            new_id[i] = ''
    
    # 3. '.'이 여러개면 하나만 표시
    
    # 4. 처음과 끝이 '.'이면 제거
    if new_id.startswith('.'):
        new_id[0] = ''
    if new_id.endswith('.'):
        new_id[-1] = ''
    # 5. 빈문자열이면 a반환
    if new_id == "":
        return "a"
    
    if new_id.length() >= 16:
        new_id = new_id[0:16]
    length = new_id.length()
    if new_id.length() <= 2:
        new_id[length:4] = new_id[-1]
        
    return new_id
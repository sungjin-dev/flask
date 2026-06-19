import re

def printWithLine(*messages):
    print('-' * 20)
    for message in messages:
        print(message)
        print('-' * 20)
    print('\n')

def isValidText(value: str, allowSpace = True) -> bool:
    
    if not isinstance(value, str):
        return False
    
    pattern = r'^[a-zA-Zㄱ-ㅣ가-힣\s]+$' if allowSpace else r'^[a-zA-Zㄱ-ㅣ가-힣]+$'
    
    return bool(re.match(pattern, value))

def convertibleToInt(value) -> bool:
    try:
        int(value)
        return True
    except (ValueError, TypeError):
        return False
    
def removeSpace(plateNum: str) -> str:
    return plateNum.replace(" ", "").upper()

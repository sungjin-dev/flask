import config
from carManageService import CMService

METHOD = 'input'

flag = True
service = CMService()

while flag:
    selectedMenuNum = int(input('1.등록     2. 조회     3. 수정     4. 삭제     0.종료'))
    if selectedMenuNum == config.REGISTER:
        service.register(method=METHOD)
    elif selectedMenuNum == config.CHECK:
        service.check(method=METHOD)
    elif selectedMenuNum == config.MODIFY:
        service.modify(method=METHOD)
    elif selectedMenuNum == config.DELETE:
        service.delete(method=METHOD)
    elif selectedMenuNum == config.EXIT:
        flag = False
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')   # 메인페이지
def home():       # 서버에서 자동 실행 
    return "<h1>Hello Flask</h1>"

#http://127.0.0.1:5000/hello
@app.route('/hello')      #hello --> command
def hello():
    return "Hello Student" 

#http://127.0.0.1:5000/me
@app.route('/me')
def me():
    return '나는 Flask 개발자 입니다.'

#http://127.0.0.1:5000/about
@app.route('/about')
def about():
    return '소개 페이지'

#http://127.0.0.1:5000/users/1
# 동적 URL 처리(Path Parameter)
                     # 파라미터
# int  정수
# float 실수
# path   전체 경로(중간에 /가 있어도 문자열 끝까지 모두 받는다)                                     
@app.route('/users/<int:user_id>')
def get_user(user_id):
    print(f'user_id: {user_id}') # 1
    return f'{user_id} 사용자 조회' # 사용자 조회 
# 사용자 화면이 아닌 개발자의 서버 터미널(VS Code 콘솔 등) 창에 로그가 찍힘.

# string 문자열
# http://127.0.0.1:5000/users/gildong
# @app.route('/users/<string:name>')
# def get_name(name):
#     return f'{name}님 요청'

# http://www.naver.com(/) 초기 메인화면으로 

# float 
# http://127.0.0.1:5000/users/pi
@app.route('/pi/<float:pi>')
def get_name(pi):
    return f'pi: {pi}'
#path 
# http://127.0.0.1:5000/files/images/cat.jpg
@app.route('/files/<path:filepath>') # filepath = images/cat.jpg
def files(filepath):
    return f'filepath: {filepath}'  # filepath: images/cat.jpg

# 구분자가 있어도 하나의 문자열로 인식

#GET
# # http://127.0.0.1:5000/search/weather   >>경로 변수
# @app.route('/search/<string:keyword>')
# def search(keyword):
#     return f'keyword: {keyword}'

#GET 
# 1. 경로 변수(path variale)

#http://127.0.0.1:5000/search/7
# @app.route('/search/<int:no>', methods=['GET'])
# def search(no):
#     return f'{no} 사용자'

# 쿼리 스트링(query string)
#http://127.0.0.1:5000/search?uNoo=7
@app.route('/search', methods=['GET'])
def search_query():
    uNo = request.args.get('uNoo')
    return f'{uNo} 사용자'

# request                     ?     키 벨류 쌍으로 
# http://127.0.0.1:5000/search?keyword=weather&age=20  >> 쿼리 스트링(query string)
@app.route('/search')
def search():
    keyword = request.args.get('keyword')      #get방식의 파라미터를 가져올 수 있음
    age = request.args.get('age')      
            # request객체에서 arguments들 중에서 keyword값만 가져와라
    return f'keyword: {keyword}, age : {age}'

#POST
# @app.route('/login', methods=["POST", "PUT", "DELETE", "GET"])   #없으면 GET방식

# http://127.0.0.1:5000/login
#POST
@app.route("/login_form")
def login_form1():
    str = ''
    str += '<form action="/login" method="post">' 
    str += '    <input type="text" name="u_id">' 
    str += '<br>' 
    str += '    <input type="password" name="u_pw">' 
    str += '<br>' 
    str += '    <input type="submit" value="SIGNUP">' 
    str += '</form>'

    return str

@app.route('/login', methods=["POST"])   
def login1():
    return "맛점"

'''             get post...
<form action="" method="" name="">
<input type="text" name="u_id"
'''

#POST
#http://127.0.0.1:5000/login
@app.route('/login', methods=["GET"])    
def login_form():
    '''
    str = ''
    str += '<form action="/login" method="post">' 
    str += '<input type="text" name="u_id" placeholder="Input user ID!!">' 
    str += '<br>' 
    str += '<input type="password" name="u_pw" placeholder="Input user PW!!>' 
    str += '<br>' 
    str += '<input type="submit" value="SIGN UP">' 
    str += '</form>'    
   
    return str
    '''
    return '''
    <form action="/login" method="post">
        <input type="text" name="u_id" placeholder="Input user ID!!">
            <br>
        <input type="password" name="u_pw" placeholder="Input user PW!!"> 
            <br>
        <input type="submit" value="SIGN UP">
    </form>
    '''
# <form action="/login" ...>  ->  무지성 택배
# 라우터(서버)의 역할: "서버 회사 1층의 우편물 분류실"
#/login으로 온 POST 택배네? 이건 3층 보안팀의 login_confirm() 함수 담당자

@app.route('/login_confirm', methods=['post'])
def login_confirm():
    u_id = request.form.get('u_id')
    u_pw = request.form.get('u_pw')

    if u_id == 'gildong' and u_pw == '1234':
        return f'{u_id}님 로그인 성공!!'
    else:
        return f'{u_id}님 로그인 성패!!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


# 요청을 하는건 클라이언트 요청을 처리하는 쪽이 서버
'''
이건 단순 문자열 출력 x  터미널 명령프롬프트 그런게 아니다 

내가 만든 프로그램이   네트워크 통신 처리
웹서버가 되어         외부의 연결을 기다리는 '서버(Server)' 프로그램으로 동작
브라우저로 참여       웹 브라우저를 통해 이 프로그램에 접속
'''

# 라우팅(Routing)  - URL 요청을 특정 함수로 연결
# 웹 서버의 '안내데스크 직원(또는 교환원)


# GET방식은 방금 위에서 한 방식  URL주소 도메인에 붙여서 

# POST 방식의 경우 요청을 할 때 
# HTTP 객체가 형성되는데 그 정보를 BODY에 숨겨서 전달함

#PUT DELETE도 POST처럼 body에 숨겨서 보냄. 각각 다른 

'''
Create: 생성   post
Read: 조회     get
Update: 수정   put
Delete: 삭제   delete
'''

'''
템플릿 엔진은 미리 정의된 '템플릿(데이터가 채워질 공간)'에 
'실제 데이터'를 주입하여, 최종적인 HTML 문서를 생성하는 프로그램 

웹문서 모양만 제공. 템플릿 -> 뼈대만 만들어 놓고 데이터만 주입해서 묶어서 응답해주는 과정
'''

# static -> css js jpg mp3 mp4 etc.
# templates - > html
# -app.py



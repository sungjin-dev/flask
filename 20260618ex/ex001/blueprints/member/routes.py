from flask import Blueprint, render_template, request, redirect, session
from utils.json_manager import load_members, save_members

member_bp = Blueprint(
    'member',
    __name__,
    url_prefix='/member'
)

#signup_form                      
@member_bp.route('/signup_form', methods=['GET'])
def signup_form():

    result = request.args.get('result')

    return render_template('signup_form.html', result = result)

#signup_confirm
@member_bp.route('/signup_confirm', methods=['POST'])
def signup_confirm():
    mId = request.form['mId']
    mPw = request.form['mPw']
    mMail = request.form['mMail']
    mPhone = request.form['mPhone']

    members = load_members()

    # 아이디 중복 체크
    if mId in members:
        return render_template('signup_result.html', 
                               result='NG')
    
    members[mId] = {
        "mId" : mId,
        "mPw" : mPw,
        "mMail" : mMail,
        "mPhone" : mPhone
    }

    save_members(members)

    return render_template('signup_result.html',
                           result='OK')

#signin_form
@member_bp.route('/signin_form', methods=['GET'])
def signin_form():
    return render_template('signin_form.html')

#signin_confirm
@member_bp.route('/signin_confirm', methods = ['POST'])
def signin_confirm():
    mId = request.form['mId']
    mPw = request.form['mPw']

    members = load_members()

    
    if mId in members and members[mId]['mPw'] == mPw:
        session['signinedMemberId'] = mId
        return render_template('signin_result.html')
    
    return redirect('/member/signin_form?result=fail')


#/member/signout_confirm
@member_bp.route('/signout_confirm', methods=['GET'])
def signout_confirm():

    session.clear()                         # 기존 세션 객체가 사라지고 새로운 객체가 생성 
    #session.pop('signinedMemberId', None)  # 특정 부분 정보만 저격해서 삭제 가능

    return redirect('/')

# /member/modify_form
@member_bp.route('/modify_form')
def modify_form():
    members = load_members()
    member =  members[session.get('signinedMemberId')]   # 현재 로그인되어 있는 회원정보 수집

    return render_template(
        'modify_form.html',
        member = member
    )

#/member/modify_confirm
@member_bp.route('/modify_confirm', methods=['POST'])
def modify_confirm():

    '''
    현재 로그인 되어 있는 회원 ID가 'gildong'이다.
    '''    
    mId = request.form['mId']
    mPw = request.form['mPw']
    mMail = request.form['mMail']
    mPhone = request.form['mPhone']

    members = load_members()
    member = members[mId]
    member['mPw'] = mPw
    member['mMail'] = mMail
    member['mPhone'] = mPhone

    save_members(members)

    return render_template('modify_result.html')


# /member/delete_confirm
@member_bp.route('/delete_confirm', methods=['POST'])
def delete_confirm():
    
    members = load_members()
    session.get('signinedMemberId')
    del members['signinedMemberId']

    save_members(members)

    session.clear()

    return render_template('delete_result.html')

# HTTP 프로토콜

# '''
# 1.클라이언트-서버 구조 


# 2.무상태(Stateless) 프로토콜
# 각 요청은 독립적으로 처리 
# 이전 정보를 기억 x 
# 로그인 상태 유지하기 위해 쿠키 세션 토큰

# 쿠키 - txt파일에 로그인 정보를 담아서 http 전송을 같이 보낸 이후에 
# 서버가 임시로 가지고 있다가 이를 나중에 요청이 들어오면 
# 이 txt파일과 대조해서 로그인한 유저인지 확인한다. 
# - 쿠키는 보안에 취약 (개인 기기에서 생성하는 태생적 한계)  - 주체가 개인

# 세션 - 서버에서 정보를 생성함.                           - 주체가 서버
#     세션 객체가 생성되어 대기하고 있다가 누군가 접속할 때 이 세션객체에 정보를 넣어둠 
#     유니크한 정보로  정보를 변환하여 해당기기 프로그램에 저장해놈. 
#     세션 정보를 서버에서 기기에 전달할 때 그 세션 정보를 하이제킹 하는 보안 헛점이 생김

# jwt - 현존 최강 보안 방식 공인인증서 
#       코드 유효시간을 굉장히 짧게 해서 방어     

# 3.비연결성(Connectionless)
#  서버 과부하를 방지하기 위해서
#  요청과 응답이 끝나면 연결이 종료하는 것이 기본동작
#  많은 사용자의 요청을 효율적으로 처리  
'''
members_trigger.json         

[아이디1, 아이디2, 아이디3...]
아이디는 고유해야하기 때문에 해당 아이디로 가입하는걸 막음

'''
# '''
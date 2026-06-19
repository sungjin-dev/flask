from flask import Blueprint, render_template, request, redirect, session
from utils.json_manager import load_accounts, save_accounts
from utils import time
import uuid

bank_bp = Blueprint(
    'bank',
    __name__,
    url_prefix='/bank'
)

#newaccount_form                      
@bank_bp.route('/newaccount_form', methods=['GET'])
def newaccount_form():

    result = request.args.get('result')

    return render_template('newaccount_form.html', result = result)

#newaccount_confirm
@bank_bp.route('/newaccount_confirm', methods=['POST'])
def newaccount_confirm():
    mId = session['signinedMemberId']

    if mId == '':
        return render_template('newaccount_result.html', 
                               result='NG')
    
    regdate = time.getCurrentDateTime()
    
    mId = request.form['mId']
    aNum = request.form['aNum']
    aPw = request.form['mPw']
    dAmount = request.form['dAmount']
    wAmount = request.form['wAmount']
    bal = request.form['bal']
    regdate = request.form['regdate']
   
    accounts = load_accounts()

    aNum = uuid.uuid4()


    userAccounts = accounts[mId]
    
    bal = dAmount - wAmount
    
    userAccounts[aNum] = {
        "aNum" : aNum,
        "aPw" : aPw,
        "dAmount" : dAmount,
        "wAmount" : wAmount,
        "bal" : bal,
        "regdate" : regdate
    }

    save_accounts(accounts)

    return render_template('newaccount_result.html',
                           result='OK')

#deposit_form
@bank_bp.route('/deposit_form', methods=['POST'])
def deposit_form():
    return render_template('deposit_form.html')

#deposit_confirm
@bank_bp.route('/deposit_confirm', methods = ['POST'])
def deposit_confirm():

    aNum = request.form['aNum']
    dAmount = int(request.form['dAmount'])

    mId  = session['signinedMemberId']

    if mId == '':
        return render_template('deposit_result.html', 
                               result='NG')
    # if aNum not in accounts:
    #     return render_template('deposit_result.html', 
    #                            result='NG')

    accounts = load_accounts()

    userAccounts = accounts.get(mId, {})

    if aNum in userAccounts:
    
        currentBal = int(userAccounts[aNum])
        userAccounts[aNum]['dAmount'] = dAmount
        int(userAccounts[aNum]['bal']) = currentBal + dAmount

    save_accounts(accounts)

    return render_template('deposit_result.html', result='OK')
    
return redirect('/bank/deposit_form?result=fail')

#withdrawal_form
@bank_bp.route('/withdrawal_form', methods=['POST'])
def withdrawal_form():
    return render_template('withdrawal_form.html')

#/bank/withdrawal_confirm
@bank_bp.route('/withdrawal_confirm', methods=['POST'])
def withdrawal_confirm():

    aNum = request.form['aNum']
    wAmount = request.form['wAmount']

    mId  = session['signinedMemberId']

    if mId == '':
        return render_template('withdrawal_result.html', 
                               result='NG')
    if aNum not in accounts:
        return render_template('withdrawal_result.html', 
                               result='NG')
    
    accounts = load_accounts()
 
    if aNum in accounts and accounts[aNum]['wAmount'] == wAmount:
        
        return render_template('withdrawal_result.html')
    
    return redirect('/bank/withdrawal_form?result=fail')

# /bank/accModify_form
@bank_bp.route('/accModify_form')
def accModify_form():
    accounts = load_accounts()
    account =  accounts[session.get('signinedMemberId')] 

    return render_template(
        'accModify_form.html',
        account = account
    )

#/bank/accModify_confirm
@bank_bp.route('/accModify_confirm', methods=['POST'])
def accModify_confirm():

    mId  = session['signinedMemberId']
   
    if mId == '':
        return render_template('newaccount_result.html', 
                               result='NG')
    
    mId = request.form['mId']
    aNum = request.form['aNum']
    aPw = request.form['mPw']
    dAmount = request.form['dAmount']
    wAmount = request.form['wAmount']
    bal = request.form['bal']
    
    accounts = load_accounts()

    bal = dAmount - wAmount

    account = accounts[mId]
    account['aNum'] = aNum
    account['aPw'] = aPw
    account['dAmount'] = dAmount
    account['wAmount'] = wAmount
    account['bal'] = bal

    save_accounts(accounts)

    return render_template('accModify_result.html')

# /bank/delete_confirm
@bank_bp.route('/delete_confirm', methods=['POST'])
def delete_confirm():
    
    accounts = load_accounts()
    session.get('signinedMemberId')
    del accounts['signinedMemberId']

    save_accounts(accounts)

    return render_template('accDelete_result.html')

# /bank/accList_confirm
@bank_bp.route('/accList_confirm', methods=['GET'])
def accList_confirm():
    
   mId  = session['signinedMemberId']

   if mId == '':
        return render_template('newaccount_result.html', 
                               result='NG')

   accounts = load_accounts()

   account = accounts[mId]

   for accNo, value in account:
       return render_template(accNo,value)
   
#    @bank_bp.route('/accList_confirm', methods=['GET'])
# def accList_confirm():
#     mId = session.get('signinedMemberId')
#     if not mId:
#         return render_template('newaccount_result.html', result='NG')

#     accounts = load_accounts()
#     user_accounts = accounts.get(mId, {})  
#     return render_template('account_list.html', accounts=user_accounts)
       

       
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

{% include 'include/header.html' %}
{% include 'include/nav.html' %}

<article>
    <h2>나의 계좌 목록</h2>
    <ul>
        {% for accNo, info in accounts.items() %}
            <li>
                <strong>계좌번호:</strong> {{ accNo }} | 
                <strong>잔액:</strong> {{ info.bal }}원 | 
                <strong>생성일:</strong> {{ info.regdate }}
            </li>
        {% else %}
            <li>등록된 계좌가 없습니다.</li>
        {% endfor %}
    </ul>
</article>

{% include 'include/footer.html' %}


'''
# '''
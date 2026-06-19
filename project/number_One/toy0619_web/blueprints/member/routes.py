from flask import Blueprint, render_template, request, redirect, session
from utils.json_manager import load_members, save_members

member_bp = Blueprint(
    'member',
    __name__,
    url_prefix='/member'
)

app_bp = Blueprint(
    'app',
    __name__,
    url_prefix='/app'
)

@member_bp.route('/signup_form', methods=['GET'])
def signup_form():
    return render_template('member_forms/signup_form.html')


@member_bp.route('/signup_confirm', methods=['POST'])
def signup_confirm():
    m_id = request.form['mId']
    m_pw = request.form['mPw']
    m_mail = request.form['mMail']
    m_phone = request.form['mPhone']

    members = load_members()

    if m_id in members:
        return render_template('member_forms/signup_result.html', result='NG')

    members[m_id] = {
        'mId': m_id,
        'mPw': m_pw,
        'mMail': m_mail,
        'mPhone': m_phone,
    }

    save_members(members)
    return render_template('member_forms/signup_result.html', result='OK')


@member_bp.route('/signin_form', methods=['GET'])
def signin_form():
    result = request.args.get('result')
    return render_template('member_forms/signin_form.html', result=result)


@member_bp.route('/signin_confirm', methods=['POST'])
def signin_confirm():
    m_id = request.form['mId']
    m_pw = request.form['mPw']

    members = load_members()

    if m_id in members and members[m_id]['mPw'] == m_pw:
        session['signedId'] = m_id
        return render_template('member_forms/signin_result.html')

    return redirect('/member/signin_form?result=fail')

@member_bp.route('/signout_confirm', methods=['GET'])
def signout_confirm():
    session.pop('signedId', None)
    return redirect('/')

@member_bp.route('/modify_form', methods=['GET'])
def modify_form():
    signed_id = session.get('signedId')

    if not signed_id:
        return redirect('/member/signin_form')

    members = load_members()
    member = members.get(signed_id)

    if not member:
        session.pop('signedId', None)
        return redirect('/member/signin_form')

    return render_template('member_forms/modify_form.html', member=member)


@member_bp.route('/modify_confirm', methods=['POST'])
def modify_confirm():
    signed_id = session.get('signedId')

    if not signed_id:
        return redirect('/member/signin_form')

    members = load_members()
    member = members.get(signed_id)

    if not member:
        session.pop('signedId', None)
        return redirect('/member/signin_form')

    member['mPw'] = request.form['mPw']
    member['mMail'] = request.form['mMail']
    member['mPhone'] = request.form['mPhone']

    save_members(members)
    return render_template('member_forms/modify_result.html')


@member_bp.route('/delete_confirm', methods=['GET'])
def delete_confirm():
    signed_id = session.get('signedId')

    if signed_id:
        members = load_members()
        members.pop(signed_id, None)
        save_members(members)
        session.pop('signedId', None)

    return redirect('/')

@app_bp.route('/bank', methods=['GET'])
def bank():
    return render_template('apps/bank.html')

@app_bp.route('/diary', methods=['GET'])
def diary():
    return render_template('apps/diary.html')

@app_bp.route('/memo', methods=['GET'])
def memo():
    return render_template('apps/memo.html')

@app_bp.route('/todolist', methods=['GET'])
def todolist():
    return render_template('apps/todolist.html')


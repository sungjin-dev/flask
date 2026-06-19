function newAccountForm() {
    console.log('newAccountForm():', newAccountForm())

    let form = document.newAccount_form;

    let aPw = form.aPw.value.trim();
  
    console.log('aPw:', aPw)

    mId = session.get('signinedMemberId')
    
    if (aPw === '') {
        alert('Please input Account PW!!')
        form.aPw.focus();
    } else {
        form.submit();
    }
}

function signinForm() {
    console.log('signinForm')

    let form = document.signin_form;

    let mId = form.mId.value.trim();
    let mPw = form.mPw.value.trim();

    console.log('mId:', mId)
    console.log('mPd:', mPw)

    if (mId === '') {
        alert('Please input member ID!!')
        form.mId.focus();
    } else if (mPw === '') {
        alert('Please input member ID!!')
        form.mPw.focus();
    } else {
        form.submit();
    }
}


function modifyForm() {
    console.log('modifyForm()')

    let form = document.modify_form;

    let mPw = form.mPw.value.trim();
    let mMail = form.mMail.value.trim();
    let mPhone = form.mPhone.value.trim();

    console.log('mPw:', mPw)
    console.log('mMail:', mMail)
    console.log('mPhone:', mPhone)

    if  (mPw === '') {
        alert('Please input member PW!!')
        form.mPw.focus();
    } else if (mMail === '') {
        alert('Please input member MAIN!!')
        form.mMail.focus();
    } else if (mPhone === '') {
        alert('Please input member PHONE!!')
        form.mPhone.focus();
    } else {
        form.submit();
    }
}

// regdate mogdate도 추가하기
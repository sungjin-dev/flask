function signupForm() {
    console.log('signupForm')

    let form = document.signup_form;

    let mId = form.mId.value.trim();
    let mPw = form.mPw.value.trim();
    let mMail = form.mMail.value.trim();
    let mPhone = form.mPhone.value.trim();

    console.log('mId:', mId)
    console.log('mPd:', mPw)
    console.log('mMail:', mMail)
    console.log('mPhone:', mPhone)

    if (mId === '') {
        alert('Please input member ID!!')
        form.mId.focus();
    } else if (mPw === '') {
        alert('Please input member ID!!')
        form.mPw.focus();
    } else if (mMail === '') {
        alert('Please input member ID!!')
        form.mMail.focus();
    } else if (mPhone === '') {
        alert('Please input member ID!!')
        form.mPhone.focus();
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
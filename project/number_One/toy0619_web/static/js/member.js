function signupForm() {
    const form = document.signup_form;

    if (form.mId.value.trim() === '') {
        alert('Please input member ID!!');
        form.mId.focus();
    } else if (form.mPw.value.trim() === '') {
        alert('Please input member PW!!');
        form.mPw.focus();
    } else if (form.mMail.value.trim() === '') {
        alert('Please input member MAIL!!');
        form.mMail.focus();
    } else if (form.mPhone.value.trim() === '') {
        alert('Please input member PHONE!!');
        form.mPhone.focus();
    } else {
        form.submit();
    }
}

function signinForm() {
    const form = document.signin_form;

    if (form.mId.value.trim() === '') {
        alert('Please input member ID!!');
        form.mId.focus();
    } else if (form.mPw.value.trim() === '') {
        alert('Please input member PW!!');
        form.mPw.focus();
    } else {
        form.submit();
    }
}

function modifyForm() {
    const form = document.modify_form;

    if (form.mPw.value.trim() === '') {
        alert('Please input member PW!!');
        form.mPw.focus();
    } else if (form.mMail.value.trim() === '') {
        alert('Please input member MAIL!!');
        form.mMail.focus();
    } else if (form.mPhone.value.trim() === '') {
        alert('Please input member PHONE!!');
        form.mPhone.focus();
    } else {
        form.submit();
    }
}
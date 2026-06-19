const SIGN_OUT_STATUS = 1;
const SIGN_IN_STATUS = 2;

function setMenuByStatus(menuStatusNo) {
    console.log('setMenuByStatus() CALLED!!');

    //menuStatusNo < -- 이 녀셕에 따라 

    switch(menuStatusNo) {

        case SIGN_OUT_STATUS:  // 로그아웃 상태
            
            document.querySelector('div.menu_wrap a.sign-up').style.display = 'inline-block';
            document.querySelector('div.menu_wrap a.sign-in').style.display = 'inline-block';
            document.querySelector('div.menu_wrap a.sign-out').style.display = 'none';
            document.querySelector('div.menu_wrap a.delete').style.display = 'none';
            break;

        case SIGN_IN_STATUS:
            document.querySelector('div.menu_wrap a.sign-up').style.display = 'none';
            document.querySelector('div.menu_wrap a.sign-in').style.display = 'none';
            document.querySelector('div.menu_wrap a.sign-out').style.display = 'inline-block';
            document.querySelector('div.menu_wrap a.delete').style.display = 'inline-block';
            break;
    }
}

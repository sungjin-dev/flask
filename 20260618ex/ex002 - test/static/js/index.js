
                            //이벤트종류     callback function
// document.addEventListener('DOMContentLoaded', function() {           
// });

document.addEventListener('DOMContentLoaded', () => { 
    console.log('DOCUMENT READY!');    
    
    init();
    
});

function init() {
    console.log('init() CALLED!!')

    //뷰와 관련된 내용
    initViews();
    //이벤트와 관련된 내용
    addEvents();
}

function addEvents() {
    console.log('addEvents() CALLED!!')

    let signUpMenuBtn = document.querySelector('div.menu_wrap a.sign-up');
    signUpMenuBtn.addEventListener('click', function(){
        console.log('signUpMenuBtn CLICKED!!');

        showSelectedView(SIGN_UP_VIEW);
    });

    let signInMenuBtn = document.querySelector('div.menu_wrap a.sign-in');
    signInMenuBtn.addEventListener('click', function(){
        console.log('signInMenuBtn CLICKED!!');

        showSelectedView(SIGN_IN_VIEW);
    });

    let signOutMenuBtn = document.querySelector('div.menu_wrap a.sign-out');
    signOutMenuBtn.addEventListener('click', function(){
        console.log('signOutMenuBtn CLICKED!!');

        signInedMemberId === '';

        // 메뉴 체인지
        setMenuByStatus(SIGN_OUT_STATUS)
        // 뷰 체인지
        showSelectedView(SIGN_OUT_VIEW);
        
    });

    let deleteMenuBtn = document.querySelector('div.menu_wrap a.delete');
    deleteMenuBtn.addEventListener('click', function(){
        console.log('deleteMenuBtn CLICKED!!');

        removeMember();
        alert('CONGRATURATION REMOVE!');

        signInedMemberId == '';

        setMenuByStatus(SIGN_IN_STATUS);

        showSelectedView(HOME_VIEW)
        
    });

    let writeMenuBtn = document.querySelector('div.menu_wrap a.write');
    writeMenuBtn.addEventListener('click', function(){
        console.log('writeMenuBtn CLICKED!!');

       if (signInedMemberId === '') {
            alert('Please SIGN IN!!');
            showSelectedView(SIGN_IN_VIEW);
            return;
       } 
        
       showSelectedView(WRITE_VIEW);
      
    });

    let listMenuBtn = document.querySelector('div.menu_wrap a.list');
    listMenuBtn.addEventListener('click', function(){
        console.log('listMenuBtn CLICKED!!');

        if (signInedMemberId === '') {
            alert('Please SIGN IN!');
            showSelectedView(SIGN_IN_VIEW);
            return;
        }
        listUpDiaries(); 
        showSelectedView(LIST_VIEW);
    });

    let NewAccMenuBtn = document.querySelector('div.menu_wrap a.new-account');
    NewAccMenuBtn.addEventListener('click', function(){
        if (signInedMemberId === '') {
            alert('Please SIGN IN!');
            showSelectedView(SIGN_IN_VIEW);
            return;
        }

        showSelectedView(NEW_ACCOUNT);
    
    });

    let depositMenuBtn = document.querySelector('div.menu_wrap a.deposit');
    depositMenuBtn.addEventListener('click', function(){
        if (signInedMemberId === '') {
            alert('Please SIGN IN!');
            showSelectedView(SIGN_IN_VIEW);
            return;
        }

        showSelectedView(DEPOSIT);

    });

    let withdrawalMenuBtn = document.querySelector('div.menu_wrap a.withdrwal');
    withdrawalMenuBtn.addEventListener('click', function(){
        if (signInedMemberId === '') {
            alert('Please SIGN IN!');
            showSelectedView(SIGN_IN_VIEW);
            return;
        }

        showSelectedView(WITHDRAWAL);
       
    });

    let accListlMenuBtn = document.querySelector('div.menu_wrap a.account-list');
    accListlMenuBtn.addEventListener('click', function(){
        if (signInedMemberId === '') {
            alert('Please SIGN IN!');
            showSelectedView(SIGN_IN_VIEW);
            return;
        }

        accListUpDiaries(); 
        showSelectedView(ACCOUNT_LIST);

    });

                        // 단일 element를 찦어냄 
    let signUpBtn = document.querySelector('div.sign_up_wrap input[type="button"]');
    signUpBtn.addEventListener('click', function(){

        let uIdEle = document.querySelector('div.sign_up_wrap > input[name="u_id"]');
        let uPwEle = document.querySelector('div.sign_up_wrap > input[name="u_pw"]');
        let uMailEle = document.querySelector('div.sign_up_wrap > input[name="u_mail"]');

        addMember(uIdEle.value, uPwEle.value, uMailEle.value);

        removeValue([uIdEle, uPwEle, uMailEle])
        
    });

    let signInBtn = document.querySelector('div.sign_in_wrap input[type="button"]');
    signInBtn.addEventListener('click', function() {

        let uIdEle = document.querySelector('div.sign_in_wrap input[name="u_id"]');
        let uPwEle = document.querySelector('div.sign_in_wrap input[name="u_pw"]');
        
        let isMember = searchMember(uIdEle.value, uPwEle.value);
        /* signInedMemberId = isMember? uIdEle.value : '';  */

        if (isMember) {
            signInedMemberId = uIdEle.value;
            alert('SIGNIN SUCCESS!!')

            showSelectedView(HOME_VIEW)
            setMenuByStatus(SIGN_IN_STATUS)

            showSelectedView()

        } else {
            signInedMemberId = '';
            alert('SIGNIN FAIL!!')
            setMenuByStatus(SIGN_OUT_STATUS)
        }

        removeValue([uIdEle, uPwEle])         
    });

    let newAccBtn = document.querySelector('div.new_account_wrap input[type="button"]');
    newAccBtn.addEventListener('click', function() {

        let uIdEle = signInedMemberId

        const uuid = crypto.randomUUID();

        let uPwEle = document.querySelector('div.new_account_wrap > input[name="acc_pw"]');
        let uAccEle = uuid

        addAccount(uIdEle, uAccEle, uPwEle.value, 0, 0);

        removeValue([uPwEle])

        alert(`NEW ACCOUNT REGISTERED! ACC NUM: ${uAccEle}`);
        showSelectedView(HOME_VIEW) 

      });    
    
    let depositBtn = document.querySelector('div.deposit_wrap input[type="button"]');
    depositBtn.addEventListener('click', function() {

        let accNumEle = document.querySelector('div.deposit_wrap > input[name="dep_accnum"]');
        let dPoEle = document.querySelector('div.deposit_wrap > input[name="dep_amount"]');

        deposit(accNumEle.value, dPoEle.value);

        removeValue([dPoEle])

        alert(`${dPoEle.value}WON DEPOSITED SUCCESS!`);
        showSelectedView(HOME_VIEW)

    });

    let withdrawalBtn = document.querySelector('div.withdrawal_wrap input[type="button"]');
    withdrawalBtn.addEventListener('click', function() {

        let accNumEle = document.querySelector('div.withdrawal_wrap > input[name="wit_accnum"]');
        let witEle = document.querySelector('div.withdrawal_wrap > input[name="wit_amount"]');

        withdrawal(accNumEle.value, witEle.value);

        removeValue([witEle])

        alert(`${witEle.value}WON WITHDRAWALED SUCCESS!`);  
        showSelectedView(HOME_VIEW)  
   
    });

    let writeBtn = document.querySelector('div.write_wrap button');
    writeBtn.addEventListener('click', function(){
        console.log('writeBtn CLICKED!!')

        let txt = document.querySelector('div.write_wrap input').value;
        
        addDiary(getCurrentDate()+txt);

        removeValue([document.querySelector('div.write_wrap input')])    

        showSelectedView(LIST_VIEW);
    });

}
  //elements?
function removeValue(eles) {
    console.log('removeValue() CALLED!!');

    for(let i = 0; i < eles.length; i++) 

        eles[i].value = '';

}

function listUpDiaries() {
    console.log('listUpDiaries() CALLED!')

    listWrap.textContent='';

    let diaryArr = searchDiaries();

    for (let i = 0; i < diaryArr.length; i++) {

        let tpl = document.querySelector('#list_item');
        let clone = document.importNode(tpl.content, true);
        let txt = clone.querySelector('div.txt');
        txt.textContent = diaryArr[i];

        listWrap.prepend(clone);
        // vs append
    }

}

function accListUpDiaries() {
    console.log('accListUpDiaries() CALLED!')

    accListWrap.textContent='';

    let accountObj = searchAccounts();

    let accountKeys = Object.keys(accountObj);
   
    for (let i = 0; i < accountKeys.length; i++) {

        let tpl = document.querySelector('#acc_list_item');
        let clone = document.importNode(tpl.content, true);
        let txt = clone.querySelector('div.txt');
        txt.textContent = accountKeys[i];

        accListWrap.prepend(clone);
        
    }

}

function deposit(accnum, amount) {

    console.log('deposit() CALLED!');
    console.log('계좌번호:', accnum);
    console.log('금액:', amount);
    console.log(' ID:', signInedMemberId);

    let accountObj = bankDB.get(signInedMemberId);

     let account = accountObj[accnum];

    if (account) {

        account.deposit += amount 
        account.balance += amount  
            
        console.log('DEPOSIT COMPLETE!');
        console.log('bankDB', bankDB);
        return;
    }    

    console.log('NO ACCOUNT!');   
}

function withdrawal(accnum, amount) {

    console.log('withdrawal() CALLED!');
    console.log('계좌번호:', accnum);
    console.log('금액:', amount);
    console.log(' ID:', signInedMemberId);
 
    let accountObj = bankDB.get(signInedMemberId);

    let account = accountObj[accnum];

    if (account) {
 
        account.withdrawal -= amount 
        account.balance -= amount  
            
        console.log('WITHDRAWAL COMPLETE!');
        console.log('bankDB', bankDB);
        return;
    }    

    console.log('NO ACCOUNT!');     
}

/* 
listWrap.textContent=''; 
    1. 진열장(listWrap)을 깨끗하게 싹 비웁니다. (어제 팔다 남은 붕어빵 폐기)
 
let diaryArr = searchDiaries();
    2. 창고(DB)에서 오늘 쓸 일기 데이터(팥, 슈크림 등)를 가져옵니다.
for (let i = 0; i < diaryArr.length; i++) {

    let tpl = document.querySelector('#list_item');
    3. 붕어빵 틀(#list_item)을 가져옵니다.

    let clone = document.importNode(tpl.content, true);
    4. [핵심] 틀을 이용해 빈 붕어빵(clone)을 하나 복제해서 찍어냅니다! (importNode)

    let txt = clone.querySelector('div.txt');
    5. 방금 찍어낸 빈 붕어빵의 속(txt)을 갈라봅니다.
    
    txt.textContent = diaryArr[i];
    6. 그 속에 일기 내용(diaryArr[i])을 앙꼬로 꽉 채워 넣습니다.
  
    listWrap.prepend(clone); 
    7. 완성된 붕어빵을 진열장(listWrap)에 올립니다!
} */


   // let u_id = document.getElements('u_id')[0].value;  array 배열 형식으로 뱉여내서 idx로 찍는다

// none null '' 이거 정리해보기 

/* 
"Write less, do more. (적게 적고, 많이 실행하라)"
jQuery 제이쿼리는 이 길고 복잡한 자바스크립트 코드를 극단적으로 짧고 직관적이게 
만들어주는 '마법 지팡이(라이브러리)'입니다. 
document.querySelector라는 길고 긴 단어를 그냥 $
*/


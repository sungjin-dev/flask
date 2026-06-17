const memberDB = new Map();
const diaryDB = new Map();
const bankDB = new Map();

function addMember(id, pw, mail) {

    console.log('addMember() CALLED!!');

    memberDB.set(id, {
            'u_id': id,
            'u_pw': pw,
            'u_mail': mail
        });   
        
    diaryDB.set(id, []);   
    bankDB.set(id, {}) 
}

function addAccount(id, accnum, pw, dep, wit) {

    console.log('addAccount() CALLED!!');

    let accountDB = bankDB.get(id); 
    
    let bal = dep - wit;
        
    accountDB[accnum] = {
            'acc_pw': pw,
            'deposit': dep,
            'withdrawal': wit,
            'balance': bal           
        };
        
    console.log('bankDB:', bankDB);    
}


function searchMember(id, pw) {
    console.log('searchMember() CALLED!!');

    let memObj = memberDB.get(id);   // -> 데이터 타입? Object

    if (memObj !== undefined && memObj.u_pw === pw ) {
        return true;
    } 
    return false;
   
}

function removeMember() {
    console.log('removeMember() CALLED!!')

    memberDB.delete(signInedMemberId); 

    console.log('memberDB:', memberDB)

}


function addDiary(txt) {
    console.log('addDiary() CALLED');
    let diaryArray = diaryDB.get(signInedMemberId);
        diaryArray.push(txt);
    return diaryArray
}

function searchDiaries() {
    console.log('searchDiaries() CALLED')

    let diaryArr = diaryDB.get(signInedMemberId); //array
    return diaryArr;
}

function searchAccounts() {
    console.log('searchDiaries() CALLED')

    let accountArr = bankDB.get(signInedMemberId); //array
    return accountArr;
}



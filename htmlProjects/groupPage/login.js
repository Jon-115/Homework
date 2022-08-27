// let fs = require("fs");


let group = [];


form.addEventListener('submit',function(event){
    event.preventDefault();

    let person = {
        first: "",
        last: "",
        num: "",
        email: "",
        pass: ""
    };
    const firstName = document.getElementById('firstName');
    const lastName = document.getElementById('lastName');
    const phoneNum = document.getElementById('phoneNum');
    const email = document.getElementById('email');
    const passWord = document.getElementById('pass');

    console.log(firstName, lastName, phoneNum, email, passWord);
    


    person.first = firstName.value;
    person.last = lastName.value;
    person.num = phoneNum.value;
    person.email = email.value;
    person.pass = passWord.value;
    console.log(person);

    group.push(person);
    // fs.writeFile('input.txt', group, function(err) {
    //     if (err) {
    //        return console.error(err);
    //     }
    // }
    // )
    
    console.log(group);

    let name = firstName.value +' '+ lastName.value;
        alert(name + " has been added to the group");

    form.reset();
    
}
)
//--------------------------------------------------------------------------------------------------------------------------------------------------------
// let secondB = document.getElementById('logButton');
// if(secondB != null){
// }
//let form = document.getElementById('logform');

logform.addEventListener('submit',function(event){
    event.preventDefault();
    
    userName = document.getElementById('user').value;
    passWord = document.getElementById('pass').value;
    
    if (userName != 'fake@gmail.com') {
        alert('Username not found. ')
    }
    else if (passWord != 'password') {
        alert('Password is incorrect.')
    }
    else {
        alert('You are signed in. ')
    }

    logform.reset();
    
}
)
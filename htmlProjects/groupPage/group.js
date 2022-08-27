let group = [];

regform.addEventListener('submit',function(event){
    console.log(checked)
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
    const passWord = document.getElementById('pass')

    console.log(firstName, lastName, phoneNum, email);

    person.first = firstName.value;
    person.last = lastName.value;
    person.num = phoneNum.value;
    person.email = email.value;
    person.pass = passWord.value;
    console.log(person);

    group.push(person);
    console.log(group);

    let name = firstName.value +' '+ lastName.value;
        alert(name + " has been added to the group");

    regform.reset();
    }
)

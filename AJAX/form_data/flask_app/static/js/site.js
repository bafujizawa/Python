
function getUsers(){
    fetch('http://127.0.0.1:5000/users')
        .then(res =>  res.json())
        .then(data => {
            var users = document.getElementById('users');
            for( let i = 0; i < data.length; i++){
                let row = document.createElement('tr');

                let name = document.createElement('td');
                name.innerHTML = data[i].user_name;
                row.appendChild(name);
                
                let email = document.createElement('td');
                email.innerHTML = data[i].email;
                row.appendChild(email);
                users.appendChild(row);
            }
        })

}

var myForm = document.getElementById('myForm');
    myForm.onsubmit = function(e){
        // "e" is the js event happening when we submit the form.
        // e.preventDefault() is a method that stops the default nature of javascript.
        e.preventDefault();
        // create FormData object from javascript and send it through a fetch post request.
        var form = new FormData(myForm);
        // this how we set up a post request and send the form data.
        fetch("http://127.0.0.1:5000/create/user", { method :'POST', body : form})
            .then( response => response.json() )
            .then( data => console.log(data) )
        // console.log(form)
    userName = document.getElementById('user_name').value
    newEmail = document.getElementById('email').value
    row = document.createElement('tr')
    let name = document.createElement('td');
        name.innerHTML = userName;
        row.appendChild(name)

    let email = document.createElement('td');
        email.innerHTML = newEmail;
        row.appendChild(email);
        users.appendChild(row);
    console.log(userName, email)
    }





getUsers();


window.onload = function() {
  if (window.localStorage.length == 0) {
    //initialize database
    database = {
      "users": [
          {
              "username": "Bob",
              "password": "1234"
          },
          {
              "username": "Alice",
              "password": "12345"
          }
      ]
      //Can add more tables here  ex: "posts": []
    }

    window.localStorage.setItem("database", database);
  }
};

function validate(formObj) {
  // validation code
  var alertString = "";
  //validation for username field
  var user = 0;
  if (formObj.username.value == "") {
    alertString += "You must enter a username\n";
    user += 1;
  }
    
  //validation for password field  
  var pass = 0;
  if (formObj.password.value == "") {
    alertString += "You must enter a password\n";
    pass += 1;
  }
  
  //alert message
  if ((user + pass) > 0) {
    alert(alertString);
    //focuses on the first field missing
    if (user == 1) {
      formObj.username.focus();
    } else {
      formObj.password.focus();
    }
      
    return false;
  } else {
    //success
    return true;
  }
}

//called in createAccount.html
function add(formObj) {
  if (validate(formObj)) {
    database["users"].push({"username": formObj.usename.value, "password": formObj.password.value});
    window.localStorage.setItem("database", database);
    return true;
  } else {
    return false;
  }
}
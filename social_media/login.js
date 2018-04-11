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
<<<<<<< HEAD

var username = ["Bob", "Alice"];
var password = ["1234", "12345"];
//can add more vars here (ex: posts)

//called in createAccount.html
function add(formObj) {
  if (validate(formObj)) {
    //var formData = JSON.stringify($(formObj).serializeArray());
    username.push(formObj.usename.value);
    password.push(formObj.password.value);
    return true;
  } else {
    return false;
  }
}
=======
>>>>>>> b9a7096be0dcb36f90aec4f6937d91550d42b65c

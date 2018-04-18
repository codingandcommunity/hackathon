function getDatabase() {
  return JSON.parse(window.localStorage.getItem("database"));
}

function saveDatabase(database) {
  window.localStorage.setItem("database", JSON.stringify(database));
}

function getCurrentUser() {
  return window.localStorage.getItem("user");
}

function setCurrentUser(username) {
  window.localStorage.setItem("user", username);
}

window.onload = function() {
  var database;
  if (window.localStorage.length === 0) {

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
    };
    saveDatabase(database);
  } else {
    database = getDatabase(); 
  }
  console.log(database);
};

function redirect(url) {
  console.log("Redirecting to " + url);
  window.location.href = url;
}

function validate(formObj) {
  // validation code
  var alertString = "";
  //validation for username field
  var user = 0;
  if (formObj.username.value === "") {
    alertString += "You must enter a username\n";
    user += 1;
  }
    
  //validation for password field  
  var pass = 0;
  if (formObj.password.value === "") {
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
function addUser(formObj) {
  if (validate(formObj)) {
    var database = getDatabase();
    database.users.push({"username": formObj.username.value, "password": formObj.password.value});
    saveDatabase(database);
    return true;
  } else {
    return false;
  }
}

function loginUser(formObj) {
  if (validate(formObj)) {
    // first check if the user exists in the database
    var database = getDatabase();
    console.log(formObj.username.value);
    database.users.forEach(function(user) { 
        if (user.username == formObj.username.value && user.password == formObj.password.value) {
          setCurrentUser(user.username);
          redirect('/index.html');
        }
    });
  } else {
    return false;
  }
  
}

document.addEventListener("DOMContentLoaded", function(){
        

    /////// Prevent closing from click inside dropdown
    document.querySelectorAll('.dropdown-menu').forEach(function(element){
        element.addEventListener('click', function (e) {
          e.stopPropagation();
        });
    })



    // make it as accordion for smaller screens
    if (window.innerWidth < 992) {

        // close all inner dropdowns when parent is closed
        document.querySelectorAll('.navbar .dropdown').forEach(function(everydropdown){
            everydropdown.addEventListener('hidden.bs.dropdown', function () {
                // after dropdown is hidden, then find all submenus
                  this.querySelectorAll('.submenu').forEach(function(everysubmenu){
                      // hide every submenu as well
                      everysubmenu.style.display = 'none';
                  });
            })
        });
        
        document.querySelectorAll('.dropdown-menu a').forEach(function(element){
            element.addEventListener('click', function (e) {
    
                  let nextEl = this.nextElementSibling;
                  if(nextEl && nextEl.classList.contains('submenu')) {	
                      // prevent opening link if link needs to open dropdown
                      e.preventDefault();
                      console.log(nextEl);
                      if(nextEl.style.display == 'block'){
                          nextEl.style.display = 'none';
                      } else {
                          nextEl.style.display = 'block';
                      }

                  }
            });
        })
    }
    // end if innerWidth

}); 
// DOMContentLoaded  end

// Show password of input-type password

const togglePassword = document.querySelector("#togglePassword");
const password = document.querySelector("#password");

togglePassword.addEventListener("click", function () {
   
  // toggle the type attribute
  const type = password.getAttribute("type") === "password" ? "text" : "password";
  password.setAttribute("type", type);
  // toggle the eye icon
  this.classList.toggle('fa-eye');
  this.classList.toggle('fa-eye-slash');
});

const togglePassword1 = document.querySelector("#togglePassword1");
const password1 = document.querySelector("#password1");

togglePassword1.addEventListener("click", function () {
   
  // toggle the type attribute
  const type1 = password1.getAttribute("type") === "password" ? "text" : "password";
  password1.setAttribute("type", type1);
  // toggle the eye icon
  this.classList.toggle('fa-eye');
  this.classList.toggle('fa-eye-slash');
});

function check(){
    var rb1= document.getElementById("student");
    var rb2= document.getElementById("mentor");
    var rb3=document.getElementById("contributor");
    if(rb1.checked){
        document.getElementById("menu-dashboard").setAttribute("href","student-dashboard.html");
        document.getElementById("menu-query").setAttribute("href","student-dashboard.html");
    }
    if(rb2.checked){
        document.getElementById("menu-dashboard").setAttribute("href","mentor-dashboard.html");
        document.getElementById("menu-query").setAttribute("href","mentor-solve-query.html");
    }

    if(rb3.checked){
        document.getElementById("menu-dashboard").setAttribute("href","contributor-dashboard.html");
    }

    var pw1 = document.getElementById("password");
    var pw2 = document.getElementById("password1");
    con
    if(pw1 != pw2)
    {	
        alert("Passwords did not match");
    }

}













/**
 * Created by Madhav on 12-06-2018.
 */


//For getting CSRF token
function getCookie(name) {
          var cookieValue = null;
          if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
          for (var i = 0; i < cookies.length; i++) {
               var cookie = jQuery.trim(cookies[i]);
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) == (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
             }
          }
      }
 return cookieValue;
}


//When submit is clicked
$("#submit").click(function(e) {

//Prevent default submit. Must for Ajax post.Beginner's pit.
 e.preventDefault();

//Prepare csrf token
 var csrftoken = getCookie('csrftoken');


 var username = $('#username').val();
 var password = $('#password').val();


 var action = $('#submit').val();
 $.ajax({
       url : window.location.href, // the endpoint,commonly same url
       type : "POST", // http method
       data : { csrfmiddlewaretoken : csrftoken,
       username : username,
       password : password,
       action : action,

 }, // data sent with the post request

 // handle a successful response
 success : function(json) {
 //On success show the data posted to server as a message
 alert(json['response']);

 if(json['working'] === "yes"){
     window.location = "/accounts/profile";
 }

 },

 // handle a non-successful response
 error : function(xhr,errmsg,err) {
 console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
 }
 });
});

$("#submit_staff").click(function(e) {

//Prevent default submit. Must for Ajax post.Beginner's pit.
 e.preventDefault();

//Prepare csrf token
 var csrftoken = getCookie('csrftoken');


//Collect data from fields
 var username = $('#username1').val();
 var password = $('#password1').val();
 var action = $('#submit_staff').val();

//This is the Ajax post.Observe carefully. It is nothing but details of where_to_post,what_to_post
//Send data
 $.ajax({
       url : window.location.href, // the endpoint,commonly same url
       type : "POST", // http method
       data : { csrfmiddlewaretoken : csrftoken,
       username : username,
       password : password,
       action : action,

 }, // data sent with the post request

 // handle a successful response
 success : function(json) {
 console.log(json); // another sanity check
 //On success show the data posted to server as a message
 alert(json['response']);

 if(json['working'] === "yes"){
     window.location = "/accounts/profile";
 }

 },

 // handle a non-successful response
 error : function(xhr,errmsg,err) {
 console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
 }
 });
});

$(document).ready(function() {
        M.updateTextFields();
});

$(document).ready(function(){
    $("#fliptofaculty").click(function(){
        $("#main1").css("-webkit-animation-name","showfaculty");
        $("#main1").css("transform","translate(-50%,-50%) rotateY(180deg)");

        $("#main2").css("-webkit-animation-name","hidestudent");
        $("#main2").css("transform","translate(-50%,-50%) rotateY(0deg)");

        $("#form1").css("-webkit-animation-name","showfaculty");
        $("#form1").css("transform","translate(-50%,-50%) rotateY(180deg)");

        $("#form2").css("-webkit-animation-name","hidestudent");
        $("#form2").css("transform","translate(-50%,-50%) rotateY(0deg)");
    });


    $("#fliptostudent").click(function(){
        $("#form1").css("-webkit-animation-name","hidefaculty");
        $("#form1").css("transform","translate(-50%,-50%) rotateY(0deg)");

        $("#form2").css("-webkit-animation-name","showstudent");
        $("#form2").css("transform","translate(-50%,-50%) rotateY(180deg)");

        $("#main1").css("-webkit-animation-name","hidefaculty");
        $("#main1").css("transform","translate(-50%,-50%) rotateY(0deg)");

        $("#main2").css("-webkit-animation-name","showstudent");
        $("#main2").css("transform","translate(-50%,-50%) rotateY(180deg)");
    });
});


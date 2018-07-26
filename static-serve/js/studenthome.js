/**
 * Created by Madhav on 19-07-2018.
 */

var ele = document.getElementById('profile-page-wall-posts');
var html_ele = ele.innerHTML;

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
$(document).on('click', '#submit', function(e) {

//Prevent default submit. Must for Ajax post.
 e.preventDefault();

//Prepare csrf token
 var csrftoken = getCookie('csrftoken');


 var QuestionTitle = $('#query').val();
 var CreatedFor = $('#CreatedFor').val();



 $.ajax({
       url : '/query/ask/', // the endpoint,commonly same url
       type : "POST", // http method
       data : {

           csrfmiddlewaretoken : csrftoken,
           QuestionTitle : QuestionTitle,
           CreatedFor : CreatedFor,

 }, // data sent with the post request

 success : function(json) {

    console.log("Hello There");

    if (json['working'] === "no")
    {
        alert(json['response']);
    }
     else{

            ele.style.opacity = 0;
            ele.innerHTML = "<h3 class=\"light-blue-text\">Successfully Submitted</h3> <button id=\"askagain\" onclick='AskAgain()' class=\"btn large waves-effect waves-light\">Have More Queries?</button>";
            ele.style.opacity = 1;

    }




 },

 // handle a non-successful response
 error : function(xhr,errmsg,err) {
 console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
 }
 });
});

function AskAgain() {

    ele.innerHTML = html_ele;

}
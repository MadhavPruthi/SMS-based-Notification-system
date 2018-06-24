 $(document).ready(function() {
    M.updateTextFields();
  });

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.dropdown-trigger');
    var instances = M.Dropdown.init(elems, options);
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








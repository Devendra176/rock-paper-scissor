$(document).ready(function(){
    $("#start_game",).click(function (e) {
    e.preventDefault();
    
    var url =$(this).attr('href_url');
    let username = $('#username').val();
    let csrf=window.CSRF_TOKEN;

    mydata={username:username,csrf:csrf}

    if(username == ''){
           console.log("enter username to start game")
      }else{
        data=mydata;
        $.ajax({
          url: url,
          type: 'POST',
          data:data,
          success : function(response){ 
            if (response.status){
                
                $("#game_inti").hide();
                $("#main_game").css("display","block")
            }
            else
            {
                console.log('response');
            }
              },
            });
        }
      });
    });
/**
 * Created by vZ on 9/13/15.
 */

$('#send_form_submit').on('click', function (){
            ga('send', 'event', 'Contact Us', 'click', 1);
            $.ajax({
                url: '/send_email/',
                type: 'GET',
                dataType: 'json',
                data: $('#send_form').serialize(),
                success: function(data){
                    console.dir(data);
                    if (data['success']){
                        $('#mail').val('');
                        $('#name').val('');
                        $('#message').val('');
                        $('#mail').css("border","1px solid black");
                        $('#name').css("border","1px solid black");
                        $('#message').css("border","1px solid black");
                        $('#finalMessage').text(data['notification']);
                        $("#success").show().fadeOut(5000);
    //                    $("#success").hide();
                        }
                    else {
                        $('#name').css("border","1px solid black");
                        $('#mail').css("border","1px solid black");
                        $('#message').css("border","1px solid black");
                        $('#name').css("border","2px solid "+data['errors']['name']);
                        $('#mail').css("border","2px solid "+data['errors']['mail']);
                        $('#message').css("border","2px solid "+data['errors']['message']);
//                        $('#finalMessage').text(data['notification']);
//                        $("#success").show().fadeOut(5000);
                        }
                }
	        })
	    });



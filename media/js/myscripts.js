/**
 * Created by vZ on 9/13/15.
 */

$('#send_form_submit').on('click', function (){
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
                        $('#success').val('');
                        $('#success').text(data['notification']);
                        $("#success").show().hide(10000);
    //                    $("#success").hide();
                        }
                    else {
                        $('#error_name').text('');
                        $('#error_mail').text('');
                        $('#error_message').text('');
                        $('#error_name').text(data['errors']['name']);
                        $('#error_mail').text(data['errors']['mail']);
                        $('#error_message').text(data['errors']['message']);
                        $('#success').text(data['notification']);
                        $("#success").show().hide(10000);
                        }
                }
	        })
	    });




$(document).ready(function() {

    // var form = $(this).serialize();
    // var url = '/signup/'
    // ajaxFunction(form, url);

    function ajaxFunction( form, url ) {
        var url = url

        $.ajax({
            type: 'POST',
            url: url,
            data: form,

            success: function ( response ) {
                console.log('this is data')
                console.log(response)
            },

            error: function() { // If something was wrong ...
                console.log( 'error' );
            },
        })
    }

    $('#person-select-field').change(function(){
        var person = $(this).val()
        var button = $('#signup-button')
        if (person == 'teacher'){
            button.attr('type', 'button');
        } else {
            button.attr('type', 'submit');
        }
    })

    $('#signup-button').click(function(){
        var person = $( "#person-select-field option:selected" ).text();
        console.log(person)
        if (person == 'Teacher'){
            existingdiv1 = $( '#serfiticator-forms-box' );
            console.log(existingdiv1)
            $('.sertificator').css('display', 'block')
            $(existingdiv1).clone().appendTo('#signup-form')
            $('#signup-form').children('#serfiticator-forms-box' ).css('display', 'none')
        }
    })



    $('.signup-form').submit(function(e) {
        var password = $('#password').val();
        var confirm_password = $('#confirm-password').val();

        if (password != confirm_password) {
            window.location.reload();
            confirm('Value in password field and confirm password are not the same! Try again.')
        }      
        
        if (person == 'Teacher'){
            
        }
    })
});
$(document).ready(function () {
    $('#id_phone').on('change', function () {
        if ($(this).validate()) {
        }
    });
    $('#contact').on('submit', function (e) {
        e.preventDefault();
        var data = $(this).serialize();
        var that = this;
        var alert = $('#alert');
        var success_message = $('.success_message');
        $(alert).removeClass('alert-danger').removeClass('alert-success');
        $.ajax({
            url: $(that).attr('action'),
            method: 'POST',
            dataType: 'JSON',
            data: data,
            success: function (response) {
                $(alert).fadeIn('fast');
                if (response.success) {
                    $(alert).addClass('alert-success');
                    $(alert).html(response.message);
                    $(success_message).removeClass('uk-hidden');
                    $(that).fadeOut();
                } else {
                    $(alert).addClass('alert-danger');
                    $(alert).html(response.message);
                }
                $('#id_name').val('');
                $('#id_email').val('');
                $('#id_phone').val('');
                $('#id_comment').val('');
            },
            error: function () {
                $(alert).fadeIn('fast');
                $(alert).addClass('alert-danger');
                $(alert).html('Произошла неизвестная ошибка...');
                console.log('asdasdasdasd');
                $('#id_name').val('');
                $('#id_email').val('');
                $('#id_phone').val('');
                $('#id_comment').val('');
            }
        });
    })
});
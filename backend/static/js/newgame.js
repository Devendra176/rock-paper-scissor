$(document).ready(function(){
    $('#newgame').click(function (e) {
        e.preventDefault();
        $('#btnRock').prop('disabled',false);
        $('#btnPaper').prop('disabled',false);
        $('#btnScissor').prop('disabled',false);
        $('#msg').text('');
        $('#btnPridict').text('');
        $('#comScore').val(0);
        $('#yourScore').val(0);
        $('#hiddenbtn').val(1);
        $('#comScore').text('com score');
        $('#yourScore').text('your score');
        $('#new_row').css("display","none");
        $('get_score').css("display","none");
    });

    $('#endgame').click(function (e){
        e.preventDefault();
        window.location.reload();
    });

    $('#get_score').on('click', function(){
        let your_score = $('#yourScore').val();
        let com_score = $('#comScore').val();
        let final_url = $('#hiddenbtn').attr('href_url');
        $.ajax({
            url : final_url,
            type: 'POST',
            data:{your_score : your_score, com_score : com_score},
            success : function(response){
                $('#btnRock').prop('disabled',true);
                $('#btnPaper').prop('disabled',true);
                $('#btnScissor').prop('disabled',true);
                $('#msg').text(response['msg']);
                $('#new_row').css("display","block");
            },
        });
    });

});

function get_score_card(value){
    if (value === '3' ){
        $('#get_score').css("display","block");
    }
}
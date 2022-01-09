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
    });
    $('#endgame').click(function (e){
        e.preventDefault();
        window.location.reload();
    });
});
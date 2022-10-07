// $(document).ready(function(){

//     $("button").click(function(){
//         var url = $(this).attr('href_url');
//         let user_value = $(this).val();
//         let your_score = $('#yourScore').val();
//         let com_score = $('#comScore').val();
//         let hidden = $('#hiddenbtn').val();
//         if(user_value ==''){
//             $('#msg').text('Choose Valid Option')
//         }
//         get_score_card(hidden);

//         data = {user_value : user_value,your_score:your_score, com_score:com_score, hidden : hidden}
//         $.ajax({
//             url: url,
//             type: 'POST',
//             data:data,
//             success : function(response){
//               if (response.status){
//                 $('#btnPridict').text(response.predicted_data['com_value']);
//                 $('#msg').text(response.predicted_data['msg']);
//                 if((response.predicted_data['user_score'] == true) && (response.predicted_data['com_score'] == true)){

//                     $('#yourScore').val(parseInt(your_score)+1);
//                     $('#yourScore').text(parseInt(your_score)+1);
//                     $('#comScore').val(parseInt(com_score)+1);
//                     $('#comScore').text(parseInt(com_score)+1);
//                 }
//                 if(response.predicted_data['user_score'] == true){

//                     $('#yourScore').val(parseInt(your_score)+1);
//                     $('#yourScore').text(parseInt(your_score)+1);
//                 }
//                 if(response.predicted_data['com_score'] == true){
//                     $('#comScore').val(parseInt(com_score)+1);
//                     $('#comScore').text(parseInt(com_score)+1);
//                 }
//                 $('#hiddenbtn').val(parseInt(hidden)+1);
//               }

//                 },
//                 error: function(response) {
//                     $('#msg').text(response['errors']);
//                 },
//             });
        
//         });
// });

  
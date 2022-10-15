$(document).ready(function(){
    ClassicTheme.init();

    var images = new Array()
    images[0] = "rock-flip.png";
    images[1] = "paper-flip.png";
    images[2] = "scissors-flip.png";
    var x=0;

    function changeImage()
    {
               let img = "/static/images/theme/classic/"+images[x];
               document.getElementById("game_image_com").src = img;

               x++;
               if (images.length == x) 
               {
                   x = 0;
               }
    }
    setInterval(changeImage, 300);    
});

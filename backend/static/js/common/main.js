var avilable_options = {
    1: 'rock.png',
    2: 'paper.png',
    3: 'scissors.png',
}
var ComOptions = {
    1: 'rock-flip.png',
    2: 'paper-flip.png',
    3: 'scissors-flip.png',
}
var ClassicTheme = {
    elements: {
        theme_card_container: $('#theme_card_container'),
        theme_btn: $('.theme_btn'),

        form_start_game: $('#form_start_game'),
        username: $('#username'),
        start_game: $('#start_game'),
        hiddenBtn: $('#hiddenbtn'),

        theme_container: $('#new_content_game'),
        user_options: $('.game_image'),

        com_options: $('#game_image_com'),
        your_score: $('#your_score_text'),
        com_score: $('#com_score_text'),
        your_option_output: $('#your_option_output'),
        com_option_output: $('#com_option_output'),
        output_image_div: $('.output_image_div'),
        game_options_btn: $('.score_btn'),
        get_score_btn: $('#get_score_btn'),

        csrf: window.CSRF_TOKEN,
    },

    init: function () {
        "use strict";
        this.initListeners();
    },

    postUserInput: function (user_option, href_url) {
        "use strict";
        return $.ajax({url: href_url, type: 'post', data:{'user_value': user_option}});
    },

    getScore: function(data, href_url){
        "use strict";
        return $.ajax({url: href_url, type: 'post', data:data});
    },

    addUser: function(data, href_url){
        "use strict";
        return $.ajax({url: href_url, type: 'post', data:data});
    },

    loadUserInput: function (user_option, href_url) {
        "use strict";
        var self = this;

        self.postUserInput(user_option, href_url)
        .done(function (response) {
            self.renderUserInput(response, user_option);
        })
        .fail(function (response_fail) {
            console.log(response_fail);
        });
    },

    loadAddUser: function(data, href_url){
        "use strict";
        var self = this;

        self.addUser(data, href_url)
        .done(function (response) {
            if (response.status){
                self.renderGameTemplate(response);
            }
        })
        .fail(function (response_fail) {
            console.log(response_fail);
        });
    },

    loadOptions: function(btn_id, href_url){
        "use strict";
        var self = this;

        var your_score = self.elements.your_score.data('value');
        var com_score = self.elements.com_score.data('value');

        if(btn_id === 'get_score'){
            var data = {your_score: your_score, com_score: com_score}
            self.getScore(data, href_url)
            .done(function (response) {
                if (response.result){
                    startConfetti();
                }else if(response.result == null){
                    stopConfetti();
                }else {
                    stopConfetti();
                }
            })
            .fail(function (response_fail) {
                console.log(response_fail);
            });
        }
        if(btn_id === 'new_game'){
            self.newGame();
        }
        if(btn_id === 'end_game'){
            self.endGame();
        }
    },

    showGetScoreBtn: function(hidden_value){
        "use strict";
        var self = this;

        if (parseInt(hidden_value) >= 3){
            self.elements.get_score_btn.removeClass('hidden');
        }
    },

    newGame: function(){
        "use strict";
        var self = this;

        stopConfetti();
        self.elements.your_score.data('value', 0);
        self.elements.com_score.data('value', 0);

        self.elements.your_score.text(0);
        self.elements.com_score.text(0);

        self.elements.hiddenBtn.data('value', 0);

        self.elements.get_score_btn.addClass('hidden');

        self.elements.output_image_div.addClass('hidden');
    },

    endGame: function(){
        "use strict";
        var self = this;
        stopConfetti();
        window.location.reload();
    },

    renderGameTemplate: function(response){
        "use strict";
        var self = this;

        self.elements.form_start_game.addClass('hidden');
        self.elements.theme_card_container.addClass('hidden');
        self.elements.theme_container.html(response.template);
    },

    renderUserInput: function(response, user_option){
        "use strict";
        var self = this;
        var your_score = self.elements.your_score.data('value');
        var com_score = self.elements.com_score.data('value');
        var hidden = self.elements.hiddenBtn.data('value');

        if (response.status){
            self.showGetScoreBtn(hidden);

            let com_data = response.predicted_data['com_data'];
            let com_image = "/static/images/theme/classic/" + ComOptions[com_data];
            let your_img = "/static/images/theme/classic/" + avilable_options[parseInt(user_option)];

            self.elements.com_option_output.attr('src', com_image);
            self.elements.your_option_output.attr('src', your_img);
            self.elements.output_image_div.removeClass('hidden');
              
            if(response.predicted_data['user_score']){
                self.elements.your_score.data('value', your_score+1);
                self.elements.your_score.text(your_score+1);
            }
            if(response.predicted_data['com_score']){
                self.elements.com_score.data('value', com_score+1);
                self.elements.com_score.text(com_score+1);
            }
            self.elements.hiddenBtn.data('value', hidden+1);
        }
    },

    initListeners: function () {
        "use strict";
        var self = this;

        self.elements.user_options.on('click', function(){
            stopConfetti();
            var user_option = $(this).data('id');
            var href_url = $(this).attr('href_url');
            self.loadUserInput(user_option, href_url);
        });

        self.elements.game_options_btn.on('click', function(){
            var btn_id = $(this).data('id');
            var href_url = $(this).attr('href_url');
            self.loadOptions(btn_id, href_url);
        });

        self.elements.start_game.on('click', function(e){
            e.preventDefault();

            let href_url = $(this).attr('href_url');
            let username = self.elements.username.val();
            var theme_value = 'default';
            self.elements.theme_btn.each((i, element)=>{
                if ($(element).hasClass('selected')){
                    theme_value = $(element).data('value');
                }
            });
            
            var data = {username: username, csrf: self.elements.csrf, theme_value: theme_value};
            self.loadAddUser(data, href_url);
        });

        self.elements.theme_btn.on('click', function(){
            self.elements.theme_btn.removeAttr("style");
            self.elements.theme_btn.removeClass("selected");
            $(this).addClass("selected");
            $(this).css({'background-color': '#008CBA', 'border': 'none'});
        });
    }
};

$(document).ready(function () {
    ClassicTheme.init();
});

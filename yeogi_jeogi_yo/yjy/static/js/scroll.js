window.onload = function(){
    get_popular_list();

    jQuery(function($) {
        var ticker = function() {
            timer = setTimeout(function(){
                $('#ticker li:first').animate( {marginTop: '-20px'}, 400, function() {
                    $(this).detach().appendTo('ul#ticker').removeAttr('style');
                });
                ticker();
            }, 2000);         
          };
      // 마우스를 올렸을 때 기능 정지
      var tickerover = function() {
        $('#ticker').mouseover(function(){
          clearTimeout(timer);
        });
        $('#ticker').mouseout(function(){
          ticker();
        });  
      };
      tickerover();
      // 끝
        ticker();
    });
}

function get_popular_list() { 
    $.ajax({
        url: "/get_popular",
        success: function(data) {
            for(let i=0; i<data.popular.length; i++) {
                $("#ticker").append("<li><label class='badge badge-danger'>" + (i+1) + "위</label>&nbsp&nbsp<strong>" + data.popular[i] + "</strong></li>");
            }
        }
    });
}
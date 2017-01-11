$(function(){
    $('button.pull').click(function(){
        var pull_id = $(this).attr("value");
        console.log(pull_id)
        $.ajax({
            url: '/pull/',
            data: JSON.stringify({
                'pull_id': pull_id,
            }) ,
            contentType:'application/json',
            type: 'POST',
            timeout: 10000000,
            success: function(response){
                var results = JSON.parse(response);
                $('#pullResults').append('<h3>引っ張った結果...</h3>')
                for(i=0; i<results.length; i++){
                    var tweet = results[i];
                    var add_row ='<blockquote class="twitter-tweet" data-conversation="none">'
                                + '<a href="http://twitter.com/'
                                + tweet["user"]["screen_name"]
                                + '/status/' 
                                + tweet["id_str"]
                                + '">https://twitter.com/'
                                + tweet["user"]["screen_name"]
                                + '/status/'
                                + tweet["id_str"]
                                + '</a>'
                                +'</blockquote>'
                    $('#pullResults').append(add_row);
                }
                twttr.widgets.load(document.getElementById('pullResults'));
            },
            error: function(error){
                console.log(error);
                $('#hello').text('aaa')
            }
        });
    });
});

$(function(){
    $('button.search').click(function(){
        var keyword = $('#txtKeyword').val();
        $.ajax({
            url: '/search/',
            data: JSON.stringify({
                'keyword': keyword,
            }) ,
            contentType:'application/json',
            type: 'POST',
            timeout: 10000000,
            success: function(response){
                var results = JSON.parse(response);
                    $('#searchResults').append('<h3>'+ keyword +'の検索結果...</h3>')
                for(i=0; i<results.length; i++){
                    var tweet = results[i];
                    var add_row ='<blockquote class="twitter-tweet" data-conversation="none">'
                                + '<a href="http://twitter.com/'
                                + tweet["user"]["screen_name"]
                                + '/status/' 
                                + tweet["id_str"]
                                + '">https://twitter.com/'
                                + tweet["user"]["screen_name"]
                                + '/status/'
                                + tweet["id_str"]
                                + '</a>'
                                +'</blockquote>'
                                + '<form class="form-pull">'
                                + '<button type="pull" class="btn btn-default pull" value='
                                + tweet["id_str"]
                                + '>引っ張る</button></form>';
                    $('#searchResults').append(add_row);
                }
                twttr.widgets.load(document.getElementById('searchResults'));
            },
            error: function(error){
                console.log(error);
                $('#hello').text('aaa')
            }
        });
    });
});

window.twttr = (function (d,s,id) {
  var t, js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return; js=d.createElement(s); js.id=id;
  js.src="https://platform.twitter.com/widgets.js"; fjs.parentNode.insertBefore(js, fjs);
  return window.twttr || (t = { _e: [], ready: function(f){ t._e.push(f) } });
}(document, "script", "twitter-wjs"));
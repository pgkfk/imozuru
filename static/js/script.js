$(window).load()
$(function(){
$("#{{tweet.id}}").click(function(){
    //クリックした要素のidをサーバに渡す
    var json = JSON.stringify($(this).attr("id"));
    $.ajax({
      type:'POST',
      url:'/',
      data:json,
      contentType:'application/json',
      //サーバからの返送データ(json)を受け取る
      success: function(data){
        var tweets = $.parseJSON( data );
        console.log(tweets)
      }
    });
    //a要素のクリックイベントの場合はfalseを返して、リンク遷移を回避する必要がある。
    return false;
  });
});

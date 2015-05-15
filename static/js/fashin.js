$(document).ready(function() {
  var page = 1;
  var limit = 20;
  var end = false;
  var lock = false;

  function loadContent(page, limit) {
      $.ajax({
          url: "/api/fashin",
          type: "get",
          data: {
            page: page,
            limit: limit,
          },
          success: function( data ) {
            lock = false;
            if (data.length == 0) {
                end = true;
            } else {
                for (var x = 0; x < data.length; x++) {
                    blurb = data[x].blurb;
                    if (blurb.split(' ').length > 32) {
                        blurb = blurb.split(' ').splice(0,32).join(" ")
                    }
                    content = "<div class='item col-md-3'> <div class='sub'> <img class='thumbnail' src='";
                    content += "";
                    content += data[x].thumbnail_url;
                    content += "' alt='thumbnail";
                    content += x;
                    content += "' width='200'> <h4>";
                    content += data[x].title;
                    content += "</h4> <p class='blurb'>"
                    content += blurb;
                    content += "<a href='";
                    content += data[x].details_url;
                    content += "'> Read More</a></p>";
                    content += "</div></div>";
                    $($.parseHTML(content)).appendTo("#content");
                }
            }
          },
          error: function(jqXHR, textStatus, errorThrown) {
            alert(errorThrown);
          }

      });
  }
  loadContent(1, 20);

  $(window).on('scroll', function(){
    if( $(window).scrollTop() > $(document).height() - $(window).height() ) {
        if (!end && !lock) {
            lock = true;
            page = page+1;
            loadContent(page, limit);
        }
    }
  }).scroll();
});
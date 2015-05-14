$(document).ready(function() {
  var page = 1;
  var limit = 20;
  var end = 0;

  function loadContent(page, limit) {
      $.ajax({
          url: "/api/fashin",
          type: "get",
          data: {
            page: page,
            limit: limit,
          },
          success: function( data ) {
            if (data.length == 0) {
                end = 1;
            } else {
                for (var x = 0; x < data.length; x++) {
                    blurb = data[x].blurb;
                    if (blurb.split(' ').length > 32) {
                        blurb = blurb.split(' ').splice(0,32).join(" ")
                    }
                    content = "<div class='item'><h3>";
                    content += data[x].title;
                    content += "</h3> <img src='";
                    content += data[x].thumbnail_url;
                    content += "' alt='image";
                    content += x;
                    content += "' width='200'><p class='blurb'>"
                    content += blurb;
                    content += "<a href='";
                    content += data[x].details_url;
                    content += "'> Read More</a></p>";
                    content += "</div>";
                    $($.parseHTML(content)).appendTo("#content");
                   // updateListing(data[x]);
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
        if (end == 0) {
            page = page+1;
            loadContent(page, limit);
        }
    }
  }).scroll();
});
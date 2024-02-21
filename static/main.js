
  $(document).ready(function() {
    renderPosts();  
  
    $(".title-input").on('input', function() {
      let currentInput_title = $(this).text();
      let trimInput_title = currentInput_title.trim();
      let currentLength_title = trimInput_title.length;
      let remaining_title = 100 - currentLength_title;
      $(".counter-title").html(remaining_title +  "/300");
      if (remaining_title < 0){
        $(".counter-title").addClass("red")
      }else{
        $(".counter-title").removeClass("red")
      }
    });
  
    $(".location-input").on('input', function() {
      let currentInput_location = $(this).text();
      let trimInput_location = currentInput_location.trim();
      let currentLength_location = trimInput_location.length;
      let remaining_location = 100 - currentLength_location;
      $(".counter-location").html(remaining_location + "/100");
      $(".counter-location").html(remaining_location);
      if (remaining_location < 0){
        $(".counter-location").addClass("red")
      }else{
        $(".counter-location").removeClass("red")
      }
    });
  
    $(".twitter-input").on('input', function() {
      let currentInput = $(this).text();
      let trimInput = currentInput.trim();
      let currentLength = trimInput.length;
      let remaining = 100 - currentLength;
      $(".counter-text").html(remaining + "/300");
      if (remaining < 0){
        $(".counter-text").addClass("red")
      }else{
        $(".counter-text").removeClass("red")
      }
    });


  });
 
  function renderPosts() {
    $(".container-for-posts").empty();
    for (let i = 0; i < post_data.length; i++) {
      let username = post_data[i]['username'];
      let title = post_data[i]['title'];
      let location = post_data[i]['location'];
      let text = post_data[i]['text'];
      let image = post_data[i]['image'];
      

      let imageElement = "";
      if (image) {
        imageElement = `<img src="../static/profile-image/${image}" alt="">`;
      }

      let post = `
        <div class="post">
          <div class="firstLine row">
            <div class="location col-md-6">at ${location}</div>
            <div class="username col-md-6">Posted by ${username}</div>
          </div>
          <div class="secondLine row">
            <div class="col-md-12 title">${title}</div>
          </div>
          <div class="thirdLine row">
            <div class="col-md-12 description">${text}</div>
          </div>
          <div class="fourthLine row">
           ${imageElement}
          </div>
        </div>`;
      $(".container-for-posts").append(post);
    }
  }

  function submit_post() {
    const location = $(".location-input").text();
    const title = $(".title-input").text();
    const text = $(".twitter-input").text();
    const imageInput = document.getElementById('image-upload');
    const imageFile = imageInput.files[0];
  
    if (location && title && text) {
      const formData = new FormData();
      formData.append('location', location);
      formData.append('title', title);
      formData.append('text', text);
      formData.append('image', imageFile);
  
      $.ajax({
        url: "/save_post",
        type: "POST",
        data: formData,
        contentType: false,
        processData: false,
        cache: false,
        success: function (response) {
          post_data = response.post_data;
          renderPosts();
        },
        error: function (error) {
          console.log("Error saving post:", error);
        }
      });
    }
  }
  

  
  function save_post(new_post) {
    $.ajax({
        url: "/save_post",
        type: "POST",
        contentType: "application/json;charset=UTF-8",
        data: JSON.stringify(new_post),
        success: function (response) {
            // Update UI based on server response
            post_data = response.post_data;
            renderPosts();
        },
        error: function (error) {
            console.log("Error saving sale:", error);
        }
    });
  }



 









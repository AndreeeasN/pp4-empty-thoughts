// Script to enable updating likes without refreshing page
// Requires {% csrf_token %} and .like-button in template
$(document).ready(function() {
    let csrfToken = $("input[name='csrfmiddlewaretoken']").val()

    $('.like-button').on('click', function(event) {
        // Prevents default link
        event.preventDefault();
        
        // Gets specific thought through attribute data-thought-id
        let thoughtId = $(this).data('thought-id');
    
        // Ajax call, updates like appearance on success
        $.ajax({
            type: 'POST',
            url: `/like/${thoughtId}`,
            data: {
            csrfmiddlewaretoken: csrfToken,
            },
            dataType: 'json',
            success: function(data) {
                if (data.liked) {
                    $(`.like-button[data-thought-id="${thoughtId}"]`).html(
                        `<i class="fa-solid fa-heart"></i> ${data.likes_count} `
                        );       
                    } 
                else {
                    $(`.like-button[data-thought-id="${thoughtId}"]`).html(
                        `<i class="fa-regular fa-heart"></i> ${data.likes_count} `
                        );
                    }
                },
            error: function(xhr, textStatus, errorThrown) {
            console.log(xhr.responseJSON.error);
            },
        });
        });
    }
);
// Script to enable updating likes without refreshing page
// Requires {% csrf_token %} and .like-comment-button in template
$(document).ready(function() {
    let csrfToken = $("input[name='csrfmiddlewaretoken']").val()

    $('.like-comment-button').on('click', function(event) {
        // Prevents default link
        event.preventDefault();
        
        // Gets specific comment through attribute data-comment-id
        let commentId = $(this).data('comment-id');

        // Ajax call, updates like appearance on success
        $.ajax({
            type: 'POST',
            url: `/like_comment/${commentId}`,
            data: {
            csrfmiddlewaretoken: csrfToken,
            },
            dataType: 'json',
            success: function(data) {
                if (data.liked) {
                    $(`.like-comment-button[data-comment-id="${commentId}"]`).html(
                        `<i class="fa-solid fa-heart"></i> ${data.likes_count} `
                        );       
                    } 
                else {
                    $(`.like-comment-button[data-comment-id="${commentId}"]`).html(
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
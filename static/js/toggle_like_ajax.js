// Script to enable updating likes without refreshing page
// Requires {% csrf_token %} and .like-button with data-obj-type and data-obj-id
// Supports likes for both thoughts and comments
$(document).ready(function () {
    let csrfToken = $("input[name='csrfmiddlewaretoken']").val();

    $('.like-button').on('click', function (event) {
        // Prevents default link
        event.preventDefault();

        // Gets specific object through attribute data-obj-id
        let objType = $(this).data('obj-type');
        let objId = $(this).data('obj-id');

        // Ajax call, updates like button appearance on success
        $.ajax({
            type: 'POST',
            url: `/like/${objType}/${objId}`,
            data: {
                csrfmiddlewaretoken: csrfToken,
            },
            dataType: 'json',
            success: function (data) {
                let likeButton = $(`.like-button[data-obj-id="${objId}"][data-obj-type="${objType}"]`);
                if (data.liked) {
                    likeButton.html(`<i class="fa-solid fa-heart"></i> ${data.likes_count} `);
                }
                else {
                    likeButton.html(`<i class="fa-regular fa-heart"></i> ${data.likes_count} `);
                }
            },
            error: function (xhr, textStatus, errorThrown) {
                // Redirects to login page if not authorized
                if (xhr.status === 401) {
                    window.location.href = '/accounts/login/';
                }

                console.log(xhr.responseJSON.error);
            },
        });
    });
}
);
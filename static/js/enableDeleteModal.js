// Script to enable bootstrap confirmation modal on class .btn-delete
// Can be used for both thoughts and comments
$(document).ready(function() {
  // Get modal elements and buttons through jquery
  var deleteModalTitle = document.querySelector('#delete-modal-title');
  var btnDelete = document.querySelector('#delete-modal-button');
  var deleteButtons = document.querySelectorAll('.btn-delete');

  // Used to get partial url from button bs-data-delete-type
  var deleteTypeToUrl ={
    "thought": "delete",
    "comment": "delete_comment",
  }

  // Add EventListener to every .btn-delete
  deleteButtons.forEach(function(button) {
      // On click change modal title/button href to match specified thought
      button.addEventListener('click', function(event) {
          // Prevents default link
          event.preventDefault();
          
          // If button has no delete type, use fallback href of button
          var deleteType = button.getAttribute('data-bs-delete-type')
          var deleteUrl = deleteTypeToUrl[deleteType]
          if (!deleteUrl) {
            window.location.href = button.getAttribute('href');
            return;
          }
          
          var deleteID = button.getAttribute('data-bs-delete-id');
          var deleteTitle = button.getAttribute('data-bs-delete-title');

          deleteModalTitle.innerHTML = `Delete ${deleteTitle}?`;
          btnDelete.setAttribute('href', `/${deleteUrl}/${deleteID}`);

          // Displays the modal
          var deleteModal = new bootstrap.Modal(document.querySelector('#delete-modal'));
          deleteModal.show();
      });
  });
});
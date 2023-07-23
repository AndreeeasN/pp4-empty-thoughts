// Script to enable bootstrap confirmation modal on class .btn-delete
// .btn-delete requires attributes data-delete-type, data-delete-id and data-delete-title
$(document).ready(function() {
  // Get modal elements and buttons through jquery
  const deleteModalTitle = document.querySelector('#delete-modal-title');
  const btnDelete = document.querySelector('#delete-modal-button');
  let deleteButtons = document.querySelectorAll('.btn-delete');

  // Used to get partial url based on data-delete-type
  let deleteTypeToUrl ={
    "thought": "delete",
    "comment": "delete_comment",
  }

  // Add EventListener to every .btn-delete
  deleteButtons.forEach(function(button) {
      // On click change modal title/button href to match specified thought
      button.addEventListener('click', function(event) {
          // Prevents default link
          event.preventDefault();
          
          // If button has no delete type, follow fallback href of button
          let deleteType = button.getAttribute('data-delete-type')
          let deleteUrl = deleteTypeToUrl[deleteType]
          if (!deleteUrl) {
            window.location.href = button.getAttribute('href');
            return;
          }
          
          let deleteID = button.getAttribute('data-delete-id');
          let deleteTitle = button.getAttribute('data-delete-title');

          deleteModalTitle.textContent = `Delete ${deleteTitle}?`;
          btnDelete.setAttribute('href', `/${deleteUrl}/${deleteID}`);

          // Displays the modal
          let deleteModal = new bootstrap.Modal(document.querySelector('#delete-modal'));
          deleteModal.show();
      });
  });
});
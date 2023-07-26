// Script to enable bootstrap confirmation modal on deleting thought/comment
// .btn-delete requires attributes data-delete-type, data-delete-id and data-delete-title
$(document).ready(function () {
  // Get modal elements and buttons through jquery
  const deleteModalTitle = document.querySelector('#delete-modal-title');
  const btnDelete = document.querySelector('#delete-modal-button');
  let deleteButtons = document.querySelectorAll('.btn-delete');

  // Add EventListener to every .btn-delete
  deleteButtons.forEach(function (button) {
    // On click change modal title/button href to match specified thought
    button.addEventListener('click', function (event) {
      // Prevents default link
      event.preventDefault();

      let deleteType = button.getAttribute('data-delete-type');
      let deleteID = button.getAttribute('data-delete-id');
      let deleteTitle = button.getAttribute('data-delete-title');

      deleteModalTitle.textContent = `Delete ${deleteTitle}?`;
      btnDelete.textContent = `Delete ${deleteType}`;
      btnDelete.setAttribute('href', `/delete/${deleteType}/${deleteID}`);

      // Displays the modal
      let deleteModal = new bootstrap.Modal(document.querySelector('#delete-modal'));
      deleteModal.show();
    });
  });
});
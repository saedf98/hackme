document.querySelector('.start-over-btn').addEventListener('click', function() {
  // alert("I got here");
  const form = document.getElementById("start-over-form");

  Swal.fire({
    title: "Are you sure?",
    text: "You won't be able to revert this!",
    icon: "warning",
    showDenyButton: false,
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    confirmButtonText: "Yes, Start over!"
  }).then((result) => {
    /* Read more about isConfirmed, isDenied below */
    if (result.isConfirmed) {
      if (form) {
        form.submit();
      }
    }
  });

});

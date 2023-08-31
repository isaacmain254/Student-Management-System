// const alertMessage = document.getElementById("alert");
// alertMessage.addEventListener("data-bs-dismiss", () => {});

$(document).ready(function () {
  // show the alert
  setTimeout(function () {
    $("#alert").alert("close");
  }, 3000);
});

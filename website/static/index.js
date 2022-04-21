
function deleteAccount(accountId) {
  fetch("/delete-account", {
    method: "POST",
    body: JSON.stringify({ accountId: accountId }),
  }).then((_res) => {
    window.location.href = "/user_profile";
  });
}

window.setTimeout(function() {
  $(".alert").fadeOut('slow') 
}, 3000);
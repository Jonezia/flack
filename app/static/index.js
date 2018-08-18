function changedisplayname() {
  var displayname = prompt("Choose a display name: ");
  if (displayname == "" || displayname == null) {
    alert("Your display name cannot be blank");
    changedisplayname();
  } else {
  localStorage.setItem("displayname",displayname);
  document.getElementById("displayname").innerHTML = localStorage.getItem("displayname")
  }
}

document.addEventListener('DOMContentLoaded', () => {
  alert("Welcome back");
  if (localStorage.getItem("displayname") == null ||
  localStorage.getItem("displayname") == "") {
    changedisplayname();
  }
});

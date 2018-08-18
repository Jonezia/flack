function changedisplayname() {
  var displayname = prompt("Choose a display name: ");
  if (displayname == "" || displayname == null) {
    alert("Your display name cannot be blank");
    changedisplayname();
  } else {
  localStorage.setItem("displayname",displayname);
  document.getElementById("displayname").innerHTML = localStorage.getItem("displayname");
  }
}

function togglesidenavuserdowntooltip() {
  var tooltip = document.getElementById("sidenavuserdowntooltip")
  if (tooltip.style.visiblity == "visible")
}

document.addEventListener('DOMContentLoaded', () => {
  if (localStorage.getItem("displayname") == null ||
  localStorage.getItem("displayname") == "") {
    changedisplayname();
  } else {
    document.getElementById("displayname").innerHTML = localStorage.getItem("displayname");
  }
});

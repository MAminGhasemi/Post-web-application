var loadingIndicator = document.getElementById("loading-indicator");

// hide the loading indicator when the page has finished loading
window.addEventListener("load", function() {
  loadingIndicator.style.display = "none";
});
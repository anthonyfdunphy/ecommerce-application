var button = document.getElementById("shop-now-button");

button.attachEvent("onmouseover", function() {
  button.classList.add("change-color");
});

button.attachEvent("onmouseout", function() {
  button.classList.remove("change-color");
});

window.onload = function() {
  const button = document.getElementById("shop-now-button");
  button.addEventListener ( 'mouseover' ,  mouseOver );
  button.addEventListener ( 'mouseout' ,  mouseOut );

  function  mouseOver() { 
    button.style.transition = "1s";
    document.documentElement.style.transition = "2s";
    document.documentElement.style.setProperty("--color", "lightblue");
  }

  function  mouseOut() { 
    button.style.transition = "1s";
    document.documentElement.style.transition = "2s";
    document.documentElement.style.setProperty("--color", "#ff90e8");
  }
};
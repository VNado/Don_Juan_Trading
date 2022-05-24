const hamburger = document.querySelector(".hamburger");
const navLinks = document.querySelector(".nav-links");
const links = document.querySelectorAll(".nav-links li");
var puntor=0;

hamburger.addEventListener("click", () => {
  navLinks.classList.toggle("open");
  puntor++;
  condicional();
});

function condicional(){
  if(puntor==1){
    disableScroll();
    puntor++;
  }
  else if (puntor!=1){
    enableScroll();
    puntor=0;
  }
}

function disableScroll() {
  // Get the current page scroll position
  scrollTop = window.pageYOffset || document.documentElement.scrollTop;
  scrollLeft = window.pageXOffset || document.documentElement.scrollLeft,

      // if any scroll is attempted, set this to the previous value
      window.onscroll = function() {
          window.scrollTo(scrollLeft, scrollTop);
      };
}
function enableScroll() {
  window.onscroll = function() {};
}
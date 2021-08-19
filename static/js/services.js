 // logostyle


 $('.logoStyle').slick({
    dots: false,
    infinite: false,
    speed: 300,
    slidesToShow: 6,
    slidesToScroll: 1,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 3,
          infinite: false,
          dots: false
        }
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      }
      // You can unslick at a given breakpoint now by adding:
      // settings: "unslick"
      // instead of a settings object
    ]
  });

let hamburgerMenu = document.querySelector(".hamburger__menu");
let mobileNavLinks = document.querySelector(".mobile__navLinks"); 
let closeBtn = document.querySelector(".nav__close");
let bodyTag = document.querySelector("body");

hamburgerMenu.addEventListener('click', () => {
    mobileNavLinks.classList.add("active__navLinks");
});

closeBtn.addEventListener("click", () => {
    mobileNavLinks.classList.remove("active__navLinks");
});
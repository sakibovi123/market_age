$('.responsive').slick({
    dots: true,
    autoplay: true,
    autoplaySpeed: 2000,
    speed: 300,
    dots: false,
    slidesToShow: 2,
    slidesToScroll: 2,
    arrows: false,
    responsive: [
      {
        breakpoint: 992,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          infinite: true,
          dots: false,
          autoplay: true,
        }
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1
        }
      }

    ]
  });




  $('.inner-service-card').slick({
    dots: false,
    autoplay: false,
    infinite: false,
    slidesToShow: 4,
    slidesToScroll: 1,

    responsive: [
      {
        breakpoint: 992,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2,
          infinite: false,
          dots: false,

        }
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2,
          dots: false,
        }
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
          dots: false,
        }
      }

    ]
  });



  $('.slidermoron').slick({
    dots: true,
    autoplay: false,
    speed: 300,
    infinite: true,
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: false,

  });

  $('.for-card-inner-img-slider').slick({
    dots: true,
  autoplay: false,
  speed: 300,
  dots: false,
  slidesToShow: 1,
  slidesToScroll: 1,
  arrows: false,
  centerMode: false,
  });



// ========================================================================
                            // For Mobile view (600 px screen)
// ========================================================================


$('.main-top').slick({
  dots: true,
  autoplay: false,
  autoplaySpeed: 2000,
  speed: 300,
  dots: false,
  slidesToShow: 2,
  slidesToScroll: 2,
  arrows: false,
  centerMode: false,
  responsive: [
    {
      breakpoint: 992,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1,
        infinite: true,
        dots: false,
        autoplay: true,
      }
    },
    {
      breakpoint: 600,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1,
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    }

  ]
});


// ========================================================================
                            // For  Nav bar menu
// ========================================================================

let hamburgerMenu = document.querySelector(".hamburger__menu");
let mobileNavLinks = document.querySelector(".mobile__navLinks");
let closeBtn = document.querySelector(".nav__close");
let bodyTag = document.querySelector("body");


let overlay = document.querySelector(".overlay");
hamburgerMenu.addEventListener('click', () => {
    mobileNavLinks.classList.add("active__navLinks");
    overlay.style.display = 'block';
    bodyTag.style.overflow = 'hidden';
});



closeBtn.addEventListener("click", () => {
    mobileNavLinks.classList.remove("active__navLinks");
    overlay.style.display = 'none';
    bodyTag.style.overflow = 'visible';
});




let hamburgerMenu = document.querySelector(".hamburger__menu");
let mobileNavLinks = document.querySelector(".mobile__navLinks"); 
let closeBtn = document.querySelector(".nav__close");
let bodyTag = document.querySelector("body");
let bgFixed = document.querySelector(".bg__fixed");

hamburgerMenu.addEventListener('click', () => {
    mobileNavLinks.classList.add("active__navLinks");
    bgFixed.style.display = "block";
    bodyTag.style.overflow = "hidden";
});

closeBtn.addEventListener("click", () => {
    mobileNavLinks.classList.remove("active__navLinks");
    bgFixed.style.display = "none";
    bodyTag.style.overflow = "visible";
});
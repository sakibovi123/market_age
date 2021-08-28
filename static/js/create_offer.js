


const proLan = document.querySelector('.pro-lan');
const expertise = document.querySelector('.expertise');

// const firstDiv = document.querySelector('.second-div-for-click');
// const lastDiv = document.querySelector('.second-div-for-click-next');
// proLan.style.backgroundColor = '#ffffff';

// expertise.addEventListener('click', function(){
//     firstDiv.style.display = 'none';
//     lastDiv.style.display = 'block';
//     expertise.style.backgroundColor = '#ffffff'
//     proLan.style.backgroundColor = '#E2E0E0';
// })


// proLan.addEventListener('click', function(){
//     firstDiv.style.display = 'block';
//     lastDiv.style.display = 'none';
//     proLan.style.backgroundColor = '#ffffff'
//     expertise.style.backgroundColor = '#E2E0E0';
// })


const getButton = document.getElementById('get');
const multiInput = document.querySelector('multi-input'); 
const values = document.querySelector('#values'); 



// for hovering div
const hoverDiv = document.querySelector('.hover-function');
const hiddingDiv = document.querySelector('.defining-gig');

// gigs title
const gigTitle = document.querySelector('.gig-title');
const discribeGig = document.querySelector('.discribe-gig');

// seo title
const seoTitle = document.querySelector('.seo-title');
const seoTitleHover = document.querySelector('.seo-title-hover');

// category
const category = document.querySelector('.category');
const categoryHover = document.querySelector('.category-hover');


// service type
const serviceType = document.querySelector('.service-type');
const serviceTypeHover = document.querySelector('.service-type-hover');

// search tag
const searchTag = document.querySelector('.search-tag');
const searchTagHover = document.querySelector('.search-tag-hover');

// for - description 
const descriptionHover = document.querySelector('.description-hover-div');
const innerDes = document.querySelector('.inner-des');
const desRightDiv = document.querySelector('.right-div-for-description');

// for image section
const imageFixed = document.querySelector('.showcase-talent');
const galleryImg = document.querySelector('.gallery-img');
const hoverImgDiv = document.querySelector('.inner-img-hover');
// for video section
const videoHover = document.querySelector('.for-video-hover');
const videosection = document.querySelector('.for-video');

const docHover = document.querySelector('.inner-doc-hover');
const docDiv = document.querySelector('.for-doc');





// doc hover
docDiv.addEventListener('mouseenter', function () {
  docHover.style.display = 'block';
  imageFixed.style.display = 'none';
})
docDiv.addEventListener('mouseleave', function () {
  docHover.style.display = 'none';
  imageFixed.style.display = 'block';
})

// video hover
videosection.addEventListener('mouseenter', function () {
  videoHover.style.display = 'block';
  imageFixed.style.display = 'none';
})
videosection.addEventListener('mouseleave', function () {
  videoHover.style.display = 'none';
  imageFixed.style.display = 'block';
})

// image hover
galleryImg.addEventListener('mouseenter', function () {
  hoverImgDiv.style.display = 'block';
  imageFixed.style.display = 'none';
})
galleryImg.addEventListener('mouseleave', function () {
  hoverImgDiv.style.display = 'none';
  imageFixed.style.display = 'block';
})



hoverDiv.addEventListener('mouseenter', function () {
    hiddingDiv.style.display = 'none';
})

hoverDiv.addEventListener('mouseleave', function () {
    hiddingDiv.style.display = 'block';
})

// gigs title
gigTitle.addEventListener('mouseenter', function() {
    discribeGig.style.display = 'block';
})

gigTitle.addEventListener('mouseleave', function() {
    discribeGig.style.display = 'none';
})

// seo title
seoTitle.addEventListener('mouseenter', function () {
  seoTitleHover.style.display = 'block';
})
seoTitle.addEventListener('mouseleave', function () {
  seoTitleHover.style.display = 'none';
})

// category
category.addEventListener('mouseenter', function () {
  categoryHover.style.display = 'block';
})
category.addEventListener('mouseleave', function () {
  categoryHover.style.display = 'none';
})

// service type
searchTag.addEventListener('mouseenter', function () {
  searchTagHover.style.display = 'block';
})
searchTag.addEventListener('mouseleave', function () {
  searchTagHover.style.display = 'none';
})
// search tag
serviceType.addEventListener('mouseenter', function () {
  serviceTypeHover.style.display = 'block';
})
serviceType.addEventListener('mouseleave', function () {
  serviceTypeHover.style.display = 'none';
})
// search tag
innerDes.addEventListener('mouseenter', function () {
  descriptionHover.style.display = 'block';
  desRightDiv.style.display = 'none';
})
innerDes.addEventListener('mouseleave', function () {
  descriptionHover.style.display = 'none';
  desRightDiv.style.display = 'block';
})

function checkResponsive1() {
  let res1 = document.getElementById("res1");

  if (res1.value === "off")
      res1.value = "on"
  else
      res1.value = "off"

  console.log(res1.value);
}

function checkResponsive2() {
  let res2 = document.getElementById("res2");

  if (res2.value === "off")
      res2.value = "on"
  else
      res2.value = "off"

  console.log(res2.value);
}

function checkResponsive3() {
  let res3 = document.getElementById("res3");

  if (res3.value === "off")
      res3.value = "on"
  else
      res3.value = "off"

  console.log(res3.value);
}

let document_element = document.getElementById("document");

document_element.addEventListener("change", () => {
  console.log(CKEDITOR.instances.document_element.getData());
});


$(function() {
  $('.chosen-select').chosen();
  $('.chosen-select-deselect').chosen({ allow_single_deselect: true });
});
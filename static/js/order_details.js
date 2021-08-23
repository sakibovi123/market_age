const select = document.getElementById('select');
const paypal = document.querySelector('.paypal');
const aamarpay = document.querySelector('.ammrpay');
const sslcommerz = document.querySelector('.sslcommerz');
const razorpay = document.querySelector('.razorpay');
const body = document.querySelector('.for-add-class');
const add = document.querySelector('.ordering');

const paypalButton = document.querySelector('#paypal-button-container');


select.addEventListener('click', function(){
    if (select.value === "paypal") {
        paypal.style.display = 'none';   
        aamarpay.style.display = 'none';
        sslcommerz.style.display = 'none';
        razorpay.style.display = 'none';
        paypalButton.style.display = 'block'; 

    } else if (select.value === "AAMMR PAY") {
        aamarpay.style.display = 'block';
        paypal.style.display = 'none';
        sslcommerz.style.display = 'none';
        razorpay.style.display = 'none';
        paypalButton.style.display = 'none'; 
    } else if(select.value === 'sslcommerz'){
        aamarpay.style.display = 'none';
        paypal.style.display = 'none';
        razorpay.style.display = 'none';
        sslcommerz.style.display = 'block';
        paypalButton.style.display = 'none'; 

    } else if(select.value === 'razorpay' ){
        aamarpay.style.display = 'none';
        paypal.style.display = 'none';
        razorpay.style.display = 'block';
        sslcommerz.style.display = 'none';
        paypalButton.style.display = 'none'; 

    }
})
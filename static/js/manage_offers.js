// For buttons
const activeBtn = document.querySelector('.active__btn')
const pendingBtn = document.querySelector('.pending__btn')
const modificationBtn = document.querySelector('.modification__btn')
const deniedBtn = document.querySelector('.denied__btn')
const pausedBtn = document.querySelector('.paused__btn')
let gigsOptions = document.querySelector('.gigs__options')
let gigsOptionLinks = document.querySelector('.gigs__optionLinks')

let gigsText = document.querySelector('.table__gigsText')

// For tables
const activatedTable = document.querySelector('.activated__table')
const pendingTable = document.querySelector('.pending__table')
const requiredTable = document.querySelector('.required__table')
const deniedTable = document.querySelector('.denied__table')
const pausedTable = document.querySelector('.paused__table')

activeBtn.addEventListener('click', () => {
  console.log('hello ')
  // For button text
  activeBtn.classList.add('active__link')
  pendingBtn.classList.remove('active__link')
  modificationBtn.classList.remove('active__link')
  deniedBtn.classList.remove('active__link')
  pausedBtn.classList.remove('active__link')
  gigsText.innerHTML = 'ACTIVE GIGS'

  // For table container
  activatedTable.classList.add('show__activeTable')
  pendingTable.classList.remove('show__activeTable')
  requiredTable.classList.remove('show__activeTable')
  deniedTable.classList.remove('show__activeTable')
  pausedTable.classList.remove('show__activeTable')
})

pendingBtn.addEventListener('click', () => {
  // For button text
  activeBtn.classList.remove('active__link')
  pendingBtn.classList.add('active__link')
  modificationBtn.classList.remove('active__link')
  deniedBtn.classList.remove('active__link')
  pausedBtn.classList.remove('active__link')
  gigsText.innerHTML = 'GIGS PENDING APPROVAL'

  // For table container
  activatedTable.classList.remove('show__activeTable')
  pendingTable.classList.add('show__activeTable')
  requiredTable.classList.remove('show__activeTable')
  deniedTable.classList.remove('show__activeTable')
  pausedTable.classList.remove('show__activeTable')
})

modificationBtn.addEventListener('click', () => {
  // For button text
  activeBtn.classList.remove('active__link')
  pendingBtn.classList.remove('active__link')
  modificationBtn.classList.add('active__link')
  deniedBtn.classList.remove('active__link')
  pausedBtn.classList.remove('active__link')
  gigsText.innerHTML = 'GIGS THAT REQUIRE MODIFICATION'

  // For table container
  activatedTable.classList.remove('show__activeTable')
  pendingTable.classList.remove('show__activeTable')
  requiredTable.classList.add('show__activeTable')
  deniedTable.classList.remove('show__activeTable')
  pausedTable.classList.remove('show__activeTable')
})

deniedBtn.addEventListener('click', () => {
  // For button text
  activeBtn.classList.remove('active__link')
  pendingBtn.classList.remove('active__link')
  modificationBtn.classList.remove('active__link')
  deniedBtn.classList.add('active__link')
  pausedBtn.classList.remove('active__link')
  gigsText.innerHTML = 'DENIED GIGS'

  // For table container
  activatedTable.classList.remove('show__activeTable')
  pendingTable.classList.remove('show__activeTable')
  requiredTable.classList.remove('show__activeTable')
  deniedTable.classList.add('show__activeTable')
  pausedTable.classList.remove('show__activeTable')
})

pausedBtn.addEventListener('click', () => {
  // For button text
  activeBtn.classList.remove('active__link')
  pendingBtn.classList.remove('active__link')
  modificationBtn.classList.remove('active__link')
  deniedBtn.classList.remove('active__link')
  pausedBtn.classList.add('active__link')
  gigsText.innerHTML = 'PAUSED GIGS'

  // For table container
  activatedTable.classList.remove('show__activeTable')
  pendingTable.classList.remove('show__activeTable')
  requiredTable.classList.remove('show__activeTable')
  deniedTable.classList.remove('show__activeTable')
  pausedTable.classList.add('show__activeTable')
})

// Ajax apply
$(document).ready(function () {
  const offer_paused_form = $('.offer-paused-form');
  const offer_btn = document.getElementsByClassName('offer__btn');
  const offer_id_hidden = document.getElementsByClassName('offer_id_hidden');

  for (let i = 0; i < offer_btn.length; i++) {
    offer_btn[i].addEventListener('click', function () {
      offer_id = offer_btn[i].getAttribute('data-content')
      offer_id_hidden[i].value = offer_id;
      console.log(offer_id_hidden.value);
      offer_paused_form.submit(function (event) {
        event.preventDefault()

        const actionEndPoint = offer_paused_form.attr('action')
        const method = offer_paused_form.attr('method')
        const data = offer_paused_form.serialize()


        $.ajax({
          url: actionEndPoint,
          method: method,
          data: data,
          success: function (data) {
            if (data.message) {
              alert(data.message);
              $(".offer" + offer_id.toString()).remove();
            }
          },
          error: function (errorData) {
            alert('Something is wrong!')
          },
        })
      })
    })
  }
})

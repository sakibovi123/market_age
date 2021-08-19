// For buttons
const priorityBtn = document.querySelector(".priority__btn");
const activeBtn = document.querySelector(".active__btn");
const lateBtn = document.querySelector(".late__btn");
const deliveredBtn = document.querySelector(".delivered__btn");
const completedBtn = document.querySelector(".completed__btn");
const cancelledBtn = document.querySelector(".cancelled__btn");
const starredBtn = document.querySelector(".starred__link");

// For tables
const priotityTable = document.querySelector('.priority__table');
const activatedTable = document.querySelector('.activated__table');
const lateTable = document.querySelector('.late__table');
const deliveredTable = document.querySelector('.delivered__table');
const completedTable = document.querySelector('.completed__table');
const cancelledTable = document.querySelector('.cancelled__table');
const starredTable = document.querySelector('.starred__table');


let orderedText = document.querySelector(".table__orderText");


priorityBtn.addEventListener("click", () => {
    // For button text
    priorityBtn.classList.add("active__link");
    activeBtn.classList.remove("active__link");
    lateBtn.classList.remove("active__link");
    deliveredBtn.classList.remove("active__link");
    completedBtn.classList.remove("active__link");
    cancelledBtn.classList.remove("active__link");
    starredBtn.classList.remove("active__link");
    orderedText.innerHTML = "PRORITY ORDERS";

    // For table container
    priotityTable.classList.add("show__activeTable");
    activatedTable.classList.remove("show__activeTable");
    lateTable.classList.remove("show__activeTable");
    deliveredTable.classList.remove("show__activeTable");
    completedTable.classList.remove("show__activeTable");
    cancelledTable.classList.remove("show__activeTable");
    starredTable.classList.remove("show__activeTable");
});

activeBtn.addEventListener("click", () => {
    // For button text
    priorityBtn.classList.remove("active__link");
    activeBtn.classList.add("active__link");
    lateBtn.classList.remove("active__link");
    deliveredBtn.classList.remove("active__link");
    completedBtn.classList.remove("active__link");
    cancelledBtn.classList.remove("active__link");
    starredBtn.classList.remove("active__link");
    orderedText.innerHTML = "ACTIVE ORDERS";

    // For table container
    priotityTable.classList.remove("show__activeTable");
    activatedTable.classList.add("show__activeTable");
    lateTable.classList.remove("show__activeTable");
    deliveredTable.classList.remove("show__activeTable");
    completedTable.classList.remove("show__activeTable");
    cancelledTable.classList.remove("show__activeTable");
    starredTable.classList.remove("show__activeTable");
});

lateBtn.addEventListener("click", () => {
    // For button text
    priorityBtn.classList.remove("active__link");
    activeBtn.classList.remove("active__link");
    lateBtn.classList.add("active__link");
    deliveredBtn.classList.remove("active__link");
    completedBtn.classList.remove("active__link");
    cancelledBtn.classList.remove("active__link");
    starredBtn.classList.remove("active__link");
    orderedText.innerHTML = "LATE ORDERS";

    // For table container
    priotityTable.classList.remove("show__activeTable");
    activatedTable.classList.remove("show__activeTable");
    lateTable.classList.add("show__activeTable");
    deliveredTable.classList.remove("show__activeTable");
    completedTable.classList.remove("show__activeTable");
    cancelledTable.classList.remove("show__activeTable");
    starredTable.classList.remove("show__activeTable");
});

deliveredBtn.addEventListener("click", () => {
    // For button text
    priorityBtn.classList.remove("active__link");
    activeBtn.classList.remove("active__link");
    lateBtn.classList.remove("active__link");
    deliveredBtn.classList.add("active__link");
    completedBtn.classList.remove("active__link");
    cancelledBtn.classList.remove("active__link");
    starredBtn.classList.remove("active__link");
    orderedText.innerHTML = "DELIVERED ORDERS";

    // For table container
    priotityTable.classList.remove("show__activeTable");
    activatedTable.classList.remove("show__activeTable");
    lateTable.classList.remove("show__activeTable");
    deliveredTable.classList.add("show__activeTable");
    completedTable.classList.remove("show__activeTable");
    cancelledTable.classList.remove("show__activeTable");
    starredTable.classList.remove("show__activeTable");
});

completedBtn.addEventListener("click", () => {
    // For button text
    priorityBtn.classList.remove("active__link");
    activeBtn.classList.remove("active__link");
    lateBtn.classList.remove("active__link");
    deliveredBtn.classList.remove("active__link");
    completedBtn.classList.add("active__link");
    cancelledBtn.classList.remove("active__link");
    starredBtn.classList.remove("active__link");
    orderedText.innerHTML = "COMPLETED ORDERS";

    // For table container
    priotityTable.classList.remove("show__activeTable");
    activatedTable.classList.remove("show__activeTable");
    lateTable.classList.remove("show__activeTable");
    deliveredTable.classList.remove("show__activeTable");
    completedTable.classList.add("show__activeTable");
    cancelledTable.classList.remove("show__activeTable");
    starredTable.classList.remove("show__activeTable");
});

cancelledBtn.addEventListener("click", () => {
    // For button text
    priorityBtn.classList.remove("active__link");
    activeBtn.classList.remove("active__link");
    lateBtn.classList.remove("active__link");
    deliveredBtn.classList.remove("active__link");
    completedBtn.classList.remove("active__link");
    cancelledBtn.classList.add("active__link");
    starredBtn.classList.remove("active__link");
    orderedText.innerHTML = "CANCELLED ORDERS";

    // For table container
    priotityTable.classList.remove("show__activeTable");
    activatedTable.classList.remove("show__activeTable");
    lateTable.classList.remove("show__activeTable");
    deliveredTable.classList.remove("show__activeTable");
    completedTable.classList.remove("show__activeTable");
    cancelledTable.classList.add("show__activeTable");
    starredTable.classList.remove("show__activeTable");
});

starredBtn.addEventListener("click", () => {
    // For button text
    priorityBtn.classList.remove("active__link");
    activeBtn.classList.remove("active__link");
    lateBtn.classList.remove("active__link");
    deliveredBtn.classList.remove("active__link");
    completedBtn.classList.remove("active__link");
    cancelledBtn.classList.remove("active__link");
    starredBtn.classList.add("active__link");
    orderedText.innerHTML = "STARRED ORDERS";

    // For table container
    priotityTable.classList.remove("show__activeTable");
    activatedTable.classList.remove("show__activeTable");
    lateTable.classList.remove("show__activeTable");
    deliveredTable.classList.remove("show__activeTable");
    completedTable.classList.remove("show__activeTable");
    cancelledTable.classList.remove("show__activeTable");
    starredTable.classList.add("show__activeTable");
});
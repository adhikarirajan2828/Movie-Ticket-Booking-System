const movieTitle = document.querySelectorAll('.card-title');
const buyTicket = document.querySelector('.buyTicket');

console.log(movieTitle);
movieTitle.forEach((e) => {
    e.addEventListener('click',(event) => {
        console.log(e.innerHTML)
    } )
})

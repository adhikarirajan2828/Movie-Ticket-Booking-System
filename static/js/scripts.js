const seats = document.querySelectorAll(".seat:not(.reserved)");
const movie = document.getElementById("movie");
const bookTicket = document.getElementById("bookTicket");

const ticketPrice = 100;
let movieName;
let seatSelectedNumber = [];
let totalPrice;
let totalSeatCount;
let seatSelected;
let seatNumber;

seats.forEach((e) => {
  e.addEventListener("click", (event) => {
    e.classList.toggle("selected");
    seatNumber = e.getAttribute("data-value");
    seatSelectedNumber.push(Number(seatNumber));
    seatSelected = document.querySelectorAll(".selected");
    totalSeatCount = seatSelected.length;
    totalPrice = ticketPrice * totalSeatCount;
    document.getElementById("count").innerHTML = totalSeatCount;
    document.getElementById("amount").innerHTML = totalPrice;
  });
});

movie.addEventListener("change", (e) => {
  console.log("changed");
  console.log(movie.value);
  movieName = movie.value;
  console.log(movieName);
});

const postSeat = async () => {
  movieName = movie.value;
  const { data } = await axios.post("http://localhost:8000/movies/ticket", {
    movieName,
    totalPrice,
    ticketPrice,
    totalSeatCount,
    seatSelectedNumber,
  });
};

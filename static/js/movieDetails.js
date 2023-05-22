const movieDate = document.getElementById("movieDate");
const bookTicket = document.getElementById("BookTicket");

let date;
// console.log(movieDate);
movieDate.addEventListener("change", () => {
  date = movieDate.value;
  console.log("here is selected date");
  console.log(date);
  let currentDate = new Date().toJSON().slice(0, 10);
  console.log("here is current date");
  console.log(currentDate);
  if (currentDate > date) {
    movieDate.value = "";
    alert("invalid movie date");
  }else{

  }
});

const BookTicketfunc = async () => {
  console.log(movieDate.value)
  if(!movieDate.value){
    alert('please select a date');
  }else {
    console.log(movieDate.value)
    console.log("inside box ticket");
    const { data } = await axios.post(
      "http://localhost:8000/movies/ticket/date",
      {
        date,
      }
    );
    console.log('book')
    bookTicket.href = '/movies/seatview'

  }
};

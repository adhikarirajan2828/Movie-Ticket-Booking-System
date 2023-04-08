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
  }
});

const BookTicketfunc = async () => {
  console.log("inside box ticket");
  console.log(date);
  const { data } = await axios.post(
    "http://localhost:8000/movies/ticket/date",
    {
      date,
    }
  );
  console.log('------------here is data')
  console.log(data)
  if(movieDate.value === ""){
    alert('please select a date');
  }else {
    bookTicket.href = '/seatView'
  }

  console.log(data);
  // fetch("http://127.0.0.1:8000/movies/ticket/date", {
  //   method: "POST",
  //   headers: {
  //     Accept: "application/json",
  //     "Content-Type": "application/json",
  //     "Access-Control-Allow-Origin": "*",
  //   },
  //   body: JSON.stringify({ id: 78912 }),
  // })
  //   .then((response) => response.json())
  //   .then((response) => console.log(JSON.stringify(response)));
};

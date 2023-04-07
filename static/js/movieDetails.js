const movieDate = document.getElementById("movieDate");
const bookTicket = document.getElementById("BookTicket");

let date;
console.log(movieDate);
movieDate.addEventListener("change", () => {
  console.log(movieDate);
  date = movieDate.value;
  let currentDate = new Date().toJSON().slice(0, 10);
  console.log(currentDate);
  if (currentDate > date) {
    alert("invalid movie date");
  }
});

const BookTicketfunc = async () => {
  console.log("inside box ticket");
  console.log(date);
  const { data } =  await axios.post("http://127.0.0.1:8000/movies/ticket/date", {
    date});
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

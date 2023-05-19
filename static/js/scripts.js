window.onload = async () => {
  const { data } = await axios.get(
    "http://localhost:8000/movies/reservedseats"
  );
  ticketPrice = price.getAttribute('data-price');
  bookedSeatNum = data.reserved_seats.split(" ");
  ReservedSeat.forEach((e, index) => {
    let seatReserved = e.getAttribute("data-value");

    if (bookedSeatNum.includes(seatReserved)) {
      e.classList.remove("selected");
      e.classList.add("reserved");
    }
  });

};
const price = document.getElementById("price");
const ReservedSeat = document.querySelectorAll(".seat");
const seats = document.querySelectorAll(".seat:not(.reserved)");
const bookTicket = document.getElementById("bookTicket");
const buyTicket = document.getElementById("buyTicket");

let bookedSeatNum = [1, 2, 3];
let bookedSeat = [];

let ticketPrice;
let movieName;
let seatSelectedNumber = [];
let totalPrice;
let totalSeatCount;
let seatSelected;
let seatNumber;

seats.forEach((e) => {
  e.addEventListener("click", (event) => {
    if (!e.classList.contains("reserved")) {
      e.classList.toggle("selected");
      seatNumber = e.getAttribute("data-value");

      seatSelectedNumber.push(Number(seatNumber));
      seatSelected = document.querySelectorAll(".selected");
      totalSeatCount = seatSelected.length;
      totalPrice = ticketPrice * totalSeatCount;
      document.getElementById("count").innerHTML = totalSeatCount;
      document.getElementById("amount").innerHTML = totalPrice;
    }
  });
});

const postSeat = async () => {
  let config = {
    publicKey: "test_public_key_c918cf965e0e41ccb38bde814a012ad0",
    productIdentity: "1234567890",
    productName: "Dragon",
    productUrl: "http://gameofthrones.wikia.com/wiki/Dragons",
    paymentPreference: [
      "KHALTI",
      "EBANKING",
      "MOBILE_BANKING",
      "CONNECT_IPS",
      "SCT",
    ],
    eventHandler: {
      async onSuccess(payload) {
        const response = await axios.post(
          "http://localhost:8000/movies/ticket",
          {
            totalPrice,
            ticketPrice,
            seatSelectedNumber,
          }
        );
        if (response.status === 200) {
          window.location.href = 'http://localhost:8000/mytickets';
        }
      },
      onError(error) {
        console.log(error);
      },
      onClose() {
        console.log("widget is closing");
      },
    },
  };

  var checkout = new KhaltiCheckout(config);
  console.log("checkout");
  console.log(checkout);
  checkout.show({ amount: totalPrice });



  console.log(response);
};

const loyaltyTicket = async () => {
  const response = await axios.post("http://localhost:8000/movies/buywithpoint", {
    totalPrice,
    ticketPrice,
    seatSelectedNumber,
  });
  console.log(response);

  if (response.status === 200) {
    window.location.href = 'http://localhost:8000/mytickets';
  }
}
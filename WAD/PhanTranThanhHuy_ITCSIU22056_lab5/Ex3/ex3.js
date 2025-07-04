function updateTimeandDate() {
const now = new Date();

const options = { weekday: 'short', month: 'short', day: '2-digit', year: 'numeric' };
const formattedDate = now.toLocaleDateString('en-US', options);

const hours = now.getHours();
const minutes = now.getMinutes();
const seconds = now.getSeconds();
const timeZone = (hours >= 12) ? "PM" : "AM";
const formattedTime = `${hours % 12 || 12}:${minutes.toString().padStart(2, "0")}:${seconds.toString().padStart(2, "0")} ${timeZone}`;

document.querySelector(".time").innerHTML = formattedTime.toString();
document.querySelector(".date").innerHTML = formattedDate.toString();
}

setInterval(() => {
    updateTimeandDate();
},1000);


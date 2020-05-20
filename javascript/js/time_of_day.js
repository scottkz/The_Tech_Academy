function TimeOfDay() {
    var time = new Date().getHours();
    var reply;
    if (time < 12 == time > 0) {
        reply = "It's morning time!"
    } else if (time > 12 == time < 18) {
        reply = "It's afternoon time!";
    } else {
        reply = "It's evening time!"
    }
    document.getElementById("time").innerHTML = reply;
}
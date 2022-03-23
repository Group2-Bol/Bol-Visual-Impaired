const express = require("express");
var path = require("path");
const app = express();

//#region server settings
app.get("/index.html", function(req, res) {
    res.sendFile(__dirname + "/index.html");
});

app.get("/js/sketch.js", function(req, res) {
    res.sendFile(__dirname + "/js/sketch.js");
});

app.get("/images/bird2.jpeg", function(req, res) {
    res.sendFile(__dirname + "/images/bird2.jpeg");
})

app.get("/", function(req, res) {
    res.sendFile(__dirname + "/index.html");
})

app.listen(4200, function() {
    console.log("Server is running on url: localhost:4200");
});
//#endregion
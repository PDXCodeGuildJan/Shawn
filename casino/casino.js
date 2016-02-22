// Loop number of times 
var  num = 6;

var inputField = document.getElementById("num-loops");
var counter = document.getElementById("counter");
var faces = ["[ . ]","[ : ]","[: .]","[: :]","[:.:]","[:::]"]


//add click listener

function loopClick() { 
	num = inputField.value;
	counter.innerHTML = ""

	for (var i = 0; i < num; i++) {

	counter.innerHTML += faces[rollDie()-1] + " "
	};

};

document.getElementById("loop-btn").onclick = loopClick;

function rollDie () {
	var randDec = Math.random();
	return Math.ceil(randDec * 6);

}



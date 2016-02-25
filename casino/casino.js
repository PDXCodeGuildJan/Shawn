// Loop number of times 
var  num = 6;

var inputField = document.getElementById("num-loops");
var counter = document.getElementById("counter");
var faces = ["<img src=\"./dice/1.png\" alt=\"1\" />",
			"<img src=\"./dice/2.png\" alt=\"2\" />",
			"<img src=\"./dice/3.png\" alt=\"3\" />",
			"<img src=\"./dice/4.png\" alt=\"4\" />",
			"<img src=\"./dice/5.png\" alt=\"5\" />",
			"<img src=\"./dice/6.png\" alt=\"6\" />"]


//add click listener

function loopClick() { 
	num = inputField.value;
	counter.innerHTML = ""

	for (var i = 0; i < num; i++) {

//counter.innerHTML changes the string inside the tag with the id = "counter"
	counter.innerHTML += faces[rollDie()-1] + " "
	};

};

document.getElementById("loop-btn").onclick = loopClick;

function rollDie () {

	//Math.random returns a dec >0 and <1
	var randDec = Math.random();
	return Math.ceil(randDec * 6);

}



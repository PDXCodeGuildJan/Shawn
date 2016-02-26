//Author Shawn Waldow Feb 2016
//
//javascript to make a title page's image cycle every 10 seconds.


//Build up list of .jpg file names. Right now we have
//60 images pdxcg_01.jpg thru pdxcg_60.jpg


var picnames = [null];

function setupStuff(picnames){

	for (var i = 1; i <= 60; i++) {
		if (i <10){
			picnames[i-1] = "../images/pdxcg_0" + i + ".jpg";	
		}
		else {
		picnames[i-1] = "../images/pdxcg_" + i + ".jpg";
		}
	}

	return picnames;
}


//picnames
//window.addEventListener('load', setupStuff, false);

//setInterval(setupStuff, 1000)
picnames = setupStuff(picnames);
i = 0

function hello(){console.log("HEllo");};

while (true){
	document.getElementById("jumbotron").style.backgroundImage = "url('"+ picnames[0] +"')";

	

	i++;

	window.setTimeout(hello, 10000);

}
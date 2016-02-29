//Javapic Inc.
//Author Shawn Waldow Feb 2016
//
//javascript to make a title page's image cycle every 10 seconds.


//Build up list of .jpg file names. Right now we have
//60 images pdxcg_01.jpg thru pdxcg_60.jpg

// Numer of pics must be less than 100 pics to work as is:
var numPics = 60;

var picnames = [null];


function setupStuff(picnames, numPics){

//Make a file name for numPics total files.
	for (var i = 1; i < numPics; i++) {
		
		if (i <10){
			picnames[i-1] = "./images/pdxcg_0" + i + ".jpg";	
		}

		//CIRCLE BACK AFTER MVP: There is still an extra null element in this 
		//file list causing a non-fatal warning.	
		else {
		picnames[i-1] = "./images/pdxcg_" + i + ".jpg";
		}
	}

	return picnames;
}

//Start the setup function to constuct a list of images
//CIRCLE BACK: Do some file i.o. to save the file list so gallery can access it.
picnames = setupStuff(picnames, numPics);
i = 0;
function callback(i){

	//Reset counter each time we iterate through all pics.
	if (i > picnames.length){i=0;}

	//Change the filename as it resides in the CSS
	document.getElementById("jumbotron").style.backgroundImage = "url('"+ picnames[i] +"')";
	i++;
	// Interesting the way you pass the function name, and as the third parameter,
	// the argument for the counter passed into callback
	setTimeout(callback, 1000, i);
}

//Start our *perhaps* psuedo-recursion in motion:
callback(i);
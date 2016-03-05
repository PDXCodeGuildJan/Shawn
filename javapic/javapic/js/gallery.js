// Javapic Inc.
// Author Shawn Waldow
// Image Gallery

var numPics = 60;
// Array to hold the filepaths for each image
var picnames = [null];

function nameIntro(){
	
	//Grab the first name from the url
	var theWholeUrl = document.URL;
	//Discard everything in the url before the ?
	var nameArray = theWholeUrl.split('?')[1];
	//Remove the space if it is there
	var nameArray = nameArray.split('%20');
	//Now nameArray just has the first name at index 0

	//Grab the website's tagline phrase.
	var tagline = document.getElementsByClassName("tagline")[0].firstChild.textContent;

	console.log(tagline, nameArray[0]);

	//Append the name and punctuation to the string copy  of the tagline
	tagline = tagline + ", " + nameArray[0] + ".";

	console.log(tagline);

	//Put the tagline and name into the DOM
	document.getElementsByClassName("tagline")[0].firstChild.textContent = tagline;
}


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

// Create a little tree with an li as the parent node of a child Img tag.
// The img will be set to display the image passed in as an arg.
function createOneLiImg(fileNameString){

	var anLi = document.createElement("li");
	var anImg = document.createElement("img");
	anImg.setAttribute("src", fileNameString);
	anLi.appendChild(anImg);
	return anLi
}


//Draw the greeting
nameIntro();

//Load up the file names
picnames = setupStuff(picnames, numPics);

//Get a handle on the gallery section
gallerySection = document.getElementById("gallery");

//Loop through and put all images into gallery
for (var i = picnames.length - 1; i >= 0; i--) {
	var liImg = createOneLiImg (picnames[i]);
	//Now insert this result into the DOM
	gallerySection.appendChild(liImg);
}


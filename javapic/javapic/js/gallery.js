// Javapic Inc.
// Author Shawn Waldow
// Image Gallery
//
// Housekeeping post MVP: Do we need to delete event listners after use?
var numPics = 60;
// Array to hold the filepaths for each image
var picnames = [null];

//Grab the user name we passed from join.html in the URL asfter the "?"
//Probably better to use var query = window.location.search.slice(1);
//Circle back after MVP.
function nameIntro(){
	
	//Grab the first name from the url
	var theWholeUrl = document.URL;
	//Discard everything in the url before the ?
	var nameArray = theWholeUrl.split('?')[1];
	//Remove the space if it is there
	var nameArray = nameArray.split('%20');
	//Now nameArray just has the first name at index 0

	//Grab the website's tagline phrase.
	var tagline = document.getElementsByClassName("tagline")[0];
	tagline = tagline.firstChild.textContent
	console.log(tagline, nameArray[0]);

	//Append the name and punctuation to the string copy  of the tagline
	tagline = tagline + ", " + nameArray[0] + ".";

	console.log(tagline);

	//Put the tagline and name into the DOM
	document.getElementsByClassName("tagline")[0].firstChild.textContent = tagline;
}


function setupStuff(picnames, numPics){

//Make a file name for numPics total files.
	for (var i = 1; i <= numPics; i++) {
		
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


//Light up a big box with the whole Image!
function lightBox(event) {

//Look for the IMG attribute from the NameNodeMap from the event.	
    if (event.target.nodeName === "IMG") {

    	//Grab the handle on the image_show div.
        var lightBox = document.getElementById("image_show");
        //copy the src attribute from the img clicked and put it
        //in the lightbox's src.
        lightBox.firstChild.src = event.target.src;
        //Turn on.
        lightBox.className = "display_img";

    }
}


function killLightBox(event){
	
	//If we click outside the event's IMG...
	//I still don't really understand how this overpowers the img in gallery.
	if (event.target.nodeName != "IMG") {
	//Grab the handle on the image_show div.
	var lightBox = document.getElementById("image_show");
	//Turn it off.
	lightBox.className = "display_none";
	}
}

////////////////////////////////////////////////////////////
//Begin the "main" operation now that all functions defined.
////////////////////////////////////////////////////////////

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

document.getElementById('gallery').addEventListener('click', lightBox);

document.getElementById('image_show').addEventListener('click', killLightBox);

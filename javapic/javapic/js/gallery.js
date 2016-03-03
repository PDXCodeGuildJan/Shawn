// Javapic Inc.
// Author Shawn Waldow
// Image Gallery


function nameIntro(){
	var theWholeUrl = document.URL;
	var nameArray = theWholeUrl.split('?')[1];
	var nameArray = nameArray.split('%20');

	var tagline = document.getElementsByClassName("tagline")[0].firstChild.textContent;

	console.log(tagline, nameArray[0]);

	tagline = tagline + ", " + nameArray[0] + ".";

	console.log(tagline);

	document.getElementsByClassName("tagline")[0].firstChild.textContent = tagline;
}

nameIntro();
// Javapic Inc.
// Author Shawn Waldow
// Image Gallery

theWholeUrl = document.URL;
nameArray = theWholeUrl.split('?')[1];
nameArray = nameArray.split('%20');

var tagline = document.getElementsByClass("tagline")[0];

tagline = tagline + nameArray[0];

document.getElementsByClass("tagline")[0] = tagline;
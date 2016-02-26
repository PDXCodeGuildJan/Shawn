//Author Shawn Waldow Feb 2016
//
//javascript to make a title page's image cycle every 10 seconds.


//Build up list of .jpg file names. Right now we have
//60 images pdxcg_01.jpg thru pdxcg_60.jpg

var picnames = [null];

function setupStuff(picnames){

for (var i = 1; i <= 60; i++) {
	if (i <10){
		picnames[i-1] = "pdxcg_0" + i + ".jpg";	
	}
	else {
	picnames[i-1] = "pdxcg_" + i + ".jpg";
	}
	//return picnames;


//picnames = setupStuff();
/*console.log(picnames);
*/

//setInterval(console.log("hello?"), 1000);

return picnames;
}


//picnames
//window.addEventListener('load', setupStuff, false);

//setInterval(setupStuff, 1000)
picnames = setupStuff(picnames);

console.log(picnames)
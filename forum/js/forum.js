// DONT FORGET TO DISABLE BROWSER SCRUBBING
var grabFormKillDefaultScrub = document.getElementById('signup');
var noValidate = document.createAttribute("novalidate");
grabFormKillDefaultScrub.setAttributeNode(noValidate);

console.log("JAVASCRIPT HAS LOADED")

var url = 'https://spreadsheets.google.com/feeds/list/1NlIJLGd32t38kt6mJgc64SFpDM_ltq7nfzaRjV1wpLI/default/public/values?alt=json-in-script';

var theNewPost = document.getElementsByName('textarea');

$.ajax({
	type: 'GET', 
	url: url, 
	dataType: "JSONP", 
	success: function(data){console.log(data);},
})


document.getElementById('submit').addEventListener('click', submitPost);

function submitPost(event) {

	//Mysterious bit necesarry for custom form submission.
	event.preventDefault();

	console.log("posted pal");
	console.log(theNewPost[0].value);

}
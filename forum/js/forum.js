// DONT FORGET TO DISABLE BROWSER SCRUBBING
var grabFormKillDefaultScrub = document.getElementById('signup');
var noValidate = document.createAttribute("novalidate");
grabFormKillDefaultScrub.setAttributeNode(noValidate);

console.log("JAVASCRIPT HAS LOADED")

var url = 'https://spreadsheets.google.com/feeds/list/1NlIJLGd32t38kt6mJgc64SFpDM_ltq7nfzaRjV1wpLI/default/public/values?alt=json-in-script';

var theNewPost = document.getElementsByName('textarea');

var postsDiv = document.getElementById('main-posts');

$.ajax({
	type: 'GET', 
	url: url, 
	dataType: "JSONP", 
	success: getPostsOnPageLoad,
});

function getPostsOnPageLoad(data){
	
	for (i=0; i<data.feed.entry.length; i++){
	
	var h2 = document.createElement('h2');
	h2.setAttribute('class', 'post');
	h2.textContent = data.feed.entry[i].gsx$title.$t;
	postsDiv.appendChild(h2);

	var bodyDiv = document.createElement('div');
	bodyDiv.setAttribute('class', 'body');
	bodyDiv.textContent = data.feed.entry[i].gsx$post.$t;
	postsDiv.appendChild(bodyDiv);

	var footer = document.createElement('footer');
	footer.textContent = data.feed.entry[i].gsx$timestamp.$t;
	postsDiv.appendChild(footer);
	}

}

document.getElementById('submit').addEventListener('click', submitPost);

function submitPost(event) {

	//Mysterious bit necesarry for custom form submission.
	event.preventDefault();



	console.log("posted pal");
	console.log(theNewPost[0].value);
	console.log("title ",data);
	console.log("post ",data);
	console.log("time",data);
}
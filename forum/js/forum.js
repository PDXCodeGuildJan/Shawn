// DONT FORGET TO DISABLE BROWSER SCRUBBING
var grabFormKillDefaultScrub = document.getElementById('signup');
var noValidate = document.createAttribute("novalidate");
grabFormKillDefaultScrub.setAttributeNode(noValidate);

console.log("JAVASCRIPT HAS LOADED")

var getUrl = 'https://spreadsheets.google.com/feeds/list/1NlIJLGd32t38kt6mJgc64SFpDM_ltq7nfzaRjV1wpLI/default/public/values?alt=json-in-script';
var postUrl = "https://docs.google.com/forms/d/1W1jO8DwInFuzlabeYqEp6hUUUqDbR8gESs1Pk6qozOc/formResponse";
var newPostsTitle = document.getElementById('title');
var theNewPost = document.getElementsByName('textarea');
var postsDiv = document.getElementById('main-posts');


$.ajax({
	type: 'GET', 
	url: getUrl, 
	dataType: "JSONP", 
	success: getPosts,
});

function removePosts(){
	while (postsDiv.hasChildNodes()){
		var child = postsDiv.firstChild;
		var oldChild = postsDiv.removeChild(child);
		}
}

function getPosts(data){
	
	removePosts();

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


	$.ajax({
		url: postUrl,
		//These entry objects are mysterious google spreadsheet stuff.
		data: {"entry.1639809944" : newPostsTitle.value, "entry.1402022725" : theNewPost[0].value},
		type: "POST",
		dataType: "xml",
		success: function(data){console.log(data);},
		statusCode: {
			0: function() {
		
				console.log("0 error good.");	
				
				$.ajax({
					type: 'GET', 
					url: getUrl, 
					dataType: "JSONP", 
					success: getPosts,
				});

			},

			200: function() {
			//make some error handling
			}
		}
	});


	console.log("posted pal");
	console.log(theNewPost[0].value);
}
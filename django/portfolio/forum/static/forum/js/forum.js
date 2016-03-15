// DONT FORGET TO DISABLE BROWSER SCRUBBING
var grabFormKillDefaultScrub = document.getElementById('signup');
var noValidate = document.createAttribute("novalidate");
grabFormKillDefaultScrub.setAttributeNode(noValidate);

console.log("JAVASCRIPT HAS LOADED")

var getUrl = 'https://spreadsheets.google.com/feeds/list/1NlIJLGd32t38kt6mJgc64SFpDM_ltq7nfzaRjV1wpLI/default/public/values?alt=json-in-script';
var postUrl = "https://docs.google.com/forms/d/1W1jO8DwInFuzlabeYqEp6hUUUqDbR8gESs1Pk6qozOc/formResponse";

//Handle for a new post's user entered title.
var newPostsTitle = document.getElementById('title');
//Handle for a new post's user entered body text.
var theNewPost = document.getElementsByName('textarea');
//Handle for where the posts-so-far show up.
var postsDiv = document.getElementById('main-posts');

//Listen for a submit button click
document.getElementById('submit').addEventListener('click', submitPost);



//This function helps us refresh the existing posts by removing them
//if we'have loaded them previously and are updating because of post.
function removePosts(){
	//Remove as long as there are children to remove.
	while (postsDiv.hasChildNodes()){
		var child = postsDiv.firstChild;
		//Kill the haflings!
		var oldChild = postsDiv.removeChild(child);
		}
}

//Display all existing posts.
function getPosts(data){
	
	//Remove previous version of posts.
	removePosts();

	//Loop through all the entries in the sheet.
	for (i=0; i<data.feed.entry.length; i++){
	
	//Make a post title
	var h2 = document.createElement('h2');
	h2.setAttribute('class', 'post');
	h2.textContent = data.feed.entry[i].gsx$title.$t;
	postsDiv.appendChild(h2);

	//Make a post body.
	var bodyDiv = document.createElement('div');
	bodyDiv.setAttribute('class', 'body');
	bodyDiv.textContent = data.feed.entry[i].gsx$post.$t;
	postsDiv.appendChild(bodyDiv);

	//Make a footer to put the timestamp into.
	var footer = document.createElement('footer');
	footer.textContent = data.feed.entry[i].gsx$timestamp.$t;
	postsDiv.appendChild(footer);
	}

}

function submitPost(event) {

	//Mysterious bit necesarry for custom form submission.
	event.preventDefault();


	$.ajax({
		url: postUrl,
		//These entry objects are mysterious google spreadsheet stuff.
		data: {
				"entry.1639809944" : newPostsTitle.value, 
				"entry.1402022725" : theNewPost[0].value
			},
		type: "POST",
		dataType: "xml",
		success: function(data){console.log(data);},
		//We expect an error code 0 because of some google docs specifics.
		statusCode: {
			0: function() {
		
				console.log("0 error good.");	
				
				setTimeout($.ajax, 3500, {
					type: 'GET', 
					url: getUrl, 
					dataType: "JSONP", 
					success: getPosts,
				});

			},

			200: function() {
			console.log("Ajax post returned 200")
			}
		}
	});


	console.log("posted pal");
	console.log(theNewPost[0].value);
}


//Start the ball rolling!!!
//Grab posts from the sheet and hand them to getPosts() to begin 
//making HTML out of!
$.ajax({
	type: 'GET', 
	url: getUrl, 
	dataType: "JSONP", 
	success: getPosts,
});

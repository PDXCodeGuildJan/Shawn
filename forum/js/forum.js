// XML Http request object request
var xhr = new XMLHttpRequest();
var thePostsJSONP;

// When response loads
xhr.onload = function() {
	// The following conditional check will not work locally.
	if(xhr.status === 200) {
		thePostsJSONP = xhr.responseText;
	}
};



xhr.open('GET', 'https://spreadsheets.google.com/feeds/list/1NlIJLGd32t38kt6mJgc64SFpDM_ltq7nfzaRjV1wpLI/default/public/values?alt=json-in-script', true);
xhr.send(null);

console.log(thePostsJSONP);

//Load as JSONP
//JSON.parse()

/*function ajaxGet (){
	// The following conditional check will not work locally.
	if(xhr.status === 200) {
		document.getElementById('gsx$post').innerHTML = xhr.responseText;
	}
};

$.get('https://spreadsheets.google.com/feeds/list/1NlIJLGd32t38kt6mJgc64SFpDM_ltq7nfzaRjV1wpLI/default/public/values?alt=json-in-script', ajaxGet ,XML)



*/
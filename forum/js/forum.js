console.log("JAVASCRIPT HAS LOADED")

var url = 'https://spreadsheets.google.com/feeds/list/1NlIJLGd32t38kt6mJgc64SFpDM_ltq7nfzaRjV1wpLI/default/public/values?alt=json-in-script'

$.ajax({type: 'GET', url: url, dataType: "JSONP", success: function(data){console.log(data)}
})
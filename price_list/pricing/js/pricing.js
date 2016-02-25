// Establish the event listener
// Add the click event handler to the "add-item"

var addItemButton = document.getElementById("add-item");
addItemButton.onclick = addItem;

var addStockButton = document.getElementById("add-stock");
addStockButton.onclick = addStock;

var removeStockButton = document.getElementById("remove-stock");
removeStockButton.onclick = removeStock;

/*	Add the item in the text fields to the inventory
*	list which is in the table body (id="inventory")
*/

function addStock() {
	console.log("good");
	//NOT ALLOWED TO USE QuerySelectorAll()
	//Get all the input tags

	var input = document.getElementsByTagName("input");

	var checkedboxes = [];

    //loop through for the number of input tags grabbed.
    for (var i=0; i<input.length; i++){
       
        // Grab only the checked boxes
        if (input[i].checked === true){

            checkedboxes.push(input[i]);

        //traverse the DOM
        var status = input[i].parentNode.nextSibling.nextSibling.nextSibling;
        status.textContent = "yes";
        status.className = "true";

            console.log("This should be checked boxes", checkedboxes)

            };
    };
};



function removeStock() {
	// USE querySelectorAll()
	var allTRsInTarnation = document.querySelectorAll('tbody>tr>td>input:checked');
	
	//loop through the array we made.
	for (var i=0; allTRsInTarnation.length > i; i++){
		var status = allTRsInTarnation[i].parentNode.parentNode.children[3];
		status.textContent = "No";
		status.className="false";

		}

	console.log(allTRsInTarnation);

};

function addItem() {
	var materialName = document.getElementById("name").value;
	var price = document.getElementById("price").value;
	var checked = document.getElementById("in-stock").checked;

	var inventory = document.getElementById("inventory");
	var yesno = "no"
	if (checked) 
		{yesno = "yes"; 
		truefalse = "true";
		} 
	else 
		{yesno = "no"; 
		truefalse = "false";
	};
	var newRow = "<tr><td><input type='checkbox' id='this-item' /></td><td>" + materialName + "</td><td>"+ price +"</td><td class='"+truefalse+"'>" + yesno + "</td></tr>";
	inventory.innerHTML += newRow

};




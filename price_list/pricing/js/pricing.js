// Establish the event listener
// Add the click event handler to the "add-item"

var addItemButton = document.getElementById("add-item");
addItemButton.onclick = addItem;

var addStockButton = document.getElementById("add-stock");
addStockButton.onclick = addStock;

/*	Add the item in the text fields to the inventory
*	list which is in the table body (id="inventory")
*/

function addStock() {
	console.log("good")
	//NOT ALLOWED TO USE QuerySelectorAll()

	//find allthe selected things

	//change their inStock value of the selected things

	//update the display?
}

function removeStock() {
	// USE querySelectorAll()
}

function addItem() {
	var materialName = document.getElementById("name").value;
	var price = document.getElementById("price").value;
	var checked = document.getElementById("in-stock").checked;

	var inventory = document.getElementById("inventory");
	var yesno = "no"
	if (checked) 
		{yesno = "yes"; 
		truefalse = "true";} 
	else 
		{yesno = "no"; 
		truefalse = "false";};
	var newRow = "<tr><td><input type='checkbox' id='inasec' /></td><td>" + materialName + "</td> <td>"+ price +"</td><td class='"+truefalse+"'>" + yesno + "</td></tr>";
	inventory.innerHTML += newRow

};




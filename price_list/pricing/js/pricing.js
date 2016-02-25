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
	
	var input = document.getElementsByTagName("input");
	
	//find allthe selected things

	 var checkedboxes = [];

    //loop through all elements and extract the info.
    for (var i=0; i<input.length; i++){
       
        // make an if statement that specifies which input we want to use
        if (input[i].checked === true){
            // start a loop that identifies whether the box is checked or not
                // Make a list for the checked boxes to go into
            checkedboxes.push(input[i]);

        var status = input[i].parentNode.nextSibling.nextSibling.nextSibling;
        status.textContent = "yes";
        status.className = "true";

            console.log("This should be checked boxes", checkedboxes)

            // change the inStock value of the selected things   
            //for (var 1=0; i<checked.length; i++)
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




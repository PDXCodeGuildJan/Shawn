// Establish the event listener
// Add the click event handler to the "add-item"

var addItemButton = document.getElementById("add-item");
addItemButton.onclick = addItem;

var addStockButton = document.getElementById("add-stock");
addStockButton.onclick = addStock;

var removeStockButton = document.getElementById("remove-stock");
removeStockButton.onclick = removeStock;

window.onload = loadDataWithAJAX;

var products = [];

/*	Add the item in the text fields to the inventory
*	list which is in the table body (id="inventory")
*/

//add delete button
var deleteItemButton = document.getElementById("del-item");
deleteItemButton.onclick = deleteItem;

function addStock() {
	console.log("good");
	//NOT ALLOWED TO USE QuerySelectorAll()
	//Get all the input tags

	var input = getSelectedRowBoxes();

    //loop through for the number of input tags grabbed.
    for (var i=0; i<input.length; i++){

        //traverse the DOM
        var status = input[i].parentNode.nextSibling.nextSibling.nextSibling;
        status.textContent = "yes";
        status.className = "true";

        // Update the prodyctin the products array that correspond s to the checkbox we are updating
        var prodId = input[i].parentNode.parentNode.id;
        products[prodId].inStock = true;

		//now make a similar change to removestock


		saveData();


    };
};



function removeStock() {
	// USE querySelectorAll()
	var allTRsInTarnation = getSelectedRowBoxes();
	
	//loop through the array we made.
	for (var i=0; allTRsInTarnation.length > i; i++){
		var status = allTRsInTarnation[i].parentNode.parentNode.children[3];
		status.textContent = "No";
		status.className="false";

		}

	//console.log(allTRsInTarnation);
	saveData();
};

function addItem() {
	var materialName = document.getElementById("name").value;
	var price = document.getElementById("price").value;
	var inStock = document.getElementById("in-stock").checked;

	var newProd = new Product(materialName, price, inStock);
	products.push(newProd);
	displayInventory();
 		//HAS A HUGE BUG THAT RESETS ALL INSOTCKS TO YES
 	saveData();
}

/* Delete selected rows from the inventory.
*/
function deleteItem(){
	// First, determine all the selected rows
	var selected = getSelectedRowBoxes();
	// Delete the products objects that correspond to those rows from the products array
	for (var i = selected.length-1; i > -1; i--) 
		{var prodId = selected[i].parentNode.parentNode.id;
		delete products[prodId];
		products.splice(prodId, 1);
	};
	//Rerender the HTML list, using displyInventory
	displayInventory();
	saveData();
}

//hrlper funct to get all the selected boxes in HTMLs inventory return array of selected checkboxes
function getSelectedRowBoxes(){
	var allTRsInTarnation = document.querySelectorAll('tbody>tr>td>input:checked');
	return allTRsInTarnation;
}

function displayInventory(){

	// Loop through the products array, addin each product
	//to the inventory table in the html.
	var inventory = document.getElementById("inventory");
	// Destroy all previous children.
	inventory.innerHTML = '';


	for (var i =0; i< products.length; i++){
		var newRow = document.createElement("TR");
		newRow.id = i;

		var checkbox = document.createElement("TD");
		var innerCheckbox = document.createElement("INPUT");
	// !!!!make sure any changes you made to the check bx get put in here too
		innerCheckbox.type = "checkbox";
		checkbox.appendChild(innerCheckbox);


		var materialName = document.createElement("TD");
		materialName.textContent = products[i].prodName;

		var price = document.createElement("TD");
		price.textContent = products[i].price;

		var inStock = document.createElement("TD");
		inStock.textContent = (function(inStock) {
			if (inStock) {return "Yes";} return "No";
		}(products[i].inStock));
		inStock.setAttribute = ("class", products[i].inStock);


		newRow.appendChild(checkbox);
		newRow.appendChild(materialName);
		newRow.appendChild(price);
		newRow.appendChild(inStock);

		inventory.appendChild(newRow);

	};
	saveData();
}


/*Object constructor for our products*/
function Product(name, price, inStock) {
	this.prodName = name;
	this.price = price;
	this.inStock = inStock;

	this.toggleStock = function(stock) {
		this.inStock;
	}

}


// Save data current products array.
function saveData(){
	//transform products array into a JSON string.
	var productJSON = JSON.stringify(products);

	//save data to local storage using built in javascript
	localStorage.setItem("variablenameprice", productJSON);
}


// Load data to products array.
function loadData(){
	//Load local data from storage
	var productJSON = localStorage.getItem("variablenameprice");
	//console.log("Loaded:", productJSON);
	products = JSON.parse(productJSON);
	console.log(products);
	if (!products){ products = [];}
	displayInventory();

}


/**
* Load the data from the json file on the server with AJAX.
**/
function loadDataWithAJAX(){

	//Create a new XMLHTTPRequest object
	var request = new XMLHttpRequest();
	//Add Call Info
	request.open('GET', 'data.json', true);
	// setup the onload function
	request.onload = function (){
		if (request.status === 200){
			console.log(request.responseText);
		}
	};

	// Actually send out the request!
	request.send();

}
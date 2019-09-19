// Put your custom javascript here

function addWidget(id) {
	var iframe = document.createElement("IFRAME");
	iframe.onload = function() {
		var divNode = document.querySelector("#lab02-wgt01");
		var widget = iframe.contentWindow.document.getElementByID("lab02-wgt01");
		divNode.appendChild(widget);
	};
	iframe.src = "http://econ-models-widget.herokuapp.com/";
	iframe.id = "lab02-wgt01-iframe";
	iframe.classList.add("widget");	
}
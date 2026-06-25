// Query dark mode setting
function isDark() {
	return localStorage.getItem("theme") === "dark" || (!localStorage.getItem("theme") && window.matchMedia("(prefers-color-scheme: dark)").matches);
}

// Get URL of current page and also current node
var curr_url = decodeURI(window.location.href.replace(location.origin, ""));
if (curr_url.endsWith("/")) {
	curr_url = curr_url.slice(0, -1);
}

// Get graph element
var container = document.getElementById("graph");

// Parse nodes and edges
try {
	var curr_node = graph_data.nodes.filter((node) => decodeURI(node.url) == curr_url);
} catch (error) {
	var curr_node = null;
}
var nodes = null;
var edges = new vis.DataSet(graph_data.edges);

if (curr_node.length > 0) {
	curr_node = curr_node[0];

	// Get nodes connected to current
	var connected_nodes = graph_data.edges
		.filter((edge) => edge.from == curr_node.id || edge.to == curr_node.id)
		.map((edge) => {
			if (edge.from == curr_node.id) {
				return edge.to;
			}
			return edge.from;
		});

	if (graph_is_local) {
		nodes = new vis.DataSet(graph_data.nodes.filter((node) => node.id == curr_node.id || connected_nodes.includes(node.id)));
	} else {
		nodes = new vis.DataSet(graph_data.nodes);
	}
} else {
	curr_node = null;
	nodes = new vis.DataSet(graph_data.nodes);
}

// Get nodes and edges from generated javascript
var max_node_val = Math.max(...nodes.map((node) => node.value));

// Highlight current node and set to center
if (curr_node) {
	nodes.update({
		id: curr_node.id,
		value: Math.max(4, max_node_val * 2.5),
		shape: "star",
		color: "#63afae", // Keep Sicily Teal accent
		font: {
			strokeWidth: 1,
		},
		x: 0,
		y: 0,
	});
}

// Construct graph
var options = ___GRAPH_OPTIONS___;

// Adjust options dynamically for better user experience
if (graph_is_local) {
	if (!options.interaction) {
		options.interaction = {};
	}
	options.interaction.zoomView = false; // Disable scroll wheel zooming to prevent page scroll hijacking
	options.interaction.dragNodes = true;  // Explicitly enable dragging nodes
	options.interaction.dragView = true;   // Explicitly enable panning the view
} else {
	if (!options.interaction) {
		options.interaction = {};
	}
	options.interaction.zoomSpeed = 0.25; // Gentle, less sensitive zoom speed
	options.interaction.dragNodes = true;
	options.interaction.dragView = true;
}

var graph = new vis.Network(
	container,
	{
		nodes: nodes,
		edges: edges,
	},
	options
);

// Gentle trackpad zoom speed proxy interceptor
if (graph && graph.interactionHandler && graph.interactionHandler.body && graph.interactionHandler.body.eventListeners && graph.interactionHandler.body.eventListeners.onMouseWheel) {
	var originalOnMouseWheel = graph.interactionHandler.body.eventListeners.onMouseWheel;
	graph.interactionHandler.body.eventListeners.onMouseWheel = function(event) {
		var proxyEvent = new Proxy(event, {
			get: function(target, prop) {
				if (prop === 'deltaY') {
					var delta = target.deltaY;
					// Trackpad pinch-to-zoom has ctrlKey set to true in browser zoom event emulation
					var multiplier = target.ctrlKey ? 0.05 : 0.25; 
					return delta * multiplier;
				}
				var value = target[prop];
				if (typeof value === 'function') {
					return value.bind(target);
				}
				return value;
			}
		});
		originalOnMouseWheel(proxyEvent);
	};
}


// Clickable URL
graph.on("selectNode", function (params) {
	if (params.nodes.length === 1) {
		var node = nodes.get(params.nodes[0]);
		if (graph_link_replace) {
			window.open(node.url, "_self");
		} else {
			window.open(node.url, "_blank");
		}
	}
});

// Focus on current node + scaling
var initialScale = 0.35;
graph.once("afterDrawing", function () {
	initialScale = graph.getScale();
	if (curr_node) {
		if (!graph_is_local) {
			graph.focus(curr_node.id, {
				scale: graph.getScale() * 1.8,
			});
		}
	} else {
		var clientHeight = container.clientHeight;
		graph.moveTo({
			position: {
				x: 0,
				y: -clientHeight / 3,
			},
			scale: graph.getScale() * 1.2,
		});
	}
});

// Enforce zoom limits on global graph
if (!graph_is_local) {
	graph.on("zoom", function (params) {
		var minScale = Math.min(0.35, initialScale * 0.85);
		var maxScale = 2.5;
		if (graph.getScale() < minScale) {
			graph.moveTo({ scale: minScale });
		} else if (graph.getScale() > maxScale) {
			graph.moveTo({ scale: maxScale });
		}
	});
}

// Zoom buttons event listeners
var zoomInBtn = document.getElementById("zoom-in-btn");
var zoomOutBtn = document.getElementById("zoom-out-btn");

if (zoomInBtn && zoomOutBtn) {
	zoomInBtn.addEventListener("click", function(e) {
		e.preventDefault();
		var currentScale = graph.getScale();
		var newScale = currentScale * 1.25;
		if (newScale <= 2.5) {
			graph.moveTo({ scale: newScale });
		}
	});

	zoomOutBtn.addEventListener("click", function(e) {
		e.preventDefault();
		var currentScale = graph.getScale();
		var newScale = currentScale / 1.25;
		var minScale = Math.min(0.35, initialScale * 0.85);
		if (newScale >= minScale) {
			graph.moveTo({ scale: newScale });
		} else {
			graph.moveTo({ scale: minScale });
		}
	});
}

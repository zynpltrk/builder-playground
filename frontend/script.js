const container = document.getElementById("items");

fetch("http://127.0.0.1:8000/items?color=red")
  .then(response => response.json())
  .then(items => {
    items.forEach(item => {
      const div = document.createElement("div");
      div.textContent = item.name + " | " + item.color;
      container.appendChild(div);
    });
  });

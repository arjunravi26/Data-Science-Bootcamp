var btn = document.getElementById('btn');
var txt = document.getElementById('txt');
var list = document.getElementById('list');
var list = document.getElementById('list');
btn.addEventListener('click', addItem);

function addItem() {
    var item = document.createElement('li');
    var text = txt.value;
    item.style.listStyleType = 'none';
    item.innerHTML = text;
    item.style.backgroundColor = "white";
    item.style.width = "100px";
    item.style.display = 'flex';
    item.style.gap = '50px';
    list.appendChild(item);
    var icon = document.createElement('i');
    icon.classList.add('fas', 'fa-trash');
    console.log(icon);
    item.appendChild(icon);
}
remove_btn.addEventListener('click', removeItem);

function removeItem(event) {
    if (event.target.classList[0] == 'fas') {
        remove_btn.parentClass.remove();
    }
}
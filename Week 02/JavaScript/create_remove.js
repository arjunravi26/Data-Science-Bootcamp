// var create = document.getElementById('create');
// var remove = document.getElementById('remove');

function create() {
    var text = document.createElement('p');
    text.innerHTML = "New Element Created";
    document.body.appendChild(text);
}
function remove() {
    var text = document.getElementsByTagName('p')
    text[0].remove()
}
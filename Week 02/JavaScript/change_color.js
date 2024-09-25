var text = document.getElementById('text');
var btn = document.getElementById('btn');

text.addEventListener('mouseover', changeBG)
text.addEventListener('mouseout', changeBG1)
btn.addEventListener('click', changeColor)
function changeColor() {
    text.style.color = "red"
}
function changeBG() {
    text.style.backgroundColor = "black"
}
function changeBG1() {
    text.style.backgroundColor = "white"
}
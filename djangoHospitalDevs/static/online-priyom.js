var form = document.getElementById('form');
form.addEventListener('submit', showMessage);

function showMessage(event) {
    alert("Your response has been recorded. (Not actually, this is just a demo!)");
    event.preventDefault();
}
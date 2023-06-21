function handleClick() {
    alert('you pressed the button');
}

window.onload = function() {
    console.log('page loaded');

    document.getElementById('button').addEventListener('Click', handleClick);
}
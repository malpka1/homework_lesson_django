var counter = 0;
function handleClick() {
    alert('you pressed the button');
    counter += 1;
    console.log('you pressed the button' + counter + 'time(s)');
    document.getElementsByTagName('span')[0].textContent = counter;
}

window.onload = function() {
    console.log('page loaded');
}
document.getElementById('button').addEventListener('click me', handleClick);


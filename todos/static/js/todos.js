function handleClick() {
    event.preventDefault();
    url = event.target.getAttribute("href");
    axios.post(url).then(response => {
        console.log(response);
        document.querySelector(`[data-todo-id="${response['data']['todo']['id']}"]`).textContent = response['data']['todo']['description'];
    });

};

window.onload = function() {
    document.querySelectorAll(".btn-like").forEach(btn => btn.addEventListener('click', handleLike))
};



window.addEventListener('load', (e) => {
    const deleteShowTime = document.querySelectorAll('.deleteShowTime');
    console.log(deleteShowTime)
    deleteShowTime.forEach(e => {
        const id = e.getAttribute('data-show-id');
        console.log(id)
        e.setAttribute('id', `delete ${id}`);
        e.addEventListener('click', (event) => {
            console.log(id);
            fetch(`http://localhost:8000/deleteShowTime${id}`, {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/x-www-form-urlencoded'
                }
            }).then(res => {
                console.log("deleted")
                location.reload();
            })
        })
    })
})


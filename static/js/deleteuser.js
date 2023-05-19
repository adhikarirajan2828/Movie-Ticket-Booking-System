
window.addEventListener('load', (e) => {
    const deleteUser = document.querySelectorAll('.deleteUser');
    console.log(deleteUser)
    deleteUser.forEach(e => {
        const id = e.getAttribute('data-user-id');
        console.log(id)
        e.setAttribute('id', `delete ${id}`);
        e.addEventListener('click', (event) => {
            console.log(id);
            fetch(`http://localhost:8000/deleteUser${id}`, {
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


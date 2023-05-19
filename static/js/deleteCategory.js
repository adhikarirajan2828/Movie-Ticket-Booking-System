
window.addEventListener('load', (e) => {
    const deleteCategory = document.querySelectorAll('.deleteCategory');
    console.log(deleteCategory)
    deleteCategory.forEach(e => {
        const id = e.getAttribute('data-movie-id');
        console.log(id)
        e.setAttribute('id', `delete ${id}`);
        e.addEventListener('click', (event) => {
            console.log(id);
            fetch(`http://localhost:8000/deleteCategory${id}`, {
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


window.addEventListener('load', (e) => {
    const deleteLanguage = document.querySelectorAll('.deleteLanguage');
    console.log(deleteLanguage)
    deleteLanguage.forEach(e => {
        const id = e.getAttribute('data-lang-id');
        console.log(id)
        e.setAttribute('id', `delete ${id}`);
        e.addEventListener('click', (event) => {
            console.log(id);
            fetch(`http://localhost:8000/deleteLanguage${id}`, {
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

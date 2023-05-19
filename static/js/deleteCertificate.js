
window.addEventListener('load', (e) => {
    const deleteCertificate = document.querySelectorAll('.deleteCertificate');
    console.log(deleteCertificate)
    deleteCertificate.forEach(e => {
        const id = e.getAttribute('data-certificate-id');
        console.log(id)
        e.setAttribute('id', `delete ${id}`);
        e.addEventListener('click', (event) => {
            console.log(id);
            fetch(`http://localhost:8000/deleteCertificate${id}`, {
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


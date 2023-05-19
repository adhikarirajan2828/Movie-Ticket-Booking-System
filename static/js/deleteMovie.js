// console.log(deleteMovies)
window.addEventListener('load', (e) => {
    const deleteMovies = document.querySelectorAll('.deleteMovie');
    deleteMovies.forEach(e => {
        const id = e.getAttribute('data-movie-id');
        console.log(id)
        e.setAttribute('id', `delete ${id}`);
        console.log(e);
        e.addEventListener('click', (event) => {
            const id = e.getAttribute('data-movie-id');
            console.log(id);
            fetch(`http://localhost:8000/deleteMovie${id}`, {
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

// const deletes = document.querySelector('.delete');
// deleteMovie.addEventListener('click',(e) => {
//     console.log(e)
// })
// deleteMovie.addEventListener('click', (e) => {
//     console.log('delete')
//     const id = deleteMovie.getAttribute('data-movie-id')
//     console.log(id)
//     e.preventDefault();

//     fetch(`http://localhost:8000/deleteMovie${id}`,{
//         method: 'POST',
//         headers: {
//             'Accept': 'application/json',
//         'Content-Type': 'application/x-www-form-urlencoded'
//         }
//     }).then(res => {console.log("deleted")
//     location.reload();
// });
// })
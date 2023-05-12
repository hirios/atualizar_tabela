fetch('http://179.98.37.51:5000/json')
.then(async function(response) {
    console.log(await response.json())
})  
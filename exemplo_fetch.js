fetch('http://127.0.0.1:5000/json')
.then(async function(response) {
    console.log(await response.json())
})  

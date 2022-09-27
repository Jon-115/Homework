// Express allows us to create a server that can host an API. We are hosting the API
// on localhost(127.0.0.1)
const express = require('express')
const app = express()


let pokedex = [{"name": 'pikachu', 'hp': 50, 'id': 1}, {"name": 'bulbasaur', 'hp': 40, 'id': 2}, {"name": 'charmander', 'hp': 50, 'id': 3}]
let id = pokedex.length


app.get('/pokemon', function (request, response) {
  response.send(pokedex)
})

app.post('/pokemon/:name/:hp', (request, response) => {
  let pokemon = {'name': request.params.name, 'hp': request.params.hp, 'id': id += 1}
  pokedex.push(pokemon)
  response.send(`The pokemon ${pokemon.name} has been created with ${pokemon.hp}`)
})


app.put('/pokemon/:id', (request, response)=> {
    let pokemonID = request.params.id;
    for(let i = 0; i < pokedex.length; i++) {
        if(pokedex[i].id == pokemonID) {
            let pokemon = pokedex[i]
            newHp = pokemon.hp += 10
            response.send(`Updated ${pokemon.name}'s hp to ${newHp}`);
        }
    }

})

app.delete('/pokemon/:id', (request, response) => {
    for(let i = 0; i < pokedex.length; i++) {
      if(pokedex[i].id == request.params.id) {
        pokeName = pokedex[i].name
        pokedex.splice(i,1)
        response.send(`${pokeName} has return to the wild.`)
      }
    }
})

app.listen(3000)
console.log("Server is running on port 3000")
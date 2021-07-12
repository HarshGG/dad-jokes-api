## Dad Jokes API Server
Description: create an API server that returns Dad Jokes as JSON<br>
Language: Python<br>
Project type: School project, solo<br>
Purpose: Learn how to create an API web application using Python's flask modules<br>

## important instructions:

### How to run: 
Run the file "dadjokes.py", this runs the flaskapp in your localhost<br>
Next, run the localhost in your browser using "http://localhost:3001/". Further instructions for routes are below.

### Routes
This API application serves the following routes.

All routes return an `application/json` content type and appropriate HTTP status code. 

#### Home
`/`
Returns JSON `{'success': True, 'message': 'This is the home page'}` with a `application/json` content type and a 200 status header.

#### Random Joke
`/random`
Pulls a random joke out of `dadjokes.json` and send it back to the browser. 

An example request may return the following JSON string.

```json
{
    "id": "b6dc0870",
    "name": "Color Blind",
    "joke": "Found out I was colour blind the other day... That one came right out the purple."
}
```

Subsequent runs return different jokes, although the tester does account for the fact that random isn't always random. 


#### Specific Joke
`/joke`

This route allows you to request a specific joke from the data file by passing an `id` parameter. For example, if you want to get joke #123 the request would be `/joke?id=123`. 

`/joke?id=c9aaad4d` returns the following JSON string.

```json
{
    "id": "c9aaad4d",
    "name": "The Royal Flush Of The Jungle",
    "joke": "Why shouldn't you play cards in the jungle? Too many cheetahs."
}
```
Server also checks that the id parameter is there. If it is not, the server returns a 404 status header.

If the requested joke id is not in the data, the server sends a 404 status header. 

### More info about status codes
[HTTP Status Cats](https://http.cat/)

[HTTP Status Dogs](https://httpstatusdogs.com/)

[List of HTTP status codes](https://en.wikipedia.org/wiki/List_of_HTTP_status_codes) 

### Credit
`dadjokes.json` came from [GitHub](https://github.com/mshwery/dad-jokes-api)

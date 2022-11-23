from masonite.routes import Route

ROUTES = [
    Route.get("/", "WelcomeController@show"),

    Route.get("/events", "EventController@index"),
    Route.get("/events/add", "EventController@add"),
    Route.post("/events/create", "EventController@store"),
    Route.get("/events/show/@id", "EventController@show"),
    Route.get('/events/delete/@id', "EventController@delete")
    ]

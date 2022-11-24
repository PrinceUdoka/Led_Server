from masonite.routes import Route

ROUTES = [
    Route.get("/", "WelcomeController@show"),

    Route.get("/events", "EventController@index"),
    Route.get("/events/add", "EventController@add"),
    Route.post("/events/create", "EventController@store"),
    Route.get('/events/delete/@id', "EventController@delete"),

    Route.get("/schedules", "ScheduleController@index"),
    Route.get("/schedules/add", "ScheduleController@add"),
    Route.post("/schedules/create", "ScheduleController@store"),
    Route.get('/schedules/delete/@id', "ScheduleController@delete")
    ]

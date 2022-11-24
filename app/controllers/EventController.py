from masonite.controllers import Controller
from masonite.views import View
from app.models.Event import Event
from masonite.request import Request
from masonite.validation import Validator
from masonite.response import Response

class EventController(Controller):
    def add(self, view: View):
        return view.render('add_event')

    def index(self, view: View):
        events = Event.all()
        return view.render('events',{'events': events})

    def store(self, request: Request, response: Response, validate: Validator):
        errors = request.validate(
            validate.required(['name', 'color']),
        )
        if errors:
            return response.redirect('/events/add').with_errors(errors)
        else:
            Event.create(
                name=request.input('name'),
                color=request.input('color')
            )
            return response.redirect('/events')

    def show(self, view: View, request: Request):
        event = Event.find(request.param('id'))
        print(event)

        return view.render('single', {'event': event})

    def delete(self, request: Request, response: Response):
        event = Event.find(request.param('id'))

        event.delete()
        return response.redirect('/events')
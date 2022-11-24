from masonite.controllers import Controller
from masonite.views import View
from app.models.Schedule import Schedule
from app.models.Event import Event
from masonite.request import Request
from masonite.validation import Validator
from masonite.response import Response

class ScheduleController(Controller):
    def add(self, view: View):
        events = Event.all()
        return view.render('add_schedule',{'events': events})

    def index(self, view: View):
        schedules = Schedule.all()


        return view.render('schedules',{'schedules': schedules})

    def store(self, request: Request, response: Response, validate: Validator):
        errors = request.validate(
            validate.required(['event_id']),
        )
        if errors:
            return response.redirect('/schedules/add').with_errors(errors)
        else:
            print(request.input('event_id'))
            Schedule.create(
                start_time=request.input('start_time'),
                event_id=request.input('event_id')
            )
            return response.redirect('/schedules')

    def delete(self, request: Request, response: Response):
        schedule = Schedule.find(request.param('id'))

        schedule.delete()
        return response.redirect('/schedules')
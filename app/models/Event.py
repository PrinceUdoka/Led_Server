""" Event Model """

from masoniteorm.models import Model
from masoniteorm.relationships import has_many

class Event(Model):
    """Event Model"""

    __fillable__ = ['name', 'color']

    @has_many("id", "event_id")
    def schedules(self):
        from app.models.Schedule import Schedule
        return Schedule
""" Schedule Model """

from masoniteorm.models import Model
from masoniteorm.relationships import belongs_to

class Schedule(Model):
    """Schedule Model"""

    __fillable__ = ['start_time', 'event_id']

    @belongs_to('event_id', 'id')
    def event(self):
        from app.models.Event import Event
        return Event
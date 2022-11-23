""" Event Model """

from masoniteorm.models import Model


class Event(Model):
    """Event Model"""

    __fillable__ = ['name', 'color']

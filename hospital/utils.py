from .models import *
class DataMixin:
    def get_user_contexxt(self,**kwargs):
        context = kwargs
        return context
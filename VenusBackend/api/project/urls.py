from rbasis.urlrouter import router
from . import views

def RegPath():
    router.register(r'project', views.Project, 'Project', '')
    router.register(r'payment', views.Payment, 'Payment', '')

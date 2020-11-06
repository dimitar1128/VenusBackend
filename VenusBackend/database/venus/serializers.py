from .models import *
from rbasis.serializers import *

class tbl_project_serializer(ShAPISerializer):
    class Meta:
        model = tbl_project
        fields = ['id', 'name', 'client_name', 'country', 'contact', 'note', 'start_date', 'status']


class tbl_payment_serializer(ShAPISerializer):
    class Meta:
        model = tbl_payment
        fields = ['id', 'project_id', 'amount', 'date', 'for_plan', 'is_directly', 'note']
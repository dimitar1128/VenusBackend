import logging
from rest_framework.response import Response
from rbasis.views import *
from operator import itemgetter
from VenusBackend.database.venus.models import *
from VenusBackend.database.venus.serializers import *

#***********************************************************************************
# ------------------------ @Class: Payment Api ------------------------
#-----------------------------------------------------------------------------------
class Payment(ShAPIView):
    queryset = tbl_payment.objects.all()
    serializer_class = tbl_payment_serializer

    # ***********************************************************************************
    # @Function: [GET]
    # @Return: Get Payment List
    # -----------------------------------------------------------------------------------
    def list(self, request, *args, **kwargs):
        payment_list = super().list(request, *args, **kwargs).data
        res = []
        for payment in payment_list:
            try:
                payment['project_name'] = tbl_project.objects.get(id=payment['project_id']).name
                res.append(payment)

            except Exception as e:
                logging.error(str(e))
                continue

        res = sorted(res, key=itemgetter('date'), reverse=True)
        return Response(res, status=200)

    # ***********************************************************************************
    # @Function: [GET]
    # @Return: Get Payment
    # -----------------------------------------------------------------------------------
    def retrieve(self, request, *args, **kwargs):
        payment = super().retrieve(request, *args, **kwargs).data
        payment['project_name'] = tbl_project.objects.get(id=payment['project_id']).name

        return Response(payment, status=200)

    # ***********************************************************************************
    # @Function: [POST]
    # @Return: Create Payment
    # -----------------------------------------------------------------------------------
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    # ***********************************************************************************
    # @Function: [PUT]
    # @Return: Update Payment
    # -----------------------------------------------------------------------------------
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    # ***********************************************************************************
    # @Function: [DELETE]
    # @Return: Delete Payment
    # -----------------------------------------------------------------------------------
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
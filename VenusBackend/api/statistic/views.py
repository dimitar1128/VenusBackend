import logging
import datetime
import calendar

from rest_framework.response import Response
from rbasis.views import *

from django.contrib.auth import authenticate
from django.db.models import Sum

from VenusBackend.database.venus.models import *
from VenusBackend.database.venus.serializers import *


def add_months(sourcedate, months):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day, calendar.monthrange(year,month)[1])
    return datetime.date(year, month, day)

#***********************************************************************************
# ------------------------ @Class: Statistic Api ------------------------
#-----------------------------------------------------------------------------------
class Statistic(ShAPIView):
    queryset = tbl_project.objects.all()
    serializer_class = tbl_project_serializer

    # ***********************************************************************************
    # @Function: [POST]
    # @Return: Status Code
    # -----------------------------------------------------------------------------------
    def create(self, request, *args, **kwargs):
        try:
            type = int(request.data['type'])
            if type == 1:
                res = {}
                cur_date = datetime.datetime.now().date()
                start_date = cur_date.replace(cur_date.year, cur_date.month, 1)
                end_date = cur_date.replace(cur_date.year, cur_date.month, calendar.monthrange(cur_date.year, cur_date.month)[1])
                res['this_month'] = tbl_payment.objects.filter(date__gte=start_date, date__lte=end_date, for_plan=1).aggregate(Sum('amount'))['amount__sum']
                if res['this_month'] == None:
                    res['this_month'] = 0
                res['this_month'] = round(res['this_month'], 2)
                plan = 5000
                res['this_month_percent'] = round(res['this_month']/plan*100, 2)

                res['all'] = tbl_payment.objects.filter(for_plan=1).aggregate(Sum('amount'))['amount__sum']
                if res['all'] == None:
                    res['all'] = 0
                res['all'] = round(res['all'], 2)

                res['months'] = []
                start_date = datetime.date(2019, 8, 1)
                while start_date <= cur_date:
                    end_date = start_date.replace(start_date.year, start_date.month, calendar.monthrange(start_date.year, start_date.month)[1])
                    sum = tbl_payment.objects.filter(date__gte=start_date, date__lte=end_date, for_plan=1).aggregate(Sum('amount'))['amount__sum']
                    if sum == None:
                        sum = 0
                    sum = round(sum, 2)
                    res['months'].append({
                        'month': start_date.strftime('%Y-%m'),
                        'score': sum
                    })
                    start_date = add_months(start_date, 1)

                res['average'] = 0
                i = len(res['months']) - 2
                sum = 0
                while i > len(res['months']) - 8:
                    sum += res['months'][i]['score']
                    i -= 1

                res['average'] = round(sum/6, 2)

                return Response(res, status=200)

            raise Exception()

        except Exception as e:
            logging.error(str(e))
            return Response({}, status=500)

    # ***********************************************************************************
    # @Function: [GET]
    # @Return: Method Not Allowed
    # -----------------------------------------------------------------------------------
    def list(self, request, *args, **kwargs):
        return Response([], status=405)

    # ***********************************************************************************
    # @Function: [PUT]
    # @Return: Method Not Allowed
    # -----------------------------------------------------------------------------------
    def retrieve(self, request, *args, **kwargs):
        return Response([], status=405)

    # ***********************************************************************************
    # @Function: [PUT]
    # @Return: Method Not Allowed
    # -----------------------------------------------------------------------------------
    def update(self, request, *args, **kwargs):
        return Response([], status=405)

    # ***********************************************************************************
    # @Function: [DELETE]
    # @Return: Method Not Allowed
    # -----------------------------------------------------------------------------------
    def destroy(self, request, *args, **kwargs):
        return Response([], status=405)
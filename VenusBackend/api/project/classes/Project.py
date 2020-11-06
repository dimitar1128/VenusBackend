import logging
from rest_framework.response import Response
from rbasis.views import *
from django.db.models import Sum

from VenusBackend.database.venus.models import *
from VenusBackend.database.venus.serializers import *

#***********************************************************************************
# ------------------------ @Class: Project Api ------------------------
#-----------------------------------------------------------------------------------
class Project(ShAPIView):
    queryset = tbl_project.objects.all()
    serializer_class = tbl_project_serializer

    # ***********************************************************************************
    # @Function: [GET]
    # @Return: Get Project List
    # -----------------------------------------------------------------------------------
    def list(self, request, *args, **kwargs):
        project_list = super().list(request, *args, **kwargs).data
        for project in project_list:
            project['cost'] = tbl_payment.objects.filter(project_id=project['id']).aggregate(Sum('amount'))['amount__sum']
            if project['cost'] == None:
                project['cost'] = 0
            project['cost'] = round(project['cost'], 2)

        project_list = sorted(project_list, key=itemgetter('cost'), reverse=True)

        return Response(project_list, status=200)


    # ***********************************************************************************
    # @Function: [GET]
    # @Return: Get Project
    # -----------------------------------------------------------------------------------
    def retrieve(self, request, *args, **kwargs):
        project = super().retrieve(request, *args, **kwargs).data
        project['cost'] = tbl_payment.objects.all().aggregate(Sum('amount'))['amount__sum']
        if project['cost'] == None:
            project['cost'] = 0

        return Response(project, status=200)

    # ***********************************************************************************
    # @Function: [POST]
    # @Return: Create Project
    # -----------------------------------------------------------------------------------
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    # ***********************************************************************************
    # @Function: [PUT]
    # @Return: Update Project
    # -----------------------------------------------------------------------------------
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    # ***********************************************************************************
    # @Function: [DELETE]
    # @Return: Delete Project
    # -----------------------------------------------------------------------------------
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
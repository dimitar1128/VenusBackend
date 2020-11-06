import logging
from rest_framework.response import Response
from rbasis.views import *

from django.contrib.auth import authenticate

from VenusBackend.database.venus.models import *
from VenusBackend.database.venus.serializers import *

#***********************************************************************************
# ------------------------ @Class: Login Api ------------------------
#-----------------------------------------------------------------------------------
class Login(ShAPIView):
    queryset = tbl_project.objects.all()
    serializer_class = tbl_project_serializer

    # ***********************************************************************************
    # @Function: [POST]
    # @Return: Status Code
    # -----------------------------------------------------------------------------------
    def create(self, request, *args, **kwargs):
        try:
            user = authenticate(username=request.data['email'], password=request.data['password'])
            if user == None:
                raise Exception('Invalid credentials')

            return Response({}, status=200)

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
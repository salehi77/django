from rest_framework import views
from rest_framework.response import Response
from . import models, serializers


class DocumentCreateView(views.APIView):

    def get(self, request, *args, **kwargs):
        queryset = models.Document.objects.all()
        serializer = serializers.DocumentSerializer(queryset, many=True)
        return Response(serializer.data)


    def post(self, request, *args, **kwargs):
        serializer = serializers.DocumentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

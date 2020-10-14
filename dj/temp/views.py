from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST


class IndexView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        # print(dir(request))

        # return Response({'lll': 'iii'}, HTTP_400_BAD_REQUEST)
        return Response({'lll': 'iii'}, HTTP_200_OK)

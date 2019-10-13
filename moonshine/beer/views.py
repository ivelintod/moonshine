from django.shortcuts import render
from django.shortcuts import get_object_or_404


from rest_framework import views
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

from beer.models import BeerModel
from beer.serializers import BeerModelSerializer

from beer.models import WhiskeyModel
from beer.serializers import WhiskeyModelSerializer


class BeerDetail(views.APIView):

    serializer_class = BeerModelSerializer

    def get(self, *args, pk=None):
        """
            Method:             GET
            Url:                /api/beer/pk/
            Request headers:
                                {
                                    "Content-Type": "application/json",
                                    "Accept": "application/json",
                                }
            Request body:       None
            Response:
                                {
                                    beer.object.dict
                                }
        """
        try:
            beer = BeerModel.objects.get(id=pk)
            beer_serializer = self.serializer_class(beer)

            return Response(
                beer_serializer.data,
                status=status.HTTP_200_OK)

        except Exception as ex:

            return Response(
                {
                    'message': str(ex)
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request, *args, **kwargs):
        """
            Method:             POST
            Url:                /api/beer/
            Request headers:
                                {
                                    "Content-Type": "application/json",
                                    "Accept": "application/json",
                                }
            Request body:       {
                                    **beer_attributes
                                }
            Response Success:
                                {
                                    beer.object.dict
                                }

            Response Error:
                                {
                                    serializer.errors
                                }
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Should be in a separate app but too much
# boilerplate code for such small stuff
class WhiskeyViewSet(viewsets.ViewSet):

    serializer_class = WhiskeyModelSerializer

    def list(self, *args):
        queryset = WhiskeyModel.objects.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, *args, pk=None):
        queryset = WhiskeyModel.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

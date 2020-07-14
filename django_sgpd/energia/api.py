from rest_framework import viewsets
from .serializers import MeterSerializer, UebSerializer, ReadingSerializer
from .models import Meter, Ueb, Reading
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response


class MeterViewSet(viewsets.ModelViewSet):
    queryset = Meter.objects.all()
    serializer_class = MeterSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'], name='Get total consumption')
    def consumption_at_month(self, request, pk=None):
        month = request.data['month']
        meter = self.get_object()
        # serializer = MeterSerializer(meter)
        # return Response(serializer,
        #                 status=status.HTTP_200_OK)
        return Response({
            "id": meter.id,
            "name": meter.name,
            "consumption": {
                "month": meter.totalConsumptionAtMonth(month),
                "percentage": meter.consumptionPercentage(month)
            }
        })

    @action(detail=True, methods=['post'], description='Get total \
         consumption at day')
    def consumption_at_day(self, request, pk=None):
        day = request.data['day']
        meter = self.get_object()
        # serializer = MeterSerializer(meter)
        # return Response(serializer,
        #                 status=status.HTTP_200_OK)
        consumption = meter.totalConsumptionAtDay(day)
        return Response({
            "id": meter.id,
            "name": meter.name,
            "consumption": consumption
        })


class UebViewSet(viewsets.ModelViewSet):
    queryset = Ueb.objects.all()
    serializer_class = UebSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['get'], name='Get total consumption')
    def totalconsumption(self, request, pk=None):
        ueb = self.get_object()
        # return Response(serializer,
        #                 status=status.HTTP_200_OK)
        return Response({
            "name": ueb.name,
            "consumption": ueb.totalConsumptionByUEB(pk)
        })


class ReadingViewSet(viewsets.ModelViewSet):
    queryset = Reading.objects.all()
    serializer_class = ReadingSerializer
    permission_classes = [permissions.IsAuthenticated]

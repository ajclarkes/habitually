from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .health import HealthCheck

class HealthView(APIView):
    health_check = HealthCheck()
    
    def get(self, request):
        health_status = self.health_check.get_status()
        return Response(health_status.to_dict())

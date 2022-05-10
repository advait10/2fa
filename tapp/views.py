from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from.util import send_otp


@api_view(['POST'])
def send_otp(request):
    data = request.data

    if data.get('phone_number') is None:
        return Response({
            'status': 400,
            'message': 'phone number required'
        })

    if data.get('password') is None:
        return Response({
            'status': 400,
            'message': 'password required'
        })
    user = User.objects.create(phone_number=data.get('phone_number'),
                               otp=send_otp(data.get('phone_number'))
                               )
    user.set_password = data.get('set_password')
    user.save()
    return Response({'status': 200, 'message': 'otp sent'})
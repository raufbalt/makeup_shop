from django.shortcuts import render
from rest_framework import status, permissions

from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from order.models import Order
from order.serializers import OrderSerializer
from .whatsapp import whatsapp_message


class OrderCreateAPIView(CreateAPIView):
    model = Order
    serializer_class = OrderSerializer
    permission_classes = [permissions.AllowAny]


    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():

            name = request.data['name']
            last_name = request.data['last_name']
            inform = request.data['inform']
            address = request.data['address']
            phone_number = request.data['phone_number']
            product = request.data['product']
            # order_number = request.data['order_number']
            quantity = request.data['quantity']
            price = request.data['price']

            whatsapp_message(name=name, last_name=last_name, inform=inform, address=address, phone_number=phone_number,
                             product=product, quantity=quantity, price=price)

            return Response(data=serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
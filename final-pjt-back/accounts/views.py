# in views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import CartsSerializer
from .models import Carts

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from django.shortcuts import get_object_or_404, get_list_or_404

class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        user = request.user
        data = request.data

        # Update user profile fields (nickname, gender, age)
        if 'nickname' in data:
            user.nickname = data['nickname']
        if 'gender' in data:
            user.gender = data['gender']
        if 'age' in data:
            user.age = data['age']

        # Update password if provided
        if 'newPassword' in data:
            user.set_password(data['newPassword'])

        user.save()

        return Response({'message': 'Profile updated successfully'}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def CartsView(request):
    if request.method == 'GET':
        carts = get_list_or_404(Carts)
        serializer = CartsSerializer(carts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CartsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def cart_detail(request, cart_pk):
    cart = get_object_or_404(Carts, pk=cart_pk)

    if request.method == 'DELETE':
        cart.delete()
        return Response({'message': '상품 삭제가 완료되었습니다.'}, status=status.HTTP_204_NO_CONTENT)
    
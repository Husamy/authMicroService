from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin ,CreateModelMixin
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework import status
from rest_framework.response import Response
from .serializers import UserLoginSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout
from rest_framework.authentication import TokenAuthentication
class UserLoginView(GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        response_data = serializer.validated_data

        return Response(response_data, status=status.HTTP_200_OK)



class UserLogoutView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def post(self, request, *args, **kwargs):
        try:
            request.user.auth_token.delete()
            logout(request)
        except (AttributeError, ObjectDoesNotExist):
            pass
        return Response({'message': 'Successfully logged out.'})











class CustomUserApi(GenericAPIView, CreateModelMixin, ListModelMixin):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)







class PersonalUserAPI(GenericAPIView, RetrieveModelMixin):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# Create your views here.

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serilaizers import UserSerializer
from .models import User, Employee
from rest_framework.exceptions import AuthenticationFailed
import jwt
from django.views.generic import TemplateView
from rest_framework import viewsets
from .serilaizers import EmployeeSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('user not found')
        if not user.check_password(password):
            raise AuthenticationFailed("incorrect password")

        payload = {
            'id': user.id,
            'email': user.email
            # 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            # 'lat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token,
            'message': 'successfully logged in',

        }
        return response


""" class UserView(APIView):
   def get(self, request):
      token = request.COOKIES.get('jwt')
     if not token:
        raise AuthenticationFailed("unauthenticated ")
    try:
        payload = jwt.decode(token, 'secret', algorithm='[HS256]')
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed("unauthenticated !")

    user = User.objects.filter(id=payload['id']).first()
    serializer = UserSerializer(user)
    return Response(serializer.data)"""


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response


class AboutView(TemplateView):
    template_name = "about.html"


def alldetails(request):
    data = User.objects.all()
    # serializer = UserSerializer(data)
    return render(request, 'details.html', {'data': data})


class EmployeemodelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
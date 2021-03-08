from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate,login,logout
import requests
import datetime
import json

from .models import ExtendUser,Subscription,UserSubscripiton,Card,Account,Bank
from .serializer import  UserSerializer,ExtendUserSerializer,UserSubscripitonSerializer
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q

class Signup(APIView) :
    def post(self,request):
        """
        request_body={"password":"archana123","username":"archana",
                      "firstname":"archana","lastname":"patil",
                      "email":"archanapatil@gmail.com",
                      "company":"xyz","address":"pune",
                      "dob":"1991-20-09"}

        """
        user_data = {'password' : request.data['password'],'username' : request.data['username'],\
                     'first_name' : request.data['firstname'],'last_name' : request.data['lastname'],\
                     'email' : request.data['email']}
        extend_user = {'company' : request.data ['company'], 'address' : request.data['address'], 'dob' : request.data['dob']}
        user = User.objects.create_user(**user_data)
        user_serializer = UserSerializer(user)
        extend_user.update({'user' : user.id})
        extend_user_serializer = ExtendUserSerializer(data= extend_user)
        if extend_user_serializer.is_valid(raise_exception=True):
            extend_user_serializer.save()
            extend_user_serializer.data.update(user_serializer.data)
            return Response(extend_user_serializer.data)
        else:
            return Response(extend_user_serializer.errors)

class Login(APIView) :
    def post(self, request, *args, **kwargs):
        """
        requset_bady={"userneme":"archana",
                         "password":"archana123"}

        """
        user = authenticate(username= request.data['username'], password=request.data['password'])
        login(request, user)
        url = requests.post("http://127.0.0.1:8000/api/token/",request.data)
        token = json.loads(url.text)
        response = {"message" : "Successfully Login","token": token}
        return Response(response)

class Logout(APIView) :
    def get(self,request,*args,**kwargs):
        logout(request)
        return Response("Successfully Logout")

class Payment(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        """
        request_body={"sub_id":1,"user_id":1,
                      "card_number":"1234567890987654",
                      "cvv":"350","expiry_date":"2025-12-10",
                      "acc_id":1}
        request_header={"Authorization":"Bearer token"}

        """
        subscribe = Subscription.objects.get(id = request.data['sub_id'])
        card = Card.objects.filter(Q(card_number = request.data['card_number'])& Q(cvv = request.data['cvv']) & Q(expiry_date = request.data['expiry_date'])& \
                                   Q(account_id=request.data['acc_id'])).first()
        if card:
            if card.expiry_date > datetime.date.today():
                account_data = Account.objects.filter(id=card.account_id).first()
                if subscribe.amount < account_data.balance:
                    account_balance = account_data.balance - subscribe.amount
                    r_balance = Account.objects.filter(id = card.account_id).update(balance = account_balance)
                    data={"subscription":subscribe.id,"user":request.data["user_id"],"active":True}
                    user_subscription_serializer = UserSubscripitonSerializer(data=data)
                    if user_subscription_serializer.is_valid(raise_exception=True):
                        user_subscription_serializer.save()
                        return Response("Payment Successfull.")
                else:
                    return Response("OOps....!!!!! Insufficient balance.")
            else:
                return Response("Card validity expired. Please update your card.....")
        else:
            return Response("You have entered wrong details.")
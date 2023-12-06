# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.models import EducationInfo, ExperienceInfo, PersonalInfo
from account.serializers import EducationInfoSerializer, ExperienceInfoSerializer, PersonalInfoSerializer, SkillInfoSerializer, UserPasswordResetSerializer, UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer, UserChangePasswordSerializer
from django.contrib.auth import authenticate
from account.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
# import django.db.models.signals

# generate token manually
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    
class UserRegistrationView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token=get_tokens_for_user(user)
            return Response({'token':token,'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception = True):
            email= serializer.data.get('email')
            password= serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:  
              token=get_tokens_for_user(user)
              return Response({'token':token,'msg':'Login Successful'}, status=status.HTTP_200_OK)
            else:
              return Response({'errors':{'non_field_errors':['Email or Password is not valid']}},status=status.HTTP_404_NOT_FOUND)
          
class UserProfileView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        serializer = UserChangePasswordSerializer(data=request.data, context={'user':request.user})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'password change successfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# class SendPasswordResetEmailView(APIView):
#      renderer_classes = [UserRenderer]
     
#      def post(self,request,format=None):
#         serializer = SendPasswordResetEmailSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             return Response({'msg':'Password reset link send'},status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
             
class UserPasswordResetView(APIView):
     renderer_classes = [UserRenderer] 
     def post(self,request,uid, token, format=None):
       serializer = UserPasswordResetSerializer(data=request.data,context={'uid':uid, 'token':token})
       if serializer.is_valid(raise_exception=True):
             return Response({'msg':'Password reset link send'},status=status.HTTP_200_OK)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
class PersonalInfoView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = PersonalInfoSerializer(data=request.data)
        # print("DEBUG ------>", serializer, request.data)
        if serializer.is_valid(raise_exception=True):
            print("INSIDE IF CONDITION ----------------------->")
            user = serializer.save()
            token=get_tokens_for_user(user)
            return Response({'token':token,'msg':'data inserted'}, status=status.HTTP_201_CREATED)
        print("OUTSIDE IF CONDITION ----------------------->")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdatePersonalInfoView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def put(self,request,pk=None):
        # data=request.data
        user = PersonalInfo.objects.filter(pk=pk).first()
        serializer = PersonalInfoSerializer(user,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Data full updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk=None):
        user = PersonalInfo.objects.filter(pk=pk).first()
        serializer = PersonalInfoSerializer(user,data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Data partially updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EducationInfoView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer =  EducationInfoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token=get_tokens_for_user(user)
            return Response({'token':token,'msg':'data inserted'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UpdateEducationInfoView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def put(self,request,pk=None):
        user = EducationInfo.objects.filter(pk=pk).first()
        serializer = EducationInfoSerializer(user,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Data full updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk=None):
        
        user = EducationInfo.objects.filter(pk=pk).first()
        serializer = EducationInfoSerializer(user,data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Data partially updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ExperienceInfoView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer =  ExperienceInfoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token=get_tokens_for_user(user)
            return Response({'token':token,'msg':'data inserted'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UpdateExperienceInfoView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def put(self,request,pk=None):
        user = ExperienceInfo.objects.filter(pk=pk).first()
        serializer = ExperienceInfoSerializer(user,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Data full updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk=None):
        
        user = ExperienceInfo.objects.filter(pk=pk).first()
        serializer = ExperienceInfoSerializer(user,data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'msg':'Data partially updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SkillInfoView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer =  SkillInfoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token=get_tokens_for_user(user)
            return Response({'token':token,'msg':'data inserted'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
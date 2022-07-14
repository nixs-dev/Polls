from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from polls.models import User, Question, Punishment, UserReport, QuestionReport
from .serializers import UserSerializer, QuestionSerializer, PunishmentSerializer, UserReportSerializer, QuestionReportSerializer


class PrivateUserView(APIView):
    permission_classes = (IsAuthenticated,)
    
    
    def get(self, request):
        user_id = request.query_params.get('user_id')
        users = User.objects.get(id=user_id)
        serializer = UserSerializer(users, many=False)
        
        return Response({"users": serializer.data})
    
    def post(self, request):
        return Response({"r": "Its working"})
        
    def put(self, request):
        return Response({"r": "Its working"})


class PrivateQuestionView(APIView):
    permission_classes = (IsAuthenticated,)
    
    
    def get(self, request):
        questions = None
        all_polls = True if 'poll_id' not in request.query_params else False
        
        if all_polls:
            questions = Question.objects.all()
        else:
            questions = Question.objects.filter(id=request.query_params.get('poll_id'))
            
        serializer = QuestionSerializer(questions, many=True)
        return Response({"polls": serializer.data})
    
    def post(self, request):
        return Response({"r": "Its working"})
        
    def put(self, request):
        return Response({"r": "Its working"})


class PrivateReportView(APIView):
    permission_classes = (IsAuthenticated,)
    
    
    def get(self, response):
        users = UserReport.objects.all()
        questions = QuestionReport.objects.all()
        
        user_serializer = UserReportSerializer(users, many=True)
        question_serializer = QuestionReportSerializer(questions, many=True)
        
        return Response({
            "users": user_serializer.data,
            "questions": question_serializer.data
        })


class PrivatePunishmentView(APIView):
    permission_classes = (IsAuthenticated,)
    
    
    def get(self, response):
        punishments = Punishment.objects.all()
        serializer = PunishmentSerializer(punishments, many=True)
        
        return Response({"punishments": serializer.data})
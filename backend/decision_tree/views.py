from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Program, Subject, Question, Answer
from .serializers import ProgramSerializer, SubjectSerializer, QuestionSerializer, AnswerSerializer

class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

    @action(detail=False, methods=['GET'])
    def available_programs(self, request):
        """Retourne la liste des programmes disponibles"""
        programs = self.get_queryset()
        print(f"Returning {programs.count()} programs")
        for program in programs:
            print(f"- {program.name} ({program.id})")
        serializer = self.get_serializer(programs, many=True)
        return Response(serializer.data)

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

    @action(detail=False, methods=['GET'])
    def by_program(self, request):
        program_id = request.query_params.get('program_id')
        if program_id:
            subjects = Subject.objects.filter(
                program_id=program_id,
                parent_subject=None
            )
            serializer = self.get_serializer(subjects, many=True)
            return Response(serializer.data)
        return Response({"error": "program_id is required"}, status=400)

    @action(detail=True, methods=['GET'])
    def sub_subjects(self, request, pk=None):
        subject = self.get_object()
        sub_subjects = Subject.objects.filter(parent_subject=subject)
        serializer = self.get_serializer(sub_subjects, many=True)
        return Response(serializer.data)

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    @action(detail=False, methods=['GET'])
    def by_subject(self, request):
        subject_id = request.query_params.get('subject_id')
        if subject_id:
            questions = Question.objects.filter(subject_id=subject_id)
            serializer = self.get_serializer(questions, many=True)
            return Response(serializer.data)
        return Response({"error": "subject_id is required"}, status=400)

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    @action(detail=False, methods=['GET'])
    def by_question(self, request):
        question_id = request.query_params.get('question_id')
        if question_id:
            answers = Answer.objects.filter(question_id=question_id)
            serializer = self.get_serializer(answers, many=True)
            return Response(serializer.data)
        return Response({"error": "question_id is required"}, status=400)

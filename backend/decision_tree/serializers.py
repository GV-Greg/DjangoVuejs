from rest_framework import serializers
from .models import Program, Subject, Question, Answer

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    
    class Meta:
        model = Question
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    sub_subjects = serializers.SerializerMethodField()
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Subject
        fields = '__all__'

    def get_sub_subjects(self, obj):
        return SubjectSerializer(obj.sub_subjects.all(), many=True).data

class ProgramSerializer(serializers.ModelSerializer):
    subjects = serializers.SerializerMethodField()

    class Meta:
        model = Program
        fields = '__all__'

    def get_subjects(self, obj):
        root_subjects = obj.subjects.filter(parent_subject=None)
        return SubjectSerializer(root_subjects, many=True).data

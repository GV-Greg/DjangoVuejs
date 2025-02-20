from django.contrib import admin
from .models import Subject, Question, Answer, Program

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'version', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_display_links = ('name',)

    def get_list_display(self, request):
        return [
            ('name', 'Nom'),
            ('version', 'Version'),
            ('created_at', 'Date de création'),
            ('updated_at', 'Date de modification')
        ]

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'program', 'parent_subject', 'order', 'created_at')
    list_filter = ('program', 'parent_subject')
    search_fields = ('title', 'description')
    ordering = ('order', 'title')
    list_display_links = ('title',)

    def get_list_display(self, request):
        return [
            ('title', 'Titre'),
            ('program', 'Programme'),
            ('parent_subject', 'Sujet parent'),
            ('order', 'Ordre'),
            ('created_at', 'Date de création')
        ]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'subject', 'order', 'created_at')
    list_filter = ('subject',)
    search_fields = ('text',)
    ordering = ('order', 'id')
    list_display_links = ('text',)

    def get_list_display(self, request):
        return [
            ('text', 'Texte'),
            ('subject', 'Sujet'),
            ('order', 'Ordre'),
            ('created_at', 'Date de création')
        ]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'text', 'order', 'created_at')
    list_filter = ('question',)
    search_fields = ('text', 'documentation_text')
    ordering = ('order', 'id')
    list_display_links = ('text',)

    def get_list_display(self, request):
        return [
            ('question', 'Question'),
            ('text', 'Texte'),
            ('order', 'Ordre'),
            ('created_at', 'Date de création')
        ]

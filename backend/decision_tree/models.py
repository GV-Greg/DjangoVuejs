from django.db import models
from django.utils import timezone

class Program(models.Model):
    name = models.CharField(max_length=200, verbose_name='nom')
    description = models.TextField(verbose_name='description')
    version = models.CharField(max_length=50, verbose_name='version')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='date de création')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='date de modification')

    def __str__(self):
        return f"{self.name} - v{self.version}"

    class Meta:
        verbose_name = 'Programme'
        verbose_name_plural = 'Programmes'

class Subject(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='subjects', verbose_name='programme')
    title = models.CharField(max_length=200, verbose_name='titre')
    description = models.TextField(blank=True, default='', verbose_name='description')
    parent_subject = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='sub_subjects', verbose_name='sujet parent')
    order = models.IntegerField(default=0, verbose_name='ordre')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='date de création')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='date de modification')

    def __str__(self):
        return f"{self.program.name} - {self.title}"

    class Meta:
        ordering = ['order', 'title']
        verbose_name = 'Sujet'
        verbose_name_plural = 'Sujets'

class Question(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='questions', verbose_name='sujet')
    text = models.TextField(verbose_name='texte')
    order = models.IntegerField(default=0, verbose_name='ordre')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='date de création')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='date de modification')

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers', verbose_name='question')
    text = models.TextField(verbose_name='texte')
    documentation_url = models.URLField(blank=True, default='', verbose_name='URL de documentation')
    documentation_text = models.TextField(blank=True, default='', verbose_name='texte de documentation')
    order = models.IntegerField(default=0, verbose_name='ordre')
    created_at = models.DateTimeField(default=timezone.now, verbose_name='date de création')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='date de modification')

    def __str__(self):
        return f"Réponse à : {self.question.text[:50]}..."

    class Meta:
        ordering = ['order', 'id']
        verbose_name = 'Réponse'
        verbose_name_plural = 'Réponses'

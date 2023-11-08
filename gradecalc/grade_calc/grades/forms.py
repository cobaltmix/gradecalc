from django import forms
from .models import StudentGrade

class SemesterFind(forms.ModelForm):
    class Meta:
        model = StudentGrade
        fields = ['quarter_1_grade', 'quarter_1_weight', 'quarter_2_grade', 'quarter_2_weight', 'semester_exam_grade_1', 'semester_exam_weight_1']
        widgets = {
            'quarter_1_grade': forms.NumberInput(attrs={'id': 'form_quarter_1_grade', 'step': "0.01"}),
            'quarter_2_grade': forms.NumberInput(attrs={'id': 'form_quarter_2_grade', 'step': "0.01"}),
            'quarter_1_weight': forms.NumberInput(attrs={'id': 'form_quarter_1_weight', 'step': "0.01"}),
            'quarter_2_weight': forms.NumberInput(attrs={'id': 'form_quarter_2_weight', 'step': "0.01"}),
            'semester_exam_grade_1': forms.NumberInput(attrs={'id': 'form_semester_exam_grade_1', 'step': "0.01"}),
            'semester_exam_weight_1': forms.NumberInput(attrs={'id': 'form_semester_exam_weight_1', 'step': "0.01"}),
        }

class DesireSemester(forms.ModelForm):
    class Meta:
        model = StudentGrade
        fields = ['quarter_1_grade', 'quarter_1_weight', 'quarter_2_grade', 'quarter_2_weight', 'semester_exam_weight_1', 'desired_grade']
        widgets = {
            'quarter_1_grade': forms.NumberInput(attrs={'id': 'form_quarter_1_grade', 'step': "0.01"}),
            'quarter_1_weight': forms.NumberInput(attrs={'id': 'form_quarter_1_weight', 'step': "0.01"}),
            'quarter_2_grade': forms.NumberInput(attrs={'id': 'form_quarter_2_grade', 'step': "0.01"}),
            'quarter_2_weight': forms.NumberInput(attrs={'id': 'form_quarter_2_weight', 'step': "0.01"}),
            'semester_exam_weight_1': forms.NumberInput(attrs={'id': 'form_semester_exam_weight_1', 'step': "0.01"}),
            'desired_grade': forms.NumberInput(attrs={'id': 'form_desired_grade', 'step': "0.01"}),
        }

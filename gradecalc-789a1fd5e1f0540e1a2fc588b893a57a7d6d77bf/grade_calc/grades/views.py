from django.shortcuts import render
from .forms import SemesterFind, DesireSemester
from .models import StudentGrade

def calculate_grade(request):
    if request.method == 'POST':
        form = SemesterFind(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            final_grade = (data['quarter_1_grade'] * data['quarter_1_weight'] +
                           data['quarter_2_grade'] * data['quarter_2_weight'] +
                           data['semester_exam_grade_1'] * data['semester_exam_weight_1']) / 100
            final_grade = round(final_grade, 2)
            print("Form Data:", data)
            print("Final Grade:", final_grade)
            return render(request, 'grades/grade_calculator.html', {'form': form, 'final_grade': final_grade})
    else:
        form = SemesterFind()
    return render(request, 'grades/grade_calculator.html', {'form': form})

def calculate_exam_score(request):
    if request.method == 'POST':
        form = DesireSemester(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            quarter_1_grade = data['quarter_1_grade']
            quarter_2_grade = data['quarter_2_grade']
            quarter_1_weight = data['quarter_1_weight']
            quarter_2_weight = data['quarter_2_weight']
            exam_weight_1 = data['semester_exam_weight_1']
            desired_grade = data['desired_grade']
            # Calculate the minimum semester exam score needed
            semester_exam_score_needed = round((((desired_grade)-(quarter_1_grade * (quarter_1_weight/100))-(quarter_2_grade * (quarter_2_weight/100)))/(exam_weight_1/100)),4)
            return render(request, 'grades/exam_score_calculator.html', {'form': form, 'semester_exam_score_needed': semester_exam_score_needed})
    else:
        form = DesireSemester()
    return render(request, 'grades/exam_score_calculator.html', {'form': form})


from django.shortcuts import render
from .models import Student
from datetime import date, time

# Create your views here.

def home(request):
    student_data = Student.objects.all()
    
    # student_data = Student.objects.filter(name__exact='sonam')

    # case insensitive
    # student_data = Student.objects.filter(name__iexact='sonam')

    # student_data = Student.objects.filter(name__contains='u')

    # student_data = Student.objects.filter(id__in=[1,3,5])

    # student_data = Student.objects.filter(marks__gt=60)
    # student_data = Student.objects.filter(marks__gte=60)

    # student_data = Student.objects.filter(marks__lt=50)
    # student_data = Student.objects.filter(marks__lte=50)

    # student_data = Student.objects.filter(name__startswith='s')
    # student_data = Student.objects.filter(name__iendswith='l')

    # student_data = Student.objects.filter(passdate__range=('2020-04-05','2020-07-18'))

    # student_data = Student.objects.filter(admdatetime__date=date(2017,1,8))
    
    # multiple looksup
    # student_data = Student.objects.filter(admdatetime__date__lt=date(2017,1,8))

    # student_data = Student.objects.filter(passdate__year=2020)
   
    # student_data = Student.objects.filter(passdate__year__gt=2020)

    # student_data = Student.objects.filter(passdate__month=7)

    # student_data = Student.objects.filter(passdate__quarter=3)


   
    print('Return:',student_data)
    print()
    print('SQL Query:', student_data.query)

    return render(request, 'school/home.html', {'students':student_data})
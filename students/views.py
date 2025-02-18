from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Student
from .models import Group




def student_list(request):
    students = Student.objects.all()
    ctx = {'students': students}
    return render(request, 'students/students-list.html', ctx)

def student_create(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        group_id = request.POST.get('group')
        date_of_birth = request.POST.get('date_of_birth')
        student_phone = request.POST.get('student_phone')
        address = request.POST.get('address')
        photo = request.FILES.get('photo')
        if full_name and group_id and date_of_birth and student_phone and address and photo:
            group = get_object_or_404(Group, pk=group_id)
            Student.objects.create(
                full_name=full_name,
                group=group,
                date_of_birth=date_of_birth,
                student_phone=student_phone,
                address=address,
                photo=photo
            )
            return redirect('students:list')
    return render(request, 'students/student-form.html')

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    ctx = {'student': student}
    return render(request, 'students/student-detail.html', ctx)

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
    ctx = {'student': student}
    return redirect('students/student-delete-confirm.html', ctx)


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        group_id = request.POST.get('group')
        date_of_birth = request.POST.get('date_of_birth')
        student_phone = request.POST.get('student_phone')
        address = request.POST.get('address')
        photo = request.FILES.get('photo')
        if full_name and group_id and date_of_birth and student_phone and address and photo:
            student.group = get_object_or_404(Group, pk=group_id)
            student.full_name = full_name
            student.date_of_birth = date_of_birth
            student.student_phone = student_phone
            student.address = address
            if photo:
                student.photo = photo
            student.save()
            return redirect(reverse('student:detail', args=[student.pk]))
    ctx = {'student': student}
    return render(request, 'students/student-form.html', ctx)









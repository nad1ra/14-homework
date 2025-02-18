from django.shortcuts import render, redirect, get_object_or_404
from subjects.models import Subject
from .models import Teacher


def teacher_list(request):
    teachers = Teacher.objects.all()
    ctx = {'teachers': teachers}
    return render(request, 'teachers/teachers-list.html', ctx)

def teacher_create(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        teacher_phone = request.POST.get('teacher_phone')
        subject_id = request.POST.get('subject')
        teacher_email = request.POST.get('teacher_email')
        work_experience = request.POST.get('work_experience')
        image = request.FILES.get('image')
        print(first_name, last_name, teacher_email, teacher_phone, subject_id, work_experience, image)
        if first_name and last_name and teacher_phone and subject_id and teacher_email and work_experience and image:
            subject = Subject.objects.get(pk=subject_id)
            Teacher.objects.create(
                first_name=first_name,
                last_name=last_name,
                subject=subject,
                teacher_phone=teacher_phone,
                teacher_email= teacher_email,
                work_experience=work_experience,
                image=image,
            )
            return redirect('teachers:list')
    subjects = Subject.objects.all()
    ctx = {'subjects': subjects}
    return render(request, 'teachers/teacher-form.html', ctx)

def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    ctx = {'teacher': teacher}
    return render(request, 'teachers/teacher-detail.html', ctx)

def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teachers:list')
    ctx = { 'teacher': teacher }
    return render(request, 'teachers/teacher-delete-confirm.html', ctx)


def teacher_update(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    subjects = Subject.objects.all()
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        teacher_phone = request.POST.get('teacher_phone')
        subject_id = request.POST.get('subject')
        teacher_email = request.POST.get('teacher_email')
        work_experience = request.POST.get('work_experience')
        image = request.FILES.get('image')

        if (first_name and last_name and teacher_phone and subject_id and
                teacher_email and work_experience):
            try:
                subject = Subject.objects.get(pk=subject_id)
                teacher.subject = subject
            except Subject.DoesNotExist:
                return redirect('teachers:update', pk=pk)
            teacher.first_name = first_name
            teacher.last_name = last_name
            teacher.teacher_phone = teacher_phone
            teacher.teacher_email = teacher_email
            teacher.work_experience = work_experience
            if image:
                teacher.image = image

            teacher.save()
            return redirect('teachers:detail', pk=teacher.pk)

    ctx = {'teacher': teacher, 'subjects': subjects,}
    return render(request, 'teachers/teacher-form.html', ctx)










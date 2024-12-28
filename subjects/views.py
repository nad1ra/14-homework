from django.shortcuts import render, redirect, get_object_or_404
from .models import Subject


def home(request):
    return render(request, 'index.html')

def subject_list(request):
    subjects = Subject.objects.all()
    ctx = {'subjects': subjects}
    return render(request, 'subjects/subjects-list.html', ctx)

def subject_create(request):
    if request.method == 'POST':
        subject_name = request.POST.get('subject_name')
        if subject_name:
            Subject.objects.create(
                subject_name=subject_name
            )
            return redirect('subjects:list')
    return render(request, 'subjects/subject-form.html')

def subject_detail(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    ctx = {'subject', subject}
    return render(request, 'subjects/subject-detail.html', ctx)

def subject_delete(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    subject.delete()
    return redirect('subjects:list')


def subject_update(request, pk):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        subject_name = request.POST.get('subject_name')
        if subject_name:
            subject.subject_name = subject_name
            subject.save()
            return redirect(subject.get_detail_url())
    ctx = {'subject': subject}
    return render(request, 'subjects/subject-form.html', ctx)









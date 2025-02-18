from django.shortcuts import render, redirect, get_object_or_404

from teachers.models import Teacher
from .models import Group

def groups_list(request):
    groups = Group.objects.all()
    ctx = {'groups': groups}
    return render(request, 'groups/groups-list.html', ctx)

def group_create(request):
    teachers = Teacher.objects.all()
    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        class_teacher_id = request.POST.get('class_teacher')
        if group_name and class_teacher_id:
            class_teacher = Teacher.objects.get(pk=class_teacher_id)
            if class_teacher:
                Group.objects.create(
                    group_name=group_name,
                    class_teacher=class_teacher
                )
                return redirect('groups:list')
            else:
                error_message = "Bunday o'qituvchi mavjud emas"
    ctx = {'teachers': teachers}
    return render(request, 'groups/group-form.html', ctx)

def group_detail(request, pk):
    group = get_object_or_404(Group, pk=pk)
    ctx = {'group', group}
    return render(request, 'groups/group-detail.html', ctx)

def group_delete(request, pk):
    group = get_object_or_404(Group, pk=pk)
    group.delete()
    return redirect('groups:list')


def group_update(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        class_teacher = request.POST.get('class_teacher')
        if group_name and class_teacher:
            group.group_name = group_name
            group.class_teacher = class_teacher
            group.save()
            return redirect(group.get_detail_url())
    ctx = {'group': group}
    return render(request, 'groups/group-form.html', ctx)









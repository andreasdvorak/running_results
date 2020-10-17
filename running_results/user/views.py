from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserForm
from .models import User


def user_create_view(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = UserForm()
    context = {
        'form': form
    }
    return render(request, "user/user_create.html", context)


def user_update_view(request, id=id):
    obj = get_object_or_404(User, id=id)
    form = UserForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "user/user_create.html", context)


def user_list_view(request):
    queryset = User.objects.all() # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "user/user_list.html", context)

def user_detail_view(request, id):
    obj = get_object_or_404(User, id=id)
    context = {
        "object": obj
    }
    return render(request, "user/user_detail.html", context)


def user_delete_view(request, id):
    obj = get_object_or_404(User, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "user/user_delete.html", context)
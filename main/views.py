import django.contrib.auth
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Question, My_Course, Profile

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .forms import RegisterForm
from django.core.mail import send_mail


def home(request):
    return render(request, "my_site_front/home_page.html")


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            return redirect('login_page')

    else:
        return render(request, "my_site_front/login_page.html")


def register_page(request):
    if request.method == "GET":
        form1 = RegisterForm()
        return render(request, "my_site_front/register_page.html", {"form": form1})
    elif request.method == "POST":
        form1 = RegisterForm(data=request.POST)
        if form1.is_valid():
            username = form1.cleaned_data.get('username')
            email = form1.cleaned_data.get('email')
            password = form1.cleaned_data.get('password')
            first_name = form1.cleaned_data.get('first_name')
            last_name = form1.cleaned_data.get('last_name')
            user = User(username=username, email=email, first_name=first_name, last_name=last_name)
            user.set_password(password)
            user.save()
            login(request, user)
            new_profile = Profile(gender="", bio="", user=user)
            new_profile.save()
            return redirect('home_page')
        else:
            return render(request, "my_site_front/register_page.html", {"form": form1})


@login_required()
def log_out(request):
    logout(request)
    return redirect('home_page')


def contact_us(request):
    if request.method == "POST":
        email = request.POST.get('email')
        content = request.POST.get('text_content')
        content = content + "  from:" + str(email)
        send_mail(
            "join in contact_us_page",
            content,
            email,
            ['danial.erfanian@divar.ir'],
        )
        return render(request, "my_site_front/adds.html")

    else:
        return render(request, "my_site_front/contact_us.html")


@login_required()
def profile(request):
    user_profile = Profile.objects.get(user_id=request.user.id)
    return render(request, "my_site_front/profile.html", {"profile": user_profile})


@login_required()
def setting_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        bio = request.POST.get('bio')
        user_profile = Profile.objects.get(user_id=request.user.id)
        user_profile.bio = bio
        user_profile.gender = gender
        user_profile.save()
        if len(first_name) != 0:
            request.user.first_name = first_name
        if len(last_name) != 0:
            request.user.last_name = last_name
        request.user.save()
        return redirect('profile')

    else:
        user_profile = Profile.objects.get(user_id=request.user.id)
        return render(request, "my_site_front/setting_page.html", {"profile": user_profile})


@login_required()
def panel(request):
    return render(request, "my_site_front/panel.html")


@login_required()
@user_passes_test(lambda u: u.is_superuser)
def make_new_course(request):
    if request.method == "GET":
        return render(request, "my_site_front/make_new_course.html")
    else:
        name = request.POST.get('name')
        department = request.POST.get('department')
        course_number = request.POST.get('course_number')
        group_number = request.POST.get('group_number')
        teacher_name = request.POST.get('teacher_name')
        s_time = request.POST.get('start_time')
        e_time = request.POST.get('end_time')
        first_day = request.POST.get('first_day')
        second_day = request.POST.get('second_day')
        new_course = My_Course(name=name, number=course_number, group_number=group_number, teacher=teacher_name
                               , start_time=s_time, end_time=e_time, first_day=first_day, second_day=second_day,
                               user=request.user, department=department)
        new_course.save()
        return redirect('courses')


@login_required()
def courses(request):
    my_c = My_Course.objects.filter(user_id=request.user.id)
    return render(request, "my_site_front/courses.html", {"courses": my_c})


def search(request):
    if request.method == "POST":
        text = request.POST.get('search')
        teachers = User.objects.filter(is_superuser=True)
        ans = teachers.filter(
            Q(first_name__contains=text) | Q(last_name__contains=text) | Q(username__contains=text))
        if len(ans) != 0:
            return render(request, "my_site_front/find_teacher.html", {"teachers": ans})
        else:
            return render(request, "my_site_front/not_found_page.html", {"teachers": ans})

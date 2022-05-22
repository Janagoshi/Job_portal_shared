# from django.shortcuts import render
from django.views.generic import CreateView, ListView, TemplateView
# import jobp.models as models
from . import models
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


class IndexView(TemplateView):
    template_name = "index.html"


class TeacherCreateView(PermissionRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = "jobp.add_teacher"
    model = models.Teacher
    template_name = "teacher/teacher_create.html"
    fields = ["name", "language", "location", "city", "level", "price", "about_me", "email"]
    success_url = reverse_lazy("index")
    success_message = "Data was updated successfully."


class TeacherUpdateView(PermissionRequiredMixin, LoginRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = "jobp.change_teacher"
    model = models.Teacher
    template_name = "teacher/teacher_update.html"
    fields = ["name", "language", "location", "level", "price", "about_me", "email"]
    success_url = reverse_lazy("index")
    success_message = "Data was updated successfully."


class TeacherListView(ListView):
    model = models.Teacher
    template_name = "teacher/teacher_list.html"
    fields = ["name", "language", "location", "city", "price", "level", "about_me", "email"]
    success_url = reverse_lazy("index")


class LocationListView(ListView):
    template_name = "location/location_list.html"
    fields = ["location", "city"]
    model = models.Teacher

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["test"] = "ahoj!"
        context["location"] = models.Teacher.objects.all()
        return context

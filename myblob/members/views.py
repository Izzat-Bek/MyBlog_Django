from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, UpdateForm, CreatePageForm
from blog.models import Profile


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserUpdateView(generic.UpdateView):
    form_class = UpdateForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        # users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context["page_user"] = page_user
        return context


class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    success_url = reverse_lazy('home')
    # fields = ['bio', 'profile_pic', 'website_url', 'facebook_url', 'instagram_url', 'twitter_url', 'github_url']
    form_class = CreatePageForm


class CreateProfilePageView(CreateView):
    model = Profile
    template_name = "registration/create_user_profile_page.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    form_class = CreatePageForm
    # fields = ('bio', 'profile_pic', 'website_url', 'facebook_url', 'instagram_url', 'twitter_url', 'github_url')

    success_url = reverse_lazy('home')


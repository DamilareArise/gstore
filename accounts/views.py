from django.shortcuts import render, redirect
from django.views import generic
from .forms import UserCreationForm, SignupForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserForm, ProfileForm

# Create your views here.

class SignupView(generic.CreateView):
    form_class = SignupForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
    
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
    
# def signupview(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
            
#         return redirect('login')
#     else:
#         form = UserCreationForm()
#         return render(
#             request,
#             template_name="registration/signup.html",
#             context={
#                 "form": form
#             }
#         )


@login_required
def userProfileView(request):
    user = request.user
    profile = UserProfile.objects.get(user=user)
    
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect("profile")
    
    else:
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=profile)
    
        return render(
            request,
            template_name="accounts/profile.html",
            context={
                "profile": profile,
                "user_form": user_form,
                "profile_form": profile_form
            }
        )
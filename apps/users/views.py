from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy, reverse
from rolepermissions.roles import assign_role


from django.contrib import messages
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.views.generic import UpdateView,DetailView

from . form import RegisterForm,UpdateForm
from . models import User
# Create your views here.
class Home(LoginRequiredMixin, TemplateView):
    template_name = "users/dashboard.html"


class Register(View):
    form_class = RegisterForm
    initial = {"key": "value"}
    template_name = "users/register.html"

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': self.form_class})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            typeUser = form.cleaned_data.get("typeUser")
            email = form.cleaned_data.get("email")
            user = User.objects.get(email=email)
            if typeUser == "secretary":
                assign_role(user,'secretary')
            if typeUser == "coordinator":
                assign_role(user,'coordinator')
            if typeUser == "asg":
                assign_role(user,'asg')
            if typeUser == "food_divider":
                assign_role(user,'fooddivider')
            if typeUser == "nutricionist":
                assign_role(user,'nutricionist')
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}")
            return redirect(to="/")
        return render(request, self.template_name, {'form': form})


class MyLoginView(LoginView):
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("dashboard")

    def form_invalid(self, form):
        messages.error(self.request, "Inválido Login e Senha.")
        return self.render_to_response(self.get_context_data(form=form))

class LogoutView(View):
    def get(self, request):
        logout(request)
        return reverse("login")

class DetailPerfil(LoginRequiredMixin,DetailView):
    model = User
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid'
    context_object_name = 'user'
    

class UpdatePerfil(LoginRequiredMixin,UpdateView):
    model = User
    slug_url_kwarg = 'uuid'
    slug_field = 'uuid'
    form_class = UpdateForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['uuid'] = self.kwargs.get('uuid')
        return context



    success_url = reverse_lazy("dashboard")
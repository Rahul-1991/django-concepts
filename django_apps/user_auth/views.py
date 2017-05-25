from django.views.generic import CreateView
from .forms import UserCreateForm
from django.core.urlresolvers import reverse_lazy


class SignUp(CreateView):

    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'user_auth/signup.html'


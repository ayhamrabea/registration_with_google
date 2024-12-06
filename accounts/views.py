from django.shortcuts import render , redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login , logout
from .forms import CreateUserForm 
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    return render(request,'index.html')


def log_out(request):
    logout(request)
    return redirect('login')

class RegesterView(CreateView):
    form_class = CreateUserForm
    template_name = 'registration/singup.html'


    def get_success_url(self) :
        login(self.request,self.object)
        return reverse_lazy('home')
    
# @login_required
# def edit_profile(request):
#     if request.method == "POST":
#         form = ProfileForm(request.POST , instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = ProfileForm(instance=request.user)
#         return render(request,'profile.html',{'form':form})
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ProjectsForm
from .models import Projects,Profile

# Create your views here.
@login_required (login_url='/accounts/login/')
def index(request):
    if request.method == "POST":
        form = ProjectsForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
    else:
        form = ProjectsForm()

    return render(request, 'index.html', {'form': form})

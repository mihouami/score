from django.shortcuts import render, redirect
from .models import Score
from .forms import ScoreForm

# Create your views here.
def index(request):
    form = ScoreForm()
    context = {"title":'Index',
               "scores":Score.objects.all(),
    }
    if request.method == "POST":
        if 'save' in request.POST:
            pk = request.POST['save']
            if not pk:
                form = ScoreForm(request.POST)
            else:
                score = Score.objects.get(id=pk)
                form = ScoreForm(request.POST, instance=score)
            if form.is_valid():
                form.save()
                return redirect('index')
        elif 'delete' in request.POST:
            pk = request.POST.get('delete')
            score = Score.objects.get(id=pk)
            score.delete()
        elif 'update' in request.POST:
            pk = request.POST.get('update')
            score = Score.objects.get(id=pk)
            form = ScoreForm(instance=score)
        elif 'cancel' in request.POST:
            return redirect('index')
    context['form']=form
    return render(request, 'crud/index.html', context)

def about(request):
    context = {"title":'About'}

    return render(request, 'crud/about.html', context)

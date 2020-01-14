from django.shortcuts import render
from .models import Image,Location,tags, Profile,Projects,NewsLetterRecipients
from django.http import HttpResponseRedirect
from .email import send_welcome_email

# Create your views here.
# def welcome(request):
#     return render(request, 'index.html')
    
def home_projects (request):
    
    if request.GET.get('search_term'):
        projects = Projects.search_project(request.GET.get('search_term'))
    else:
        projects = Projects.objects.all()

    form = NewsLetterRecipients

    if request.method == 'POST':
        form = NewsLetterForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = NewsLetterRecipients(name=name, email=email)
            recipient.save()
            send_welcome_email(name, email)

            HttpResponseRedirect('home_projects')

    return render(request, 'index.html', {'projects':projects, 'letterForm':form})


def search_projects(request):

    if 'projects' in request.GET and request.GET["Project"]:
        search_term = request.GET.get("Projects")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"Projects": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
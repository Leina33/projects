from django.shortcuts import render
from django.http import HttpResponseRedirect


# Create your views here.
# def welcome(request):
#     return render(request, 'index.html')
    
def home_projects (request):
    

    return render(request, 'index.html')

def search_results(request):

    if 'projects' in request.GET and request.GET["Project"]:
        search_term = request.GET.get("Projects")
        searched_articles = Article.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"Projects": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})
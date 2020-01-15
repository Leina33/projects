from django.shortcuts import render
from .models import Image,Location,tags, Profile,Projects,NewsLetterRecipients,Like
from django.http import HttpResponseRedirect
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# from .forms import NewsLetterForm

# Create your views here.
# def welcome(request):
#     return render(request, 'index.html')
@login_required(login_url='/accounts/login/')    
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
    
    
    
def project(request, id):

    try:
        project = Project.objects.get(pk = id)

    except DoesNotExist:
        raise Http404()

    current_user = request.user
    comments = Review.get_comment(Review, id)
    latest_review_list=Review.objects.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            design_rating = form.cleaned_data['design_rating']
            content_rating = form.cleaned_data['content_rating']
            usability_rating = form.cleaned_data['usability_rating']
            comment = form.cleaned_data['comment']
            review = Review()
            review.project = project
            review.user = current_user
            review.comment = comment
            review.design_rating = design_rating
            review.content_rating = content_rating
            review.usability_rating = usability_rating
            review.save()

    else:
        form = ReviewForm()

        # return HttpResponseRedirect(reverse('image', args=(image.id,)))

    return render(request, 'image.html', {"project": project,
                                          'form':form,
                                          'comments':comments,
                                          'latest_review_list':latest_review_list})




##################################Ajax functionalities############################################
def newsletter(request):
    name = request.POST.get('your_name')
    email= request.POST.get('email')

    recipient= NewsLetterRecipients(name= name, email =email)
    recipient.save()
    send_welcome_email(name, email)
    data= {'success': 'You have been successfully added to the newsletter mailing list'}
    return JsonResponse(data)
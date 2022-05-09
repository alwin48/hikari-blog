from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from .models import BlogPost, Profile
from .forms import AddPostForm
from django.contrib.auth.decorators import login_required


# from django.template import Context
# from django.template.loader import render_to_string, get_template
# from django.core.mail import EmailMessage

def index(request):
    """View function for home page of site"""
    num_posts = BlogPost.objects.all().count()
    num_users = Profile.objects.all().count()

    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_posts' : num_posts,
        'num_users' : num_users,
        'num_visits' : num_visits
    }

    # msg = EmailMessage(
    #     'Subject',
    #     'Hi this is testing for main',
    #     'alwinjospeh49@gmail.com',
    #     ['alwinjoseph48@gmail.com'],
    # )
    # msg.content_subtype ="html"# Main content is now text/html
    # msg.send()
    # print("Mail successfully sent")

    return render(request, 'index.html', context=context)

@login_required
def create_post(request):
    if request.method == 'POST':
        print("reached post")
        form = AddPostForm(request.POST, request.FILES)
        print('reached below post')
        form.is_valid()
        title1=form.cleaned_data['title']
        text1=form.cleaned_data['text']
        #date_time1=form.cleaned_data['date_time']
        image1=request.FILES['image_1']
        post = BlogPost.objects.create(title=title1, text=text1, image=image1, author=request.user)
        print("reached here")
        post.save()
        return HttpResponseRedirect(reverse("posts"))

    else :
        form = AddPostForm()
        context = {
            'form' : form,
        }
        return render(request, 'create_post.html', context=context)


class BlogPostListView(generic.ListView):
    model = BlogPost
    context_object_name = 'post_list'
    template_name = 'post_list.html'

class BlogPostDetailView(generic.DetailView):
    model = BlogPost
    template_name = 'post_detail.html'
    context_object_name = 'post'


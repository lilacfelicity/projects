from django.db.models.base import Model
from django.shortcuts import render,get_object_or_404,redirect
#from django.views.generic import DetailView
from .models import Post
from .form import CommentForm
#from django.views.generic import ListView

#class HomePageView(ListView):
    #model = Post
    #template_name = 'home.html'


def main(request):
    return render(request,'base.html', {'title':'Блог-Lilacfelicity'})


def show_post_list(request,slug): 
    posts=Post.objects.all().filter(categorys=slug)
    return render(request,'post/list.html',{'posts':posts})

def show_post(request,slug):
    post=get_object_or_404(Post,slug=slug)
    comments = post.comments.filter(active=True)

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            newcomment = comment_form.save(commit=False)
            # Assign the current post to the comment
            newcomment.post = post
            # Save the comment to the database
            newcomment.save()
    else:
        comment_form = CommentForm()
    return render(request,'post/one_post.html',
    {'post': post, 
    'comments': comments,
     'comment_form': comment_form})

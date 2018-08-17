from django.shortcuts import render, redirect
#from django.http import HttpResponse
from .models import Comment
from .forms import CommentForm

def index(request):
    #return HttpResponse('<h1>Hello Tee</h1>')

    blog_comments = Comment.objects.order_by('-date_added')
    data = {'table' : blog_comments }

    return render(request, 'blog/index.html', data)

def sign(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)

        #This is HTML
        #print(form)

        #print(request.POST)

        if form.is_valid():
            new_comment = Comment(
                name = request.POST['name'],
                comment = request.POST['comment']
            )

            new_comment.save()
            return redirect('index')

    else:
        form = CommentForm()

    context = { 'comment_form': form }

    return render(request, 'blog/sign.html', context)

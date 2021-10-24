from django.shortcuts import render, redirect
from .models import Post, Like

def post_view(request):
    qs = Post.objects.all()
    user = request.user

    context = {
        'qs':qs, 
        'user':user
    }
    return render(request, 'post/main.html', context)



def like_post(request):
    user = request.user
    if request.method=='POST':
        post_id = request.POST.get('post_id')
        print(post_id)
        post_obj = Post.objects.get(id=post_id)
        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)
        like,created = Like.objects.get_or_create(user = user, post_id=post_id)
        print(created)
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        like.save()
    return redirect('post-list')

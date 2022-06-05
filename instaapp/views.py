from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, Http404


@login_required
def index(request):
    images = Image.objects.all()
    comments = Comment.objects.all()
    users = User.objects.exclude(id=request.user.id)
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit = False)
            image.user = request.user.profile
            image.save()
            messages.success(request, f'Successfully uploaded your pic!')
            return redirect('index')
    else:
        form = ImageUploadForm()
    return render(request, 'index.html', {"images":images[::-1], "form": form, "users": users, "comments": comments })
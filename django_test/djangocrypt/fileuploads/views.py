from django.shortcuts import render, redirect
from .models import FileUpload
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def file_list(request):
    file_uploads = FileUpload.objects.all().order_by('date')
    return render(request, 'fileuploads/file_list.html', {'file_uploads':file_uploads})

def file_detail(request,slug):
    # return HttpResponse(slug)
    file_upload = FileUpload.objects.get(slug=slug)
    return render(request, 'fileuploads/file_detail.html', {'file_upload':file_upload})

@login_required(login_url="/accounts/login/")
def fileupload_create(request):
    if request.method == 'POST':
        form = forms.CreateFileUpload(request.POST, request.FILES)
        if form.is_valid():
            # save upload to db
            instance = form.save(commit=False)
            instance.upload_user = request.user
            instance.save()
            return redirect('file_uploads:list')
    else:
        form = forms.CreateFileUpload()
    return render(request, 'fileuploads/fileupload_create.html',{'form':form})
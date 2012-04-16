from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

@login_required
def f_list(request):
    return render_to_response('index.html',{'user':request.user})

@login_required
def f_upload(request):
    return render to response('upload.html',{'form':form})
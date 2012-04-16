from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from files_manager.forms import UploadFileForm
from django.http import HttpResponseRedirect

@login_required
def f_list(request):
    return render_to_response('index.html',{'user':request.user})

@login_required
def f_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        #handle_uploaded_file(request.FILES['file'])
        return HttpResponseRedirect('/upload/success/')
    else:
        form = UploadFileForm()
        c={'form':form}
        c.update(csrf(request))
        return render_to_response('upload.html',c)

def upload_success(request):
    return render_to_response('upload_success.html')
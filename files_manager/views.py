from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from files_manager.forms import UploadFileForm
from django.http import HttpResponseRedirect
from files_manager.file_handling import handle_uploaded_file
from django.template import RequestContext

@login_required
def file_list(request):
    return render_to_response('index.html',{'user':request.user})

@login_required
def file_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['upload_file'],\
                request.POST['category'])
            return HttpResponseRedirect('/view_file/')
    else:
        form = UploadFileForm()
    return render_to_response('upload.html',{'form':form},context_instance=RequestContext(request))

def view_file(request):
    return render_to_response('upload_success.html')
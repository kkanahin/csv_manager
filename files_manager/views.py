from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from files_manager.forms import UploadFileForm
from django.http import HttpResponseRedirect
from files_manager.models import Func_var,Function
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
            added_file=handle_uploaded_file(request.FILES['upload_file'],\
                request.POST['category'])
            return HttpResponseRedirect('/view_file/%s/' % added_file)
    else:
        form = UploadFileForm()
    return render_to_response('upload.html',{'form':form},\
           context_instance=RequestContext(request))

def GetTableValue(id_file):
    result={}
    result['table_value']={get_variable.variable:Function.objects.\
                           filter(variable=get_variable).\
                           values_list('function',flat=True)
                           for get_variable in Func_var.objects.\
                           filter(data=id_file)}
    result['column']=range(1,max([len(val) for val in result['table_value'].\
                     values()])+1)
    return result
    
def view_file(request,file_id):
    template_variables={}
    template_variables['table_value']={get_variable.variable:Function.objects.\
                           filter(variable=get_variable).\
                           values_list('function',flat=True)
                           for get_variable in Func_var.objects.\
                           filter(data=file_id)}
    template_variables['column']=range(1,max([len(val) for val in template_variables['table_value'].\
                     values()])+1)
    return render_to_response('file_view.html',template_variables,\
           context_instance=RequestContext(request))

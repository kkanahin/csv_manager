from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from files_manager.forms import UploadFileForm
from django.http import HttpResponseRedirect,Http404
from files_manager.models import Func_var,Function,CSVData
from files_manager.file_handling import handle_uploaded_file
from django.template import RequestContext
from django.contrib import messages

def file_list(request):
    return render_to_response('index.html',{'user':request.user})

@login_required
def file_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            added_file=handle_uploaded_file(request.FILES['upload_file'],\
                request.POST['category'])
            messages.success(request,'File was uploaded succesfully ')
            return HttpResponseRedirect('/file_view/%s/' % added_file)
    else:
        form = UploadFileForm()
    return render_to_response('upload.html',{'form':form},\
           context_instance=RequestContext(request))

def file_view(request,file_id):
    template_variables={}
    
    template_variables['table_value']={}
    query_result=Function.objects.filter(variable__data=file_id).\
        values('variable','variable__variable','function').order_by('variable')
    if not query_result:
        raise Http404
    template_variables['file_name']=CSVData.objects.values('name_file').\
                                    get(id=file_id)['name_file']
    for fetch_raws in query_result:
       if not fetch_raws['variable'] in template_variables['table_value'].keys():
           template_variables['table_value'][fetch_raws['variable']]=[]
           template_variables['table_value'][fetch_raws['variable']].\
               append(fetch_raws['variable__variable'])
       template_variables['table_value'][fetch_raws['variable']].\
           append(fetch_raws['function'])
    template_variables['column']=range(1,max([len(val)\
        for val in template_variables['table_value'].values()]))
    return render_to_response('file_view.html',template_variables,\
           context_instance=RequestContext(request))

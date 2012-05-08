from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from files_manager.forms import UploadFileForm
from django.http import HttpResponseRedirect,Http404
from files_manager.models import Func_var,Function,CSVData,Category,File_head
from files_manager.file_handling import handle_uploaded_file
from django.template import RequestContext
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from files_manager.tasks import upload_data

def file_list(request,choiced_category=''):
    categories_list=Category.objects.all().values('category_slug','name_category')
    if not choiced_category:
        files_list=CSVData.objects.all().values('id','name_file','upload_date')
    else:
        files_list=CSVData.objects.filter(category__category_slug=choiced_category).\
                       values('id','name_file','upload_date')
    paginator=Paginator(files_list,10)
    page=request.GET.get('page')
    try:
        files_output_list=paginator.page(page)
    except PageNotAnInteger:
        files_output_list=paginator.page(1)
    except EmptyPage:
        files_output_list=paginator.page(paginator.num_pages)
    files_indexes=range(files_output_list.start_index(),\
                      files_output_list.end_index())
    return render_to_response('index.html',{'categories_list':categories_list,\
                            'files_output_list': files_output_list,\
                            'files_indexes':files_indexes},\
                            context_instance=RequestContext(request)
                                             )

@login_required
def file_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            save_file=form.save()
            upload_data.delay(save_file.id)
            messages.info(request,'File is uploading by name %s' % save_file.name_file)
            return HttpResponseRedirect(reverse('file_view',args=[save_file.id]))
    else:
        form = UploadFileForm()
    return render_to_response('upload.html',{'form':form},\
           context_instance=RequestContext(request))

@login_required
def file_view(request,file_id):
    try:
        requirement_file=CSVData.objects.get(id=file_id)
    except CSVData.DoesNotExist:
        raise Http404
    file_name=requirement_file.name_file.name
    
    if requirement_file.upload_status=='uploaded':
        query_result=Function.objects.filter(variable__data=file_id).\
            values('variable','variable__variable','function').\
                order_by('variable__variable')
        header_values=File_head.objects.filter(data=file_id).\
            values_list('column_head_str',flat=True).order_by('column_number')
        template_variables={'file_name': file_name, 'table_value': query_result,\
                            'header_values':header_values}
    else:
        template_variables={'file_name':file_name}
    template_variables['file_status']=requirement_file.get_upload_status_display()
    
    return render_to_response('file_view.html',template_variables,\
           context_instance=RequestContext(request))

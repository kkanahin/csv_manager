from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from files_manager.forms import UploadFileForm
from django.http import HttpResponseRedirect,Http404
from files_manager.models import Func_var,Function,CSVData,Category
from files_manager.file_handling import handle_uploaded_file
from django.template import RequestContext
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 

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
        page=1
        files_output_list=paginator.page(page)
    except EmptyPage:
        files_output_list=paginator.page(paginator.num_pages)
    if paginator.num_pages<=5:
        page_range=range(1,paginator.num_pages+1)
    elif page>=paginator.num_pages-5:
        page_range=range(paginator.num_page-5,paginator.num_page)
    elif page<=5:
        page_range=range(1,5)
    else:
        page_range=range(page-2,page+2)
    return render_to_response('index.html',{'user':request.user,\
                            'categories_list':categories_list,\
                            'files_output_list': files_output_list,\
                            'page_range': page_range},\
                            context_instance=RequestContext(request)
                                             )

@login_required
def file_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            added_file=handle_uploaded_file(request.FILES['upload_file'],\
                request.POST['category'])
            messages.success(request,'File was uploaded succesfully ')
            return HttpResponseRedirect(reverse('file_view',args=[added_file]))
    else:
        form = UploadFileForm()
    return render_to_response('upload.html',{'form':form},\
           context_instance=RequestContext(request))

def file_view(request,file_id):
#    template_variables={}
#    
#    template_variables['table_value']={}
#    query_result=Function.objects.filter(variable__data=file_id).\
#        values('variable','variable__variable','function').order_by('variable')
#    if not query_result:
#        raise Http404
#    template_variables['file_name']=CSVData.objects.values('name_file').\
#                                    get(id=file_id)['name_file']
#    for fetch_raws in query_result:
#       if not fetch_raws['variable'] in template_variables['table_value'].keys():
#           template_variables['table_value'][fetch_raws['variable']]=[]
#           template_variables['table_value'][fetch_raws['variable']].\
#               append(fetch_raws['variable__variable'])
#       template_variables['table_value'][fetch_raws['variable']].\
#           append(fetch_raws['function'])
#    template_variables['column']=range(1,max([len(val)\
#        for val in template_variables['table_value'].values()]))
#    return render_to_response('file_view.html',template_variables,\
#           context_instance=RequestContext(request))
    try:
        file_name=CSVData.objects.values('name_file').get(id=file_id)['name_file']
    except CSVData.DoesNotExist:
        raise Http404
    query_result=Function.objects.filter(variable__data=file_id).\
        values('variable','variable__variable','function').order_by('variable')
    template_variables={'file_name': file_name, 'table_value': query_result}
    return render_to_response('file_view.html',template_variables,\
           context_instance=RequestContext(request))     

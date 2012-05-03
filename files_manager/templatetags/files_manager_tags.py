from django.template import Library,TemplateSyntaxError,Node,Variable
from django.utils.safestring import mark_safe

register = Library()

@register.inclusion_tag('table.html')
def show_table(values_list,headers_list,table_caption):
    table_value={}
    for values_raw in values_list:
            if not values_raw['variable'] in table_value.keys():
                table_value[values_raw['variable']]=[]
                table_value[values_raw['variable']].\
                    append(values_raw['variable__variable'])
            table_value[values_raw['variable']].append(values_raw['function'])
    columns_number = range(1,max([len(val) for val in table_value.values()]))
    for raw in table_value.values():
        raw.extend([0]*(len(columns_number)-len(raw)+1))
    data_chart=[[values for values in value_list] \
                for value_list in map(None,*table_value.values())]
    data_chart=map(None,headers_list[:],data_chart[:])
    return {'table_raws': table_value.values(),'columns_number': columns_number,\
            'table_caption':table_caption,'headers_list':headers_list,'data_chart':data_chart}

@register.inclusion_tag('pagination.html')
def files_paginator(pagination_obj):
    num_pages=pagination_obj.paginator.num_pages
    page=pagination_obj.number
    if num_pages<=10:
        page_range=range(1,num_pages+1)
    elif page>=num_pages-5:
        page_range=range(num_pages-4,num_pages+1)
    elif page<=5:
        page_range=range(1,6)
    else:
        page_range=range(page-2,page+2)
    return {'pagination_obj':pagination_obj,'page_range':page_range}

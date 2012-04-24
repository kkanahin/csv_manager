from django.template import Library,TemplateSyntaxError,Node,Variable
from django.utils.safestring import mark_safe

register = Library()

@register.inclusion_tag('table.html')
def show_table(values_list,table_caption):
    table_value={}
    for values_raw in values_list:
            if not values_raw['variable'] in table_value.keys():
                table_value[values_raw['variable']]=[]
                table_value[values_raw['variable']].append(values_raw['variable__variable'])
            table_value[values_raw['variable']].append(values_raw['function'])
    table_raws=[mark_safe('<tr>%s</tr>' % (''.join(["<td>%s</td>" % cell_value for cell_value in raw])))\
                for raw in table_value.values()]
    columns_number = range(1,max([len(val) for val in table_value.values()]))
    return {'table_raws': table_raws,'columns_number': columns_number,\
            'table_caption':table_caption}



#class TableOutputNode(Node):
#    def __init__(self,values_list,attrs,caption):
#        self.values_list=Variable(values_list)
#        self.attrs=attrs
#        self.caption=Variable(caption)
#        
#    def render(self,context):
#        table_value={}
#        values_list=self.values_list.resolve(context)
#        for raws in values_list:
#            if not raws['variable'] in table_value.keys():
#                table_value[raws['variable']]=[]
#                table_value[raws['variable']].append(raws['variable__variable'])
#            table_value[raws['variable']].append(raws['function'])
#        column = range(1,max([len(val) for val in table_value.values()]))
#        table_head_column=["<th>f%s(X)</th>" % head_column for head_column in \
#                          column]
#        table_head="<thead><tr><th>X</th>%s</tr></thead>" %\
#                             ''.join(table_head_column)
#        table_body="<tbody>%s</tbody>" % (''.join(['<tr>%s</tr>' %  \
#                    (''.join(["<td>%s</td>" % cell_value for cell_value in raw]))\
#                     for raw in table_value.values()]))    
#        output_table_string="<table %s><caption><b>File: %s</b></caption>%s%s</table>"\
#                            % (self.attrs,self.caption,table_head,table_body)
#        return output_table_string
#        
#@register.tag
#def table_output(parser,token):
#    try:
#        tag_name,table_value,table_attrs,table_caption = token.split_contents()
#    except ValueError:
#        msg='%r tag requires only 3 arguments' % token.contents[0]
#    return TableOutputNode(table_value,table_attrs,table_caption)

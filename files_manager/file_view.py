from files_manager.models import Func_var,Function

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
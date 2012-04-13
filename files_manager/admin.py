from django.contrib import admin
from files_manager.models import Category,CSVData,Func_var,Function

class CSVDataAdmin(admin.ModelAdmin):
    list_display=('id','name_file','upload_date','category')

class FunctionInline(admin.StackedInline):
    model=Function
    extra=3


class Func_varAdmin(admin.ModelAdmin):
     list_display=('id','variable','data')
     inlines=[FunctionInline]
     list_filter=['data']


class FunctionAdmin(admin.ModelAdmin):
    list_display=('id','variable','function','variable_id','variable_data')
#    fieldsets=[
#        (None,{'fields':['variable']}),
#        ('Function value',{'fields':['function']}),
#    ]



admin.site.register(Category)
admin.site.register(CSVData,CSVDataAdmin)
admin.site.register(Func_var,Func_varAdmin)
admin.site.register(Function,FunctionAdmin)
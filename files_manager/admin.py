from django.contrib import admin
from files_manager.models import Category,CSVData,Func_var,Function

class CSVDataAdmin(admin.ModelAdmin):
    list_display=('id','name_file','upload_date','last_change','category')

class FunctionInline(admin.StackedInline):
    model=Function
    extra=3


class Func_varAdmin(admin.ModelAdmin):
     list_display=('id','variable','data')
     inlines=[FunctionInline]
     list_filter=['data']


class FunctionAdmin(admin.ModelAdmin):
    list_display=('id','variable','function','variable_id','variable_data')
    list_filter=['variable__data','variable__id']
#    fieldsets=[
#        (None,{'fields':['variable']}),
#        ('Function value',{'fields':['function']}),
#    ]
    def variable_id(self,obj):
        return obj.variable.id
    variable_id.short_description="variable id"
    
    def variable_data(self,obj):
        return obj.variable.data
    variable_data.short_description="variable data"


admin.site.register(Category)
admin.site.register(CSVData,CSVDataAdmin)
admin.site.register(Func_var,Func_varAdmin)
admin.site.register(Function,FunctionAdmin)
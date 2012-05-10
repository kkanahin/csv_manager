from django.contrib import admin
from files_manager.models import Category,CSVData,File_head,Func_var,Function

class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','name_category','category_slug')
    
class CSVDataAdmin(admin.ModelAdmin):
    list_display=('id','name_file','upload_date','last_change','category','upload_status','owner')

class FunctionInline(admin.StackedInline):
    model=Function
    extra=3


class Func_varAdmin(admin.ModelAdmin):
     list_display=('id','variable','data')
     inlines=[FunctionInline]
     list_filter=['data']

class File_headAdmin(admin.ModelAdmin):
    list_display=('id','data','column_number','column_head_str')

class FunctionAdmin(admin.ModelAdmin):
    list_display=('id','variable','function','variable_id','variable_data')
    list_filter=['variable__data','variable__id']

    def variable_id(self,obj):
        return obj.variable.id
    variable_id.short_description="variable id"
    
    def variable_data(self,obj):
        return obj.variable.data
    variable_data.short_description="variable data"

admin.site.register(File_head,File_headAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(CSVData,CSVDataAdmin)
admin.site.register(Func_var,Func_varAdmin)
admin.site.register(Function,FunctionAdmin)
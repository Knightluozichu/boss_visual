from django.contrib import admin
from myApp.models import JobInfo,User,History
# Register your models here.
# 设置管理后台的头部标题
admin.site.site_header = '招聘后台管理'
# 设置管理后台在浏览器标签页中显示的标题
admin.site.site_title = '招聘后台管理'
# 设置管理后台主页的标题
admin.site.index_title = '招聘后台管理'
class JobManager(admin.ModelAdmin):
    list_display = ["id","title","address","type","educational","workExperience","workTag","salary","salaryMonth","companyTags","hrWork","hrName","pratice","companyTitle","companyAvatar","companyNature","companyStatus","companyPeople","detailUrl","companyUrl","dist"]
    list_display_links = ['title']
    list_filter = ['type']
    search_fields = ['title']
    list_editable = ["address","type","educational","workExperience","workTag","salary","salaryMonth",
                                 "companyTags","hrWork","hrName","pratice","companyTitle","companyAvatar","companyNature",
                                 "companyStatus","companyPeople","detailUrl","companyUrl","dist"]
    readonly_fields = ['id']
    list_per_page = 20
    date_hierarchy = "createTime"

class UserManager(admin.ModelAdmin):
    list_display = ['id','username','password','avatar','createTime','address','educational','work','workExpirence']
    list_display_links = ['username']
    search_fields = ['username']
    list_editable = ['password','avatar','address','educational','work','workExpirence']
    readonly_fields = ['username']
    list_per_page = 5
    date_hierarchy = "createTime"



admin.site.register(JobInfo, JobManager)
admin.site.register(User, UserManager)


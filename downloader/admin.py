from django.contrib import admin
from . models import *

# Register your models here.
class DownloaderAdmin(admin.ModelAdmin):
    list_display=['Name','Enable']
class PagesAdmin(admin.ModelAdmin):
    list_display= ['pageid','privacy','termsandcondition','dmca','disclaimer','contactus']
class RenderTxtAdmin(admin.ModelAdmin):
    list_display= ['Robots','Ads']
class HeaderCodeAdmin(admin.ModelAdmin):
    list_display= ['Header_Codes']
class HomePageAdmin(admin.ModelAdmin):
    list_display= ['Name']
admin.site.register(Downloader,DownloaderAdmin)
admin.site.register(Pages,PagesAdmin)
admin.site.register(RenderTxt,RenderTxtAdmin)
admin.site.register(HeaderCode,HeaderCodeAdmin)
admin.site.register(HomePage,HomePageAdmin)

from django.contrib import admin
from scrapper.models import NyTimesModel,FoxNewsModel,PcMagModel,CnetModel

# Register your models here.
# class MasterAdmin(admin.ModelAdmin):
#     pass

class NyTimesAdmin(admin.ModelAdmin):
    pass

class FoxNewsAdmin(admin.ModelAdmin):
    pass

class PcMagAdmin(admin.ModelAdmin):
    pass

class CnetAdmin(admin.ModelAdmin):
    pass

# admin.site.register(MasterModel,MasterAdmin)
admin.site.register(NyTimesModel,NyTimesAdmin)
admin.site.register(FoxNewsModel,FoxNewsAdmin)
admin.site.register(PcMagModel,PcMagAdmin)
admin.site.register(CnetModel,CnetAdmin)
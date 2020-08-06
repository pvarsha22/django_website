from django.contrib import admin

# Register your models here.
from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from . import models

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(models.Item6, MyModelAdmin)
admin.site.register(models.Item7, MyModelAdmin)
admin.site.register(models.Item8, MyModelAdmin)
admin.site.register(models.Item9, MyModelAdmin)
admin.site.register(models.Item10, MyModelAdmin)
admin.site.register(models.Item11, MyModelAdmin)
admin.site.register(models.Item12, MyModelAdmin)
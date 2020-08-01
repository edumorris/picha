from django.contrib import admin

from .models import Images, Category, Location, Subs

# Register your models here.
class PictorialAdmin(admin.ModelAdmin):
    filter_horizontal =('Category, Location,')
    
admin.site.register(Location)
admin.site.register(Category)
admin.site.register(Images)
admin.site.register(Subs)
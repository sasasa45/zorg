from django.contrib import admin
from .models import Items, Photos, ProductCode, Spy, Parts
# Register your models here.
admin.site.register(Items)
admin.site.register(Photos)
admin.site.register(ProductCode)
admin.site.register(Spy)
from django.contrib.admin import ModelAdmin

@admin.register(Parts)
class UserDataAdmin(ModelAdmin):

    list_display = ('name', 'image_tag', 'qty', 'get_items')
    # list_filter = 'all'
    # readonly_fields = ('transactions_created', )
    fieldsets = (
        ('General', {
            'fields': ('name', 'picture', 'item')
        }),
        ('Block Numbers', {
            'fields': ('qty', 'price')
        }),
        ('Block URLs', {
            'fields': ('url_1', 'url_2', )
        })
    )


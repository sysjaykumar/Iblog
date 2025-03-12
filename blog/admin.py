from django.contrib import admin
from .models import Category, Post
# Register your models here

#for configuration of category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','description','url','add_date','image_tag')
    search_fields = ('title',)

#for Configuration of post admin
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','cat','url','image_tag2')
    search_fields = ('title',)
    list_filter= ('cat',)
    list_per_page = 50

    # class Media:
    #     js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/7/tinymce.min.js','js/script.js')

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
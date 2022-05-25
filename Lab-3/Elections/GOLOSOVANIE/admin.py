from django.contrib import admin
from .models import StartPage, Candidate, Slogan, Batch, MyUser
from django.utils.safestring import mark_safe


class StartPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'img')


class CandidateAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'batch', 'date_of_birth', 'region',
                    'support_count', 'get_preview', 'creator')
    search_fields = ('region', 'last_name', 'creator')
    list_display_links = ('id', 'first_name', 'last_name',)
    list_filter = ('date_of_birth', 'region', 'batch', 'creator')
    list_editable = ('batch', 'region')
    fields = ('first_name', 'last_name', 'middle_name', 'date_of_birth', 'region', 'description', 'preview',
              'batch', 'slogan', 'support_count', 'get_photo', 'creator')
    readonly_fields = ('support_count', 'get_photo',)


    def get_preview(self, obj):
        if obj.preview:
            return mark_safe(f'<img src= "{obj.preview.url}" width="200px">')

    get_preview.short_description = 'Фото'


    def get_photo(self, obj):
        if obj.preview:
            return mark_safe(f'<img src= "{obj.preview.url}">')

    get_photo.short_description = 'Фото'


class SloganAdmin(admin.ModelAdmin):
    list_display = ('id', 'slogan')


class BatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'political_views')
    search_fields = ('political_views',)
    list_display_links = ('id', 'name',)


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'nick_name', 'email')
    list_display_links = ('id', 'username', 'nick_name')
    fields = ('id', 'username', 'nick_name', 'email', 'password')
    readonly_fields = ('id', 'password')


admin.site.register(StartPage, StartPageAdmin)
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Slogan, SloganAdmin)
admin.site.register(Batch, BatchAdmin)
admin.site.register(MyUser, UserAdmin)



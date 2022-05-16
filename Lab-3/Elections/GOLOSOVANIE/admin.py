from django.contrib import admin

from .models import StartPage, Candidate, Slogan, Batch


class StartPageAdmin(admin.ModelAdmin):
    list_display = ('img',)


class CandidateAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'batch', 'date_of_birth', 'region',)
    search_fields = ('region', 'last_name')
    list_display_links = ('id', 'first_name', 'last_name',)
    list_filter = ('date_of_birth', 'region', 'batch')
    list_editable = ('batch', 'region')


class SloganAdmin(admin.ModelAdmin):
    list_display = ('id', 'slogan')


class BatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'political_views')
    search_fields = ('political_views',)
    list_display_links = ('id', 'name',)


admin.site.register(StartPage, StartPageAdmin)
admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Slogan, SloganAdmin)
admin.site.register(Batch, BatchAdmin)

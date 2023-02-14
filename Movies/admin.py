from django.contrib import admin

# Register your models here.
from .models import Movies, movieCertificate, movieType, movieLanguage, movieShowtime
admin.site.register(Movies)
admin.site.register(movieCertificate)
admin.site.register(movieType)
admin.site.register(movieLanguage)
admin.site.register(movieShowtime)
# @admin.register(Movies)
# class moviesAdmin(admin.ModelAdmin):
#     list_display = ('movie_img','movie_title','movie_cast')
    
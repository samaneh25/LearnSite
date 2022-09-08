from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import *


@admin.register(SinglePostModel)
class SinglePostModel(SummernoteModelAdmin):
    summernote_fields = ('content',)


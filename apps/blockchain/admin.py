from django.contrib import admin
from .models import Block, BlockAdmin
# Register your models here.

admin.site.register(Block, BlockAdmin)


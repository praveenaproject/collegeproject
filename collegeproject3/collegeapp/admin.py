from django.contrib import admin

# Register your models here.
from django.contrib import admin
from . models import Department,Branch , Applicationform
# Register your models here.
admin.site.register(Department)
admin.site.register(Branch)
admin.site.register(Applicationform)
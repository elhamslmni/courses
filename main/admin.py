from django.contrib import admin
from .models import Choose
from .models import Question
from .models import My_Course
admin.site.register(Question)
admin.site.register(Choose)
admin.site.register(My_Course)

# Register your models here.

from django.contrib import admin
from .models import resourceRequest,onGoingProjects,LoginPage,makeObjection

admin.site.register(resourceRequest)
admin.site.register(onGoingProjects)
admin.site.register(LoginPage)
admin.site.register(makeObjection)
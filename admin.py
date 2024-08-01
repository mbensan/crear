from django.contrib import admin
from main.models import Nota, UserProfile
# Register your models here.
class NotaAdmin(admin.ModelAdmin):
  pass

class UserProfileAdmin(admin.ModelAdmin):
  pass

admin.site.register(Nota, NotaAdmin)

admin.site.register(UserProfile, UserProfileAdmin)
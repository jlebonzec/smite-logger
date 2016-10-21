from django.contrib import admin
from logger.models import(
    Pantheon,
    Role,
    God,
)

# Register your models here.
admin.site.register(Pantheon)
admin.site.register(Role)
admin.site.register(God)

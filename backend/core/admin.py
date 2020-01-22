from django.contrib import admin
from .models import Party
from .models import Donation


admin.site.register(Party)
admin.site.register(Donation)

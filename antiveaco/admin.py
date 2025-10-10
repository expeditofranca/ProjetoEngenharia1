from django.contrib import admin

from .models import Cliente, Divida, Pagamento

admin.site.register(Cliente)
admin.site.register(Divida)
admin.site.register(Pagamento)
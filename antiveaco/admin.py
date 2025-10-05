from django.contrib import admin

from .models import Cliente, Compra, Divida, Pagamento

admin.site.register(Cliente)
admin.site.register(Compra)
admin.site.register(Divida)
admin.site.register(Pagamento)
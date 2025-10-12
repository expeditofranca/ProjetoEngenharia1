from django.contrib import admin

from .models import Cliente, Divida, Pagamento,Endereco


class EnderecoInline(admin.StackedInline):
    model = Endereco
    can_delete = False
class ClienteAdmin(admin.ModelAdmin):
        inlines = [
        EnderecoInline,
    ]
        
admin.site.register(Endereco)
admin.site.register(Cliente)
admin.site.register(Divida)
admin.site.register(Pagamento)
from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Tree, Post


class TreeResource(resources.ModelResource):
    class Meta:
        model = Tree
        import_id_fields = ("N_placa",)
        fields = ["N_placa", "nome_popular", "nome_cientifico", "dap", "altura", "latitude", "longitude", "laudo"]

class MedicamentoDataAdmin(ImportExportModelAdmin):
    resource_class = TreeResource

admin.site.register(Tree, MedicamentoDataAdmin)
admin.site.register(Post)
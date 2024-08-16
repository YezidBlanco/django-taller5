from django.forms import ModelForm
from myapp.models import Producto, Categoria

# Create the form class.
class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = [
            "code",
            "name",
            "brand",
            "reference",
            "description",
            "price",
            "batch",
            "manufacturing",
            "expedition",
            "categoria",
        ]

class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        fields = [
            "name",
            "description",
        ]
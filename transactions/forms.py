from django import forms
from django.forms import inlineformset_factory
from .models import Purchase, PurchaseDetail

class BootstrapMixin(forms.ModelForm):
    """
    A mixin to add Bootstrap classes to form fields.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.setdefault('class', 'form-control')

class PurchaseDetailForm(BootstrapMixin, forms.ModelForm):
    """
    A form for creating and updating PurchaseDetail instances.
    """
    class Meta:
        model = PurchaseDetail
        fields = [
            'item', 'price', 'quantity', 'type_de_casier', 'total_bouteilles'
        ]

PurchaseDetailFormSet = inlineformset_factory(
    Purchase, PurchaseDetail, form=PurchaseDetailForm, extra=1, can_delete=True
)

class PurchaseForm(BootstrapMixin, forms.ModelForm):
    """
    A form for creating and updating Purchase instances.
    """
    class Meta:
        model = Purchase
        fields = [
            'description', 'vendor', 'order_date', 'delivery_date', 'delivery_status'
        ]
        widgets = {
            'delivery_date': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'datetime-local'
                }
            ),
            'description': forms.Textarea(
                attrs={'rows': 1, 'cols': 40}
            ),
            'delivery_status': forms.Select(
                attrs={'class': 'form-control'}
            ),
        }

import django_tables2 as tables
from .models import Item, Delivery

class ItemTable(tables.Table):
    """
    Table representation for Item model.
    """
    class Meta:
        model = Item
        template_name = "django_tables2/semantic.html"
        fields = (
            'id', 'name', 'category', 'quantity',
            'price', 'expiring_date', 'vendor',
            'type_de_casier',  # Ajout du champ type_de_casier
            'total_bouteilles',  # Ajout du champ total_bouteilles
        )
        order_by_field = 'sort'

class DeliveryTable(tables.Table):
    """
    Table representation for Delivery model.
    """
    class Meta:
        model = Delivery
        fields = (
            'id', 'item', 'customer_name', 'phone_number',
            'location', 'date', 'is_delivered'
        )

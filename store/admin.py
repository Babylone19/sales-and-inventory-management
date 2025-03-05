from django.contrib import admin
from .models import Category, Item, Delivery

class CategoryAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Category model.
    """
    list_display = ('name', 'slug')
    search_fields = ('name',)
    ordering = ('name',)

class ItemAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Item model.
    """
    list_display = (
        'name', 'category', 'quantity', 'price',
        'expiring_date', 'vendor', 'type_de_casier',  # Ajout du champ type_de_casier
        'total_bouteilles',  # Ajout du champ total_bouteilles
    )
    search_fields = ('name', 'category__name', 'vendor__name')
    list_filter = ('category', 'vendor', 'type_de_casier')  # Ajout du filtre pour type_de_casier
    ordering = ('name',)

class DeliveryAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Delivery model.
    """
    list_display = (
        'item', 'customer_name', 'phone_number',
        'location', 'date', 'is_delivered'
    )
    search_fields = ('item__name', 'customer_name')
    list_filter = ('is_delivered', 'date')
    ordering = ('-date',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Delivery, DeliveryAdmin)

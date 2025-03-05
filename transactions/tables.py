import django_tables2 as tables
from .models import Sale, SaleDetail
from .models import Purchase, PurchaseDetail
class SaleTable(tables.Table):
    item = tables.Column(verbose_name='Item', accessor='saledetail_set.first.item.name')
    type_de_casier = tables.Column(verbose_name='Type de Casier', accessor='saledetail_set.first.type_de_casier')
    total_bouteilles = tables.Column(verbose_name='Total Bouteilles', accessor='saledetail_set.first.total_bouteilles')
    customer_name = tables.Column(verbose_name='Customer Name', accessor='customer.name')
    transaction_date = tables.Column(verbose_name='Transaction Date', accessor='date_added')
    payment_method = tables.Column(verbose_name='Payment Method', empty_values=())
    quantity = tables.Column(verbose_name='Quantity', accessor='saledetail_set.first.quantity')
    price = tables.Column(verbose_name='Price', accessor='saledetail_set.first.price')
    total_value = tables.Column(verbose_name='Total Value', accessor='saledetail_set.first.total_detail')
    amount_received = tables.Column(verbose_name='Amount Received', accessor='amount_paid')
    balance = tables.Column(verbose_name='Balance', accessor='amount_change')
    profile = tables.Column(verbose_name='Profile', empty_values=())

    class Meta:
        model = Sale
        template_name = "django_tables2/semantic.html"
        fields = (
            'item',
            'customer_name',
            'transaction_date',
            'payment_method',
            'quantity',
            'price',
            'total_value',
            'amount_received',
            'balance',
            'profile',
            'type_de_casier',
            'total_bouteilles'
        )
        order_by_field = 'sort'





class PurchaseTable(tables.Table):
    item = tables.Column(verbose_name='Item', accessor='purchasedetail_set.first.item.name')
    type_de_casier = tables.Column(verbose_name='Type de Casier', accessor='purchasedetail_set.first.type_de_casier')
    total_bouteilles = tables.Column(verbose_name='Total Bouteilles', accessor='purchasedetail_set.first.total_bouteilles')
    vendor = tables.Column(verbose_name='Vendor', accessor='vendor.name')
    order_date = tables.Column(verbose_name='Order Date', accessor='order_date')
    delivery_date = tables.Column(verbose_name='Delivery Date', accessor='delivery_date')
    quantity = tables.Column(verbose_name='Quantity', accessor='purchasedetail_set.first.quantity')
    delivery_status = tables.Column(verbose_name='Delivery Status', accessor='delivery_status')
    price = tables.Column(verbose_name='Price', accessor='purchasedetail_set.first.price')
    total_value = tables.Column(verbose_name='Total Value', accessor='purchasedetail_set.first.total_detail')

    class Meta:
        model = Purchase
        template_name = "django_tables2/semantic.html"
        fields = (
            'item',
            'vendor',
            'order_date',
            'delivery_date',
            'quantity',
            'delivery_status',
            'price',
            'total_value',
            'type_de_casier',
            'total_bouteilles'
        )
        order_by_field = 'sort'

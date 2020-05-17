from django.contrib import admin

from .models import Item, OrderItem, Order, Payment, Coupon, Refund, Address, UserProfile


def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)


make_refund_accepted.short_description = 'Update orders to refund granted'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',
                    'being_delivered',
                    'received',
                    'refund_requested',
                    'refund_granted',
                    'shipping_address',
                    'billing_address',
                    'payment',
                    'coupon'
                    ]
    list_display_links = [
        'user',
        'shipping_address',
        'billing_address',
        'payment',
        'coupon'
    ]
    list_filter = ['ordered',
                   'being_delivered',
                   'received',
                   'refund_requested',
                   'refund_granted']
    search_fields = [
        'user__username',
        'ref_code'
    ]
    actions = [make_refund_accepted]


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'apartment_address',
        'country',
        'zip',
        'address_type',
        'default'
    ]
    list_filter = ['default', 'address_type', 'country']
    search_fields = ['user', 'street_address', 'apartment_address', 'zip']

class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'discount_price',
                    'category', 'price', 'label', 'slug', 'description', 'show_image']
    list_filter = ['title','category','price']
    search_fields = list_filter


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['user', 'ordered', 'item', 'quantity']
    list_filter = ['item','user']
    search_fields = list_filter

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['stripe_charge_id', 'user', 'amount', 'timestamp']
    list_filter = ['amount', 'user', 'timestamp']
    search_fields = list_filter


class CouponAdmin(admin.ModelAdmin):
    list_display = ['code', 'amount']
    list_filter = list_display
    search_fields = list_display


class RefundAdmin(admin.ModelAdmin):
    list_display = ['order', 'reason', 'accepted', 'email']
    list_filter = ['order', 'reason', 'accepted']
    search_fields = list_display


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'stripe_customer_id']
    list_filter = ['user',]
    search_fields = list_filter
admin.site.register(Item, ItemAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Coupon, CouponAdmin)
admin.site.register(Refund, RefundAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(UserProfile, UserProfileAdmin)

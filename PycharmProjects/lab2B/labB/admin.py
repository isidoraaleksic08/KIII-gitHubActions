from django.contrib import admin
from .models import Vraboten, Product, Market, Market_Product, Contact_Info


class MarketProductInline(admin.TabularInline):
    model = Market_Product
    extra = 1

class MarketAdmin(admin.ModelAdmin):
    inlines = [MarketProductInline]
    list_display = ('name', )
    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            if request.user.is_superuser:
                return True
            return False

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(MarketAdmin, self).save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            if request.user.is_superuser:
                return True
            return False

class VrabotenAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', )

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(VrabotenAdmin,self).save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False
    def has_delete_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False

class ProductAdmin(admin.ModelAdmin):
    list_filter = ('type', 'homeMade', )
    list_display = ('name', 'type', 'homeMade', 'code', )


admin.site.register(Market, MarketAdmin)
admin.site.register(Vraboten, VrabotenAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Contact_Info)
admin.site.register(Market_Product)

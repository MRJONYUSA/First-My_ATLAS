from django.contrib import admin
from . import models
class CryptoCoinsAdmin(admin.ModelAdmin):
    list_display = ('title', 'blockcheyn', 'category')\

class CryptoInline(admin.TabularInline):
    model = models.Crypto_Coins
    model = models.Physic_coin
    model = models.Currensy_coin



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'creat_at')
    fieldset = [
        (None, {"fields":['title']}),
        ('Dates',{
            'fields':['creat_at'],
            'classes':['collapse']
        })
    ]
admin.site.register(models.Crypto_Coins,CategoryAdmin)
admin.site.register(models.Physic_coin, CategoryAdmin)
admin.site.register(models.Currensy_coin, CategoryAdmin)
#####################################################################################################################
admin.site.register(models.CryptoCoins, CryptoCoinsAdmin)
admin.site.register(models.PhysicCoins, CryptoCoinsAdmin)
admin.site.register(models.CurrensyCoins, CryptoCoinsAdmin)
#####################################################################################################################
admin.site.site_header = "Juma Trade"
admin.site.site_title = "Juma Trading"
admin.site.index_title = "Welcome to the site of JUMA TRADE"
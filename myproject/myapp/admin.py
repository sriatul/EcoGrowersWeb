from django.contrib import admin
from .models import Commodity
from .models import State
from .models import Market,CommodityData,AllData
# Register your models here.

class adminState(admin.StackedInline):
    model = Market
class adminMarket(admin.ModelAdmin):
    inlines = [adminState]
admin.site.register(Commodity)
admin.site.register(State,adminMarket)
admin.site.register(Market)
admin.site.register(CommodityData)
admin.site.register(AllData)



from .models import Subscribers
admin.site.register(Subscribers)
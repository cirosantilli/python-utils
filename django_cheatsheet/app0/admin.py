from django.contrib import admin

from app0.models import Tab0
from app0.models import Tab1

class Tab1Inline(admin.TabularInline): #makes a table with fields of Tab1
    #class Tab1Inline(admin.StackedInline): #stacks the fields of Tab1

    model = Tab1 #each one is based on a Tab1 object
    extra = 3    #show 3 Tab1 inlines per Tab0 add page

class Tab0Admin(admin.ModelAdmin):
    #organizes forms in categories
    #data information is collapsable

    fieldsets = [
        (None,               {'fields': ['r1']}),
        ('Date information', {'fields': ['r2'], 'classes': ['collapse']}),
    ]

    inlines = [Tab1Inline]
    #show Tab1 ojects, which refer to Tab0 objects in the same page as Tab0 add page
    #each one will use the id of this Tab0 object

    list_display = ('r1', 'r2', was_published_recently)
    #what data to display on the choose/add Tab0 page
    #default is str(), which tends not to be very useful
    #can also include functions instead of fields as was_published_recently.

admin.site.register(Tab0, Tab0Admin)

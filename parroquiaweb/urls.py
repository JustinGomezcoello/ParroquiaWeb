from django.contrib import admin
from django.urls import path, include
from catequesis.views import home

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('catequesis/', include('catequesis.urls', namespace='catequesis')),  # ← nota el `namespace`
]

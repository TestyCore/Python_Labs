from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls', namespace='cart')),
    path('order/', include('order.urls', namespace='order')),
    path('administrator/', include('administrator.urls', namespace='administrator')),
    path('edostavka/', include('edostavka.urls')),
    path('', RedirectView.as_view(url='edostavka/')),
    path('accounts/', include('django.contrib.auth.urls')),
]

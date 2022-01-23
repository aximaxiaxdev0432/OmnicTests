from django.contrib import admin
from django.urls import path
from app.views import exchange, exchange_period

	
urlpatterns = [
	path('', exchange),  
	path('period/', exchange_period),  
    path('admin/', admin.site.urls),

]

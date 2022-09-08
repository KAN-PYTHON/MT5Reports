from django.contrib import admin
from django.urls import path
from APP import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bonus_report/', views.bonus_report, name='bonus_report'),
    path('deposit_report/', views.deposit_report, name='deposit_report'),
    path('correction_report/', views.correction_report, name='correction_report'),
    path('bbook_dangerous/', views.bbook_dangerous, name='bbook_dangerous'),
    path('abook_dangerous/', views.abook_dangerous, name='abook_dangerous'),
    path('all_book_dangerous/', views.all_book_dangerous, name='all_book_dangerous'),
    path('symbols_profit/', views.symbols_profit, name='symbols_profit'),
    path('admin/', admin.site.urls),
]

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
    path('abook_all/', views.abook_all, name='abook_all'),
    path('bbook_all/', views.bbook_all, name='bbook_all'),
    path('inactive_users/', views.inactive_users, name='inactive_users'),
    path('open_positions/', views.open_positions, name='open_positions'),
    path('zero_accounts/', views.zero_accounts, name='zero_accounts'),
    path('all_book_dangerous/', views.all_book_dangerous, name='all_book_dangerous'),
    path('symbols_profit/', views.symbols_profit, name='symbols_profit'),
    path('welcome_bonus_report/', views.welcome_bonus_report, name='welcome_bonus_report'),
    path('bonus100_report/', views.bonus100_report, name='bonus100_report'),
    path('abook_commission_report/', views.abook_commission_report, name='abook_commission_report'),
    path('bbook_commission_report/', views.bbook_commission_report, name='bbook_commission_report'),
    path('admin/', admin.site.urls),
]

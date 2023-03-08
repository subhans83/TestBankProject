from django.urls import path
from . import views
from users import views as user_views
app_name = 'bankingapp'
urlpatterns = [
    path('', views.index, name='index'),


    path('register_success/', views.register_success, name='register_success'),
    #path('login/',views.login_request, name='login'),
    #path('register/', views.register_request, name='register'),
    path('member/add/', views.create_view, name='add'),
    path('member/<int:pk>/', views.update_view, name='change'),

    path('member/ajax/load-branches/', views.load_branches, name='ajax_load_branches'),  # AJAX
]

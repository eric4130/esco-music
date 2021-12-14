from django.urls import path
from . import views
app_name = 'band_profiles'
urlpatterns = [
    #Home Page
    path('', views.index, name='index'),
    #Profiles Page
    path('profiles/', views.profiles, name='profiles'),
    #Detail page for a single band profile
    path('profiles/<int:profile_id>/', views.profile, name='profile'),
    #Page for adding a new profile
    path('new_profile/', views.new_profile, name='new_profile'),
    #Page for editing a profile
    path('edit_profile/<int:profile_id>/', views.edit_profile, name='edit_profile'),

]


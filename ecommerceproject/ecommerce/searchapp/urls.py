from django.urls import path, include

from searchapp import views
app_name = 'search_app'
urlpatterns = [

    path('',views.SearchResult,name='to_search'),

]

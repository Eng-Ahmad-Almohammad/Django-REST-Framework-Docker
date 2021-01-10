from django.urls import path, include

from .views import dataView, detailsView
urlpatterns = [
    path('', dataView.as_view() , name = 'book'),
    path('/<int:pk>/',detailsView.as_view(), name = 'details_view')
]
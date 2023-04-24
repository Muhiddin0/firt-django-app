from django.urls import path

from .views import (
    ArticlListView,
    ArticlDetailsView,
    ArticlUpdateView,
    ArticlDeleteView,
    ArticlNewView
    )

from os import abort
urlpatterns = [
    path('new/', ArticlNewView.as_view(), name='articl_new'),
    path('<int:pk>/edit/', ArticlUpdateView.as_view(), name='articl_edit'),
    path('<int:pk>', ArticlDetailsView.as_view(), name='articl_details'),
    path('<int:pk>/delete/', ArticlDeleteView.as_view(), name='articl_delete'),
    path('', ArticlListView.as_view(), name='articl_list'),
]
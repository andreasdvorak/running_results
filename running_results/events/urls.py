from django.urls import path
from .views import (
    events_create_view, 
    events_detail_view, 
    events_delete_view,
    events_for_year_list_view,
    events_update_view,
    get_years_with_events_view,
)

app_name = 'events'
urlpatterns = [
    path('', get_years_with_events_view, name='events-list'),
    path('year:<int:year>/', events_for_year_list_view, name='events-for-year-list'),
    path('create/', events_create_view, name='events-create'),
    path('<int:id>/', events_detail_view, name='events-detail'),
    path('<int:id>/update/', events_update_view, name='events-update'),
    path('<int:id>/delete/', events_delete_view, name='events-delete'),
]
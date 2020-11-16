from django.urls import path
from .views import (
    distances_list_view,
    distance_detail_view,
    events_create_view, 
    events_detail_view, 
    events_delete_view,
    events_for_year_list_view,
    events_update_view,
    get_years_with_events_view,
)

app_name = 'results'
urlpatterns = [
    path('distances', distances_list_view, name='distances-list'),
    path('distances/<int:id>/', distance_detail_view, name='distance-details'),
    path('events', get_years_with_events_view, name='events-list'),
    path('events/year:<int:year>/', events_for_year_list_view, name='events-for-year-list'),
    path('event/create/', events_create_view, name='events-create'),
    path('event/<int:id>/', events_detail_view, name='events-detail'),
    path('event/<int:id>/update/', events_update_view, name='events-update'),
    path('event/<int:id>/delete/', events_delete_view, name='events-delete'),
]
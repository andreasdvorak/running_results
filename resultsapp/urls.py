from django.urls import path
from .views import (
    annual_records_m_view,
    annual_records_w_view,
    club_view,
    discipline_list_view,
    discipline_detail_view,
    event_create_view,
    event_detail_view,
    event_for_year_list_view,
    years_with_annual_records_m_view,
    years_with_annual_records_w_view,
    years_with_events_view,
    record_list_m_view,
    record_list_w_view,
    statistics_view
)

# url namespace, if there are several apps
app_name = 'resultsapp'

urlpatterns = [
    path('annualrecordlistm', years_with_annual_records_m_view, name='annual-record-list-m'),
    path('annualrecordlistm/year:<int:year>/', annual_records_m_view, name='annual-records-m-for-year-list'),
    path('annualrecordlistw', years_with_annual_records_w_view, name='annual-record-list-w'),
    path('annualrecordlistw/year:<int:year>/', annual_records_w_view, name='annual-records-w-for-year-list'),
    path('club_details', club_view, name='club_view'),
    path('disciplines', discipline_list_view, name='discipline-list'),
    path('disciplines/<int:id>/', discipline_detail_view, name='discipline_distance_details'),
    path('events', years_with_events_view, name='event-list'),
    path('events/year:<int:year>/', event_for_year_list_view, name='event-for-year-list'),
    path('event/create/', event_create_view, name='events-create'),
    path('event/<int:id>/', event_detail_view, name='events-detail'),
    path('recordlistm', record_list_m_view, name='record-list-m'),
    path('recordlistw', record_list_w_view, name='record-list-w'),
    path('statistics', statistics_view, name='statistics'),
]

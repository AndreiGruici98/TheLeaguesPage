from django.urls import path

from .views import ChampionListView, ChampionDetailView, ChampionCreateView, ChampionUpdateView, ChampionDeleteView


urlpatterns = [
    path('', ChampionListView.as_view(), name="champion_list"),
    path('add_champion/', ChampionCreateView.as_view(), name="champion_create"),
    path('champions/<str:slug>/', ChampionDetailView.as_view(), name="champion_detail"),
    path('champions/<str:slug>/update/', ChampionUpdateView.as_view(), name="champion_update"),
    path('champions/<str:slug>/delete/', ChampionDeleteView.as_view(), name="champion_delete"),
]

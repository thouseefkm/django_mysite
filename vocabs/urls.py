from django.urls import path

from . import views

app_name = 'vocabs'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:vocab_id>/', views.detail, name='detail'),
    path('<int:vocab_id>/results/', views.results, name='results'),
    path('<int:vocab_id>/vote/', views.vote, name='vote'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('elections/', views.CandidateListView.as_view(), name='elections'),
    path('batch/<int:batch_id>/', views.CandidateByBatchView.as_view(), name='batch'),
    path('candidate/<int:pk>/', views.CandidateProfileView.as_view(), name='candidate'),
    path('candidate/add-candidate/', views.CreateCandidateView.as_view(), name='add_candidate'),
    path('registry/', views.UserRegistryView.as_view(), name='registry'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('candidate/add-slogan/', views.AddSloganView.as_view(), name='add_slogan'),
    path('add-batch/', views.AddBatchView.as_view(), name='add_batch'),
    path('my-candidates/', views.MyCandidatesView.as_view(), name='my_candidates'),
    path('update-candidate/<int:pk>/', views.UpdateCandidateView.as_view(), name='update_candidate'),
    path('delete-candidate/<int:pk>/', views.DeleteCandidateView.as_view(), name='delete_candidate'),
    # path('search-candidate/', views.SearchCandidate.as_view(), 'search_candidate'),

]

from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.Index.as_view(), name='index'),
   # path('elections', views.elections, name='elections'),
    path('elections/', views.CandidateList.as_view(), name='elections'),
    #path('batch/<int:batch_id>/', views.get_batch, name='batch'),
    path('batch/<int:batch_id>/', views.CandidateByBatch.as_view(), name='batch'),
    # path('candidate/<int:candidate_id>', views.candidate, name='candidate'),
    path('candidate/<int:pk>', views.CandidateProfile.as_view(), name='candidate'),
    # path('candidate/add-candidate/', views.add_candidate, name='add_candidate')
    path('candidate/add-candidate/', views.CreateCandidate.as_view(), name='add_candidate'),
    path('registry/', views.UserRegistry.as_view(), name='registry'),
    #path('registry/', views.UserRegistry.as_view(), name='registry'),
    path('login/', views.UserLogin.as_view(), name='login'),
    path('logout/', views.UserLogout.as_view(), name='logout'),
    path('candidate/add-slogan/', views.AddSlogan.as_view(), name='add_slogan'),
    # path('candidate/delete-candidate/', views.DeleteCandidate.as_view(), name='delete_candidate'),
    path('my-candidates/', views.MyCandidates.as_view(), name='my_candidates'),

]

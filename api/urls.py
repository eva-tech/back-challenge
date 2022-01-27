from django.urls import path, include

from api.views import StudyView, StudyDetail

urlpatterns = [
    path('studies/', StudyView.as_view()),
    path('studies/<int:pk>/', StudyDetail.as_view()),
    path('api-auth/', include('rest_framework.urls'))
]

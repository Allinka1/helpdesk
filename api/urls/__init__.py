from django.urls import include, path

app_name = 'api'
urlpatterns = [
    path('request/', include('api.urls.request', namespace='request'), name='request'),
    path('user/', include('api.urls.user', namespace='user'), name='user'),
    path('', include('api.urls.comment', namespace='comment'), name='comment'),
]

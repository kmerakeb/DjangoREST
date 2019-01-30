from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.UserListView.as_view()),
    path('<int:pk>/', views.UserDetailsView.as_view())
]


''' 
/// this is a function to return a token, user detials for jwt for the method obtain_auth_token
def post(self, request, *args, **kwargs):
    serializer = self.get_serializer(data=request.data)

    if serializer.is_valid():
        user = serializer.object.get('user') or request.user
        token = serializer.object.get('token')
        response_data = {
            'token': token,
            'user': UserSerializer(user).data
        }
        response = Response(response_data, status=status.HTTP_200_OK)
        if api_settings.JWT_AUTH_COOKIE:
            expiration = (datetime.utcnow() +
                          api_settings.JWT_EXPIRATION_DELTA)
            response.set_cookie(api_settings.JWT_AUTH_COOKIE,
                                response.data['token'],
                                expires=expiration,
                                httponly=True)
        return response

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''

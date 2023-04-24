from django.urls import path


from .views import SignUpView
# Create your views here.
urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup")
]
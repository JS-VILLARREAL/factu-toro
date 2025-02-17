from django.urls import path, include
from rest_framework import routers

from .viewsets.lot import LotViewSet
from .viewsets.cattle import CattleViewSet

# from .viewsets.auth import AuthViewSet

from .apiviews.lot import LotAPIView
from .apiviews.auth import login_apiview
from .apiviews.auth import RegisterAPIView

router = routers.SimpleRouter()
router.register(r"lot", LotViewSet, basename="lot")
router.register(r"cattle", CattleViewSet, basename="cattle")
# router.register(r"user", AuthViewSet, basename="user")

urlpatterns = router.urls + [
    path("Lot/", LotAPIView.as_view(), name="Lot"),
    path("Login/", login_apiview, name="Login"),
    # path("Register/", register_apiview, name="Register"),
    path("Register/", RegisterAPIView.as_view(), name="Register"),
]

from django.urls import path, re_path
from rest_framework import routers

from .viewsets.lot import LotViewSet
from .viewsets.cattle import CattleViewSet

# from .viewsets.auth import AuthViewSet

from .apiviews.lot import LotAPIView
from .apiviews.auth import SignupAPIView, LoginAPIView

router = routers.SimpleRouter()
router.register(r"lot", LotViewSet, basename="lot")
router.register(r"cattle", CattleViewSet, basename="cattle")
# router.register(r"user", AuthViewSet, basename="user")

urlpatterns = router.urls + [
    path("lot/", LotAPIView.as_view(), name="lot"),
    # path("login/", LoginAPIView.as_view(), name="login"),
    path("register/", SignupAPIView.as_view(), name="register"),
]

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("permissions.urls")),
    path('',include("Users.urls")),
    path('',include("clubreps.urls")),
    path('',include("FacultyCoordinator.urls")),
    path('',include("VenueFacultyCoordinator.urls")),
    path('',include("VenueFacultyStaff.urls")),
    path('',include("Security.urls")),
    path('',include("Office.urls")),
    path('',include("Faculty.urls"))
]


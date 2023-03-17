from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page, name="home"),
    path("snippetv/", views.view_snippet, name="snippetv"),
    path('snippets/add/', views.create_snippet, name='add_snippets'),
    path('snippets/list/', views.snippets_page, name='list_snippets'),
    path('snippets/<int:id>/', views.view_snippet_page, name='view_snippets'),
    path('snippets/<int:id>/delete', views.delete_snippet_page, name="delete_snippet"),
    path('snippets/<int:id>/raw', views.raw_snippet_page, name="raw_snippet"),
    path('snippets/<int:id>/view', views.html_snippet_page, name="html_snippet"),
    path("auth/signup/", views.register, name="signup"),
    path("auth/signin/", views.login_request, name="signin"),
    path("auth/logout/", views.logout_request, name="logout"),
    path("profile/snippets", views.profile_snippets_page, name="profile_snippets"),
    path("languages", views.languages)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

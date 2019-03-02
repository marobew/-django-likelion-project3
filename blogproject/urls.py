from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import blog.views
import portfolio.views
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    # blog app
    path('', blog.views.home, name="home"),
    path('blog/<int:blog_id>/', blog.views.detail, name="detail"),
    path('blog/new/', blog.views.new, name="new"),
    path('blog/create/', blog.views.create, name="create"),
    # portfolio app
    path('portfolio/', portfolio.views.portfolio, name="portfolio"),
    # accounts app
    path('accounts/signup/', accounts.views.signup, name="signup"),
    path('accounts/login/', accounts.views.login, name="login"),
    path('accounts/logout/', accounts.views.logout, name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

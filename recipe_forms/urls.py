"""recipe_forms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from recipe_forms.models import Author
from recipe_forms.models import Recipes
from recipe_forms.views import (index.html, recipe.html, author.html, add_author.html, 
add_recipe.html)

admin.site.register(Author)
admin.site.register(Recipes)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index),
    path('author/<int:author_id>/', author_stuff),
    path('recipes/<int:recipe_id>/', recipe_stuff),
    path('addrecipe', add_recipe),
    path('addauthor', add_author)

]

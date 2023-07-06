"""
URL configuration for test_demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView


from app01 import views
from app02 import views as app02_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', RedirectView.as_view(url='employee/list')),
    path('home/', views.home_index),
    path('home/templates', views.home_templates),
    path('grammar/summary', views.grammar_summary),

    # 登录案例
    path('user/add', views.user_add),
    path('user/list', views.user_list),
    path('user/login', views.user_login),
    path('user/delete', views.user_delete),

    # app02
    path('dept/list', app02_views.dept_index),
    path('employee/list', app02_views.employee_index),
    path('employee/add', app02_views.employee_add_user_form),
    path('employee/<int:nid>/edit', app02_views.employee_edit_user),

    # class Mobile
    path('mobile/list', app02_views.Mobile.as_view()),
    path('mobile/<int:nid>', app02_views.mobile_form_prompt),

    # api
    path('api/dept', app02_views.dept),
    path('api/employee/add_user', app02_views.employee_add_user)
]

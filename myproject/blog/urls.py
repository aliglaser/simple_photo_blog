from django.urls import path, include


from . import views

app_name='blog'


urlpatterns = [
	path('', views.index, name="blog"),	#글 목록
	path('<int:pk>/', views.detail, name="post_detail"),
	path('<int:pk>/comment/new', views.comment_new, name="comment_new"),
	path('<int:post_pk>/comment/<pk>/edit', views.comment_edit, name="comment_edit"),
	path('new/', views.post_new, name="new"),	#새 포스팅
]
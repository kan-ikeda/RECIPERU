from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

app_name = 'myapp'
urlpatterns = [
    path('',views.RecipeList.as_view(), name='recipe_list'),  #レシピ一覧（ホーム）
    path('recipes/add/', views.RecipeCreateView.as_view(), name='recipe_create'), #レシピ作成
    path('recipes/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe_detail'), #レシピ詳細
    path('recipes/<int:pk>/edit/', views.RecipeUpdateView.as_view(), name='recipe_update'), #レシピ編集
    path('recipes/<int:pk>/delete/', views.RecipeDeleteView.as_view(), name='recipe_delete'), #レシピ削除
    path('categories/', views.CategoryListView.as_view(), name='category_list'), #カテゴリ一覧
    path('categories/<int:pk>/', views.CategoryRecipesView.as_view(), name='category_recipes'), #カテゴリ別レシピ一覧
    path('contact/', views.ContactFormView.as_view(), name='contact_form'), #お問い合わせフォーム
    path('search/',views.RecipeSearchFormView.as_view(), name='recipe_search_form'), #レシピ検索
    path('logout/', auth_views.LogoutView.as_view(next_page='myapp:recipe_list'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
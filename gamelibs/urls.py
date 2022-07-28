from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views
from .decorators import check_recaptcha

urlpatterns = [
    path('', include('social_django.urls', namespace='social')),
    path("game_filter/<str:slug>/", views.GameGanreView.as_view(), name='ganre_filter'),
    path("game_filter/category/<str:slug>/", views.GameCategoryView.as_view(), name='category_filter'),
    path("post_filter/<str:slug>/", views.PostTagsView.as_view(), name='tag_filter'),
    path("", views.GameView.as_view(), name='main'),
    path("signup/", check_recaptcha(views.SignUp.as_view()), name="signup"),
    path("login/", views.LogIn.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("contactus/", views.contact_us, name="contact_us"),
    path("contact_done/", views.contact_done, name="contact_done"),
    path("user/", views.userpage, name="userpage"),
    path("user-settings/<int:pk>/", views.ProfileEdit.as_view(), name="user_settings_page"),
    path("add_post/", views.addpost, name="add_post"),
    path("сheckout/", views.сheckout, name="сheckout"),
    path("post/<int:pk>/update", views.EditPost.as_view(), name='edit_post'),
    path("post/<int:pk>/delete", views.DeletePost.as_view(), name='delete_post'),
    path("search/", views.Search.as_view(), name='search'),
    path("search_games/", views.SearchByGames.as_view(), name='search_games'),
    path("search_post/", views.SearchByPosts.as_view(), name='search_posts'),
    path("store/", views.StoreGameView.as_view(), name='store'),
    path("store/popular/", views.PopularStoreGameView.as_view(), name='store_popular'),
    path("blogs/", views.PostGameView.as_view(), name='blog'),
    path("blogs/popular/", views.PopularPostGameView.as_view(), name='blog_popular'),
    path("<slug:slug>/", views.GameDetailsView.as_view(), name='game_details'),
    path("company/<str:slug>/", views.CompanyDetailsView.as_view(), name='company_details'),
    path("profile/<int:slug>/", views.ProfileDetailsView.as_view(), name='user_profile'),
    path("post/<slug:slug>/", views.PostDetailsView.as_view(), name='post_details'),
    path("user/new_email/", views.NewEmail.as_view(), name='add_email'),
    path("review/<int:pk>", views.AddGameReview.as_view(), name='add_review'),
    path("post_review/<int:pk>", views.AddPostReview.as_view(), name='add_post_review'),
    path("review/some/", views.AddReview.as_view(), name='add_some_review'),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/', views.cart_detail, name='cart_detail'),
]

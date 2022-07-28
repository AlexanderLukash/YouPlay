from itertools import chain
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View, generic
from django.views.generic import ListView, DetailView, CreateView, FormView, UpdateView, DeleteView
from urllib import request
from django.http import HttpResponse
from pyexpat import model
from hitcount.views import HitCountDetailView
from cart.cart import Cart
from .forms import RegisterUserForm, LoginUserForm, UserForm, ProfileForm, GameReviewForm, PostReviewForm, ReviewForm, \
    AddPost, PostForm
from .models import Game, Post, Company, Profile, Ganre, Category, Tags


def contact_us(request):
    return render(request, 'gamelibs/contact.html')


def contact_done(request):
    return render(request, 'gamelibs/contact_done.html')


def сheckout(request):
    return render(request, 'gamelibs/checkout.html')


def page_not_found_view(request, exception):
    return render(request, 'gamelibs/404.html', status=404)


@login_required(login_url="/login")
def userpage(request):
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    return render(request=request, template_name="gamelibs/user-profile.html",
                  context={"user": request.user, "user_form": user_form, "profile_form": profile_form})


class ProfileEdit(UpdateView):
    model = Profile
    template_name = "gamelibs/user-settings.html"

    form_class = ProfileForm
    success_url = "../../user/"


class NewEmail(View):
    def post(self, request, pk):
        profile_form = ProfileForm(request.POST)
        profile = Profile.objects.get(id=pk).id
        if profile_form.is_valid():
            profile_form = profile_form.save(commit=False)
            profile_form.id = profile
            profile_form.save()
            return redirect('../user/')
        else:
            return redirect('../user-settings/')


class SignUp(CreateView):
    form_class = RegisterUserForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

    def form_valid(self, form):
        if self.request.recaptcha_is_valid:
            form.save()
            return render(self.request, 'registration/sign_up_done.html', self.get_context_data())
        return render(self.request, 'registration/signup.html', self.get_context_data())


class LogIn(LoginView):
    form_class = LoginUserForm
    success_url = reverse_lazy("/")
    template_name = "registration/login.html"


def addpost(request):
    if request.method == "POST":
        form = AddPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            form.save_m2m()

            return redirect('../blogs/')
    else:
        form = AddPost()

    data = {
        'form': form,
        'add': True
    }

    return render(request, 'gamelibs/user-post-manager.html', {'form': form})


class EditPost(UpdateView):
    model = Post
    template_name = "gamelibs/user-post-edit.html"

    form_class = AddPost


class EditProfile(UpdateView):
    model = Profile
    template_name = "gamelibs/user-settings.html"

    form_class = ProfileForm


class DeletePost(DeleteView):
    model = Post
    template_name = "gamelibs/user-post-delete.html"
    success_url = "../../blogs/"


class AddReview(DetailView):
    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect("../../contact_done/")


class GameView(ListView):
    model = Game
    queryset = Game.objects.filter(draft=False)
    template_name = "gamelibs/index.html"


class GameDetailsView(HitCountDetailView):
    model = Game
    slug_field = 'url'
    count_hit = True


class CompanyDetailsView(DetailView):
    model = Company
    slug_field = "name"
    template_name = "gamelibs/company_detail.html"


class PostDetailsView(HitCountDetailView):
    model = Post
    slug_field = 'url'
    count_hit = True


class StoreGameView(ListView):
    model = Game
    queryset = Game.objects.filter(draft=False).order_by('-id')
    template_name = "gamelibs/store-1.html"
    paginate_by = 15


class PopularStoreGameView(ListView):
    model = Game
    queryset = Game.objects.filter(draft=False).order_by('-hit_count_generic__hits')
    template_name = "gamelibs/store-2.html"
    paginate_by = 15


class PostGameView(ListView):
    model = Post
    queryset = Post.objects.filter(draft=False).order_by('-id')
    template_name = "gamelibs/blog-1.html"
    paginate_by = 6


class PopularPostGameView(ListView):
    model = Post
    queryset = Post.objects.filter(draft=False).order_by('-hit_count_generic__hits')
    template_name = "gamelibs/blog-2.html"
    paginate_by = 6


class AddGameReview(View):
    def post(self, request, pk):
        form = GameReviewForm(request.POST)
        user = request.user.id
        games = Game.objects.get(id=pk).id
        game = Game.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.game_id = games
            form.user_id = user
            form.save()
        return redirect(game.get_absolute_url())


class AddPostReview(View):
    def post(self, request, pk):
        form = PostReviewForm(request.POST)
        user = request.user.id
        posts = Post.objects.get(id=pk).id
        post = Post.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = posts
            form.user_id = user
            form.save()
        return redirect(post.get_absolute_url())


class ProfileDetailsView(DetailView):
    model = Profile
    slug_field = "user_id"
    template_name = "gamelibs/user-profile-all.html"


class Search(ListView):
    template_name = "gamelibs/search.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)

        if query is not None:
            blog_results = Post.objects.search(query)
            game_results = Game.objects.search(query)

            # combine querysets
            queryset_chain = chain(
                blog_results,
                game_results,
            )
            qs = sorted(queryset_chain,
                        key=lambda instance: instance.pk,
                        reverse=True)
            return qs
        return Post.objects.none()  # just an empty queryset as default


class SearchByGames(ListView):
    template_name = "gamelibs/search_by_game.html"

    def get_queryset(self):
        return Game.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        return context


class SearchByPosts(ListView):
    template_name = "gamelibs/search_by_post.html"

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['q'] = self.request.GET.get('q')
        return context


@login_required(login_url="/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Game.objects.get(id=id)
    cart.add(product=product)
    return redirect("main")


@login_required(login_url="/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Game.objects.get(id=id)
    cart.remove(product)
    return redirect("main")


@login_required(login_url="/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/login")
def cart_detail(request):
    return render(request, 'gamelibs/cart.html')


class GameGanreView(ListView):
    model = Ganre
    template_name = 'gamelibs/ganre_filter.html'
    context_object_name = 'game_list'

    def get_queryset(self):
        return Game.objects.filter(ganres__url=self.kwargs.get('slug'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['ganre_name'] = self.kwargs.get('slug')
        return context


class GameCategoryView(ListView):
    model = Category
    template_name = 'gamelibs/category_filter.html'
    context_object_name = 'game_list'

    def get_queryset(self):
        return Game.objects.filter(category__url=self.kwargs.get('slug'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['category_name'] = self.kwargs.get('slug')
        return context


class PostTagsView(ListView):
    model = Tags
    template_name = 'gamelibs/tag_filter.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return Post.objects.filter(tags__url=self.kwargs.get('slug'))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['tags_name'] = self.kwargs.get('slug')
        return context

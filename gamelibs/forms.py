from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from gamelibs.models import Profile, GameReview, PostReview, ReviewContact, Post, Game, Tags, Good, Bad


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'placeholder': 'Логін'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Електронна пошта'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='Confirm Password',
                                widget=forms.PasswordInput(attrs={'placeholder': 'Підтвердьте пароль'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'placeholder': 'Логін'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')


class ProfileForm(forms.ModelForm):
    avatar = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Add a comment...'}), required=False)
    town = forms.CharField(label='Town', widget=forms.TextInput(attrs={'placeholder': 'Місто...'}), required=False)
    country = forms.CharField(label='Country', widget=forms.TextInput(attrs={'placeholder': 'Країна...'}),
                              required=False)
    phone_number = forms.IntegerField(label=' Phone',
                                      widget=forms.TextInput(attrs={'placeholder': 'Номер телефону...'}),
                                      required=False, help_text='Інформацію про номер бачете лише ви.')
    github = forms.CharField(label='GitHub', widget=forms.TextInput(attrs={'placeholder': 'Посилання на GitHub...'}),
                             required=False)
    about = forms.CharField(label='About', widget=CKEditorUploadingWidget(), required=False)
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'Електронна пошта...'}),
                             required=False)

    class Meta:
        model = Profile
        fields = ('email', 'town', 'country', 'phone_number', 'github', 'about', 'avatar')


class GameReviewForm(forms.ModelForm):
    class Meta:
        model = GameReview
        fields = ('text',)


class PostReviewForm(forms.ModelForm):
    class Meta:
        model = PostReview
        fields = ('text',)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewContact
        fields = ('name', 'email', 'text')


class AddPost(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'placeholder': 'Заголовок...'}),
                            help_text='Максимум 100 символів.')
    games = forms.ModelMultipleChoiceField(queryset=Game.objects.filter(draft=False), widget=forms.SelectMultiple(
        attrs={'style': "padding: 10px; background:#edf2ff; border:none;"}), required=True)
    tags = forms.ModelMultipleChoiceField(queryset=Tags.objects.all(), widget=forms.SelectMultiple(
        attrs={'style': "padding: 10px; background:#edf2ff; border:none;"}))
    foreword_description = forms.CharField(label='Small Description',
                                           widget=forms.Textarea(attrs={'placeholder': 'Коротке описання...'}),
                                           help_text='Максимум 335 символів.')
    description = forms.CharField(label='Description', widget=CKEditorUploadingWidget())
    rank = forms.FloatField(label='Rank', widget=forms.TextInput(attrs={'placeholder': 'Оцінка...'}))
    good = forms.ModelMultipleChoiceField(queryset=Good.objects.all(), widget=forms.SelectMultiple(
        attrs={'style': "padding: 10px; background:#edf2ff; border:none;"}))
    bad = forms.ModelMultipleChoiceField(queryset=Bad.objects.all(), widget=forms.SelectMultiple(
        attrs={'style': "padding: 10px; background:#edf2ff; border:none;"}))
    url = forms.SlugField(label='Title', widget=forms.TextInput(attrs={'placeholder': 'Унікальний ідентифікатор...'}),
                          help_text='Максимум 255 символів.')
    premiere = forms.DateField(label='Date',
                               widget=forms.SelectDateWidget(attrs=({'style': 'width: 10%; display: inline-block;'})),
                               help_text='У форматі: 24.03.2022.')

    class Meta:
        model = Post
        fields = (
            'title', 'games', 'tags', "foreword_description", "description", "rank", "good", "bad", "url", "premiere",)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title', 'games', 'tags', "foreword_description", "description", "rank", "good", "bad", "url", "premiere",)


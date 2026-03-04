from django import forms
from .models import Post, Comment, User


class PostForm(forms.ModelForm):
    """Форма для создания и редактирования публикаций."""

    class Meta:
        model = Post
        fields = (
            "title",
            "text",
            "pub_date",
            "location",
            "category",
            "image",
        )
        widgets = {
            "pub_date": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }


class CommentForm(forms.ModelForm):
    """Форма для создания и редактирования комментариев."""

    class Meta:
        model = Comment
        fields = ("text",)


class UserEditForm(forms.ModelForm):
    """Форма для редактирования профиля пользователя."""

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
        )

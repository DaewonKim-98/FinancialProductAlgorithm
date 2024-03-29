from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings


# Create your models here.
class User(AbstractUser):
    gender = models.TextField()
    age = models.TextField()
    nickname = models.TextField()

    class Meta:
        db_table = 'user'
    pass


class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        from allauth.account.utils import user_email, user_field, user_username
        # 기존 코드를 참고하여 새로운 필드들을 작성해줍니다.
        data = form.cleaned_data
        username = data.get("username")
        age = data.get("age")
        gender = data.get("gender")
        nickname = data.get("nickname")
        user_username(user, username)
        if age:
            user.age = age
        if gender:
            user.gender = gender
        if nickname:
            user.nickname = nickname
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            # Ability not to commit makes it easier to derive from
            # this adapter by adding
            user.save()
        return user


class Carts(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fin_prdt_cd  = models.TextField()                      # 금융 상품 코드
    kor_co_nm = models.TextField()                         # 금융회사명
    fin_prdt_nm = models.TextField()                       # 금융 상품명
    created_at = models.DateTimeField(auto_now_add=True)
    pass

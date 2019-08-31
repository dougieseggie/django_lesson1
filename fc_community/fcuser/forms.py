from django import forms
from .models import Fcuser
from django.contrib.auth.hashers import check_password


class LoginForm(forms.Form):
    username = forms.CharField(
        error_messages={
            'required': '아이디를 입력해주세요.'
        },
        max_length=32, label="사용자 이름")
    password = forms.CharField(
        error_messages={
            'required': '비밀번호를 입력해주세요.'
        }, widget=forms.PasswordInput, label="비밀번호")

    def clean(self):
        # clean()은 Form에 들어있던 clean 함수 호출해주며, 값이 없으면 아래에서 실패처리 돼서 나감.
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            try:
                fcuser = Fcuser.objects.get(username=username)
            except Fcuser.DoesNotExist:  # 없을 때
                self.add_error('username', '아이디가 없습니다')
                return

            if not check_password(password, fcuser.password):
                self.add_error('password', '틀린 비밀번호입니다.')
            else:
                # session을 위해 id를 사용하려면, 여기서 self 안에 id를 넣어야한다.
                self.user_id = fcuser.id

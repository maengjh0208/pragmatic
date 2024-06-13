from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    # OneToOneField: User와 Profile을 일대일 매칭한다.
    # CASCADE: User가 삭제되면 Profile도 삭제된다.
    # related_name: API 요청시 request.user.profile 으로 단번에 프로필 정보를 얻을 수 있다.
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    # upload_to: 파일이 저장되는 중간 경로 설정. image는 media/profile/ 디렉토리 하위에 저장된다.
    image = models.ImageField(upload_to='profile/', null=True)

    # 유저는 닉네임 정보는 unique하다. (중복 X)
    nickname = models.CharField(max_length=20, unique=True, null=True)
    message = models.CharField(max_length=100, null=True)




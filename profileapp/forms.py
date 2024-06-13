from django.forms import ModelForm

from profileapp.models import Profile


# django의 ModelForm을 이용하면 기존의 Model을 Form으로 자동 변환해서 사용할 수 있다.
class ProfileCreationForm(ModelForm):
    class Meta:
        # Profile이라는 모델을 가져와서 Form으로 사용하겠다.
        model = Profile
        # Profile 모델에서 image, nickname, message 컬럼만 가져와서 사용하겠다.
        fields = ['image', 'nickname', 'message']

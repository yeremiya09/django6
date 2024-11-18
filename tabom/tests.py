from django.test import TestCase

from tabom.models import User

# Create your tests here.


class TestAutoNow(TestCase):
    def test_auto_now_filed_is_set_when_save(self) -> None:

        user = User(name="test")
        user.save()
        self.assertIsNotNone(user.updated_at)
        self.assertIsNotNone(user.created_at)


# django 의 TestCase 클래스를 상속하는 클래스를 만든다.
# class 의 이름은 Test 로 시작해야 합니다. (pytest 에서는 무조건적인 규칙인데, unit test 에서는 강제는 아닙니다.)
#
# - unit test -> 파이썬 언어 자체에 내장된 테스트 프레임워크
# - pytest -> 써드파티 라이브러리 (poetry add 로 추가해야 됩니다.) 사실상 파이썬 표준.

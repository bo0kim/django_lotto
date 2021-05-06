from django.test import TestCase
from .models import GuessNumbers

# Create your tests here.
class GuessNumbersTestCase(TestCase):
    def test_generate(self):
        g = GuessNumbers(name='Test numbers', text='selected numbers')

        print('Pre-generate : ', g.lottos)
        g.generate() # 6개씩 5세트 숫자가 리스트로 묶여지고 문자열로 변환됨

        print(g.update_date)
        print(g.lottos)

        self.assertTrue(len(g.lottos)>20)

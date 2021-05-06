from django.shortcuts import render
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    # return HttpResponse('<h1>Hello,world!</h1>')
    lottos = GuessNumbers.objects.all()
    return render(request, 'lotto/default.html', {'lottos' : lottos}) # context

def hello(request):
    return HttpResponse('<h1 style="color:red;">Hello,world!</h1>')

def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        # print("******")
        # print(request.POST['name'])
        # print(request.POST['text'])
        # print("******")
        # form = PostForm()

        if form.is_valid():
            lotto = form.save(commit=False) # 임시 저장. 실제 DB에는 반영X
            lotto.generate() # generate 함수 내에서 DB 저장까지 완료.

            return redirect('index')

    else :
        form = PostForm()
        return render(request, 'lotto/form.html', {'form':form})

def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk=lottokey)
    return render(request, 'lotto/detail.html', {'lotto':lotto})

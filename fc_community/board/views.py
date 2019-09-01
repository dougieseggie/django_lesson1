from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404
from .models import Board
from tag.models import Tag
from .forms import BoardForm
from fcuser.models import Fcuser
# Create your views here.


def board_list(request):
    all_boards = Board.objects.all().order_by('-id')
    # all 은 다 가져오는 함수 / -id의 -는 역순이란 뜻

    page = request.GET.get('p', 1)
    # p라는 값으로 받고 없으면 첫 번째 페이지로
    paginator = Paginator(all_boards, 3)
    # 한 페이지 당 몇 개씩 보여줄건지
    boards = paginator.get_page(page)
    # 앞서 설정한 page 값을 paginator 에 넣어서 보여줌
    return render(request, 'board_list.html', {'boards': boards})


def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시글을 찾을 수 없습니다')

    return render(request, 'board_detail.html', {'board': board})


def board_write(request):
    if not request.session.get('user'):
        return redirect('/fcuser/login/')
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            fcuser = Fcuser.objects.get(pk=user_id)
            tags = form.cleaned_data['tags'].split(',')

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = fcuser
            board.save()

            for tag in tags:
                if not tag:
                    continue
                _tag, _ = Tag.objects.get_or_create(name=tag)
                board.tags.add(_tag)
               # 아래는 뒤의 조건이 일치하는 모델이 있으면 가져오고, 없으면 생성해서 가져오는 함수.
               # 복수의 조건도 넣을 수 있음
               # created는 생성이 되었으면 1 아니면 0 식으로 변수를 가짐.
               # 사용하지 않는 변수는 _로 넣으면 됨.
               # _tag, created= tag.objects.get_or_create(name=tag)

               # 앞에서 보드가 저장이 되어야 _tag를 더할 수 있음.

            return redirect('/board/list/')
    else:
        form = BoardForm()

    return render(request, 'board_write.html', {'form': form})

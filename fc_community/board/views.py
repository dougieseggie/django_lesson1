from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404
from .models import Board
from .forms import BoardForm
from fcuser.models import Fcuser
# Create your views here.


def board_list(request):
    all_boards = Board.objects.all().order_by('-id')
    # all 은 다 가져오는 함수 / -id의 -는 역순이란 뜻

    page = request.GET.get('p', 1)
    # p라는 값으로 받고 없으면 첫 번째 페이지로
    paginator = Paginator(all_boards, 2)
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

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = fcuser
            board.save()

            return redirect('/board/list/')
    else:
        form = BoardForm()

    return render(request, 'board_write.html', {'form': form})

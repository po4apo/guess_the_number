import math

import form as form
from django.http import HttpResponse
from django.shortcuts import render
from .forms import InputTwoNumberForm


def show_input_two_number(request):
    DEFAULT_ONE = 0
    DEFAULT_TWO = 1000
    one_num = int(request.session.get('one_num', 1))
    two_num = int(request.session.get('two_num', 1))
    print(one_num, two_num)

    if request.method == 'POST':

        if 'submit' in request.POST:
            request.session['one_num'] = request.POST['one_number']
            request.session['two_num'] = request.POST['two_number']
            num = int((int(request.session['two_num']) + int(request.session['one_num'])) / 2)
            request.session['num'] = num
            return render(request, 'guess_the_number_app/game.html', {'num': num})


        elif 'change' in request.POST:
            form = InputTwoNumberForm({'one_number': DEFAULT_ONE, 'two_number': DEFAULT_TWO})
            return render(request, 'guess_the_number_app/input_two_number.html',
                          {'form': form})

        elif (two_num - one_num <= 1):
            return render(request,
                          'guess_the_number_app/end.html',
                          {'text': 'Вы наврали!(',
                           })

        elif 'more' in request.POST:
            request.session['one_num'] = request.session['num']
            num = math.ceil((int(request.session['two_num']) + int(request.session['one_num'])) / 2)
            request.session['num'] = num
            return render(request, 'guess_the_number_app/game.html', {'num': num})

        elif 'less' in request.POST:
            request.session['two_num'] = request.session['num']
            num = math.floor((int(request.session['two_num']) + int(request.session['one_num'])) / 2)
            request.session['num'] = num
            return render(request, 'guess_the_number_app/game.html', {'num': num})

        elif 'my_num' in request.POST:
            return render(request,
                          'guess_the_number_app/end.html',
                          {'text': 'Всё получилось! </br>Ваше число:',
                           'num':request.session.get('num'),
                           })



    else:
        form = InputTwoNumberForm({'one_number': DEFAULT_ONE, 'two_number': DEFAULT_TWO})
        return render(request, 'guess_the_number_app/input_two_number.html',
                      {'form': form})

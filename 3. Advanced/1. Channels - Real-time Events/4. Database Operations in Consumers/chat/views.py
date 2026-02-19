from django.shortcuts import render


def room(request, room_name):
    context: dict = {
        'room': room_name
    }

    return render(request, 'chat/lobby.html', context)

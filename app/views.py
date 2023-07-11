from django.shortcuts import render, redirect

cards = [
    {
        "id": 1,
        "name": "Paciente 1",
    },
    {
        "id": 2,
        "name": "Paciente 2",
    },
    {
        "id": 3,
        "name": "Paciente 3",
    },
    {
        "id": 4,
        "name": "Paciente 4",
    },
    {
        "id": 5,
        "name": "Paciente 5",
    },
    {
        "id": 6,
        "name": "Paciente 6",
    },
    {
        "id": 7,
        "name": "Paciente 7",
    },
    {
        "id": 8,
        "name": "Paciente 8",
    },
    {
        "id": 9,
        "name": "Paciente 9",
    },
]


def index(request):
    return render(request, "templates\home.html", context={"cards": cards})


def command(request, id, cmd):
    return redirect("/")
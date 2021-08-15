from django.shortcuts import render, redirect, HttpResponse
import requests

# Create your views here.
# cards = [
#     {
#         "id": 1,
#         "name": "Subhasis Paul",
#         "image": "https://media-exp1.licdn.com/dms/image/C4D03AQE5iJhY2fOMaA/profile-displayphoto-shrink_800_800/0/1605475274253?e=1634169600&v=beta&t=OXxicamf2y4QufrrH_c5zSncVAqtxBw4rEU_2NITh_Y",
#         "college": "Narula Institute of Technology",
#         "roll": "96",
#     },
#     {
#         "id": 2,
#         "name": "Simran Kumari",
#         "image": "https://media-exp1.licdn.com/dms/image/C5603AQFcEYiO8ZHdbw/profile-displayphoto-shrink_800_800/0/1625846489464?e=1634169600&v=beta&t=GKL1tOeLLm1B-pV3OJRUTEbNWh1uiPYDpJNqNyULiNM",
#         "college": "Narula Institute of Technology",
#         "roll": "124",
#     },
#     {
#         "id": 3,
#         "name": "Barsha Pal",
#         "image": "https://media-exp1.licdn.com/dms/image/C4E03AQH3pfc65UHEeg/profile-displayphoto-shrink_800_800/0/1604145085479?e=1634169600&v=beta&t=V_be2RcP5734912ZRlGmqTxtstBvZWTjKHWft-Qubps",
#         "college": "Narula Institute of Technology",
#         "roll": "122",
#     },
#     {
#         "id": 4,
#         "name": "Suraj Maity",
#         "image": "https://media-exp1.licdn.com/dms/image/C4E03AQEqpTcrUqaA3Q/profile-displayphoto-shrink_800_800/0/1628011755535?e=1634169600&v=beta&t=Kp2oDf0WWMMVCSlOfxYHazmGee1latbSNi15IWE8Hto",
#         "college": "Narula Institute of Technology",
#         "roll": "93",
#     },
#     {
#         "id": 5,
#         "name": "Ayush",
#         "image": "https://media-exp1.licdn.com/dms/image/C4E03AQExyUIDw4XoOA/profile-displayphoto-shrink_800_800/0/1618897688768?e=1634169600&v=beta&t=V-CF3ipYiV5eAJIGvl7KpXhG4wszAHEWQt9g4Jr_oo0",
#         "college": "Narula Institute of Technology",
#         "roll": "121",
#     },
# ]

# credentials = [
#     {
#         "username": "Subhashis",
#         "password": "dev123"
#     },
#     {
#         "username": "Nikhil",
#         "password": "dev123"
#     },
#     {
#         "username": "Barsha",
#         "password": "dev123"
#     },
#     {
#         "username": "Simran",
#         "password": "dev123"
#     },
#     {
#         "username": "Ayush",
#         "password": "dev123"
#     },
#     {
#         "username": "Suraj",
#         "password": "dev123"
#     }
# ]


cards = requests.get('https://developapi.herokuapp.com/api/users/').json()

credentials = requests.get('https://developapi.herokuapp.com/api/cred/').json()

# auth = False


# def index(request):

#     return render(request, "index.html", context={"cards": cards}, )


def login(request):
    if(request.POST):
        login_data = request.POST.dict()
        username = login_data.get("username")
        password = login_data.get("password")
        # print(username, password)
        # print(credentials[0].get('username'))
        auth = False
        for cred in credentials:
            if(cred.get('username') == username and cred.get('password') == password):
                auth = True
        if(auth):
            return render(request, "index.html", context={"cards": cards},)
        else:
            # return HttpResponse("This is incorrect user")
            return render(request, "login.html", context={'color': 'red'})
    else:
        return render(request, "login.html", context={'color': 'none'})


def command(request, id, cmd):
    for card in cards:
        # print(card)
        if id == card["id"]:
            if cmd == "delete":
                cards.remove(card)
                # print('card removed')
    return render(request, "index.html", context={"cards": cards},)
    # return redirect("/")


# def default():
#     return redirect("/")

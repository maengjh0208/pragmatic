from django.shortcuts import render

from accountapp.models import HelloWorld


def hello_world(request):
    if request.method == "POST":
        text = request.POST.get("hello_world_input")

        # DB 저장
        new_hello_world = HelloWorld()
        new_hello_world.text = text
        new_hello_world.save()

        return render(request, 'accountapp/hello_world.html', context={'new_hello_world_output': new_hello_world})
    else:
        text = "Get Method"

        return render(request, 'accountapp/hello_world.html', context={'text': text})

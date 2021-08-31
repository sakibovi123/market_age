from django.shortcuts import render, HttpResponse, redirect
from ChatApp.models import ChatRoom, Message
from django.contrib.auth.models import User
from django.db.models import Q
# Create your views here.


def get_all_users(request):
    users = User.objects.exclude(username=request.user)
    
    args = {
        'users': users
    }
    return render(request, 'Test/index.html', args)


def user_details(request, id):
    user_details = User.objects.get(id=id)
    if request.method == 'POST':
        user_details = User.objects.get(id=id)
        wc_msg = request.POST.get('welcome_msg')
        sender = request.user
        
        form = ChatRoom.objects.create(
            user=user_details, sender=sender, welcome_msg=wc_msg)
        # print("Saved Data" + user + sender + welcome_msg)
        
        form.save()
        return redirect("room")

    args = {
        'user_details': user_details
    }
    return render(request, 'Test/user_details.html', args)



def room(request):
    room = ChatRoom.objects.filter(sender=request.user)
    # buyer_msg = ChatRoom.objects.filter(sender=request)
    args = {
        "room": room
    }
    return render(request, 'Test/room.html', args)


def continue_chat(request, id):
    msgs = ChatRoom.objects.get(id=id)
    
    # buyer_msg = ChatRoom.objects.filter()
    if request.method == 'POST':
        msgs = ChatRoom.objects.get(id=id)
        user = msgs.user
        sender = msgs.sender
        messages = request.POST.get('messages')
        print(user, sender)
        
        chat = Message.objects.create(
            user=user, sender=sender, messages=messages
        )
        
        chat.save()
        
        return HttpResponse("Message Sent my friend!")
    
    
    rec = Message.objects.filter(
            user=msgs.user
            # user=request.user
        )
    sen = Message.objects.filter(
        sender=msgs.sender
    )
    
    # rec = Message.objects.all()
    # sen = Message.objects.all()
    
    args = {
        "msgs": msgs,
        "rec": rec,
        "sen": sen
    }
    return render(request, 'Test/chat.html', args)






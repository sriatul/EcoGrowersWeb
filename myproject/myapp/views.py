from django.shortcuts import render
from django.contrib import messages

from .forms import CreateUserForm , LoginForm 
from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request , 'index.html')


from django.db.models import Q

from .models import State,Market,Commodity,CommodityData,AllData

from .forms import SubscribersForm  

# Create your views here.
def price(request):
    commodityid = request.GET.get('commodity',None)
    stateid = request.GET.get('state',None)
    marketid = request.GET.get('market',None)
    state= None
    market = None
    commodityData=None
    allData = None
    if commodityid:
        getcommodity = Commodity.objects.get(id = commodityid)
        state = State.objects.filter(commodity = getcommodity)
        allData = AllData.objects.filter(commodity = getcommodity)
        
    if stateid:
           getcommodity = Commodity.objects.get(id=commodityid)
           getstate = State.objects.get(Q(id=stateid) & Q(commodity=getcommodity))
           market = Market.objects.filter(state=getstate)
        
    if marketid:
            getmarket = Market.objects.filter(Q(id=marketid) & Q(state__commodity__id=commodityid)).first()
        
            commodityData = CommodityData.objects.filter(market=getmarket)
            
        
    commodity = Commodity.objects.all()
    return render (request,'mandi.html',{'commodity':commodity,'state':state,'market':market,'commodityData':commodityData,'allData':allData})

            
            
def about(request):
    return render(request,'about_us.html')


def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact_us.html')


def tools(request):
    return render(request,'tools.html')

def precesion(request):
    return render(request,'precesion.html')
def animals(request):
    return render(request,'animals.html')

    

# CHAT ROOM
from django.shortcuts import render,redirect
from .models import Room , Message
from django.http import HttpResponse,JsonResponse
# Create your views here.
def Chat_home(request):
    return render(request,'Chat_home.html')

# def room(request,room):
#     username = request.GET.get("username")
#     room_details = Room.objects.get(name=room)
#     return render(request,'Chat_room.html',{
#         'username':username,
#         'room':room,
#         'room_details':room_details
#     })
    
    
def checkview(request):
    room = request.POST['name']
    username =request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message,user=username,room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')



def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    
    return JsonResponse({"messages": list(messages.values())})

    
    
   
   
 


# Register
def register(request):
    
    form = CreateUserForm()
    
    if request.method == "POST":
        
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            
            form.save()
            messages.success(request,"Successfully")
            return redirect('login')
    context = {'form':form}
    return render(request,'register.html',context)


# Login

def login(request):
    form = LoginForm(request, data=request.POST)
    
    if request.method == "POST":  
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')        
            # USER
            user = authenticate(request, username=username ,password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('index')
            
    context = {'form':form}
    
    return render(request,'login.html',context)

# LogOut

def user_logout(request):
    
    auth.logout(request)
    
    return redirect("login")    



def subscriber(request):
    if request.method == 'POST':
        form = SubscribersForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully subscribed")
            return redirect('index')
    else:
        form = SubscribersForm()

    context = {'form': form}
    return render(request, 'mail_letter.html', context)
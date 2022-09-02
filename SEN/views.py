from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
# Create your views here.
def upload_image(request):
   if request.method == 'GET':
    return render(request, 'upload_image.html')
   elif request.method == 'POST':
       form = ImageForm(request.POST, request.FILES)
   if form.is_valid():
    new_image = Image(  image = form.cleaned_data["image"],
    name = form.cleaned_data["name"]) 
    new_image.save()
    return HttpResponseRedirect('image_gallery/')

#ver_laimagen 
def image_gallery(request):
        images =  Image.objects.all()
        return render (request ,'image_gallery.html' ,{'images': images})
           
def generate_request(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()



def calendario(request):
    return render (request, 'calendario.html')


def  index (request):
    return render (request, 'index.html',{})

def  pago (request):
    return render (request, 'pago.html,',{})

 
def  suscripcion(request):
     return render (request, 'matricula.html',{})    
 
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("/account/loggedin/")
    else:
        # Show an error page
        return HttpResponseRedirect("/account/invalid/")

def user(request):
    return render (request,'user.html')
    

def cita (request):
    return render (request 'cita.html')
     
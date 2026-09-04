from django.shortcuts import render, redirect
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def login(request):
    error = None
    
    if request.method == 'POST':
        name = request.POST.get('name', '').lower().strip()
        password = request.POST.get('password', '').lower().strip()
        
        # Password: 04 september
        valid_password = password in ['04 september', '04september', '4 september', '4september', '04-09', '0409']
        
        if valid_password:
            request.session['authenticated'] = True
            request.session['name'] = name
            return redirect('birthday:landing')
        else:
            error = 'Password salah! Coba lagi ya sayang 💕'
    
    return render(request, 'birthday/login.html', {'error': error})

def landing(request):
    if not request.session.get('authenticated'):
        return redirect('birthday:login')
    return render(request, 'birthday/landing.html')

def main(request):
    if not request.session.get('authenticated'):
        return redirect('birthday:login')
    
    name = request.session.get('name', 'Sayangku')
    display_name = ' '.join(word.capitalize() for word in name.split())
    
    return render(request, 'birthday/main.html', {'name': display_name})

def logout(request):
    request.session.flush()
    return redirect('birthday:login')

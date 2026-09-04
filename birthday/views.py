from django.shortcuts import render, redirect
from django.http import JsonResponse
import json

def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name', '').lower().strip()
        password = data.get('password', '').lower().strip()
        
        # Password: 04 september (tanggal ultah & jadian)
        valid_password = password in ['04 september', '04september', '4 september', '4september', '04-09', '0409']
        
        if valid_password:
            request.session['authenticated'] = True
            request.session['name'] = name
            return JsonResponse({'status': 'success', 'message': 'Selamat datang!'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Password salah! Coba lagi ya sayang 💕'})
    
    return render(request, 'birthday/login.html')

def landing(request):
    if not request.session.get('authenticated'):
        return redirect('birthday:login')
    return render(request, 'birthday/landing.html')

def main(request):
    if not request.session.get('authenticated'):
        return redirect('birthday:login')
    
    name = request.session.get('name', 'Sayangku')
    # Capitalize each word
    display_name = ' '.join(word.capitalize() for word in name.split())
    
    return render(request, 'birthday/main.html', {'name': display_name})

def logout(request):
    request.session.flush()
    return redirect('birthday:login')

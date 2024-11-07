from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Ticket, TicketReply

@login_required
def ticket_list(request):
    tickets = Ticket.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'active_tab': 'support',
        'tickets': tickets,
        'open_count': tickets.filter(status='open').count(),
        'in_progress_count': tickets.filter(status='in_progress').count(),
        'closed_count': tickets.filter(status='closed').count(),
    }
    return render(request, 'user_dashboard/tickets/ticket_list.html', context)

@login_required
def ticket_create(request):
    context = {
        'active_tab': 'support'
    }
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        priority = request.POST.get('priority')
        
        if subject and message:
            ticket = Ticket.objects.create(
                user=request.user,
                subject=subject,
                message=message,
                priority=priority
            )
            messages.success(request, 'Ticket created successfully!')
            return redirect('ticket_detail', pk=ticket.pk)
    return render(request, 'user_dashboard/tickets/ticket_create.html', context)

@login_required
def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk, user=request.user)
    
    if request.method == 'POST':
        message = request.POST.get('message')
        if message:
            TicketReply.objects.create(
                ticket=ticket,
                user=request.user,
                message=message
            )
            messages.success(request, 'Reply added successfully!')
            return redirect('ticket_detail', pk=ticket.pk)
    
    return render(request, 'user_dashboard/tickets/ticket_detail.html', {
        'ticket': ticket,
        'replies': ticket.replies.all()
    })

@login_required
def dashboard(request):
    context = {
        'active_tab': 'dashboard'
    }
    return render(request, 'user_dashboard/dashboard.html', context)

@login_required
def profile(request):
    if request.method == 'POST':
        # Handle basic information update
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        timezone = request.POST.get('timezone')
        password = request.POST.get('password')
        
        user = request.user
        user.first_name = first_name
        user.last_name = last_name
        user.timezone = timezone
        
        if password:
            user.set_password(password)
        
        user.save()
        messages.success(request, 'Profile updated successfully!')
        
    context = {
        'active_tab': 'profile'
    }
    return render(request, 'user_dashboard/profile.html', context)

@login_required
def profile_more(request):
    if request.method == 'POST':
        # Handle additional information update
        user = request.user
        user.website = request.POST.get('website')
        user.phone = request.POST.get('phone')
        user.skype = request.POST.get('skype')
        user.whatsapp = request.POST.get('whatsapp')
        user.address = request.POST.get('address')
        user.city = request.POST.get('city')
        user.save()
        
        messages.success(request, 'Additional information updated successfully!')
        return redirect('user_profile')
    
    return redirect('user_profile')

@login_required
def security_settings(request):
    context = {
        'active_tab': 'security'
    }
    return render(request, 'user_dashboard/security.html', context)

@login_required
def posts(request):
    context = {
        'active_tab': 'posts'
    }
    return render(request, 'user_dashboard/posts.html', context)

@login_required
def favorites(request):
    context = {
        'active_tab': 'favorites'
    }
    return render(request, 'user_dashboard/favorites.html', context)

@login_required
def messages(request):
    context = {
        'active_tab': 'messages'
    }
    return render(request, 'user_dashboard/messages.html', context)

@login_required
def notifications(request):
    context = {
        'active_tab': 'notifications'
    }
    return render(request, 'user_dashboard/notifications.html', context)

@login_required
def preferences(request):
    context = {
        'active_tab': 'preferences'
    }
    return render(request, 'user_dashboard/preferences.html', context)

@login_required
def new_order(request):
    context = {
        'active_tab': 'order'
    }
    if request.method == 'POST':
        # Handle form submission here
        pass
    return render(request, 'user_dashboard/order/new_order.html', context)

@login_required
def order_log(request):
    orders = [{
        'order_id': '390480',
        'api_order': 'API123',
        'user': 'john_doe',
        'details': 'YouTube subscribers lifetime - 750',
        'created': '2024-11-04 05:25:04',
        'status': 'In Progress',
        'api_response': 'Success',
    }]
    context = {
        'active_tab': 'order',
        'orders': orders
    }
    return render(request, 'user_dashboard/order/order_log.html', context)

@login_required
def services(request):
    services = [{
        'id': '26192',
        'name': 'Facebook page like + Followers Non Drop All Type of page',
        'rate': '0.28',
        'min_max': '100 / 50000',
        'details': 'Details'
    }]
    context = {
        'active_tab': 'services',
        'services': services
    }
    return render(request, 'user_dashboard/services.html', context)

@login_required
def api_documentation(request):
    api_data = {
        'api_key': '61AMKvJNRmP2M2JjFkTWZwzsnlLzNzpl',
        'api_url': 'https://boostmasterbdpro.com/api/v1',
        'endpoints': []
    }
    context = {
        'active_tab': 'api',
        'api_data': api_data
    }
    return render(request, 'user_dashboard/api_documentation.html', context)

@login_required
def add_funds(request):
    context = {
        'active_tab': 'add_funds',
        'payment_methods': [
            {'id': 'perfectmoney', 'name': 'Perfectmoney'},
            {'id': 'bkash', 'name': 'Bkash'},
            {'id': 'manual', 'name': 'Manual Payment'},
        ]
    }
    return render(request, 'user_dashboard/add_funds.html', context)

@login_required
def transaction_logs(request):
    transactions = [
        {
            'id': 1,
            'amount': 4.08,
            'payment_method': 'Bkash',
            'status': 'Waiting for buyer funds...',
            'created': '2023-01-20 18:03:24'
        }
    ]
    context = {
        'active_tab': 'transactions',
        'transactions': transactions
    }
    return render(request, 'user_dashboard/transaction_logs.html', context)

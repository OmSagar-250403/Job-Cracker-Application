from django.shortcuts import redirect, render
from templates import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.http import HttpResponseRedirect,HttpResponse
from .models import Profile
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from accounts.models import Cart, CartItem, Product, SizeVariant
from products.models import *
from django.http import JsonResponse
from django.views.decorators.http import require_POST

def login_page(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)

        if not user_obj.exists():
            messages.warning(request, 'Account not found.')
            return HttpResponseRedirect(request.path_info)


        if not user_obj[0].profile.is_email_verified:
            messages.warning(request, 'Your account is not verified.')
            return HttpResponseRedirect(request.path_info)

        user_obj = authenticate(username = email , password= password)
        if user_obj:
            login(request , user_obj)
            return redirect('/')

        

        messages.warning(request, 'Invalid credentials')
        return HttpResponseRedirect(request.path_info)


    return render(request ,'accounts/login.html')

def register_page(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)

        if user_obj.exists():
            messages.warning(request, 'Email is already taken.')
            return HttpResponseRedirect(request.path_info)

        print(email)

        user_obj = User.objects.create(first_name = first_name , last_name= last_name , email = email , username = email)
        user_obj.set_password(password)
        user_obj.save()

        messages.success(request, 'An email has been sent on your mail.')
        return HttpResponseRedirect(request.path_info)


    return render(request ,'accounts/register.html')


def activate_email(request , email_token):
    try:
        user = Profile.objects.get(email_token= email_token)
        user.is_email_verified = True
        user.save()
        return redirect('/')
    except Exception as e:
        return HttpResponse('Invalid Email token')
    



@require_POST
def add_to_cart(request):
    product_slug = request.POST.get('product_slug')
    color_variant_id = request.POST.get('color_variant')
    size_variant_id = request.POST.get('size_variant')

    product = get_object_or_404(Product, slug=product_slug)

    cart, created = Cart.objects.get_or_create(user=request.user)

    color_variant_obj = None
    size_variant_obj = None

    if color_variant_id:
        color_variant_obj = get_object_or_404(ColorVariant, id=color_variant_id)

    if size_variant_id:
        size_variant_obj = get_object_or_404(SizeVariant, id=size_variant_id)

    try:
        cart_item = CartItem.objects.get(
            cart=cart,
            product=product,
            color_variant=color_variant_obj,
            size_variant=size_variant_obj
        )
        cart_item.quantity += 1
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            cart=cart,
            product=product,
            color_variant=color_variant_obj,
            size_variant=size_variant_obj,
            quantity=1
        )
    cart_item.save()

    return JsonResponse({'success': True}) 
 


def remove_from_cart(request, slug):
    try:
        cart_item = get_object_or_404(CartItem, product__slug=slug, cart__user=request.user, cart__is_paid=False)
        cart_item.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    except Exception as e:
        print(f"Error removing from cart: {e}")
        return redirect('cart')  # Redirect to cart page in case of error


from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.contrib import messages

def cart(request):
    try:
        cart = Cart.objects.get(is_paid=False, user=request.user) 
    except Cart.DoesNotExist:
        cart = Cart.objects.create(user=request.user) 

    if request.method == 'POST':
        coupon_code = request.POST.get('coupon')
        if coupon_code:
            try:
                coupon = Coupon.objects.get(coupon_code=coupon_code)
                if cart.coupon:  # Check if coupon already exists
                    messages.warning(request, 'Coupon already exists.')
                else:
                    cart.coupon = coupon
                    cart.save()
                    messages.success(request, 'Coupon applied.')
            except Coupon.DoesNotExist:
                messages.warning(request, 'Invalid Coupon Code.')
        else:
            messages.warning(request, 'Coupon Code not exist.') 

        return redirect('cart')  # Redirect after processing coupon

    return render(request, 'accounts/cart.html', {'cart': cart}) 
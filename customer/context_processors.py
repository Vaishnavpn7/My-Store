from api.models import Carts


def cart_count(request):
    if request.user.is_authenticated:
        count = Carts.objects.filter(user=request.user, status='in-cart').count()
    else:
        count = 0
    return {'count': count}

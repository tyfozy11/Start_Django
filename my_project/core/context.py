from core.models import Category


def get__all_categories(request):
    return {
        'categories': Category.objects.all()
    }

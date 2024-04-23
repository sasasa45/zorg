from item.models import Items


class ListItemsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.items = Items.objects.all().order_by('slug').values('name', 'slug')
        response = self.get_response(request)
        return response

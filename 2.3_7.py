class HandlerGET:
    def __init__(self, funk):
        self.__funk = funk

    def __call__(self, *args, **kwargs):
        if 'method' not in args:
            pass

    def get(self, func, request, *args, **kwargs):
        if 'method' in request and request['method'] == "GET" or 'method' not in request:
            return "GET: Сергей Балакирев"
        if 'method' in request and request['method'] != "GET":
            return None


@HandlerGET
def contact(request):
    return "Сергей Балакирев"


res = contact({"method": "GET", "url": "contact.html"})

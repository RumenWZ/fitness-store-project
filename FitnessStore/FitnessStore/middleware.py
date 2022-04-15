

def handle_exception(get_response):
    def middleware(request):
        response = get_response(request)
        pass

    return middleware()
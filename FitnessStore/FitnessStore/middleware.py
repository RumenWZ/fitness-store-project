from django.shortcuts import render

from FitnessStore.main.views import error404, internal_server_error


def handle_exception(get_response):
    def middleware(request):
        response = get_response(request)
        if response.status_code == 404:
            return error404(request)
        elif response.status_code >= 500:
            return internal_server_error(request)
        return response

    return middleware
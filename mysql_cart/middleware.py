from django.http import HttpResponse

class PrintMiddleWareLifeCyle(object):
    # only invoked one once on instantiation when the object is created initially on server start
    def __init__(self, get_response):
        print('▐▓▒░ ͶΔͲΞ ░▒▓▌ Yo, you got the custom middleware: PrintMiddleWareLifeCycle instantiated now!')
        self.get_response=get_response

    # this call method is invoked on EVERY INCOMING REQUEST
    def __call__(self, request):
        # print('▐▓▒░ ͶΔͲΞ ░▒▓▌ mysql_cart.PrintMiddleWareLifeCyle interupts everything BEFORE the view is executed')
        # this will occure before the next middleware in the chain ... OR it will occure direclty before the view.
        response = self.get_response(request)
        # print('▐▓▒░ ͶΔͲΞ ░▒▓▌ mysql_cart.PrintMiddleWareLifeCyle interupts everything AFTER the view is executed')
        return response

class PrintMiddleWareExceptionHandle(object):
    # only invoked one once on instantiation when the object is created initially on server start
    def __init__(self, get_response):
        self.get_response=get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if request.path_info == '/aesspoded-evrahdang/':
            return HttpResponse("<h1>HOED MAH BARE!</h1><p>Somephan aesspode'd evrahdang.  Y'all baeder caughw Nate.</p>")
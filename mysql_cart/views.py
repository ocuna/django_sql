from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,DeleteView
from mysql_cart.models import SKUs


class SKUshop(ListView):
    model = SKUs #default context_object_name = SKUs_list
    #pushing a button here should add products to the cart & throw a notification
    template_name = 'shop.html'
    context_object_name = 'SKUs'

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Shop SKUs'
        return context

class SKUdetail(DetailView):
    model = SKUs
    context_object_name = 'SKUs'
    # assert False, model
    template_name = 'SKUdetail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'SKUs Details'
        return context

class SKUupdate(UpdateView):
    model = SKUs
    fields = ('sku','mfg','name','desc','price')
    template_name = 'SKUupdate.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Update SKUs'
        return context

class SKUcreate(CreateView):
    model = SKUs
    fields = ('sku','mfg','name','desc','price')
    # context is passed the "form" from the model here.
    template_name = 'SKUcreate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['heading'] = 'Create SKUs'
        return context

class SKUdelete(DeleteView):
    model = SKUs
    template_name = 'SKUConfirmDelete.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the view
        context['heading'] = 'Delete SKU'
        return context

def Cart(request):
    context = {
        'title' : "Shopping Cart"
    }
    return render(request,'cart.html', context)







##################################################
################# COOKIE SANDBOX #################
##################################################
def Cookie(request,arg = None):
    suf = '</p><p><a href="/">Cookies are dumb ... </a></p>'

    if arg == 'cookie_verify':
        s = 'cookies are disabled.'
        pre = '<h1>Verify Cookie</h1><p><a href="/cookie/cookie_verify">Re-Verify Cookie</a></p><p><a href="/cookie/">back to Cookie LP</a></p><p>'
        if request.session.test_cookie_worked() :
            s = pre + 'cookies are enabled.' + suf
        else:
            s = pre + 'test cookie was not enabled, but is now.' + suf
            request.session.set_test_cookie()

        return HttpResponse(s)

    if arg == 'cookie_count':
        if 'count' in request.COOKIES:
            count = int(request.COOKIES['count']) + 1
        else:
            count = 0
        pre = '<h1>Count Cookies</h1><p><a href="/cookie/cookie_verify">Verify Cookie</a></p><p><a href="/cookie/cookie_count">Cookie Counting</a></p>'
        s = pre + '<p>Cookie Counting Value: ' + str(count) + '</p>' + suf
        # response needs to contain the HttpResponse Object (which has the cookie)
        # sin order to create set or update the cookie before sending it back to the user1
        response = HttpResponse(s)
        response.set_cookie('count',count)
        return response
        

    if arg == 'cookie_delete':
        if request.session.test_cookie_worked() :
            request.session.delete_test_cookie()
        if 'count' in request.COOKIES:
            temp = str(request.COOKIES['count'])
            pre = '<h1>Delete Cookies</h1><p>You used to have a cookie value of: ' + temp + '</p><p><a href="/cookie/">back to Cookie LP</a></p>'
            s = pre + suf
            response = HttpResponse(s)
            response.delete_cookie('count')
            return response
        else:
            pre = '<h1>Delete Cookies</h1><p>You must have already deleted your cookie count.</p><p><a href="/cookie/">back to Cookie LP</a></p>'
            s = pre + suf
            return HttpResponse(s)
        
    pre = '<h1>Cookie LP</h1><p><a href="/cookie/cookie_verify">Verify Cookie</a></p><p><a href="/cookie/cookie_count">Cookie Counting</a></p><p><a href="/cookie/cookie_delete">Cookie Delete</a></p>'
    s = pre + 'This is designed to simply test the cookie functionality of Django.' + suf
    return HttpResponse(s)

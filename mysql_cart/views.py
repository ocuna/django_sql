from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.template import loader
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,DeleteView
from mysql_cart.models import SKUs
from mysql_cart.easy import process_list
import json


class SKUshop(ListView):
    model = SKUs #default context_object_name = SKUs_list
    #pushing a button here should add products to the cart & throw a notification
    template_name = 'shop.html'
    context_object_name = 'SKUs'
    # initial = {'key': 'value'}

    def get_context_data(self,**kwargs):
        # in get context from 'self' we can retrieve the request data
        # context['temp'] = self.request.GET
        context = super().get_context_data(**kwargs)
        return context

    # from https://docs.djangoproject.com/en/3.1/topics/class-based-views/intro/#handling-forms-with-class-based-views
    def get(self, request, *args, **kwargs):
        template = loader.get_template(self.template_name)
        response = HttpResponse()
        cart_list = []
        cart_json = ''

        if 'cart' in request.COOKIES.keys():
            cart_json = request.COOKIES['cart']
            cart_list = json.loads(cart_json)
       
        if 'pk' in kwargs:
            cart_list.append(kwargs['pk'])
            #CookieProcessor(HttpResponse,'billy','goat').add
            cart_json = json.dumps(cart_list)
            response.set_cookie('cart',cart_json)

        context = {
            'heading' : 'Shop SKUs',
            'SKUs' : self.model.objects.all(),
            'DEBUG' : request.COOKIES,
            'CART' : cart_list,
            'JSON' : cart_json
        }
        response.write(template.render(context))
        return response
    # 

def Cart(request):
    cart_items = []
    total = 0
    if 'cart' in request.COOKIES.keys():
        cart_html = '<p>You Bought This Stuff: </p>'
        process = process_list(json.loads(request.COOKIES['cart']))
        uniques = process.uniques()
        count_uniques = process.count_uniques()
 
        for uid in uniques:
            thissku = SKUs.objects.only('id','name','sku','price').get(pk=uid)
            thisqty = count_uniques[uid]
            total = total + (int(thisqty) * int(thissku.price))
            cart_items.append({'sku':thissku.id, 'name': thissku.name, 'price':thissku.price, 'qty':thisqty}) 
    
    else:
        cart_html = '<p><a href="/shop">Go shop for stuff</a>, your cart is empty..</p>'

    context = {
        'heading' : "Shopping Cart",
        'cart_html' : cart_html,
        'cart_items':cart_items,
        'total':total
    }
    return render(request,'cart.html', context)

def EmptyCart(request):
    response = HttpResponseRedirect('/shop/cart/')
    response.delete_cookie('cart')
    return response


class SKUdetail(DetailView):
    model = SKUs
    context_object_name = 'SKUs'
    # assert False, model
    template_name = 'SKUdetail.html'

    def get_context_data(self, **kwargs):
        # set the count for this SKU with the session
        sessionname = 'SKU_' + str(self.kwargs['pk']) + '_count'
        #use the session name to get the prior number of visits
        count = self.request.session.get(sessionname, 0)
        # increment that visit count
        count = count + 1
        # set the session variable with the new modified count of +1
        self.request.session[sessionname] = count

        context = super().get_context_data(**kwargs)
        context['heading'] = 'SKUs Details'
        context['count'] = count
        context['session'] = self.request.session
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

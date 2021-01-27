from django.shortcuts import render
from django.http import HttpResponse

# we are 
def Cookie(request,arg = None):
    suf = '</p>'
    s = 'cookies are disabled.'
    if arg == 'cookie_verify':
        pre = '<h1>Verify Cookie</h1><p><a href="/cart/cookie/cookie_verify">Re-Verify Cookie</a></p><p><a href="/cart/cookie/">back to Cookie LP</a></p><p>'
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
        pre = '<h1>Count Cookies</h1><p><a href="/cart/cookie/cookie_verify">Verify Cookie</a></p><p><a href="/cart/cookie/cookie_count">Cookie Counting</a></p>'
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
            pre = '<h1>Delete Cookies</h1><p>You used to have a cookie value of: ' + temp + '</p><p><a href="/cart/cookie/">back to Cookie LP</a></p>'
            s = pre + suf
            response = HttpResponse(s)
            response.delete_cookie('count')
            return response
        else:
            pre = '<h1>Delete Cookies</h1><p>You must have already deleted your cookie count.</p><p><a href="/cart/cookie/">back to Cookie LP</a></p>'
            s = pre + suf
            return HttpResponse(s)
        
    pre = '<h1>Cookie LP</h1><p><a href="/cart/cookie/cookie_verify">Verify Cookie</a></p><p><a href="/cart/cookie/cookie_count">Cookie Counting</a></p><p><a href="/cart/cookie/cookie_delete">Cookie Delete</a></p>'
    s = pre + 'This is designed to simply test the cookie functionality of Django.' + suf
    return HttpResponse(s)

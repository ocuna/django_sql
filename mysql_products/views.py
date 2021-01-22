from django.shortcuts import render

def products(request,category):

    # this view retrieves product/'category'
    # switch_category function uses a switch-like processing method to 
    # pick the correct function from what is defined within
    # each function returns a matching product_dict
    # finaly, the lambda function below returns a string  
    def switch_category(category):
        
        def electronics():
            product_d={
                'product1':'Mac',
                'product2':'IPhone',
                'product3':'Dell',
                'image1':'mac_logo.jpg',
                'image2':'iphone_logo.jpg',
                'image3':'dell_logo.jpg',
            }
            return product_d

        def toys():
            product_d={
                'product1':'Remote Car',
                'product2':'Drone',
                'product3':'Rocket Launcher',
                'image1':'rc_car.jpg',
                'image2':'drone.jpg',
                'image3':'rl_nerf.jpg',
            }
            return product_d

        def shoes():
            product_d={
                'product1':'Nike',
                'product2':'Adidas',
                'product3':'Reebok',
                'image1':'nike_shoe.jpg',
                'image2':'adidas_shoe.jpg',
                'image3':'reebok_shoe.jpg',
            }
            return product_d

        switcher_d = {
            # this is a dictionary of the above functions
            'electronics': electronics,
            'toys': toys,
            'shoes': shoes
        }

        product_d={'error':'Invalid Product'}

        func = switcher_d.get(category, lambda: product_d)
        return func()

    # output should return a function.
    # assert False, switch_category(category)
    context = {
        'product_d' : switch_category(category),
        'heading' : category
    }
    return render(request, 'products.html', context)


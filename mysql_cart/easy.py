from django.http import HttpResponse
# requires the request object from views.py to function - other Key Value pairs are required for adding and removing cookies
class process_list:
    output_list = []
    output_dict = {}
    
    def __init__ (self,list):
        self.list = list

    def uniques(self):
        if type(self.list).__name__ == 'list':
            for x in self.list:
                if x not in self.output_list: 
                    self.output_list.append(x)
        # assert False, self.output_list
        return self.output_list 
    

    def count_uniques(self):
        only_unique = self.uniques()
        for u in only_unique:
            count = 0
            for element in self.list:
                if element == u:
                    count = count + 1
            self.output_dict[u] = count
        return self.output_dict
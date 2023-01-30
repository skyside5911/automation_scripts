class MyMiddleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print("one time initialization")
    def __call__(self,request):
       print("this is before view")
       response=self.get_response(request)
       print("this is after view")
       return response

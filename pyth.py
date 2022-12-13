class Example:
	def __init__(self, response):
		self.response=response
	
	# Defining __call__ method
	def __call__(self, request):
		print("Start", self.name)
        response=self.response(request)
        print("End", self.name)
        
class test1(Example):
    name="First"
class test2(Example):
    name="Second"
class test3(Example):
    name="Three"

# Author:GaoYuCai
def my_shiny_new_decorator(a_function_to_decorator):
    def the_wrapper_around_the_original_function():
        print("Before the function runs")
        a_function_to_decorator()
        print("After the function runs")
    return  the_wrapper_around_the_original_function

def a_stand_alone_function():
    print("I am a stand alone function,don't you  dare modify me")
#a_stand_alone_decorator=my_shiny_new_decorator(a_stand_alone_function)
#a_stand_alone_decorator()
#a_stand_alone_function=my_shiny_new_decorator(a_stand_alone_function)
#a_stand_alone_function()
@my_shiny_new_decorator
def anthor_new_decorator():
    print("Leave me alone")

anthor_new_decorator()
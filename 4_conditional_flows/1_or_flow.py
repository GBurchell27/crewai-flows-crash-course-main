# This flow, OrExampleFlow, demonstrates a conditional flow using CrewAI.
# It uses the or_() function to combine two methods into a single conditional flow.
# The flow is initiated by creating an instance of OrExampleFlow and calling the kickoff() method.
# The final state is printed after the flow has completed.  



from crewai.flow.flow import Flow, listen, or_, start # or_ is a function that combines two methods into a single conditional flow

class OrExampleFlow(Flow):

    @start()
    def start_method(self):
        print("Starting flow")
        return "Hello from the start method"

    @listen(start_method)
    def second_method(self):
        print("Second method")
        return "Hello from the second method"

    @listen(or_(start_method, second_method)) # This listens for either the start_method or second_method to finish and then calls the logger function (prints the result   )
    def logger(self, result):
        print(f"Logger: {result}")


flow = OrExampleFlow()
flow.kickoff()

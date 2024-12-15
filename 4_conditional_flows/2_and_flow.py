from crewai.flow.flow import Flow, and_, listen, start


class AndExampleFlow(Flow):

    @start()
    def start_method(self):
        print("---- Start Method ----")
        self.state["greeting"] = "Hello from the start method"

    @listen(start_method)
    def second_method(self):
        print("---- Second Method ----")
        self.state["joke"] = "What do computers eat? Microchips."

    @listen(and_(start_method, second_method)) # This listens for both the start_method AND second_method to finish, ONLY THEN does it the logger function (prints the result)
    def logger(self):
        print("---- Logger ----")
        print(self.state)


flow = AndExampleFlow()
flow.kickoff()

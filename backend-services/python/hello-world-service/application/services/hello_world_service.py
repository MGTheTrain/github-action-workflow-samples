from domain.interfaces.ihello_world_service import IHelloWorldService

class HelloWorldService(IHelloWorldService):
    def get_hello_world_message(self):
        return "Hello, World from Python"
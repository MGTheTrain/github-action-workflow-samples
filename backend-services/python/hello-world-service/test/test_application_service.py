import pytest
from application.services.hello_world_service import HelloWorldService

class TestHelloWorldService:
    def test_get_hello_world_message(self):
        # Arrange
        hello_world_service = HelloWorldService()

        # Act
        result = hello_world_service.get_hello_world_message()

        # Assert
        assert result == "Hello, World from Python"

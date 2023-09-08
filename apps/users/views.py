from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import RegisterSerializer


class RegisterAPIView(GenericAPIView):
    """
    This class is used to handle the registration of users in an API.
    """
    serializer_class = RegisterSerializer

    def post(self, request) -> Response:
        """
        This method is responsible for handling the HTTP POST request for user registration in an API.
        It receives the request data, validates it and saves the serialized data if it is valid.
        """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

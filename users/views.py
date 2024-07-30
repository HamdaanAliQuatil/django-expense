from rest_framework import generics
from rest_framework.exceptions import NotFound
from .models import User
from .serializers import UserSerializer


class UserCreateView(generics.CreateAPIView):
    """
    API view for creating a new user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    """
    API view for retrieving a user by ID.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        """
        Retrieve the user object based on the provided ID.
        Raises a NotFound exception if the user does not exist.
        """
        try:
            user_id = self.kwargs['pk']
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise NotFound("User not found.")

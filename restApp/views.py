from rest_framework.response import Response
from rest_framework import generics
from . models import Posts
from . serializers import PostsSerializer
from rest_framework.permissions import IsAuthenticated

class PostsView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Posts.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PostsSerializer(queryset, many=True)
        return Response(serializer.data)
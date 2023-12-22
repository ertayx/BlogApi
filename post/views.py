from rest_framework import generics, permissions, mixins, viewsets
from rest_framework.viewsets import ModelViewSet
import django_filters
from post.filters import PostModelFilter
from .serializers import PostSerializer
from .models import Post

class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_class = PostModelFilter

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)
        return queryset







# class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     lookup_field = 'id'
#     serializer_class = PostSerializer
#     permission_classes = [permissions.IsAuthenticated]

# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
    

# написать FullCRUD на ModelViewSet(Post)
# n+1 & lazy queryset
# mixins | generics
# написать логику поиска и филтрации для постов
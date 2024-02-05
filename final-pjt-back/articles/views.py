from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer
from .models import Article, Comment
from accounts.models import Carts
from accounts.serializers import CartsSerializer


@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def article_list(request):
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        article_data = ArticleListSerializer(articles, many=True).data

        for article in article_data:
            user_id = article['user']  # 각 아티클의 사용자 ID 가져오기
            carts = Carts.objects.filter(user_id=user_id)
            carts_data = CartsSerializer(carts, many=True).data
            article['carts'] = carts_data  # 각 아티클에 카트 정보 추가

        return Response(article_data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes([IsAuthenticated])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        article_data = serializer.data

        user_id = article_data['user']  # 아티클의 사용자 ID 가져오기
        carts = Carts.objects.filter(user_id=user_id)
        carts_data = CartsSerializer(carts, many=True).data

        article_data['carts'] = carts_data  # 아티클에 카트 정보 추가

        return Response(article_data)

    elif request.method == 'PUT':
        if request.user != article.user:
            return Response({'error': '이 게시물에 대한 수정 권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        if request.user != article.user:
            return Response({'error': '이 게시물에 대한 삭제 권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

        article.delete()
        return Response({'message': '게시물 삭제가 완료되었습니다.'}, status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated])
def comment_list(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        comments = get_list_or_404(Comment, article=article)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(article=article, user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def comment_detail(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk, article=article)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        if request.user != comment.user:
            return Response({'error': '이 댓글에 대한 수정 권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        if request.user != comment.user:
            return Response({'error': '이 댓글에 대한 삭제 권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

        comment.delete()
        return Response({'message': '댓글 삭제가 완료되었습니다.'}, status=status.HTTP_204_NO_CONTENT)
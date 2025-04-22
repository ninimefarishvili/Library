from ninja import Router
from .models import Book
from .serializers import BookSchema
from django.shortcuts import get_object_or_404
import json
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from ninja.security import HttpBearer
from rest_framework_simplejwt.authentication import JWTAuthentication

router = Router()

@router.get("/books")
def get_books(request):
    books = Book.objects.all()  
    return [BookSchema.from_orm(book) for book in books]  

@router.get("/borrowedbooks")
def borrowed_books(request):
    borrowed_books = books 
    borrowed = BorrowedBook.objects.all()
    return [BorrowedBookSchema.from_orm(book) for book in borrowed]


@router.get("/Genre")
def get_genres(request):
    genres = Genre.objects.all()  
    return [GenreSchema.from_orm(genre) for genre in genres]  


auth_router = Router()

@auth_router.post("/token")
def get_token(request, username: str, password: str):
    user = authenticate(username=username, password=password)

    if user:
        refresh = RefreshToken.for_user(user)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
    return {"error": "Invalid credentials"}, 401


class JWTBearer(HttpBearer):
    def authenticate(self, request, token):
        try:
            auth = JWTAuthentication()
            validated_token = auth.get_validated_token(token)
            user = auth.get_user(validated_token)
            return user  
        except Exception as e:
            print(f"Authentication failed: {e}")
            return None

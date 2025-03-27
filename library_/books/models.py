from ninja import Router
from .models import Book, Genre
from .serializers import BookSchema, GenreSchema

router = Router()

@router.get("/books")
def get_books(request):
    books = Book.objects.all()  
    return [BookSchema.from_orm(book) for book in books]  

@router.get("/borrowedbooks")
def borrowed_books(request):
    
    borrowed_books = Book.objects.filter(borrowed_by__isnull=False) 
    return [BookSchema.from_orm(book) for book in borrowed_books]

@router.get("/availablebooks")
def available_books(request):
    
    available_books = Book.objects.filter(borrowed_by__isnull=True) 
    return [BookSchema.from_orm(book) for book in available_books]

@router.get("/genres")
def get_genres(request):
    genres = Genre.objects.all()  
    return [GenreSchema.from_orm(genre) for genre in genres]
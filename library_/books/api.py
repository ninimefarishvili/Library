from ninja import Router
from .models import Book
from .serializers import BookSchema

router = Router()

@router.get("/books")
def get_books(request):
    books = Book.objects.all()  
    return [BookSchema.from_orm(book) for book in books]  

@router.get("/Genre")
def get_genres(request):
    genres = Genre.objects.all()  
    return [GenreSchema.from_orm(genre) for genre in genres]  

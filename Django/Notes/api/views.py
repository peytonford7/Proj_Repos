from .forms import NoteForm, TodoForm
from .models import Note, Todo

from rest_framework.response import Response
from rest_framework.decorators import api_view
from web_project.serializers import NoteSerializer, TodoSerializer

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
        {
            'Endpoint': '/todo/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of todo lists'
        },
        {
            'Endpoint': '/todo/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single todo object'
        },
        {
            'Endpoint': '/todo/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new todo list with data sent in post request'
        },
        {
            'Endpoint': '/todo/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Updates an existing todo with data sent in post request'
        },
        {
            'Endpoint': '/todo/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting todo list'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getNote(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def getTodos(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTodo(request, pk):
    todo = Note.objects.get(id=pk)
    serializer = TodoSerializer(todo, many=False)
    return Response(serializer.data)

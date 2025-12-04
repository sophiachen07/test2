from django.shortcuts import render

def index(request):
    args = {
        'data': [
            {'title': 'This is a pending title 1', 'content': 'Some quick example text to build on the card title and make up the bulk of content.', 'url': 'https://images.pexels.com/photos/2668314/pexels-photo-2668314.jpeg'},
            {'title': 'This is a pending title 2', 'content': 'Some quick example text to build on the card title and make up the bulk of content.', 'url': 'https://images.pexels.com/photos/592077/pexels-photo-592077.jpeg'},
            {'title': 'This is a pending title 3', 'content': 'Some quick example text to build on the card title and make up the bulk of content.', 'url': 'https://images.pexels.com/photos/2093323/pexels-photo-2093323.jpeg'},
            {'title': 'This is a pending title 4', 'content': 'Some quick example text to build on the card title and make up the bulk of content.', 'url': 'https://images.pexels.com/photos/2064693/pexels-photo-2064693.jpeg'},
            {'title': 'This is a pending title 5', 'content': 'Some quick example text to build on the card title and make up the bulk of content.', 'url': 'https://images.pexels.com/photos/21787/pexels-photo.jpg'},
            {'title': 'This is a pending title 6', 'content': 'Some quick example text to build on the card title and make up the bulk of content.', 'url': 'https://images.pexels.com/photos/547125/pexels-photo-547125.jpeg'},
        ]
    }
    search_term = request.GET.get('keyword')
    if search_term:
        print('***', search_term)

    return render(request, './polls/index.html', args)

def about(request):
    return render(request, 'polls/about.html')

from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dictionary = {}
    for word in words:
        #add new word
        if word in word_dictionary:
            word_dictionary[word] += 1
        #count up
        else:
            word_dictionary[word] = 1

    return render(request, 'result.html', {'text':text, 'length':len(words), 'dict':word_dictionary.items()})
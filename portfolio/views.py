from annoying.decorators import render_to

@render_to('index.html')
def main(request):
    return {}
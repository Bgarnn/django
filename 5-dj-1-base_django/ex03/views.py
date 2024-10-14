from django.shortcuts import render

def index(request):
    shades = []
    for c in [x * 5.2 for x in range(50)]:
        cc = 255 - round(c)
        shades.append({
            'r': f'{cc}, 0, 0',
            'g': f'0, {cc}, 0',
            'b': f'0, 0, {cc}',
            'a': f'{cc}, {cc}, {cc}',
        })
    return render(request, "ex03/index.html", {"shades": shades})
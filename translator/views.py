# from django.shortcuts import render
# from deep_translator import GoogleTranslator

# def translate_text(request):
#     translated_text = ""
#     if request.method == "POST":
#         text = request.POST.get("text")
#         dest = request.POST.get("dest")
#         translated_text = GoogleTranslator(source='auto', target=dest).translate(text)

#     return render(request, "translator.html", {"translated_text": translated_text})
from deep_translator import GoogleTranslator
from django.shortcuts import render

def translate_text(request):
    translated_text = ""

    if request.method == "POST":
        text = request.POST.get("text")
        dest = request.POST.get("dest")
        src = request.POST.get("src") or "auto"

        translated_text = GoogleTranslator(
            source=src,
            target=dest
        ).translate(text)

    return render(request, "translator.html", {
        "translated_text": translated_text
    })
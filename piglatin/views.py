from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response


def translate(input):
    if not input:
        return ''
    vowels = ["a", "e", "i", "o", "u"]
    output = ""
    # words = input.lower()
    words = input.split(" ")
    for word in words:
        if word[0] in vowels:
            output += word + "ay"
        else:
            start = 0
            for letter in list(word):
                if letter in vowels:
                    break
                else:
                    if letter is "y":
                        break
                    else:
                        start += 1
            output += word[start:] + word[:start] + "ay "
    return output


class TranslateView(RetrieveAPIView):

    def post(self, request):
        try:
            input = request.data['input']
            results = translate(input)
        except Exception as e:
            return Response({'error': 'Kindly provide an {}'.format(e), 'status': 400}, status=400)

        return Response(
            {"result": results, "status": 200},
            status=200
        )

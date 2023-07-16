from django.shortcuts import render
from django.http import HttpRequest


def index(request):
    context = {}
    try_count = request.session.get('try_count', 0)
    number = None

    if request.method == 'POST':
        if try_count < 3:
            number = int(request.POST.get('number'))
            order = len(str(number))
            temp = number
            total = 0

            while temp > 0:
                digit = temp % 10
                total += digit ** order
                temp //= 10

            if number == total:
                context['result'] = f'Congratulations! {number} is an Armstrong number.'
            else:
                context['result'] = f'Sorry! {number} is not an Armstrong number.'
            try_count += 1
            request.session['try_count'] = try_count
        else:
            context['result'] = 'You have exceeded the maximum number of tries.'
    else:
        try_count = 0
        request.session['try_count'] = 0

    # Clear the input field after form submission
    context['number'] = ''

    # Pass the try count and number value back to the HTML page
    context['try_count'] = try_count
    context['number'] = number

    return render(request, 'index.html', context)

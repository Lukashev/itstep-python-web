from django.shortcuts import render
from .forms import UserForm, PrimeNumbersForm, ProfileInfoForm

# Create your views here.
def index(request):
    form = UserForm()
    response = None
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        response = f'Добрый день, {firstname} {lastname}!'
    return render(request, 'index.html', {'form': form, 'response': response })

def task2(request):
    form = PrimeNumbersForm()
    response = 'Введите диапазон'
    if request.method == 'POST':
        start = abs(int(request.POST.get('start')))
        end = abs(int(request.POST.get('end')))
        (start, end) = (end if end < start else start, start if start > end else end)

        # search prime numbers 1st example
        prime_numbers = []
        for i in range(start, end + 1):
            isPrime = True
            for j in range(2, i):
                if i % j == 0:
                    isPrime = False
            if isPrime:
                prime_numbers.append(i)

        # # search prime numbers 2nd example
        # number_list = [i for i in range(2 if start == 1 else start, end+1)]
        # k = 2
        # while k < end**1/2:
        #     for n in number_list:
        #         if n % k == 0 and n != k:
        #             number_list.remove(n)
        #     k += 1


        result = ','.join(map(lambda n: str(n), prime_numbers))
        # result = ','.join(map(lambda n: str(n), number_list))
        response = f'Результат, ! {result}'
    return render(request, 'task2.html', {'form': form, 'response': response })


def task3(request):
    form = ProfileInfoForm()
    response = None
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        email = request.POST.get('email')
        response = {
           'firstname': firstname,
            'lastname': lastname,
            'gender': gender,
            'age': age,
            'email': email
        }
    return render(request, 'task3.html', {'form': form, 'response': response})


def task4(request):
    form = PrimeNumbersForm()
    response = 'Введите диапазон'
    if request.method == 'POST':
        start = abs(int(request.POST.get('start')))
        end = abs(int(request.POST.get('end')))
        (start, end) = (end if end < start else start, start if start > end else end)

        # generate matrix
        matrix = [[f"{j} * {i} = {i * j}" for j in range(start, end + 1)] for i in range(1, 10)]
    return render(request, 'task4.html', {'form': form, 'matrix': matrix})
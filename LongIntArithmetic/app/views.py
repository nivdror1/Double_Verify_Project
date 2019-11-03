
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from controller.arithmetic_unit import long_int_addition, long_int_multiplication

from .forms import UserRegisterForm, LongIntForm


def str_to_int_array(str_number):
    """
    Convert string to int array
    :param str_number: The number in string representation
    :return: Int array
    """
    return [int(digit) for digit in str_number]


def int_array_to_str(result):
    """
    Convert int array to str
    :param result: The result in string representation
    :return: String
    """
    result = [str(i) for i in result]
    return "".join(result)


class RegisterView(View):

    def post(self, request):

        # Assign the form with the request content
        form = UserRegisterForm(request.POST)
        # Verify it and redirect to the login page
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account created for {}!'.format(username))
            return redirect('login')
        return render(request, 'app/register.html', {'form': form})

    def get(self, request):

        # retrieve the empty user registration form
        form = UserRegisterForm()
        return render(request, 'app/register.html', {'form': form})


class HomeView(View):

    def get(self, request):
        return render(request, 'app/home.html')


class AddLongIntView(LoginRequiredMixin, View):

    def get(self, request):
        form = LongIntForm()
        return render(request, 'app/add.html', {'form': form})

    def post(self, request):

        # Assign the form with the request content
        form = LongIntForm(request.POST)
        # Verify the form
        if form.is_valid():
            form_dict = form.cleaned_data

            # Convert the numbers to int array
            number1 = str_to_int_array(form_dict["number1"])
            number2 = str_to_int_array(form_dict["number2"])

            # Perform long addition
            result = long_int_addition(number1, number2)

            # Convert the result back to string
            result_str = int_array_to_str(result)

            return render(request, 'app/result.html', {'data': result_str})
        else:
            form = LongIntForm()
            return render(request, 'app/add.html', {'form': form})


class MultiplyLongIntView(LoginRequiredMixin, View):

    def get(self, request):
        form = LongIntForm()
        return render(request, 'app/multiply.html', {'form': form})

    def post(self, request):

        # Assign the form with the request content
        form = LongIntForm(request.POST)
        # Verify the form
        if form.is_valid():
            form_dict = form.cleaned_data

            # Convert the numbers to int array
            number1 = str_to_int_array(form_dict["number1"])
            number2 = str_to_int_array(form_dict["number2"])

            # Perform long multiplication
            result = long_int_multiplication(number1, number2)

            # Convert the result to str
            result_str = int_array_to_str(result)

            return render(request, 'app/result.html', {'data': result_str})
        else:
            form = LongIntForm()
            return render(request, 'app/multiply.html', {'form': form})
from django.shortcuts import render

def index(request):
    result = None
    if request.method == "POST":
        num1 = request.POST.get("num1")
        num2 = request.POST.get("num2")
        operation = request.POST.get("operation")

        try:
            num1 = float(num1)
            num2 = float(num2)

            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Error: Division by zero!"
        except ValueError:
            result = "Invalid input!"

    return render(request, "calc.html", {"result": result})

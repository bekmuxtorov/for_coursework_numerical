from django.shortcuts import render

from .forms import MatrisItemInputForm
from .utils import krilov_method
# Create your views here.


def input_view(request):
    content = {}
    if request.method == "POST":
        null_form = MatrisItemInputForm()
        form = MatrisItemInputForm(request.POST)
        if form.is_valid():
            item_00 = form.cleaned_data['item_00']
            item_01 = form.cleaned_data['item_01']
            item_02 = form.cleaned_data['item_02']
            item_03 = form.cleaned_data['item_03']
            item_10 = form.cleaned_data['item_10']
            item_11 = form.cleaned_data['item_11']
            item_12 = form.cleaned_data['item_12']
            item_13 = form.cleaned_data['item_13']
            item_20 = form.cleaned_data['item_20']
            item_21 = form.cleaned_data['item_21']
            item_22 = form.cleaned_data['item_22']
            item_23 = form.cleaned_data['item_23']
            item_30 = form.cleaned_data['item_30']
            item_31 = form.cleaned_data['item_31']
            item_32 = form.cleaned_data['item_32']
            item_33 = form.cleaned_data['item_33']
            matris = [
                [int(item_00), int(item_01), int(item_02), int(item_03)],
                [int(item_10), int(item_11), int(item_12), int(item_13)],
                [int(item_20), int(item_21), int(item_22), int(item_23)],
                [int(item_30), int(item_31), int(item_32), int(item_33)]
            ]
            y_matris_1, y_matris_2, y_matris_3, y_matris_4, solution = krilov_method(
                matris)
            try:
                p1 = int(solution[0])
                p2 = int(solution[1])
                p3 = int(solution[2])
                p4 = int(solution[3])

                solution_items = f"$$D(λ) = λ^4 {'+' + str(p1) if p1 >= 0 else p1}λ^3 {'+' + str(p2) if p2 > 0 else p2}λ^2 {'+' + str(p3) if p3 > 0 else p3}λ {'+' + str(p4) if p4 > 0 else p4}$$"
                # solution_items = {
                #     "p1": int(solution[0]),
                #     "p2": int(solution[1]),
                #     "p3": int(solution[2]),
                #     "p4": int(solution[3]),
                # }
            except Exception as e:
                print(e)
                solution_items = "Error"

            content = {
                "y_matris_1": y_matris_1,
                "y_matris_2": y_matris_2,
                "y_matris_3": y_matris_3,
                "y_matris_4": y_matris_4,
                "solution": solution_items,
                "form": null_form,
                "matris": matris
            }

            print("="*20)
            print(content)
            return render(request, "input_request.html", content)
    else:
        form = MatrisItemInputForm()
        content = {"form": form}
        return render(request, "input_request.html", content)

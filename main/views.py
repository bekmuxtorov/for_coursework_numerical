from django.shortcuts import render

from .forms import MatrisItemInputForm, BasicVektorInputForm
from .utils import krilov_method, basic_vektor, solve_eq
# Create your views here.


def input_view(request):
    content = {}
    if request.method == "POST":
        null_form = MatrisItemInputForm()
        basic_vector_form = BasicVektorInputForm()
        form = MatrisItemInputForm(request.POST)
        basic_form = BasicVektorInputForm(request.POST)
        if form.is_valid() and basic_form.is_valid():
            basic_item_0 = basic_form.cleaned_data['basic_item_0']
            basic_item_1 = basic_form.cleaned_data['basic_item_1']
            basic_item_2 = basic_form.cleaned_data['basic_item_2']
            basic_item_3 = basic_form.cleaned_data['basic_item_3']

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
            basic_vektor_num = basic_vektor(
                basic_item_0, basic_item_1, basic_item_2, basic_item_3)
            if basic_vektor_num:
                y_matris_1, y_matris_2, y_matris_3, y_matris_4, solution = krilov_method(
                    matris, basic_vektor_num)
            else:
                content = {
                    'basic_vektor_error': "Error",
                    "basic_vektor": basic_vektor_num,
                    "form": form,
                    "basic_form": basic_form,
                }
                return render(request, "input_request.html", content)

            try:
                p1 = round(solution[0], 4)
                p2 = round(solution[1], 4)
                p3 = round(solution[2], 4)
                p4 = round(solution[3], 4)
                solution_items = f"$$D(λ) = λ^4 {'+' + str(p1) if p1 >= 0 else p1}λ^3 {'+' + str(p2) if p2 > 0 else p2}λ^2 {'+' + str(p3) if p3 > 0 else p3}λ {'+' + str(p4) if p4 > 0 else p4}$$"
                koef = [1, p1, p2, p3, p4]
                solution_status = True
                for koef_item in koef:
                    if abs(koef_item) > 100_000_000:
                        solution_status = False

                if solution_status:
                    solution_roots = solve_eq(koef)
                    solution_roots_str = "$$ "
                    for indx, solution_root in enumerate(solution_roots):
                        solution_roots_str += f"λ_{indx+1} = {solution_root},\;"
                    solution_roots_str += "$$"
                else:
                    solution_roots_str = "Tanlangan matrissaning hadlari juda katta! Sonlarni kichiklashtiring."
            except Exception as e:
                print(e)
                solution_items = "Error"

            content = {
                "y_matris_1": y_matris_1,
                "y_matris_2": y_matris_2,
                "y_matris_3": y_matris_3,
                "y_matris_4": y_matris_4,
                "solution": solution_items,
                "solution_roots": solution_roots_str,
                "form": form,
                "basic_form": basic_form,
            }
            return render(request, "input_request.html", content)
    else:
        form = MatrisItemInputForm()
        basic_form = BasicVektorInputForm()
        content = {"form": form, "basic_form": basic_form}
        return render(request, "input_request.html", content)

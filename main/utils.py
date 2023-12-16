def basic_vektor(basic_item_0, basic_item_1, basic_item_2, basic_item_3) -> list[int]:
    """Ixtiyoriy noldan farqli vektor"""
    if basic_item_0 == 0 and basic_item_1 == 0 and basic_item_2 == 0 and basic_item_3 == 0:
        return []
    return [[int(basic_item_0)], [int(basic_item_1)], [int(basic_item_2)], [int(basic_item_3)]]


def y_matris_aniqlash(matris: list[list[int]], y_matris) -> list[list[int]]:
    new_y_funskiya = []  # {1: [], 2: [], 3: [], 4}
    if len(matris) == 4:
        for matris_item in matris:
            new_y_funskiya.append([matris_item[0] * y_matris[0][0] + matris_item[1] * y_matris[1]
                                  [0] + matris_item[2]*y_matris[2][0] + matris_item[3]*y_matris[3][0]])
    return new_y_funskiya


# Detarminantni hisoblash uchun funksiya
def determinant(matris):
    size = len(matris)
    if size == 1:
        return matris[0][0]
    elif size == 2:
        return matris[0][0] * matris[1][1] - matris[0][1] * matris[1][0]
    else:
        det = 0
        for i in range(size):
            minor = [row[:i] + row[i+1:] for row in (matris[1:])]
            det += matris[0][i] * ((-1) ** i) * determinant(minor)
        return det


def merge_matris(*matrislar):
    """
    Berilgan matris larni birlashtiradi

    Berilgan matrislar: 
        [[-39], [20], [11], [13]],   
        [[12], [-5], [-2], [-4]],
        [[-4], [2], [1], [1]],
        [[1], [0], [0], [0]],

    Natija: 
        [[-39, 12, -4, 1], [20, -5, 2, 0], [11, -2, 1, 0], [13, -4, 1, 0]]
    """
    row_count = len(matrislar[0])
    merged_matris = []

    for i in range(row_count):
        row = [matris[i][0] for matris in matrislar]
        merged_matris.append(row)

    return merged_matris


def kramer_method(y_matris_0, y_matris_1, y_matris_2, y_matris_3, y_matris_4):
    """Tenglamalar sistemasini Kramer usulida ishlashuvchi funksiya"""
    koefitsient_matris = merge_matris(
        y_matris_3, y_matris_2, y_matris_1, y_matris_0)
    determinant_main = determinant(koefitsient_matris)

    determinant_1 = determinant(merge_matris(
        y_matris_4, y_matris_2, y_matris_1, y_matris_0))
    determinant_2 = determinant(merge_matris(
        y_matris_3, y_matris_4, y_matris_1, y_matris_0))
    determinant_3 = determinant(merge_matris(
        y_matris_3, y_matris_2, y_matris_4, y_matris_0))
    determinant_4 = determinant(merge_matris(
        y_matris_3, y_matris_2, y_matris_1, y_matris_4))

    try:
        return [determinant_1 / determinant_main, determinant_2 / determinant_main, determinant_3 / determinant_main, determinant_4 / determinant_main]
    except ZeroDivisionError as e:
        return ["Tenglamar sistemasi yechimga ega emas. Sabab: Asosiy determinant 0 ga teng"]


def y_matris_minus(matris: list[list[int]]) -> list[list[int]]:
    """
    Matrisni manfiyga ko'paytiradi
    Berilgan:
        [[129], [132], [30], [102]]

    Natija:
        [[-129], [-132], [-30], [-102]]

    """
    result = []
    for item in matris:
        result.append([(-1) * item[0]])
    return result


def xarakteristik_kophad(solution: list[int]):
    """
    Xarakteristik ko'pxad ko'rinishi
    """
    return f"D(λ) = λ^4 - {int(solution[0])}λ^3 + {int(solution[1])}λ^2 + {int(solution[2])}λ + {int(solution[3])}"


def krilov_method(matris: list[list[int]], basic_vektor: list[list[int]]):
    y_matris_0 = basic_vektor
    y_matris_1 = y_matris_aniqlash(matris, y_matris_0)
    y_matris_2 = y_matris_aniqlash(matris, y_matris_1)
    y_matris_3 = y_matris_aniqlash(matris, y_matris_2)
    y_matris_4 = y_matris_minus(y_matris_aniqlash(matris, y_matris_3))

    solution = kramer_method(y_matris_0, y_matris_1,
                             y_matris_2, y_matris_3, y_matris_4)
    return y_matris_1, y_matris_2, y_matris_3, y_matris_4, solution

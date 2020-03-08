import pytest
from src.square import square_area

@pytest.mark.parametrize(   # wykona się to tyle razy ile mamy zestawów danych, dekorator jest nadpisywany tylko na 1 metodę i dla każdej metody wstawiamy nowy
    "a,b,result",
 [
     (4,24,4),   # tu muszą być przecinki pomiędzy tuplami, parametr/wynik

 ]
)

def test_square_area(a,b,result):  # test musi być na początku
    assert square_area(a,b) == result



import pytest
import eqwid_test

@pytest.mark.parametrize("price", range(0,800,100))
def test_2(price):
    parsed_data_array = eqwid_test.filtred_data_price_from(price);
    if parsed_data_array:
        for i in parsed_data_array:
            assert i.price >= float(price), 'Цена должна быть больше';

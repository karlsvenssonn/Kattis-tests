import sys

units_id = {
    'thou': 0, 'th': 0,
    'inch': 1, 'in': 1,
    'foot': 2, 'ft': 2,
    'yard': 3, 'yd': 3,
    'chain': 4, 'ch': 4,
    'furlong': 5, 'fur': 5,
    'mile': 6, 'mi': 6,
    'league': 7, 'lea': 7
}

units_translation = [1, 1000, 12, 3, 22, 10, 8, 3]

for i in sys.stdin:
    in_data = i.split()
    in_value = int(in_data[0])
    in_unit = units_id[in_data[1]]
    out_unit = units_id[in_data[3]]

    if in_unit == out_unit:
        print (n_value)
    
    elif in_unit < out_unit:
        res = 1
        while in_unit != out_unit:
            in_unit += 1
            res /= units_translation[in_unit]
        print(res * in_value)

    elif in_unit > out_unit:
        res = 1
        while in_unit != out_unit:
            res *= units_translation[in_unit]
            in_unit -= 1
        print(in_value* res)

    



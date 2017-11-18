def numeral(number):
    r_vals = ((1000, 'M'),
              (500, 'D'),
              (100, 'C'),
              (50, 'L'),
              (10, 'X'),
              (5, 'V'), 
              (1, 'I'))
    r_replacements = (('DCCCC', 'CM'),
                      ('CCCC', 'CD'),
                      ('LXXXX', 'XC'),
                      ('XXXX', 'XL'),
                      ('VIIII', 'IX'),
                      ('IIII', 'IV'))
    
    def strip_roman(number):
        for v, c in r_vals:
            if number >= v:
                return c, number - v
            
    rds = ''
    while number:
        c, number = strip_roman(number)
        rds += c
    for s, r in r_replacements:
        rds = rds.replace(s, r)
    return rds

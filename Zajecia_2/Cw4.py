def temperature(a):

    C = float(a)

    temperature_f = float(32) + float((9/5)) * C
    temperature_k = C + 273.15
    temperature_r = (9/5) * float(temperature_k)


    print(temperature_f, temperature_k, temperature_r )

temperature(40)
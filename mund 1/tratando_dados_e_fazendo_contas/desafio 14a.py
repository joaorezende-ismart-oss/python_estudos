temperatura_c = float(input('Qual é a temperatura atual (°C): '))
temperatura_f = temperatura_c * 1.8 + 32
print('A temperatura de {}°C em fahrenheit será de: {:.2f}°F'.format(temperatura_c, temperatura_f))
escala_kelvin = temperatura_c + 273.15
print('A temperatura de {}°C convertida para a escala Kelvin é de: {:.2f} K'.format(temperatura_c, escala_kelvin))

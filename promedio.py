# Calculadora de promedio de notas
# TPI - Arquitectura y Sistemas Opertativos

notas = []

for i in range(1, 4):
	nota = float(input(f"Ingresa la nota {i}: "))
	notas.append(nota)

promedio = sum(notas) / len(notas)

print("\n---Resultado---")
print(f"Notas ingresadas: {notas}")
print(f"Promedio: {promedio:.2f}")

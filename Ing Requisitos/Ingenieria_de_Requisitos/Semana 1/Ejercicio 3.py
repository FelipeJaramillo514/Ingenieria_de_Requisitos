SalarioMensual = float(input('Ingresa el salario mensual:'))
HorasTrabajadasMensuales = float(input('Ingrese las horas trabajadas mensualmente:'))
HorasTrabajadasSemanales = float(input('Ingrese las horas trabajadas semanalmente:'))

PagoPorHora = SalarioMensual/HorasTrabajadasSemanales
PagoSemanal = HorasTrabajadasSemanales*PagoPorHora

print('Tu salario por hora es de', PagoPorHora, 'Tu salario semanal es de', PagoSemanal)

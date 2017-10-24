# class Any:
# 	def potenciar(self,number,potencia):
# 		# AQUÍ VA TODA LA LÓGICA DE NEGOCIO
# 		return number**potencia
#
#
# def main():
# 	any = Any()
# 	n = any.potenciar(2,10)
# 	print(n)
#
# if __name__ == '__main__':
# 	main()
#

class Rect:
	pass

class Cuadrado(Rect):
	pass

def main():
	rect = Rect()
	#rect.altura = 0
	#rect.base = 0
	rect.asignar_altura(20)
	#rect.altura = 20
	rect.asignar_base(30)
	#rect.base = 30

	cua = Cuadrado()
	cua.asignar_altura(20)
	#cua.altura = 20

	rect.calcular_area()

if __name__ == '__main__':
	main()



class X:
	def metodo_x():
		print('x')
		print('x')
		print('x')
		print('x')
		print('x')
		print('x')
		print('x')
		print('x')
		print('x')
		print('x')
		print('x')

class Profesor:
	def metodo_x():
		X().metodo_x()
		pass

class Alumno:
	def metodo_x():
		X().metodo_x()
		pass


class Interface:
	def operar():
		pass

class Alumno:
	def estudiar():
		print('estudiar')


class Empleado:
	def a():
		pass

	def b():
		pass

	def c():
		pass

	def a():
		pass

	def b():
		pass

class Empleado2:
	def c():
		pass
	def a():
		pass

	def b():
		pass

	def c():
		pass

class Obrero(Empleado, Empleado2):
	def a():
		print('')

	def b():
		pass

	def c():
		pass

class JefeDeArea(Empleado):
	pass


class A:
	def any():
		Abstraccion().any()
	pass

class B:
	pass


class Abstraccion:






class Boton:
	lampara = Lampara()

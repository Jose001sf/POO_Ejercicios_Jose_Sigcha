from modelo import Modelo_Licencia
from vista import Vista_Licencia
from controlador import Controlador_Licencia

modelo = Modelo_Licencia()
vista = Vista_Licencia()
controlador = Controlador_Licencia(modelo, vista)
controlador.menu()
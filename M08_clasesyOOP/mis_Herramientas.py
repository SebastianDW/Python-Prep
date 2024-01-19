class Herramientas:
    def __init__(self, lista_numeros):
        self.lista = lista_numeros
        
    def Verificar_primo(self,numero):
        for a in range(2,(numero//2)+1):
            if numero%a==0:
                return False
        return True
    
    def Valor_modal(self, lista):
        frecuencia = {}

        for elemento in lista: 
            if elemento in frecuencia: 
                frecuencia[elemento]+=1
            else:
                frecuencia[elemento]=1
        valor_modal=None
        frecuencia_maxima=0
        for clave, frec in frecuencia.items():
            if frec>frecuencia_maxima:
                valor_modal=clave
                frecuencia_maxima=frec
        return valor_modal
    def conversion_de_temperatura2(self, temperatura, temp_origen, temp_destino):
        temp=0
        if temp_origen=="farenheit":
            if temp_destino=="celsius":
                temp=(temperatura-32)*5/9
            elif temp_destino=="kelvin":
                temp=((temperatura-32)*5/9)+273.15
        elif temp_origen== "kelvin":
            if temp_destino=="celsius":
                temp=temperatura-273.15
            elif temp_destino=="farenheit":
                temp= ((temperatura-273.15)*9/5)+32
        elif temp_origen=="celsius":
            if temp_destino=="farenheit":
                temp=(temperatura*9/5)+32
            elif temp_destino=="kelvin": 
                temp=(temperatura+273.15)   
            else:
                print("ingrese una medida existente ")
        return temp
    def factorial(self, numero):
        if isinstance(numero, int) and numero > 0:
            if numero == 1:
                return 1
            else:
                return numero * self.factorial(numero - 1)
    
    #creé un metodo para usar el resto de metodos para no cambiar el codigo de todos los metodos
    def usar_Operaciones(self,opcion, t_origen="", t_destino=""):
        
        if opcion == 1 or opcion ==3 or opcion==4:
            for i in self.lista:
                if opcion==1:
                    print(self.Verificar_primo(i))
                elif opcion==3:
                    print(self.conversion_de_temperatura2(i,t_origen,t_destino))
                elif opcion == 4:
                    print(self.factorial(i))
        elif opcion == 2:
            print(self.Valor_modal(self.lista))

def main():
    # Escribe tu código abajo de esta línea
    def proceso(horas,minutos,segundos):
        segundos+=horas*60*60+minutos*60
        return segundos

    def main():
        print('proceso 1:')
        horas=int(input('Introduce las horas: '))
        minutos=int(input('Introduce las minutos: '))
        segundos=int(input('Introduce las segundos: '))
        print('proceso 2:')
        horas2=int(input('Introduce las horas: '))
        minutos2=int(input('Introduce las minutos: '))
        segundos2=int(input('Introduce las segundos: '))    
        print('proceso 1:',proceso(horas,minutos,segundos))
        print('proceso 2:',proceso(horas2,minutos2,segundos2))
    
    main()

if __name__ == '__main__':
    main()

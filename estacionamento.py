from datetime import datetime # importa a biblioteca com as funções de pegar a data e hora do usuário naquele momento e separar o ano, mês, dia, hora, minuto... 

class Veiculo:
    def __init__(self, tipo, placa, modelo):
        self.tipo = tipo
        self.placa = placa
        self.modelo = modelo
        self.minutoEntrada = 0
        self.horaEntrada = 0
        self.diaEntrada = 0
        self.mesEntrada = 0
        self.anoEntrada = 0
        self._entrada = 0
        self._saida = 0


    def entrada (self): 
        entrada = datetime.now ()  #pega a data do usuário no momento que ele apertar o botão
        entradaStr = entrada.strftime('%d/%m/%y  %H:%M:%S') #transforma os números da variável 'entrada' em string, congelando aqueles valores e impedindo a função datetime.now de atualizá-los a cada minuto 

        #separa os valores do dia,  mês, ano, hora e minuto em variáveis e, dentro de cada variável, converte-os em inteiros    
        self.diaEntrada = entrada.strftime('%d')
        self.diaEntrada = int(self.diaEntrada)
        self.mesEntrada = entrada.strftime('%m')
        self.mesEntrada = int(self.mesEntrada)
        self.anoEntrada = entrada.strftime('%y')
        self.anoEntrada = int(self.anoEntrada)

        self.horaEntrada = entrada.strftime('%H')
        self.horaEntrada = int(self.horaEntrada)
        self.minutoEntrada = entrada.strftime('%M')
        self.minutoEntrada = int(self.minutoEntrada)

        entrada = datetime.strptime(entradaStr, '%d/%m/%y  %H:%M:%S') #transforma a data completa da variável entrada em números inteiros sem descongelá-los
        self._entrada = entrada

        return self._entrada


    @property
    def saida (self):
        saida = datetime.now()
        saidaStr = saida.strftime('%d/%m/%y  %H:%M:%S')

        saida = datetime.strptime(saidaStr, '%d/%m/%y  %H:%M:%S')
        self._saida = saida

        if saida < self._entrada:
            input('Data e horário de saída não podem ser maior que os de entrada!')
        else:
            return self._saida


    def valorFinal (self, valorHora):
        saida = datetime.now()
        
        anoSaida = saida.strftime('%y')
        anoSaida = int(anoSaida)

        mesSaida = saida.strftime('%m')
        mesSaida = int(mesSaida)

        diaSaida = saida.strftime('%d')
        diaSaida = int(diaSaida)

        horaSaida = saida.strftime('%H')
        horaSaida = int(horaSaida)
        
        minutoSaida = saida.strftime('%M')
        minutoSaida = int(minutoSaida)

        anoPermanencia = (anoSaida - self.anoEntrada)
        mesPermanencia = (mesSaida - self.mesEntrada)
        diaPermanencia = (diaSaida - self.diaEntrada)

        horaPermanencia = (horaSaida - self.horaEntrada)
        minutoPermanencia = (minutoSaida - self.minutoEntrada)

        horasTotais = 0

        anosEmHoras = anoPermanencia * 8760
        horasTotais += anosEmHoras
        mesesEmHoras = mesPermanencia *730
        horasTotais += mesesEmHoras
        diasEmHoras = diaPermanencia * 24
        horasTotais += diasEmHoras
        horasTotais += horaPermanencia

        self.valorHora = valorHora
        valorTotal = float(valorHora) * float(horasTotais)

        return (f'Você ficou {horasTotais} horas no estacionamento, portanto, o valor total a pagar é de R${valorTotal}')


print('---- ESTACIONAMENTO RIO MAR FORTALEZA ----\n \n')
veiculo = input('Digite o tipo do veículo: \n')
placa = input('Digite a placa do veículo: \n')
modelo = input('Digite o modelo do veículo: \n')
valorHora = input('\nDigite o valor da hora do estacionamento em R$: \n')

teste = Veiculo (veiculo, placa, modelo)

print(f'\nEntrada Liberada: {teste.entrada()} \nSeja bem-vindo(a) ao estacionamento Rio Mar Fortaleza! \n')

input('\nAperte o botão ENTER para sair do estacionamento!\n')

print(f'Saída liberada: {teste.valorFinal(valorHora)}')


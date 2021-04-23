#sistema de perguntas e respostas com dicionarios python
#
perguntas = {
    'Pergunta 1':{
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '3',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 2':{
        'pergunta': 'Quanto é 2+1? ',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '3',
        },
        'resposta_certa': 'c',
    },
    'Pergunta 3':{
        'pergunta': 'Quanto é 9-1? ',
        'respostas': {
            'a': '1',
            'b': '8',
            'c': '3',
        },
        'resposta_certa': 'b',
    },
    'Pergunta 4':{
        'pergunta': 'Quanto é 2*5? ',
        'respostas': {
            'a': '10',
            'b': '4',
            'c': '3',
        },
        'resposta_certa': 'a',
    },
    'Pergunta 5':{
        'pergunta': 'Quanto é 2*7? ',
        'respostas': {
            'a': '1',
            'b': '14',
            'c': '3',
        },
        'resposta_certa': 'b',
    },
}
print()

respostas_certas = 0
for chave_pergunta, chave_resposta in perguntas.items():
    print(f'{chave_pergunta}: {chave_resposta["pergunta"]}')

    print('Respostas: ')
    for resposta_key, resposta_velho in chave_resposta['respostas'].items():
        print(f'[{resposta_key}]: {resposta_velho}')


    resposta_usuario = input('Sua resposta:  ')

    if resposta_usuario == chave_resposta['resposta_certa']:
        print('Parabéns, alternativa correta.')
        respostas_certas += 1
    else:
        print('Alternativa incorreta.')
    
    print()

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} respostas.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%.')
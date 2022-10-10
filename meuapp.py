import streamlit as st
import pandas as pd
from random import sample
from PIL import Image

pagina = ['Boas-Vindas','Lotofacil','Calculo de salario','Sobre','Teste']
st.sidebar.markdown('# Streamlit CV - Currículo Interativo')
st.sidebar.subheader('Navegue pelo menu')
pagina = st.sidebar.selectbox('Menu', pagina)

def calcular_pagamento(qtd_horas, valor_hora):
  horas = float(qtd_horas)
  taxa = float(valor_hora)
  if horas <= 40:
    salario=horas*taxa
  else:
    h_excd = horas - 40
    salario = 40*taxa+(h_excd*(1.5*taxa))
  return salario

def lista_random(m, n, i, f):
	lista = list()
	for c in range(1, m + 1):
		lista.append(sorted(sample(range(i, f + 1), n)))
	return lista


if pagina == 'Boas-Vindas':
	foto = Image.open('jone.png')
	st.image(foto,
		caption='Logo do Streamlit',
		use_column_width=False)
	st.title('Jone Nascimento')
	
	st.subheader('Olá!! Muito Prazer!!')
	st.write('Sou engenheiro eletricista com experiente em planejamento estratégico, com foco em gestão de equipes de manutenção elétrica, instrumentação, automação, projetos elétricos e implantação industrial. Tenho longa vivência em organizações do setor privado no segmento agroindustrial, e de geração de energia térmica e renovável.')
	st.write('Como um apaixonado por tecnologia, atualmente, faço uso de **Data Driven** para resolver problemas de negócio complexos por meio de análises avançada de dados. Também, estou em fase de aperfeiçoamente na área de **cloud computing da AWS**, e técnicas de análises de dados utilizando a linguagem **Python**, com enfase em **Machine Learning**.')
	st.text(' O propósito dessa página é funcionar como um Currículo Interativo.')
	st.text(' utilizando o Streamlit + Markdow')
	st.markdown('---')
	

if pagina == 'Lotofacil':
	st.title('Vamos jogar na lotofácil!!')
	st.markdown('---')
	st.write('Entre com o seu jogo:')
	num = int(st.number_input('Desejas gerar quantas listas? '))
	quant = int(st.number_input('Quantos números por lista? '))
	ini = int(st.number_input('Limite inferior do range: '))
	fin = int(st.number_input('Limite superior do range: '))
	l = lista_random(num, quant, ini, fin)
	st.write('Seus jogos são:',l)

if pagina == 'Calculo de salario':
	st.title('Vamos calcular o seu salario mensal')
	st.markdown('---')
	qtd_horas = st.number_input('Digite a quantidade de horas trabalhadas!')
	valor_hora = st.number_input('Digite o valor da sua hora!')
	c = calcular_pagamento(qtd_horas,valor_hora)
	st.write('Meu salário é:',c)

if pagina == 'Sobre':
	st.title('Versão 0.0.1 ainda em desenvolvimento!!')
	st.markdown('---')
	botao = st.button('Liberar os balõeszinhos!!')
	if botao:
		st.balloons()

if pagina == 'Teste':
	st.markdown('# Título')
	st.markdown('## Título')
	st.markdown('### Título')
	st.markdown('*Título*')
	st.markdown('Emojis do markdown:  :smiley:  :poop:  :kissing:')
	st.write('Entrada padrao de texto')
	st.text('Texto com aquela fonte quadrada')
	st.sidebar.title('Teste')
	st.sidebar.latex('\int_a^bf(x)dx = F(b) - F(a)')
	st.sidebar.title('Barra Lateral 02')
	st.sidebar.code('import pandas as pd')
	n = st.slider('Entre com um número', 10, 70, 20, 2)
	st.title(f'O quadrado de {n} é {n**2}')
	nome = st.text_input('Digite o seu nome!')
	



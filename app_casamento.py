import streamlit as st
import pandas as pd
from datetime import date
from PIL import Image
import io

# --- 1. CONFIGURAÇÃO INICIAL ---
st.set_page_config(page_title="Wedding Planner J&R", page_icon="💍", layout="wide")

# --- 2. SISTEMA DE TEMAS ---
def aplicar_tema(usuario):
    if usuario == "Raysa":
        # TEMA RAYSA
        cor_primaria = "#d63031"
        cor_destaque = "#e84393"
        cor_fundo = "#ffe3ec"
        cor_card = "#fff0f5"
        borda_radius = "20px"
        gradiente_btn = "linear-gradient(90deg, #e84393 0%, #d63031 100%)"
        fonte = "'Poppins', sans-serif"
        borda_input = "2px solid #e84393"
    else:
        # TEMA JOÃO
        cor_primaria = "#0984e3"
        cor_destaque = "#74b9ff"
        cor_fundo = "#dfe6e9"
        cor_card = "#ffffff"
        borda_radius = "8px"
        gradiente_btn = "linear-gradient(90deg, #0984e3 0%, #2d3436 100%)"
        fonte = "'Roboto', sans-serif"
        borda_input = "2px solid #b2bec3"

    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');
        
        html, body, [class*="css"]  {{
            font-family: {fonte};
            color: #2d3436;
        }}
        
        .stApp {{
            background-color: {cor_fundo};
        }}

        /* CARDS */
        div.css-card, div.stDataFrame, div[data-testid="stMetric"] {{
            background-color: {cor_card};
            border-radius: {borda_radius};
            padding: 25px;
            box-shadow: 0 8px 20px rgba(0,0,0,0.1);
            border: 1px solid rgba(0,0,0,0.05);
        }}
        
        /* EXPANDER (Hacks) Customizado */
        .streamlit-expanderHeader {{
            background-color: {cor_card};
            border-radius: 10px;
            font-weight: 600;
            color: {cor_primaria};
            border: 1px solid rgba(0,0,0,0.1);
        }}
        
        /* INPUTS */
        .stTextInput input, .stNumberInput input, .stSelectbox div[data-baseweb="select"] {{
            background-color: white !important;
            border: {borda_input} !important;
            color: #2d3436 !important;
            font-weight: 500;
            border-radius: 8px;
        }}
        
        h1, h2, h3 {{ color: {cor_primaria} !important; }}
        
        .stButton>button {{
            background: {gradiente_btn};
            color: white !important;
            border: none;
            border-radius: {borda_radius};
            font-weight: 600;
            box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        }}
        
        section[data-testid="stSidebar"] {{
            background-color: white;
            border-right: 1px solid #ddd;
        }}
    </style>
    """, unsafe_allow_html=True)

# --- 3. INICIALIZAÇÃO DE DADOS ---
if 'data_casamento' not in st.session_state:
    st.session_state['data_casamento'] = date(2026, 8, 15)

if 'financas' not in st.session_state:
    st.session_state['financas'] = {"ganhos_joao_fixo": 5000.0, "ganhos_raysa_fixo": 5000.0, "economias_banco": 15000.0}

if 'renda_extra' not in st.session_state:
    st.session_state['renda_extra'] = pd.DataFrame([
        {"Data": date.today(), "Descrição": "Freela Python", "Quem": "João", "Valor": 500.00}
    ])

if 'orcamento' not in st.session_state:
    st.session_state['orcamento'] = pd.DataFrame([
        {"Item": "Buffet", "Categoria": "Festa", "Previsto": 18000.0, "Gasto": 2000.0},
        {"Item": "Fotografia", "Categoria": "Festa", "Previsto": 4500.0, "Gasto": 1000.0},
    ])

if 'lua_de_mel' not in st.session_state:
    st.session_state['lua_de_mel'] = pd.DataFrame([
        {"Atividade/Item": "Passagens", "Custo Estimado": 5000.0, "Status": "Comprado"},
        {"Atividade/Item": "Hotel", "Custo Estimado": 4000.0, "Status": "Reservar"},
    ])

if 'enxoval' not in st.session_state:
    st.session_state['enxoval'] = []

if 'checklist' not in st.session_state:
    st.session_state['checklist'] = {
        "Fevereiro 2026": [{"task": "Definir local", "done": True}],
    }

# --- LISTA MESTRA DE HACKS (20 DICAS) ---
# Só carrega se a lista estiver vazia ou pequena (para não sobrescrever sempre)
if 'hacks' not in st.session_state or len(st.session_state['hacks']) < 5:
    st.session_state['hacks'] = [
        # --- DINHEIRO ---
        {"cat": "💸", "titulo": "Câmbio Blue via Western Union (O Segredo #1)", 
         "desc": "**Isso dobra seu dinheiro.**\n1. Baixe o app da Western Union no Brasil.\n2. Envie dinheiro (PIX) para **você mesmo** na Argentina.\n3. Vá a uma loja física da WU em Bariloche com seu passaporte.\n4. Você sacará pesos no valor 'Blue' (paralelo legal), que vale muito mais que o cartão de crédito."},
        {"cat": "💸", "titulo": "Leve Notas de $100 Dólares 'Cara Grande'", 
         "desc": "Se levar dinheiro vivo, leve Dólares. Mas atenção:\n- Notas de $100 novas (faixa azul).\n- Sem riscos ou amassados.\n- Casas de câmbio (Cuevas) pagam menos por notas velhas ou de menor valor ($20, $50)."},
        {"cat": "💸", "titulo": "Isenção de IVA (21%) em Hotéis", 
         "desc": "**Economia de 21% na estadia!**\n- Ao pagar o hotel com cartão de crédito internacional ou débito internacional (Wise/Nomad), você é isento do imposto IVA.\n- Se pagar em dinheiro vivo (pesos), você PAGA o imposto. Faça as contas de qual câmbio compensa mais."},
        
        # --- TRANSPORTE ---
        {"cat": "🚌", "titulo": "Cartão SUBE (Busão Barato)", 
         "desc": "Táxi é caro. Ônibus é muito barato.\n1. Compre um cartão SUBE em qualquer 'Kiosko' no centro.\n2. Carregue com pesos.\n3. O ônibus #20 leva para os principais pontos turísticos (Llao Llao, Cerro Campanario)."},
        {"cat": "🚌", "titulo": "Saída do Aeroporto (Evite Táxi Oficial)", 
         "desc": "O táxi do aeroporto é tabelado e caro.\n- Opção econômica: Ônibus de linha (sai da frente do aero).\n- Opção média: Apps como Cabify costumam ser mais baratos que os táxis da fila."},
        {"cat": "🚌", "titulo": "Aluguel de Carro: Reserve Antes", 
         "desc": "Em alta temporada, os carros somem.\n- Reserve com meses de antecedência.\n- Verifique se o pneu tem 'cravos' ou correntes para neve (obrigatório em nevascas)."},

        # --- COMIDA ---
        {"cat": "🍔", "titulo": "Mercado La Anónima", 
         "desc": "Restaurante todo dia quebra o orçamento.\n- Compre vinhos, queijos, fiambres e água no supermercado 'La Anónima'.\n- O vinho que custa R$ 80 no restaurante custa R$ 15 no mercado."},
        {"cat": "🍔", "titulo": "Menu del Día (Almoço Executivo)", 
         "desc": "Muitos restaurantes oferecem 'Menu del Día' no almoço (entrada + prato + bebida + sobremesa) por um preço fixo muito baixo. Jantar costuma ser 'A la carte' e mais caro."},
        {"cat": "🍔", "titulo": "Mamuschka vs Rapanui", 
         "desc": "A briga eterna.\n- **Rapanui:** Tem sorvetes incríveis e é levemente mais barato.\n- **Mamuschka:** Embalagens lindas, ótimo para presentes, mas cobra preço de grife."},
        {"cat": "🍔", "titulo": "Água da Torneira", 
         "desc": "A água de Bariloche vem do degelo das montanhas e é potável e deliciosa. Leve garrafinhas reutilizáveis e encha na torneira do hotel. Economia garantida."},

        # --- PASSEIOS ---
        {"cat": "🏔️", "titulo": "Circuito Chico (Faça você mesmo)", 
         "desc": "Agências cobram caro por isso.\n1. Pegue o ônibus #20.\n2. Desça no km 18.3.\n3. Alugue uma bicicleta lá e faça o percurso pedalando. É lindo e custa metade do preço."},
        {"cat": "🏔️", "titulo": "Cerro Campanario (A melhor vista)", 
         "desc": "Dizem que é a vista mais bonita. É mais barato que o Cerro Otto.\n- Dica Hardcore: Se subir a trilha a pé (30-40 min de subida íngreme), não paga o teleférico!"},
        {"cat": "🏔️", "titulo": "Roupas de Neve: Galerias da Mitre", 
         "desc": "Não alugue roupa no pé da montanha (Cerro Catedral), é o triplo do preço.\n- Alugue nas galerias da Rua Mitre (centro) no dia anterior."},
        {"cat": "🏔️", "titulo": "Refugio Frey (Trekking Grátis)", 
         "desc": "Se vocês curtem trilha, o caminho para o Refugio Frey é deslumbrante e 100% gratuito. Leva o dia todo, mas vale cada centavo economizado."},
        {"cat": "🏔️", "titulo": "Free Walking Tour", 
         "desc": "Procure pelo 'Bariloche Free Walking Tour'. É um passeio guiado a pé pelo centro cívico onde você paga apenas uma gorjeta (propina) no final."},
        
        # --- DICAS GERAIS ---
        {"cat": "💡", "titulo": "Chip de Celular (Claro/Personal)", 
         "desc": "Não use roaming do Brasil. Compre um chip pré-pago (chip prepago) da Claro AR ou Personal em um Kiosko e carregue. Internet rápida e barata."},
        {"cat": "💡", "titulo": "Tomada Tipo I", 
         "desc": "A tomada na Argentina é diferente (três pinos chatos na diagonal). Leve adaptadores universais ou compre um lá (ferretería)."},
        {"cat": "💡", "titulo": "Horário de Jantar", 
         "desc": "Argentinos jantam tarde (21h30 - 22h). Se chegar às 19h, vai encontrar restaurantes vazios ou fechados."},
        {"cat": "💡", "titulo": "Gorjeta (La Propina)", 
         "desc": "O costume é deixar 10% em dinheiro na mesa. Não costuma vir na conta (cubierto é outra coisa, é taxa de talher/pão)."},
        {"cat": "💡", "titulo": "Temporada de Ombros", 
         "desc": "Ir em Agosto é alta temporada (caro). Ir no final de Setembro ou Outubro ainda tem neve no topo, mas os preços de hospedagem caem pela metade."}
    ]

# --- 4. SIDEBAR ---
with st.sidebar:
    st.markdown("### 💍 Planner J&R")
    usuario = st.radio("Quem é você?", ["Raysa", "João"], horizontal=True)
    aplicar_tema(usuario)
    
    st.markdown("---")
    menu = st.radio("Navegação", [
        "🏠 Dashboard", 
        "💰 Entradas (Carteira)", 
        "💸 Saídas (Planejamento)", 
        "🎁 Enxoval (Casa Nova)", 
        "✅ Tarefas",
        "💡 Hacks & Dicas"
    ])
    
    st.markdown("---")
    nova_data = st.date_input("Data Casamento", value=st.session_state['data_casamento'])
    if nova_data != st.session_state['data_casamento']:
        st.session_state['data_casamento'] = nova_data
        st.rerun()
    dias = (st.session_state['data_casamento'] - date.today()).days
    st.caption(f"Faltam {dias} dias!")

# --- 5. LÓGICA DAS PÁGINAS ---

# >>>> DASHBOARD <<<<
if menu == "🏠 Dashboard":
    st.title(f"Bem-vindo, {usuario}!")
    
    total_festa = st.session_state['orcamento']['Previsto'].sum()
    total_viagem = st.session_state['lua_de_mel']['Custo Estimado'].sum()
    total_enxoval = sum([item['preco'] for item in st.session_state['enxoval']])
    total_nec = total_festa + total_viagem + total_enxoval
    
    total_extra = st.session_state['renda_extra']['Valor'].sum()
    total_caixa = st.session_state['financas']['economias_banco'] + total_extra
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Meta Total", f"R$ {total_nec:,.2f}")
    c2.metric("Em Caixa", f"R$ {total_caixa:,.2f}")
    c3.metric("Faltam", f"R$ {max(0, total_nec - total_caixa):,.2f}")
    st.progress(min(total_caixa/total_nec if total_nec > 0 else 0, 1.0))

# >>>> ENTRADAS <<<<
elif menu == "💰 Entradas (Carteira)":
    st.title("💰 Entradas")
    tab1, tab2 = st.tabs(["Fixos", "Extras"])
    with tab1:
        c1, c2 = st.columns(2)
        with c1:
            vf_j = st.number_input("Renda João", value=st.session_state['financas']['ganhos_joao_fixo'])
            vf_r = st.number_input("Renda Raysa", value=st.session_state['financas']['ganhos_raysa_fixo'])
            st.session_state['financas']['ganhos_joao_fixo'] = vf_j
            st.session_state['financas']['ganhos_raysa_fixo'] = vf_r
        with c2:
            v_banco = st.number_input("Banco Inicial", value=st.session_state['financas']['economias_banco'])
            st.session_state['financas']['economias_banco'] = v_banco
    with tab2:
        edited_extra = st.data_editor(st.session_state['renda_extra'], num_rows="dynamic", use_container_width=True)
        st.session_state['renda_extra'] = edited_extra
        st.success(f"Total Extra: R$ {edited_extra['Valor'].sum():,.2f}")

# >>>> SAÍDAS <<<<
elif menu == "💸 Saídas (Planejamento)":
    st.title("💸 Saídas")
    tab1, tab2 = st.tabs(["Casamento", "Lua de Mel"])
    with tab1:
        st.data_editor(st.session_state['orcamento'], num_rows="dynamic", use_container_width=True)
    with tab2:
        st.data_editor(st.session_state['lua_de_mel'], num_rows="dynamic", use_container_width=True)

# >>>> ENXOVAL <<<<
elif menu == "🎁 Enxoval (Casa Nova)":
    st.title("🎁 Enxoval")
    with st.expander("➕ Adicionar Item"):
        with st.form("enxoval_form", clear_on_submit=True):
            nome = st.text_input("Nome")
            preco = st.number_input("Preço", min_value=0.0)
            foto = st.file_uploader("Foto", type=['png', 'jpg'])
            parc = st.checkbox("Parcelado?")
            vezes = st.number_input("Vezes", 2, 24) if parc else 1
            if st.form_submit_button("Salvar"):
                img = foto.getvalue() if foto else None
                st.session_state['enxoval'].append({"nome": nome, "preco": preco, "parcelado": parc, "vezes": vezes, "imagem": img})
                st.rerun()
    
    if st.session_state['enxoval']:
        cols = st.columns(3)
        for i, item in enumerate(st.session_state['enxoval']):
            with cols[i%3]:
                with st.container():
                    st.markdown(f"**{item['nome']}**")
                    if item['imagem']: st.image(item['imagem'], use_container_width=True)
                    st.write(f"R$ {item['preco']:,.2f}")
                    if st.button("🗑️", key=f"d_enx_{i}"):
                        st.session_state['enxoval'].pop(i)
                        st.rerun()

# >>>> TAREFAS <<<<
elif menu == "✅ Tarefas":
    st.title("Tarefas")
    c_nav, c_list = st.columns([1, 3])
    with c_nav:
        mes = st.selectbox("Mês", list(st.session_state['checklist'].keys()))
        novo = st.text_input("Novo Mês")
        if st.button("Criar"):
            if novo: st.session_state['checklist'][novo] = []
            st.rerun()
    with c_list:
        if mes:
            st.subheader(f"Lista: {mes}")
            c1, c2 = st.columns([0.8, 0.2])
            nt = c1.text_input("Tarefa", label_visibility="collapsed")
            if c2.button("Add", use_container_width=True):
                st.session_state['checklist'][mes].append({"task": nt, "done": False})
                st.rerun()
            st.markdown("---")
            for i, t in enumerate(st.session_state['checklist'][mes]):
                cc, ct, cd = st.columns([0.05, 0.85, 0.1])
                chk = cc.checkbox("", t['done'], key=f"k_{mes}_{i}")
                st.session_state['checklist'][mes][i]['done'] = chk
                style = "text-decoration: line-through; color: #aaa" if chk else ""
                ct.markdown(f"<span style='{style}'>{t['task']}</span>", unsafe_allow_html=True)
                if cd.button("🗑️", key=f"del_{mes}_{i}"):
                    st.session_state['checklist'][mes].pop(i)
                    st.rerun()

# >>>> HACKS & DICAS (ATUALIZADO) <<<<
elif menu == "💡 Hacks & Dicas":
    st.title("💡 Segredos de Bariloche")
    st.markdown("Clique nos itens abaixo para ver o passo a passo de como economizar.")
    
    # Barra de busca simples
    filtro = st.text_input("🔍 Buscar dica (ex: Câmbio, Comida...)", "")
    
    for i, hack in enumerate(st.session_state['hacks']):
        # Filtro de busca
        if filtro.lower() in hack['titulo'].lower() or filtro.lower() in hack['desc'].lower():
            
            # O SEGREDO DO CLIQUE: st.expander
            with st.expander(f"{hack['cat']} {hack['titulo']}"):
                st.markdown(hack['desc'])
                
                # Opção de excluir dica se quiser limpar a lista
                if st.button("Remover Dica", key=f"del_hack_{i}"):
                    st.session_state['hacks'].pop(i)
                    st.rerun()
    
    st.markdown("---")
    with st.expander("➕ Adicionar seu próprio segredo"):
        with st.form("form_hacks"):
            cat = st.selectbox("Categoria", ["💸", "🍔", "🚌", "🏔️", "💡"])
            h_tit = st.text_input("Título")
            h_desc = st.text_area("Passo a passo")
            if st.form_submit_button("Salvar"):
                st.session_state['hacks'].append({"cat": cat, "titulo": h_tit, "desc": h_desc})
                st.rerun()
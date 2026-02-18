import streamlit as st
import pandas as pd
from datetime import date
import pickle
import os

# --- 1. CONFIGURAÇÃO INICIAL ---
st.set_page_config(page_title="Wedding Planner J&R", page_icon="💍", layout="wide")

# NOME DO ARQUIVO DE BANCO DE DADOS
DB_FILE = "dados_casamento.pkl"

# --- 2. FUNÇÕES DE PERSISTÊNCIA (SALVAR/CARREGAR) ---
def carregar_dados():
    """Tenta carregar o arquivo. Se não existir, cria os dados padrão."""
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "rb") as f:
                return pickle.load(f)
        except Exception as e:
            st.error(f"Erro ao carregar dados: {e}")
            return None
    return None

def salvar_dados():
    """Salva todo o session_state relevante no arquivo."""
    dados_para_salvar = {
        'data_casamento': st.session_state.get('data_casamento'),
        'financas': st.session_state.get('financas'),
        'renda_extra': st.session_state.get('renda_extra'),
        'orcamento': st.session_state.get('orcamento'),
        'lua_de_mel': st.session_state.get('lua_de_mel'),
        'enxoval': st.session_state.get('enxoval'),
        'checklist': st.session_state.get('checklist'),
        'hacks': st.session_state.get('hacks')
    }
    with open(DB_FILE, "wb") as f:
        pickle.dump(dados_para_salvar, f)

# --- 3. INICIALIZAÇÃO DE DADOS (COM CARREGAMENTO) ---
dados_salvos = carregar_dados()

# Se existirem dados salvos, carregamos. Se não, usamos o padrão.
if dados_salvos:
    if 'data_casamento' not in st.session_state: st.session_state['data_casamento'] = dados_salvos.get('data_casamento', date(2026, 8, 15))
    if 'financas' not in st.session_state: st.session_state['financas'] = dados_salvos.get('financas')
    if 'renda_extra' not in st.session_state: st.session_state['renda_extra'] = dados_salvos.get('renda_extra')
    if 'orcamento' not in st.session_state: st.session_state['orcamento'] = dados_salvos.get('orcamento')
    if 'lua_de_mel' not in st.session_state: st.session_state['lua_de_mel'] = dados_salvos.get('lua_de_mel')
    if 'enxoval' not in st.session_state: st.session_state['enxoval'] = dados_salvos.get('enxoval', [])
    if 'checklist' not in st.session_state: st.session_state['checklist'] = dados_salvos.get('checklist')
    if 'hacks' not in st.session_state: st.session_state['hacks'] = dados_salvos.get('hacks', [])
else:
    # --- DADOS PADRÃO (PRIMEIRA VEZ) ---
    if 'data_casamento' not in st.session_state: st.session_state['data_casamento'] = date(2026, 8, 15)
    
    if 'financas' not in st.session_state:
        st.session_state['financas'] = {"ganhos_joao_fixo": 5000.0, "ganhos_raysa_fixo": 5000.0, "economias_banco": 15000.0}

    if 'renda_extra' not in st.session_state:
        st.session_state['renda_extra'] = pd.DataFrame([
            {"Data": date.today(), "Descrição": "Freela Exemplo", "Quem": "João", "Valor": 0.0}
        ])

    if 'orcamento' not in st.session_state:
        st.session_state['orcamento'] = pd.DataFrame([
            {"Item": "Buffet", "Categoria": "Festa", "Previsto": 18000.0, "Gasto": 2000.0},
            {"Item": "Fotografia", "Categoria": "Festa", "Previsto": 4500.0, "Gasto": 1000.0},
        ])

    if 'lua_de_mel' not in st.session_state:
        st.session_state['lua_de_mel'] = pd.DataFrame([
            {"Atividade/Item": "Passagens", "Custo Estimado": 5000.0, "Status": "Comprado"},
        ])

    if 'enxoval' not in st.session_state: st.session_state['enxoval'] = []

    if 'checklist' not in st.session_state:
        st.session_state['checklist'] = {
            "Fevereiro 2026": [{"task": "Definir local", "done": True}],
        }
    
    if 'hacks' not in st.session_state:
        st.session_state['hacks'] = [
            {"cat": "💸", "titulo": "Câmbio Blue (Western Union)", "desc": "Envie dinheiro para si mesmo pela Western Union para pegar o câmbio blue."},
            {"cat": "🚌", "titulo": "Cartão SUBE", "desc": "Compre um cartão SUBE em qualquer Kiosko para usar ônibus barato."},
            {"cat": "🍔", "titulo": "Menu del Día", "desc": "Almoce pratos executivos, é metade do preço do jantar."}
        ]

# --- 4. SISTEMA DE TEMAS (CSS) ---
def aplicar_tema(usuario):
    if usuario == "Raysa":
        cor_primaria, cor_fundo, cor_card, borda_radius, fonte, borda_input = "#d63031", "#ffe3ec", "#fff0f5", "20px", "'Poppins', sans-serif", "2px solid #e84393"
        gradiente_btn = "linear-gradient(90deg, #e84393 0%, #d63031 100%)"
    else:
        cor_primaria, cor_fundo, cor_card, borda_radius, fonte, borda_input = "#0984e3", "#dfe6e9", "#ffffff", "8px", "'Roboto', sans-serif", "2px solid #b2bec3"
        gradiente_btn = "linear-gradient(90deg, #0984e3 0%, #2d3436 100%)"

    st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&display=swap');
        html, body, [class*="css"] {{ font-family: {fonte}; color: #2d3436; }}
        .stApp {{ background-color: {cor_fundo}; }}
        div.css-card, div.stDataFrame, div[data-testid="stMetric"] {{ background-color: {cor_card}; border-radius: {borda_radius}; padding: 25px; box-shadow: 0 8px 20px rgba(0,0,0,0.1); }}
        .stTextInput input, .stNumberInput input, .stSelectbox div[data-baseweb="select"] {{ background-color: white !important; border: {borda_input} !important; color: #2d3436 !important; border-radius: 8px; }}
        h1, h2, h3 {{ color: {cor_primaria} !important; }}
        .stButton>button {{ background: {gradiente_btn}; color: white !important; border: none; border-radius: {borda_radius}; font-weight: 600; box-shadow: 0 4px 10px rgba(0,0,0,0.2); }}
        section[data-testid="stSidebar"] {{ background-color: white; border-right: 1px solid #ddd; }}
    </style>
    """, unsafe_allow_html=True)

# --- 5. SIDEBAR ---
with st.sidebar:
    st.markdown("### 💍 Planner J&R")
    usuario = st.radio("Quem é você?", ["Raysa", "João"], horizontal=True)
    aplicar_tema(usuario)
    
    st.markdown("---")
    menu = st.radio("Navegação", ["🏠 Dashboard", "💰 Entradas", "💸 Saídas", "🎁 Enxoval", "✅ Tarefas", "💡 Hacks"])
    
    st.markdown("---")
    nova_data = st.date_input("Data Casamento", value=st.session_state['data_casamento'])
    if nova_data != st.session_state['data_casamento']:
        st.session_state['data_casamento'] = nova_data
        salvar_dados() # Salvar ao mudar data
        st.rerun()
    
    # Botão manual de salvar (por segurança)
    if st.button("💾 Salvar Tudo Agora"):
        salvar_dados()
        st.success("Salvo!")

# --- 6. LÓGICA DAS PÁGINAS ---

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
elif menu == "💰 Entradas":
    st.title("💰 Entradas")
    tab1, tab2 = st.tabs(["Fixos", "Extras"])
    with tab1:
        c1, c2 = st.columns(2)
        with c1:
            vf_j = st.number_input("Renda João", value=st.session_state['financas']['ganhos_joao_fixo'])
            vf_r = st.number_input("Renda Raysa", value=st.session_state['financas']['ganhos_raysa_fixo'])
            # Se mudou valor, salva
            if vf_j != st.session_state['financas']['ganhos_joao_fixo'] or vf_r != st.session_state['financas']['ganhos_raysa_fixo']:
                st.session_state['financas']['ganhos_joao_fixo'] = vf_j
                st.session_state['financas']['ganhos_raysa_fixo'] = vf_r
                salvar_dados()
        with c2:
            v_banco = st.number_input("Banco Inicial", value=st.session_state['financas']['economias_banco'])
            if v_banco != st.session_state['financas']['economias_banco']:
                st.session_state['financas']['economias_banco'] = v_banco
                salvar_dados()
    with tab2:
        edited_extra = st.data_editor(st.session_state['renda_extra'], num_rows="dynamic", use_container_width=True)
        # Verifica se houve mudança no dataframe
        if not edited_extra.equals(st.session_state['renda_extra']):
            st.session_state['renda_extra'] = edited_extra
            salvar_dados()

# >>>> SAÍDAS <<<<
elif menu == "💸 Saídas":
    st.title("💸 Saídas")
    tab1, tab2 = st.tabs(["Casamento", "Lua de Mel"])
    with tab1:
        df_orc = st.data_editor(st.session_state['orcamento'], num_rows="dynamic", use_container_width=True)
        if not df_orc.equals(st.session_state['orcamento']):
            st.session_state['orcamento'] = df_orc
            salvar_dados()
    with tab2:
        df_lua = st.data_editor(st.session_state['lua_de_mel'], num_rows="dynamic", use_container_width=True)
        if not df_lua.equals(st.session_state['lua_de_mel']):
            st.session_state['lua_de_mel'] = df_lua
            salvar_dados()

# >>>> ENXOVAL <<<<
elif menu == "🎁 Enxoval":
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
                salvar_dados()
                st.rerun()
    
    if st.session_state['enxoval']:
        cols = st.columns(3)
        for i, item in enumerate(st.session_state['enxoval']):
            with cols[i%3]:
                with st.container():
                    st.markdown(f"**{item['nome']}**")
                    if item.get('imagem'): st.image(item['imagem'], use_container_width=True)
                    st.write(f"R$ {item['preco']:,.2f}")
                    if st.button("🗑️", key=f"d_enx_{i}"):
                        st.session_state['enxoval'].pop(i)
                        salvar_dados()
                        st.rerun()

# >>>> TAREFAS <<<<
elif menu == "✅ Tarefas":
    st.title("Tarefas")
    c_nav, c_list = st.columns([1, 3])
    with c_nav:
        mes = st.selectbox("Mês", list(st.session_state['checklist'].keys()))
        novo = st.text_input("Novo Mês")
        if st.button("Criar"):
            if novo: 
                st.session_state['checklist'][novo] = []
                salvar_dados()
                st.rerun()
    with c_list:
        if mes:
            st.subheader(f"Lista: {mes}")
            c1, c2 = st.columns([0.8, 0.2])
            nt = c1.text_input("Tarefa", label_visibility="collapsed")
            if c2.button("Add", use_container_width=True):
                st.session_state['checklist'][mes].append({"task": nt, "done": False})
                salvar_dados()
                st.rerun()
            st.markdown("---")
            for i, t in enumerate(st.session_state['checklist'][mes]):
                cc, ct, cd = st.columns([0.05, 0.85, 0.1])
                chk = cc.checkbox("", t['done'], key=f"k_{mes}_{i}")
                
                # Se status mudou, salva
                if chk != t['done']:
                    st.session_state['checklist'][mes][i]['done'] = chk
                    salvar_dados()
                    
                style = "text-decoration: line-through; color: #aaa" if chk else ""
                ct.markdown(f"<span style='{style}'>{t['task']}</span>", unsafe_allow_html=True)
                if cd.button("🗑️", key=f"del_{mes}_{i}"):
                    st.session_state['checklist'][mes].pop(i)
                    salvar_dados()
                    st.rerun()

# >>>> HACKS <<<<
elif menu == "💡 Hacks":
    st.title("💡 Hacks de Viagem")
    filtro = st.text_input("🔍 Buscar dica...", "")
    for i, hack in enumerate(st.session_state['hacks']):
        if filtro.lower() in hack['titulo'].lower() or filtro.lower() in hack['desc'].lower():
            with st.expander(f"{hack['cat']} {hack['titulo']}"):
                st.markdown(hack['desc'])
                if st.button("Remover", key=f"del_hack_{i}"):
                    st.session_state['hacks'].pop(i)
                    salvar_dados()
                    st.rerun()
    
    with st.expander("➕ Adicionar Hack"):
        with st.form("form_hacks"):
            cat = st.selectbox("Icone", ["💸", "🍔", "🚌", "🏔️", "💡"])
            h_tit = st.text_input("Título")
            h_desc = st.text_area("Descrição")
            if st.form_submit_button("Salvar"):
                st.session_state['hacks'].append({"cat": cat, "titulo": h_tit, "desc": h_desc})
                salvar_dados()
                st.rerun()
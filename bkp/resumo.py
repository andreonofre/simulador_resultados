# # ====================== FORMATADO COMO MILHAR =======================================

# import streamlit as st

# # ===== Função para formatação BR =====
# def br(num, decimais=2):
#     """Formata número para o padrão brasileiro: 1.234.567,89"""
#     if num is None:
#         return "-"
#     return f"{num:,.{decimais}f}".replace(",", "X").replace(".", ",").replace("X", ".")

# # ===== Configuração da página =====
# st.set_page_config(page_title="Simulações - E se?", layout="wide")

# # ===== CSS customizado =====

# st.markdown("""
# <style>
# /* ======== Ajuste de espaçamento global ======== */
# .block-container {
#     padding-top: 1.4rem !important;
#     padding-bottom: 0rem !important;
# }

# /* ======== Divider ======== */
# hr {
#     margin: 0.1rem 0rem !important;
#     padding: 2px 0 5px 0 !important;
#     border-width: 1px !important;
# }

# /* ======== Títulos ======== */
# h1 {font-size: 1.8rem !important; margin-bottom: 0.4rem !important;}
# h2 {font-size: 1.2rem !important; margin-bottom: 0.3rem !important;}
# h3 {font-size: 1.0rem !important; margin-bottom: 0.2rem !important;}

# /* ======== Sliders e inputs ======== */
# .stSlider {margin-bottom: 0.2rem !important;}
# .stNumberInput {margin-top: -0.4rem !important;}

# /* ======== Métricas ======== */
# div[data-testid="metric-container"] {
#     margin: 0rem !important;
#     padding: 0rem 0rem !important;
# }
# div[data-testid="stMetricLabel"] > div {
#     font-size: 0.75rem !important;  /* diminui o texto da label */
# }
# div[data-testid="stMetricValue"] > div {
#     font-size: 1.0rem !important;   /* diminui o número da métrica */
#     line-height: 1.2rem !important;
# }

# /* ======== Cards customizados ======== */
# div[data-testid="stMarkdownContainer"] > div {
#     margin-bottom: 0rem !important;
# }

# /* ======== Cards principais ======== */
# div.card-principal h3 {
#     font-size: 1.8rem !important; /* aumenta o valor principal */
# }
# div.card-principal h5 {
#     font-size: 2.0rem !important; /* título levemente maior */
# }
# </style>
# """, unsafe_allow_html=True)


# # ===== Título =====
# st.title("🌾 Simulações - \"E se?\"")

# # ===== Parâmetros fixos =====
# AREA_TOTAL_HA = 962.70
# peso_caixa_kg = 4.0

# # ===== Sliders =====

# col1, col2, col3, col4, col5 = st.columns(5)

# with col1:
#     produtividade_slider = st.slider("Produtividade Ton/ha", 10.0, 50.0, 32.0, 0.5, key="s1")
#     produtividade = st.number_input(
#         "Digitar valor:", 
#         min_value=10.0, 
#         max_value=50.0, 
#         value=produtividade_slider, 
#         step=0.5, 
#         key="n1",
#         label_visibility="collapsed"
#     )

# with col2:
#     preco_venda_euro_slider = st.slider("Preço Venda (€/Cx)", 1.0, 10.0, 5.0, 0.1, key="s2")
#     preco_venda_euro = st.number_input(
#         "Digitar valor:", 
#         min_value=1.0, 
#         max_value=10.0, 
#         value=preco_venda_euro_slider, 
#         step=0.1, 
#         key="n2",
#         label_visibility="collapsed"
#     )

# with col3:
#     cambio_slider = st.slider("Câmbio (R$)", 3.0, 8.0, 6.0, 0.05, key="s3")
#     cambio = st.number_input(
#         "Digitar valor:", 
#         min_value=3.0, 
#         max_value=8.0, 
#         value=cambio_slider, 
#         step=0.05, 
#         key="n3",
#         label_visibility="collapsed"
#     )

# with col4:
#     custo_campo_slider = st.slider("R$/Kg Campo", 0.5, 5.0, 1.80, 0.1, key="s4")
#     custo_campo = st.number_input(
#         "Digitar valor:", 
#         min_value=0.5, 
#         max_value=5.0, 
#         value=custo_campo_slider, 
#         step=0.1, 
#         key="n4",
#         label_visibility="collapsed"
#     )

# with col5:
#     refugo_slider = st.slider("% Refugo", 0.01, 0.2, 0.05, 0.01, key="s5")
#     refugo = st.number_input(
#         "Digitar valor:", 
#         min_value=0.01, 
#         max_value=0.2, 
#         value=refugo_slider, 
#         step=0.01, 
#         key="n5",
#         label_visibility="collapsed"
#     )

# # ===== Segunda linha de sliders =====
# col6, col7, col8, col9 = st.columns(4)

# with col6:
#     custo_packing_slider = st.slider("R$/Cx Packing", 1.0, 15.0, 5.0, 0.1, key="s6")
#     custo_packing = st.number_input(
#         "Digitar valor:", 
#         min_value=1.0, 
#         max_value=15.0, 
#         value=custo_packing_slider, 
#         step=0.1, 
#         key="n6",
#         label_visibility="collapsed"
#     )

# with col7:
#     desp_adm_slider = st.slider("Desp. Adm (R$/Cx)", 0.0, 10.0, 2.30, 0.1, key="s7")
#     desp_adm = st.number_input(
#         "Digitar valor:", 
#         min_value=0.0, 
#         max_value=10.0, 
#         value=desp_adm_slider, 
#         step=0.1, 
#         key="n7",
#         label_visibility="collapsed"
#     )

# with col8:
#     desp_financeira_slider = st.slider("Desp. Financeira (R$/Cx)", 0.0, 10.0, 1.0, 0.1, key="s8")
#     desp_financeira = st.number_input(
#         "Digitar valor:", 
#         min_value=0.0, 
#         max_value=10.0, 
#         value=desp_financeira_slider, 
#         step=0.1, 
#         key="n8",
#         label_visibility="collapsed"
#     )

# with col9:
#     valor_medio_folha_slider = st.slider("Valor Médio Folha (R$)", 1_000_000.0, 5_000_000.0, 2_300_000.0, 50_000.0, key="s9")
#     valor_medio_folha = st.number_input(
#         "Digitar valor:", 
#         min_value=1_000_000.0, 
#         max_value=5_000_000.0, 
#         value=valor_medio_folha_slider, 
#         step=50_000.0, 
#         key="n9",
#         label_visibility="collapsed"
#     )

# st.divider()

# # ===== Cálculos =====
# producao_total_ton = AREA_TOTAL_HA * produtividade
# producao_total_kg = producao_total_ton * 1000
# qtd_caixas = (producao_total_kg / peso_caixa_kg) * (1 - refugo)
# preco_caixa_reais = preco_venda_euro * cambio
# faturamento_proporcional = qtd_caixas * preco_caixa_reais

# custo_campo_total = producao_total_kg * custo_campo
# custo_packing_total = qtd_caixas * custo_packing
# desp_adm_total = qtd_caixas * desp_adm
# desp_financeira_total = qtd_caixas * desp_financeira
# custos_despesas_total = custo_campo_total + custo_packing_total + desp_adm_total + desp_financeira_total

# lucro_liquido = faturamento_proporcional - custos_despesas_total
# margem_liquida = (lucro_liquido / faturamento_proporcional * 100) if faturamento_proporcional > 0 else 0
# participacao_resultados = (lucro_liquido * 0.10) / valor_medio_folha if valor_medio_folha > 0 else 0

# # ===== Exibição dos resultados =====
# col_r1, col_r2, col_r3 = st.columns(3)

# with col_r1:
#     st.markdown(f"""
#     <div style='background-color: #1e7ba3; padding: 8px; border-radius: 8px; margin-bottom: 8px;'>
#         <h5 style='color: white; margin: 0; font-size: 0.9rem;'>💰 Faturamento Próprio</h5>
#         <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>R$ {br(faturamento_proporcional, 0)}</h3>
#     </div>
#     """, unsafe_allow_html=True)

#     st.divider()

#     st.metric("📦 Caixas", f"{br(qtd_caixas, 0)}")

# with col_r2:
#     cor_lucro = "#2d5016" if lucro_liquido >= 0 else "#8B0000"
#     st.markdown(f"""
#     <div style='background-color: {cor_lucro}; padding: 8px; border-radius: 8px; margin-bottom: 8px;'>
#         <h5 style='color: white; margin: 0; font-size: 0.9rem;'>💵 Lucro Líquido</h5>
#         <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>R$ {br(lucro_liquido, 0)}</h3>
#     </div>
#     """, unsafe_allow_html=True)

#     st.divider()

#     st.metric("📊 Margem Líquida", f"{br(margem_liquida, 1)}%")

# with col_r3:
#     st.markdown(f"""
#     <div style='background-color: #812378; padding: 8px; border-radius: 8px; margin-bottom: 8px;'>
#         <h5 style='color: white; margin: 0; font-size: 0.9rem;'>👥 PPR (10%)</h5>
#         <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>{br(participacao_resultados, 2)}</h3>
#     </div>
#     """, unsafe_allow_html=True)

#     st.divider()

#     st.metric("🌾 Produção", f"{br(producao_total_ton, 0)} ton")


# st.divider()

# # ===== Detalhamento de custos =====
# col_d1, col_d2, col_d3, col_d4, col_d5 = st.columns(5)

# with col_d1:
#     st.markdown(f"""
#     <div style='background-color: #ff8c00; padding: 10px; border-radius: 6px; text-align: center;'>
#         <p style='color: white; margin: 0; font-size: 0.75rem;'>Custo Campo</p>
#         <h5 style='color: white; margin: 3px 0; font-size: 1rem;'>R$ {br(custo_campo_total, 0)}</h5>
#     </div>
#     """, unsafe_allow_html=True)

# with col_d2:
#     st.markdown(f"""
#     <div style='background-color: #ff8c00; padding: 10px; border-radius: 6px; text-align: center;'>
#         <p style='color: white; margin: 0; font-size: 0.75rem;'>Custo PH</p>
#         <h5 style='color: white; margin: 3px 0; font-size: 1rem;'>R$ {br(custo_packing_total, 0)}</h5>
#     </div>
#     """, unsafe_allow_html=True)

# with col_d3:
#     st.markdown(f"""
#     <div style='background-color: #ff8c00; padding: 10px; border-radius: 6px; text-align: center;'>
#         <p style='color: white; margin: 0; font-size: 0.75rem;'>Desp. Financeira</p>
#         <h5 style='color: white; margin: 3px 0; font-size: 1rem;'>R$ {br(desp_financeira_total, 0)}</h5>
#     </div>
#     """, unsafe_allow_html=True)

# with col_d4:
#     st.markdown(f"""
#     <div style='background-color: #ff8c00; padding: 10px; border-radius: 6px; text-align: center;'>
#         <p style='color: white; margin: 0; font-size: 0.75rem;'>Adm. Sede</p>
#         <h5 style='color: white; margin: 3px 0; font-size: 1rem;'>R$ {br(desp_adm_total, 0)}</h5>
#     </div>
#     """, unsafe_allow_html=True)

# with col_d5:
#     st.markdown(f"""
#     <div style='background-color: #d35400; padding: 10px; border-radius: 6px; text-align: center;'>
#         <p style='color: white; margin: 0; font-size: 0.75rem;'>Total Custos</p>
#         <h5 style='color: white; margin: 3px 0; font-size: 1rem;'>R$ {br(custos_despesas_total, 0)}</h5>
#     </div>
#     """, unsafe_allow_html=True)

# # ===== Informações adicionais =====

# st.divider()

# st.info(f"""
# **ℹ️ Informações da Simulação:**
# - Área Total: {br(AREA_TOTAL_HA, 2)} ha  
# - Peso por Caixa: {peso_caixa_kg} kg  
# - Preço de Venda: €{br(preco_venda_euro, 2)}/cx = R$ {br(preco_caixa_reais, 2)}/cx  
# - Caixas (automático): {br(qtd_caixas, 0)}  
# - Kg Totais: {br(producao_total_kg, 2)}
# """)
















# ====================== FORMATADO COMO MILHAR =======================================


import streamlit as st


# ===== Função para formatação BR =====
def br(num, decimais=2):
    """Formata número para o padrão brasileiro: 1.234.567,89"""
    if num is None:
        return "-"
    return f"{num:,.{decimais}f}".replace(",", "X").replace(".", ",").replace("X", ".")


# ===== Configuração da página =====
st.set_page_config(page_title="Simulações - E se?", layout="wide")


# ===== CSS customizado =====


st.markdown("""
<style>
/* ======== Ajuste de espaçamento global ======== */
.block-container {
    padding-top: 1.4rem !important;
    padding-bottom: 0rem !important;
}


/* ======== Divider ======== */
hr {
    margin: 0.1rem 0rem !important;
    padding: 2px 0 5px 0 !important;
    border-width: 1px !important;
}


/* ======== Títulos ======== */
h1 {font-size: 1.8rem !important; margin-bottom: 0.4rem !important;}
h2 {font-size: 1.2rem !important; margin-bottom: 0.3rem !important;}
h3 {font-size: 1.0rem !important; margin-bottom: 0.2rem !important;}


/* ======== Inputs ======== */
.stNumberInput {margin-bottom: 0.5rem !important;}


/* ======== Métricas ======== */
div[data-testid="metric-container"] {
    margin: 0rem !important;
    padding: 0rem 0rem !important;
}
div[data-testid="stMetricLabel"] > div {
    font-size: 0.75rem !important;  /* diminui o texto da label */
}
div[data-testid="stMetricValue"] > div {
    font-size: 1.0rem !important;   /* diminui o número da métrica */
    line-height: 1.2rem !important;
}


/* ======== Cards customizados ======== */
div[data-testid="stMarkdownContainer"] > div {
    margin-bottom: 0rem !important;
}


/* ======== Cards principais ======== */
div.card-principal h3 {
    font-size: 1.8rem !important; /* aumenta o valor principal */
}
div.card-principal h5 {
    font-size: 2.0rem !important; /* título levemente maior */
}
</style>
""", unsafe_allow_html=True)



# ===== Título =====
st.title("🌾 Simulações - \"E se?\"")


# ===== Parâmetros fixos =====
AREA_TOTAL_HA = 1097.74
peso_caixa_kg = 4.0


# ===== Inputs de Parâmetros =====


col1, col2, col3, col4, col5 = st.columns(5)


with col1:
    # Input para produtividade
    produtividade = st.number_input(
        "Produtividade Ton/ha", 
        min_value=10.0, 
        max_value=50.0, 
        value=31.0,
        step=0.1,
        format="%.1f"
    )


with col2:
    # Input para preço de venda em euros
    preco_venda_euro = st.number_input(
        "Preço Venda (€/Cx)", 
        min_value=1.0, 
        max_value=10.0, 
        value=4.5,
        step=0.1,
        format="%.2f"
    )


with col3:
    # Input para câmbio
    cambio = st.number_input(
        "Câmbio (R$)", 
        min_value=3.0, 
        max_value=8.0, 
        value=6.0,
        step=0.05,
        format="%.2f"
    )


with col4:
    # Input para custo de campo
    custo_campo = st.number_input(
        "R$/Kg Campo", 
        min_value=0.5, 
        max_value=5.0, 
        value=1.90,
        step=0.1,
        format="%.2f"
    )


with col5:
    # Input para refugo (percentual)
    refugo = st.number_input(
        "% Refugo", 
        min_value=0.01, 
        max_value=0.20, 
        value=0.08,
        step=0.01,
        format="%.2f"
    )


# ===== Segunda linha de inputs =====
col6, col7, col8, col9 = st.columns(4)


with col6:
    # Input para custo de packing
    custo_packing = st.number_input(
        "R$/Cx Packing", 
        min_value=1.0, 
        max_value=15.0, 
        value=4.9,
        step=0.1,
        format="%.2f"
    )


with col7:
    # Input para despesa administrativa
    desp_adm = st.number_input(
        "Desp. Adm (R$/Cx)", 
        min_value=0.0, 
        max_value=10.0, 
        value=2.30,
        step=0.1,
        format="%.2f"
    )


with col8:
    # Input para despesa financeira
    desp_financeira = st.number_input(
        "Desp. Financeira (R$/Cx)", 
        min_value=0.0, 
        max_value=10.0, 
        value=1.0,
        step=0.1,
        format="%.2f"
    )


with col9:
    # Input para valor médio da folha de pagamento
    valor_medio_folha = st.number_input(
        "Valor Médio Folha (R$)", 
        min_value=1000000.0, 
        max_value=5000000.0, 
        value=2200000.0,
        step=50000.0,
        format="%.0f"
    )


st.divider()


# ===== Cálculos =====
# Calcula a produção total em toneladas
producao_total_ton = AREA_TOTAL_HA * produtividade

# Converte a produção total para kg
producao_total_kg = producao_total_ton * 1000

# Calcula a quantidade de caixas considerando o refugo
qtd_caixas = (producao_total_kg / peso_caixa_kg) * (1 - refugo)

# Calcula o preço da caixa em reais
preco_caixa_reais = preco_venda_euro * cambio

# Calcula o faturamento proporcional
faturamento_proporcional = qtd_caixas * preco_caixa_reais


# Calcula os custos
custo_campo_total = producao_total_kg * custo_campo
custo_packing_total = qtd_caixas * custo_packing
desp_adm_total = qtd_caixas * desp_adm
desp_financeira_total = qtd_caixas * desp_financeira

# Soma todos os custos e despesas
custos_despesas_total = custo_campo_total + custo_packing_total + desp_adm_total + desp_financeira_total


# Calcula o lucro líquido
lucro_liquido = faturamento_proporcional - custos_despesas_total

# Calcula a margem líquida (percentual)
margem_liquida = (lucro_liquido / faturamento_proporcional * 100) if faturamento_proporcional > 0 else 0

# Calcula a participação nos resultados (PPR)
participacao_resultados = (lucro_liquido * 0.10) / valor_medio_folha if valor_medio_folha > 0 else 0


# ===== Exibição dos resultados =====
col_r1, col_r2, col_r3 = st.columns(3)


with col_r1:
    st.markdown(f"""
    <div style='background-color: #1e7ba3; padding: 8px; border-radius: 8px; margin-bottom: 8px;'>
        <h5 style='color: white; margin: 0; font-size: 0.9rem;'>💰 Faturamento Próprio</h5>
        <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>R$ {br(faturamento_proporcional, 0)}</h3>
    </div>
    """, unsafe_allow_html=True)


    st.divider()


    st.metric("📦 Caixas", f"{br(qtd_caixas, 0)}")


with col_r2:
    # Define a cor do card de lucro (verde se positivo, vermelho se negativo)
    cor_lucro = "#2d5016" if lucro_liquido >= 0 else "#8B0000"
    st.markdown(f"""
    <div style='background-color: {cor_lucro}; padding: 8px; border-radius: 8px; margin-bottom: 8px;'>
        <h5 style='color: white; margin: 0; font-size: 0.9rem;'>💵 Lucro Líquido</h5>
        <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>R$ {br(lucro_liquido, 0)}</h3>
    </div>
    """, unsafe_allow_html=True)


    st.divider()


    st.metric("📊 Margem Líquida", f"{br(margem_liquida, 1)}%")


with col_r3:
    st.markdown(f"""
    <div style='background-color: #812378; padding: 8px; border-radius: 8px; margin-bottom: 8px;'>
        <h5 style='color: white; margin: 0; font-size: 0.9rem;'>👥 PPR (10%)</h5>
        <h3 style='color: white; margin: 5px 0; font-size: 1.4rem;'>{br(participacao_resultados, 2)}</h3>
    </div>
    """, unsafe_allow_html=True)


    st.divider()


    st.metric("🌾 Produção", f"{br(producao_total_ton, 0)} ton")



st.divider()


# ===== Detalhamento de custos =====
col_d1, col_d2, col_d3, col_d4, col_d5 = st.columns(5)


with col_d1:
    st.markdown(f"""
    <div style='background-color: #ff8c00; padding: 10px; border-radius: 6px; text-align: center;'>
        <p style='color: white; margin: 0; font-size: 0.75rem;'>Custo Campo</p>
        <h5 style='color: white; margin: 3px 0; font-size: 1rem;'>R$ {br(custo_campo_total, 0)}</h5>
    </div>
    """, unsafe_allow_html=True)


with col_d2:
    st.markdown(f"""
    <div style='background-color: #ff8c00; padding: 10px; border-radius: 6px; text-align: center;'>
        <p style='color: white; margin: 0; font-size: 0.75rem;'>Custo PH</p>
        <h5 style='color: white; margin: 3px 0; font-size: 1rem;'>R$ {br(custo_packing_total, 0)}</h5>
    </div>
    """, unsafe_allow_html=True)


with col_d3:
    st.markdown(f"""
    <div style='background-color: #ff8c00; padding: 10px; border-radius: 6px; text-align: center;'>
        <p style='color: white; margin: 0; font-size: 0.75rem;'>Desp. Financeira</p>
        <h5 style='color: white; margin: 3px 0; font-size: 1rem;'>R$ {br(desp_financeira_total, 0)}</h5>
    </div>
    """, unsafe_allow_html=True)


with col_d4:
    st.markdown(f"""
    <div style='background-color: #ff8c00; padding: 10px; border-radius: 6px; text-align: center;'>
        <p style='color: white; margin: 0; font-size: 0.75rem;'>Adm. Sede</p>
        <h5 style='color: white; margin: 3px 0; font-size: 1rem;'>R$ {br(desp_adm_total, 0)}</h5>
    </div>
    """, unsafe_allow_html=True)


with col_d5:
    st.markdown(f"""
    <div style='background-color: #d35400; padding: 10px; border-radius: 6px; text-align: center;'>
        <p style='color: white; margin: 0; font-size: 0.75rem;'>Total Custos</p>
        <h5 style='color: white; margin: 3px 0; font-size: 1rem;'>R$ {br(custos_despesas_total, 0)}</h5>
    </div>
    """, unsafe_allow_html=True)


# ===== Informações adicionais =====


st.divider()


st.info(f"""
**ℹ️ Informações da Simulação:**
- Área Total: {br(AREA_TOTAL_HA, 2)} ha  
- Peso por Caixa: {peso_caixa_kg} kg  
- Preço de Venda: €{br(preco_venda_euro, 2)}/cx = R$ {br(preco_caixa_reais, 2)}/cx  
- Caixas (automático): {br(qtd_caixas, 0)}  
- Kg Totais: {br(producao_total_kg, 2)}
""")

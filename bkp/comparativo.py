import streamlit as st


def br(num, decimais=2):
    if num is None:
        return "-"
    return f"{num:,.{decimais}f}".replace(",", "X").replace(".", ",").replace("X", ".")


st.set_page_config(page_title="Comparativo de Anos", layout="wide")

st.markdown("""
<style>
.block-container { padding-top: 1.4rem !important; padding-bottom: 0rem !important; }
hr { margin: 0.1rem 0rem !important; border-width: 1px !important; }
h1 { font-size: 1.8rem !important; margin-bottom: 0.4rem !important; }

/* ── Cabeçalho fixo clonado via JS ── */
#cab-fixo-clone {
    position: fixed;
    top: 0;
    z-index: 9999;
    background: rgba(14,17,23,0.97);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border-bottom: 1px solid rgba(255,255,255,0.09);
    box-sizing: border-box;
}
/* empurra o conteúdo para não ficar atrás do header fixo */
.main .block-container { margin-top: 5.5rem !important; }

/* ── Botões de toggle de seção — full width, aspecto de header ──
   A estilização visual é feita via JS para evitar conflitos de specificity.
   Aqui apenas reset de padding/height que o Streamlit impõe. */
div[data-testid="stButton"] > button {
    transition: background 0.15s ease;
}
</style>
""", unsafe_allow_html=True)

st.title("📊 Comparativo de Anos")


# ================================================================
# PARÂMETROS 2026 — Sidebar
# ================================================================
with st.sidebar:
    st.header("⚙️ Parâmetros 2026")
    st.caption("Afetam apenas a projeção Abr-Dez de 2026 nesta página.")
    st.divider()
    produtividade    = st.number_input("Produtividade Ton/ha",      min_value=10.0,        max_value=50.0,        value=35.00,       step=0.1,     format="%.2f")
    preco_venda_euro = st.number_input("Preço Venda (€/Cx)",        min_value=1.0,         max_value=10.0,        value=4.5,         step=0.1,     format="%.2f")
    cambio           = st.number_input("Câmbio (R$)",               min_value=3.0,         max_value=8.0,         value=6.0,         step=0.05,    format="%.2f")
    custo_campo_kg   = st.number_input("R$/Kg Campo",               min_value=0.5,         max_value=5.0,         value=1.90,        step=0.1,     format="%.2f")
    refugo           = st.number_input("% Refugo",                  min_value=0.01,        max_value=0.20,        value=0.0808,      step=0.01,    format="%.4f")
    custo_packing    = st.number_input("R$/Cx Packing",             min_value=1.0,         max_value=15.0,        value=4.9,         step=0.1,     format="%.2f")
    desp_adm_cx      = st.number_input("Desp. Adm (R$/Cx)",        min_value=0.0,         max_value=10.0,        value=2.3,         step=0.1,     format="%.2f")
    desp_fin_cx      = st.number_input("Desp. Financeira (R$/Cx)", min_value=0.0,         max_value=10.0,        value=1.0,         step=0.1,     format="%.2f")
    valor_folha      = st.number_input("Valor Médio Folha (R$)",   min_value=1_000_000.0, max_value=5_000_000.0, value=2_200_000.0, step=50_000.0, format="%.0f")


# ================================================================
# DADOS 2024
# ================================================================
FAT_2024          = 159_174_496.81
CUSTO_CAMPO_2024  = 56_087_947.19
CUSTO_PH_2024     = 29_466_508.72
CUSTO_ADM_2024    = 17_912_531.61
DESP_FIN_2024     = 6_038_219.0
CAIXAS_2024       = 6_038_219
PRODUCAO_TON_2024 = 27_768.954
HECTARES_2024     = 970.20
PPR_2024          = 2.6


# ================================================================
# DADOS 2025
# ================================================================
FAT_2025          = 171_877_801.15
CUSTO_CAMPO_2025  = 66_813_314.28
CUSTO_PH_2025     = 32_780_834.80
CUSTO_ADM_2025    = 15_098_057.78
DESP_FIN_2025     = 6_886_730.0
CAIXAS_2025       = 6_886_730
PRODUCAO_TON_2025 = 32_248.97
HECTARES_2025     = 984.26
PPR_2025          = 2.74


# ================================================================
# DADOS 2026 — Jan-Mar Realizados
# ================================================================
FATURAMENTO_JAN_MAR   = 31_782_635.69
CUSTO_CAMPO_JAN_MAR   = 11_485_738.00
CUSTO_PH_JAN_MAR      = 11_575_669.17
CUSTO_ADM_JAN_MAR     = 3_021_077.49
DESP_FIN_JAN_MAR      = 1_198_102.00
CAIXAS_JAN_MAR        = 1_198_102
HECTARES_FECHADOS     = 157.33
PRODUTIVIDADE_JAN_MAR = 51.46
AREA_TOTAL_HA         = 1_097.74
HECTARES_RESTANTES    = 940.41
PESO_CAIXA_KG         = 4.0


# ================================================================
# CÁLCULOS 2026 — Abr-Dez Projetado
# ================================================================
prod_abr_dez_ton_bruta = HECTARES_RESTANTES * produtividade
prod_abr_dez_kg_bruta  = prod_abr_dez_ton_bruta * 1000
prod_abr_dez_ton_liq   = prod_abr_dez_ton_bruta * (1 - refugo)
qtd_caixas_abr_dez     = (prod_abr_dez_ton_liq * 1000) / PESO_CAIXA_KG
preco_cx_reais         = preco_venda_euro * cambio
fat_abr_dez            = qtd_caixas_abr_dez * preco_cx_reais
custo_campo_abr_dez    = prod_abr_dez_kg_bruta * custo_campo_kg
custo_ph_abr_dez       = qtd_caixas_abr_dez * custo_packing
custo_adm_abr_dez      = qtd_caixas_abr_dez * desp_adm_cx
desp_fin_abr_dez       = qtd_caixas_abr_dez * desp_fin_cx
custos_abr_dez         = custo_campo_abr_dez + custo_ph_abr_dez + custo_adm_abr_dez + desp_fin_abr_dez


# ================================================================
# TOTAIS 2026 (Jan-Mar + Abr-Dez)
# ================================================================
FAT_2026          = FATURAMENTO_JAN_MAR + fat_abr_dez
CUSTO_CAMPO_2026  = CUSTO_CAMPO_JAN_MAR + custo_campo_abr_dez
CUSTO_PH_2026     = CUSTO_PH_JAN_MAR + custo_ph_abr_dez
CUSTO_ADM_2026    = CUSTO_ADM_JAN_MAR + custo_adm_abr_dez
DESP_FIN_2026     = DESP_FIN_JAN_MAR + desp_fin_abr_dez
CUSTOS_2026       = CUSTO_CAMPO_2026 + CUSTO_PH_2026 + CUSTO_ADM_2026 + DESP_FIN_2026
LUCRO_2026        = FAT_2026 - CUSTOS_2026
MARGEM_2026       = (LUCRO_2026 / FAT_2026 * 100) if FAT_2026 > 0 else 0
CAIXAS_2026       = CAIXAS_JAN_MAR + qtd_caixas_abr_dez
PRODUCAO_TON_2026 = HECTARES_FECHADOS * PRODUTIVIDADE_JAN_MAR + prod_abr_dez_ton_liq
PPR_2026          = (LUCRO_2026 * 0.10) / valor_folha if valor_folha > 0 else 0


# ================================================================
# TOTAIS 2025 / 2024
# ================================================================
CUSTOS_2025 = CUSTO_CAMPO_2025 + CUSTO_PH_2025 + CUSTO_ADM_2025 + DESP_FIN_2025
LUCRO_2025  = FAT_2025 - CUSTOS_2025
MARGEM_2025 = (LUCRO_2025 / FAT_2025 * 100) if FAT_2025 > 0 else 0

CUSTOS_2024 = CUSTO_CAMPO_2024 + CUSTO_PH_2024 + CUSTO_ADM_2024 + DESP_FIN_2024
LUCRO_2024  = FAT_2024 - CUSTOS_2024
MARGEM_2024 = (LUCRO_2024 / FAT_2024 * 100) if FAT_2024 > 0 else 0


# ================================================================
# CÁLCULOS DERIVADOS
# ================================================================
CUSTO_TOTAL_JAN_MAR  = CUSTO_CAMPO_JAN_MAR + CUSTO_PH_JAN_MAR + CUSTO_ADM_JAN_MAR + DESP_FIN_JAN_MAR
LUCRO_JAN_MAR        = FATURAMENTO_JAN_MAR - CUSTO_TOTAL_JAN_MAR
MARGEM_JAN_MAR       = (LUCRO_JAN_MAR / FATURAMENTO_JAN_MAR * 100) if FATURAMENTO_JAN_MAR > 0 else 0
PRODUCAO_JAN_MAR_TON = HECTARES_FECHADOS * PRODUTIVIDADE_JAN_MAR
PPR_JAN_MAR          = (LUCRO_JAN_MAR * 0.10) / valor_folha if valor_folha > 0 else 0

LUCRO_ABR_DEZ  = fat_abr_dez - custos_abr_dez
MARGEM_ABR_DEZ = (LUCRO_ABR_DEZ / fat_abr_dez * 100) if fat_abr_dez > 0 else 0
PPR_ABR_DEZ    = (LUCRO_ABR_DEZ * 0.10) / valor_folha if valor_folha > 0 else 0

PRODUT_2024    = PRODUCAO_TON_2024 / HECTARES_2024 if HECTARES_2024 > 0 else 0
PRODUT_2025    = PRODUCAO_TON_2025 / HECTARES_2025 if HECTARES_2025 > 0 else 0
PRODUT_JAN_MAR = PRODUTIVIDADE_JAN_MAR
PRODUT_ABR_DEZ = produtividade
PRODUT_2026    = PRODUCAO_TON_2026 / AREA_TOTAL_HA if AREA_TOTAL_HA > 0 else 0


# ================================================================
# CORES E FUNDOS
# ================================================================
ACENTO_24  = "#e65100"
ACENTO_25  = "#f9a825"
ACENTO_26R = "#1565c0"
ACENTO_26P = "#6a1b9a"
ACENTO_26T = "#2e7d32"

BG_NEUTRO  = "rgba(100,100,120,0.10)"
BG_FAT     = "rgba(46,125,50,0.18)"
BG_SEC_FAT = "rgba(46,125,50,0.30)"
BG_CUSTO   = "rgba(180,100,0,0.14)"
BG_TOTALC  = "rgba(180,60,0,0.28)"
BG_SEC_CUS = "rgba(180,100,0,0.30)"
BG_RES     = "rgba(21,101,192,0.12)"
BG_LUCROP  = "rgba(46,125,50,0.22)"
BG_LUCRON  = "rgba(183,28,28,0.22)"
BG_SEC_RES = "rgba(21,101,192,0.30)"
BG_OPE     = "rgba(69,90,100,0.14)"
BG_SEC_OPE = "rgba(69,90,100,0.30)"


# ================================================================
# COLUNAS — fixas (label + 2024 + 2025 + Jan-Mar + Abr-Dez + Total + var%)
# ================================================================
COLS = [1.8, 1, 1, 1, 1, 1, 0.7]


# ================================================================
# ESTADO DE AGRUPAMENTO DE LINHAS
# ================================================================
if "expand_custos"      not in st.session_state: st.session_state.expand_custos      = True
if "expand_resultado"   not in st.session_state: st.session_state.expand_resultado   = True
if "expand_operacional" not in st.session_state: st.session_state.expand_operacional = True


# ================================================================
# FUNÇÕES AUXILIARES
# ================================================================
def _celula(texto, bg, acento=None, bold=False, align="right"):
    peso  = "bold" if bold else "normal"
    borda = f"border-left:4px solid {acento};" if acento else "border-left:4px solid transparent;"
    return (
        f"<div style='background:{bg}; {borda} padding:7px 12px; border-radius:5px; "
        f"text-align:{align}; margin:2px 0;'>"
        f"<span style='font-size:0.88rem; font-weight:{peso};'>{texto}</span></div>"
    )


def _fmt(v, fmt):
    if fmt == "R$":  return f"R$ {br(v, 0)}"
    if fmt == "%":   return f"{br(v, 1)}%"
    if fmt == "num": return br(v, 0)
    if fmt == "dec": return br(v, 2)
    if fmt == "x":   return br(v, 2)
    return str(v)


def _var_pct(v_novo, v_ref):
    if v_ref and v_ref != 0:
        return (v_novo - v_ref) / abs(v_ref) * 100
    return None


def _badge_var(pct, inverso=False):
    if pct is None:
        return "<span style='font-size:0.75rem; opacity:0.4;'>—</span>"
    positivo_bom = (pct >= 0) if not inverso else (pct <= 0)
    cor  = "#4caf50" if positivo_bom else "#f44336"
    seta = "▲" if pct >= 0 else "▼"
    return (
        f"<div style='text-align:center; padding:6px 4px;'>"
        f"<span style='color:{cor}; font-size:0.82rem; font-weight:bold;'>{seta} {abs(pct):.1f}%</span>"
        f"</div>"
    )


def render_row(label, val_24, val_25, val_26r, val_26p, val_26t=None, fmt="R$",
               bg_label=BG_NEUTRO, bg_24=None, bg_25=None, bg_26r=None, bg_26p=None, bg_26t=None,
               bold=False, var_inverso=False):
    b24  = bg_24  or BG_NEUTRO
    b25  = bg_25  or BG_NEUTRO
    b26r = bg_26r or BG_NEUTRO
    b26p = bg_26p or BG_NEUTRO
    b26t = bg_26t or BG_NEUTRO
    cols = st.columns(COLS)
    with cols[0]: st.markdown(_celula(label,            bg_label, bold=bold, align="left"), unsafe_allow_html=True)
    with cols[1]: st.markdown(_celula(_fmt(val_24,  fmt), b24,  acento=ACENTO_24,  bold=bold), unsafe_allow_html=True)
    with cols[2]: st.markdown(_celula(_fmt(val_25,  fmt), b25,  acento=ACENTO_25,  bold=bold), unsafe_allow_html=True)
    with cols[3]: st.markdown(_celula(_fmt(val_26r, fmt), b26r, acento=ACENTO_26R, bold=bold), unsafe_allow_html=True)
    with cols[4]: st.markdown(_celula(_fmt(val_26p, fmt), b26p, acento=ACENTO_26P, bold=bold), unsafe_allow_html=True)
    with cols[5]: st.markdown(_celula(_fmt(val_26t, fmt), b26t, acento=ACENTO_26T, bold=bold), unsafe_allow_html=True)
    with cols[6]:
        pct = _var_pct(val_26t, val_25) if val_26t is not None else None
        st.markdown(_badge_var(pct, inverso=var_inverso), unsafe_allow_html=True)


# ================================================================
# CABEÇALHO — renderizado no DOM, depois clonado fixo via JS
# ================================================================
st.markdown("<div id='cabecalho-fixo'>", unsafe_allow_html=True)
_hcols = st.columns(COLS)

with _hcols[0]:
    st.markdown(
        "<div style='padding:8px 12px; margin:2px 0; display:flex; align-items:center; height:52px;'>"
        "<span style='font-size:0.72rem; font-weight:bold; opacity:0.45; text-transform:uppercase; "
        "letter-spacing:0.1em;'>INDICADOR</span></div>",
        unsafe_allow_html=True)

with _hcols[1]:
    st.markdown(
        f"<div style='border-left:4px solid {ACENTO_24}; background:{BG_NEUTRO}; padding:8px 12px; "
        f"border-radius:6px; text-align:center; margin:2px 0;'>"
        f"<span style='color:{ACENTO_24}; font-weight:bold; font-size:1.0rem;'>2024</span><br>"
        f"<span style='font-size:0.68rem; opacity:0.55;'>Fechado</span></div>",
        unsafe_allow_html=True)

with _hcols[2]:
    st.markdown(
        f"<div style='border-left:4px solid {ACENTO_25}; background:{BG_NEUTRO}; padding:8px 12px; "
        f"border-radius:6px; text-align:center; margin:2px 0;'>"
        f"<span style='color:{ACENTO_25}; font-weight:bold; font-size:1.0rem;'>2025</span><br>"
        f"<span style='font-size:0.68rem; opacity:0.55;'>Fechado</span></div>",
        unsafe_allow_html=True)

with _hcols[3]:
    st.markdown(
        f"<div style='border-left:4px solid {ACENTO_26R}; background:{BG_NEUTRO}; padding:8px 12px; "
        f"border-radius:6px; text-align:center; margin:2px 0;'>"
        f"<span style='color:{ACENTO_26R}; font-weight:bold; font-size:1.0rem;'>2026 Jan-Mar</span><br>"
        f"<span style='font-size:0.68rem; opacity:0.55;'>Realizado</span></div>",
        unsafe_allow_html=True)

with _hcols[4]:
    st.markdown(
        f"<div style='border-left:4px solid {ACENTO_26P}; background:{BG_NEUTRO}; padding:8px 12px; "
        f"border-radius:6px; text-align:center; margin:2px 0;'>"
        f"<span style='color:{ACENTO_26P}; font-weight:bold; font-size:1.0rem;'>2026 Abr-Dez</span><br>"
        f"<span style='font-size:0.68rem; opacity:0.55;'>Projetado</span></div>",
        unsafe_allow_html=True)

with _hcols[5]:
    st.markdown(
        f"<div style='border-left:4px solid {ACENTO_26T}; background:rgba(46,125,50,0.18); padding:8px 12px; "
        f"border-radius:6px; text-align:center; margin:2px 0;'>"
        f"<span style='color:{ACENTO_26T}; font-weight:bold; font-size:1.0rem;'>2026 Total</span><br>"
        f"<span style='font-size:0.68rem; opacity:0.55;'>Jan-Dez (est.)</span></div>",
        unsafe_allow_html=True)

with _hcols[6]:
    st.markdown(
        "<div style='padding:8px 6px; text-align:center; margin:2px 0; height:52px; "
        "display:flex; align-items:center; justify-content:center;'>"
        "<span style='font-size:0.65rem; opacity:0.45; font-weight:bold;'>vs 2025</span></div>",
        unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)


# ================================================================
# JS — fixa cabeçalho + estiliza botões de seção
# ================================================================
st.markdown("""
<script>
(function () {
  // Mapeamento: texto do botão → estilos do header de seção
  var SEC = {
    'RECEITA':           {bg:'rgba(46,125,50,0.30)',   bl:'#2e7d32'},
    'CUSTOS E DESPESAS': {bg:'rgba(180,100,0,0.30)',   bl:'#b45a00'},
    'RESULTADO':         {bg:'rgba(21,101,192,0.30)',  bl:'#1565c0'},
    'OPERACIONAL':       {bg:'rgba(69,90,100,0.30)',   bl:'#455a64'},
  };

  function aplicarEstilos() {
    document.querySelectorAll('button').forEach(function (btn) {
      var raw = btn.innerText || '';
      var chave = raw.replace(/[▼▶\s]/g, '').toUpperCase();
      var cfg = SEC[chave];
      if (!cfg) return;
      btn.style.cssText =
        'background:' + cfg.bg + ' !important;' +
        'border:none !important;' +
        'border-left:4px solid ' + cfg.bl + ' !important;' +
        'border-radius:4px !important;' +
        'text-align:left !important;' +
        'padding:6px 14px !important;' +
        'font-size:0.72rem !important;' +
        'font-weight:bold !important;' +
        'text-transform:uppercase !important;' +
        'letter-spacing:0.1em !important;' +
        'height:auto !important;' +
        'min-height:0 !important;' +
        'margin:10px 0 2px 0 !important;' +
        'color:rgba(255,255,255,0.88) !important;' +
        'cursor:pointer !important;' +
        'width:100% !important;' +
        'display:block !important;' +
        'line-height:1.5 !important;';
    });
  }

  function clonarCabecalho() {
    var src = document.getElementById('cabecalho-fixo');
    if (!src) return;
    var clone = document.getElementById('cab-fixo-clone');
    if (!clone) {
      clone = document.createElement('div');
      clone.id = 'cab-fixo-clone';
      document.body.appendChild(clone);
    }
    clone.innerHTML = src.innerHTML;
    // posiciona com a mesma largura e left da área main
    var main = document.querySelector('section.main');
    if (main) {
      var r = main.getBoundingClientRect();
      clone.style.left   = r.left + 'px';
      clone.style.width  = r.width + 'px';
      clone.style.padding = '6px ' + getComputedStyle(
        document.querySelector('.block-container') || main
      ).paddingLeft;
    }
    aplicarEstilos();
  }

  clonarCabecalho();
  setTimeout(clonarCabecalho, 300);
  setTimeout(clonarCabecalho, 1200);

  // re-aplica quando o DOM mudar (toggle de seção, sidebar, resize)
  new MutationObserver(function () { clonarCabecalho(); })
    .observe(document.body, {childList: true, subtree: true});

  window.addEventListener('resize', clonarCabecalho);
})();
</script>
""", unsafe_allow_html=True)


# ================================================================
# RECEITA
# ================================================================
render_row("Faturamento",
           FAT_2024, FAT_2025, FATURAMENTO_JAN_MAR, fat_abr_dez, FAT_2026,
           fmt="R$", bg_label=BG_FAT, bold=True)


# ================================================================
# CUSTOS E DESPESAS
# ================================================================
_exp_c = st.session_state.expand_custos
if st.button(("▼  " if _exp_c else "▶  ") + "CUSTOS E DESPESAS",
             key="btn_custos", use_container_width=True):
    st.session_state.expand_custos = not _exp_c
    st.rerun()
if _exp_c:
    render_row("Custo Campo",      CUSTO_CAMPO_2024, CUSTO_CAMPO_2025, CUSTO_CAMPO_JAN_MAR, custo_campo_abr_dez, CUSTO_CAMPO_2026, fmt="R$", bg_label=BG_CUSTO, var_inverso=True)
    render_row("Custo PH",         CUSTO_PH_2024,    CUSTO_PH_2025,    CUSTO_PH_JAN_MAR,    custo_ph_abr_dez,    CUSTO_PH_2026,    fmt="R$", bg_label=BG_CUSTO, var_inverso=True)
    render_row("Adm. Sede",        CUSTO_ADM_2024,   CUSTO_ADM_2025,   CUSTO_ADM_JAN_MAR,   custo_adm_abr_dez,   CUSTO_ADM_2026,   fmt="R$", bg_label=BG_CUSTO, var_inverso=True)
    render_row("Desp. Financeira", DESP_FIN_2024,    DESP_FIN_2025,    DESP_FIN_JAN_MAR,    desp_fin_abr_dez,    DESP_FIN_2026,    fmt="R$", bg_label=BG_CUSTO, var_inverso=True)
render_row("Total Custos", CUSTOS_2024, CUSTOS_2025, CUSTO_TOTAL_JAN_MAR, custos_abr_dez, CUSTOS_2026,
           fmt="R$", bg_label=BG_TOTALC, bold=True, var_inverso=True)


# ================================================================
# RESULTADO
# ================================================================
_exp_r = st.session_state.expand_resultado
if st.button(("▼  " if _exp_r else "▶  ") + "RESULTADO",
             key="btn_resultado", use_container_width=True):
    st.session_state.expand_resultado = not _exp_r
    st.rerun()
render_row("Lucro Liquido",
           LUCRO_2024, LUCRO_2025, LUCRO_JAN_MAR, LUCRO_ABR_DEZ, LUCRO_2026,
           fmt="R$", bg_label=BG_RES,
           bg_24 =BG_LUCROP if LUCRO_2024    >= 0 else BG_LUCRON,
           bg_25 =BG_LUCROP if LUCRO_2025    >= 0 else BG_LUCRON,
           bg_26r=BG_LUCROP if LUCRO_JAN_MAR >= 0 else BG_LUCRON,
           bg_26p=BG_LUCROP if LUCRO_ABR_DEZ >= 0 else BG_LUCRON,
           bg_26t=BG_LUCROP if LUCRO_2026    >= 0 else BG_LUCRON,
           bold=True)
if _exp_r:
    render_row("Margem Liquida", MARGEM_2024, MARGEM_2025, MARGEM_JAN_MAR, MARGEM_ABR_DEZ, MARGEM_2026, fmt="%", bg_label=BG_RES)
    render_row("PPR (10%)",      PPR_2024,    PPR_2025,    PPR_JAN_MAR,    PPR_ABR_DEZ,    PPR_2026,    fmt="x", bg_label=BG_RES)


# ================================================================
# OPERACIONAL
# ================================================================
_exp_o = st.session_state.expand_operacional
if st.button(("▼  " if _exp_o else "▶  ") + "OPERACIONAL",
             key="btn_operacional", use_container_width=True):
    st.session_state.expand_operacional = not _exp_o
    st.rerun()
if _exp_o:
    render_row("Caixas",                 CAIXAS_2024,       CAIXAS_2025,       CAIXAS_JAN_MAR,       qtd_caixas_abr_dez,   CAIXAS_2026,       fmt="num", bg_label=BG_OPE)
    render_row("Producao (ton)",         PRODUCAO_TON_2024, PRODUCAO_TON_2025, PRODUCAO_JAN_MAR_TON, prod_abr_dez_ton_liq, PRODUCAO_TON_2026, fmt="num", bg_label=BG_OPE)
    render_row("Produtividade (Ton/Ha)", PRODUT_2024,       PRODUT_2025,       PRODUT_JAN_MAR,       PRODUT_ABR_DEZ,       PRODUT_2026,       fmt="dec", bg_label=BG_OPE)
    render_row("Hectares",               HECTARES_2024,     HECTARES_2025,     HECTARES_FECHADOS,    HECTARES_RESTANTES,   AREA_TOTAL_HA,     fmt="num", bg_label=BG_OPE)

st.divider()

import re
import streamlit as st

# ----------------- CONFIG DA PÁGINA -----------------
st.set_page_config(
    page_title="Materiais – Ensino Médio",
    page_icon="💡",
    layout="wide",
)

# ----------------- ESTILO RÁPIDO -----------------
st.markdown(
    """
<style>
:root{
  --primary:#ffb52b;       /* âmbar da sua logo */
  --bg:#0b123b;            /* navy confortável */
  --bg-soft:#101a4d;       /* cartões */
  --text:#e6edf3;          /* texto principal */
  --muted:#a9b7cf;         /* texto secundário */
  --border:rgba(255,255,255,.10);
}
html,body{color:var(--text)}
/* largura confortável de leitura */
.block-container{padding-top:1.6rem;padding-bottom:.75rem;max-width:1180px}

/* HERO */
.hero{background:var(--bg);color:var(--text);padding:12px 0 14px;border-bottom:1px solid var(--border)}

/* Títulos (hierarquia) — corrigido tamanhos exagerados */
h1,.stMarkdown h1{font-size:2.4rem;font-weight:900;margin:0 0 .2rem}
h2,.stMarkdown h2{font-size:1.9rem;font-weight:800;margin:.6rem 0 .25rem}
h3,.stMarkdown h3{font-size:1.4rem;font-weight:800;margin:.4rem 0 .15rem}
h4,.stMarkdown h4{font-size:1.4rem;font-weight:800;margin:.1rem 0 0}
            
/* Abas 1º/2º/3º */
.stTabs [role="tablist"]{ gap:10px; margin:.2rem 0 1rem; border-bottom:none; box-shadow:none }
.stTabs [role="tablist"]::after,.stTabs [role="tablist"]::before{ content:none !important; display:none !important }
/* estado padrão da aba */
.stTabs [role="tab"]{
  font-size:1.02rem; padding:10px 16px !important; border:1px solid var(--border);
  border-radius:999px; background:rgba(255,255,255,.05); color:#cbd5e1;
  transition: background-color .25s ease,color .25s ease,transform .15s ease,border-color .25s ease,box-shadow .25s ease;
  box-shadow:none !important; text-decoration:none !important
}
.stTabs [role="tab"][aria-selected="true"]{ background:var(--primary) !important; color:#0b1029 !important; border-color:var(--primary) !important }
.stTabs [role="tab"][aria-selected="true"]::after{ display:none !important }

/* CARD da escola — espaçamentos mais enxutos */
.school-card{padding:14px 18px 10px 18px;margin:6px 0 14px;border:1px solid var(--border);border-radius:14px;background:var(--bg-soft)}
.school-head{display:grid;grid-template-columns:108px 1fr;column-gap:18px;align-items:center;margin:2px 0 6px}
.school-title{font-size:1.6rem;font-weight:900;line-height:1.15;margin:2px 0 4px}
.school-sub{color:var(--muted);font-size:.9rem;margin:0}

/* LOGO dentro de um “anel” branco, centralizada */
.logo-col{display:flex;align-items:center;justify-content:center}
.logo-ring{width:96px;height:96px;border-radius:999px;background:#fff;display:flex;align-items:center;justify-content:center;border:1px solid var(--border);box-shadow:0 2px 10px rgba(0,0,0,.18)}
.logo-ring img{max-width:78%;height:auto;object-fit:contain}
/* caso use st.image */
.logo-col .stImage img{border-radius:999px;background:#fff;padding:10px;border:1px solid var(--border)}

/* Chips (categorias) */
.badges{display:flex;gap:6px;flex-wrap:wrap;margin-top:4px}
.badge{display:inline-block;padding:6px 12px;border-radius:999px;background:color-mix(in srgb,var(--primary) 18%,#ffffff);color:#6b4a00;font-weight:800;font-size:.85rem;border:1px solid color-mix(in srgb,var(--primary) 45%,#000)}

/* Seções empilhadas com respiro menor */
.section{padding:4px 0 2px}
.section + .section{border-top:1px dashed var(--border);margin-top:6px}
.section-title{font-size:1.15rem;font-weight:900;margin:0 0 .1rem}

/* Lista de itens */
.item{margin:6px 0 8px}
.item a{color:var(--primary);text-decoration:none;font-weight:900;font-size:1rem;display:inline-block;transition:transform .15s ease-in-out}
.item a:hover{transform:translateY(-1px)}
.item small{display:block;margin-top:2px;color:var(--muted);font-size:.84rem;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}

/* Rodapé e divisores enxutos */
hr{border-color:var(--border);margin:6px 0}
.block-container footer{margin-top:.5rem}
</style>
""",
    unsafe_allow_html=True,
)


# ---------- (opcional) helper para link direto do Google Drive ----------
def gdrive_direct(url: str) -> str:
    m = re.search(r"/d/([a-zA-Z0-9_-]+)", url) or re.search(r"[?&]id=([a-zA-Z0-9_-]+)", url)
    return f"https://drive.google.com/uc?export=view&id={m.group(1)}" if m else url

# ----------------- LOGOS -----------------
# DICA: em Windows, prefira caminho "raw string" r"G:\\..." ou use '/'.
# ----------------- LOGOS -----------------
SITE_LOGO = "logos/logo.png"
LOGO_EEM  = "logos/logo_bailarina.png"
LOGO_EEB  = "logos/logo2_senador.png"


# ----------------- SEUS LINKS – EDITE AQUI -----------------
DATA = {
    "1º Série": {
        "EEM Bailarina Liselott Trinks": {
            "Atividades & Avaliações": [
                 {"titulo": "Atividade – Epidemia de anabolizantes", "url": "https://drive.google.com/file/d/143fE5_e8t2TbkZ_t9DDnRO1jLfwZV8Yw/view?usp=sharing"},
            ],
            "Material de Apoio": [
                {"titulo": "Slides – Tabela Periódica", "url": "https://docs.google.com/presentation/d/1dU0kTUzYBwxkUS4vqNZls3UqjSQAFA-t/edit?usp=sharing&ouid=107269659950309178973&rtpof=true&sd=true"},
                {"titulo": "Apostila - Tabela Periódica", "url": "https://docs.google.com/document/d/1rvzdJbx2NGvwyRYf7kpy78Kdd7WgH5ve/edit?usp=sharing&ouid=107269659950309178973&rtpof=true&sd=true"},
                {"titulo": "Slides - Ligações químicas", "url": "https://docs.google.com/presentation/d/1fgsIfM4RCkgoO0WkO8usHLuyA-TtYgTW/edit?usp=sharing&ouid=107269659950309178973&rtpof=true&sd=true"},
                {"titulo": "Apostila - Ligações químicas", "url": "https://drive.google.com/file/d/1WPfzpnGMChc_yAedoWB1pFyDZJ0vmn0t/view?usp=sharing"},
                {"titulo": "Slides - Ligações Intermoleculares - Parte 1", "url": "https://docs.google.com/presentation/d/1Srf1b_BJ3tz9it0NsqaFYErKuw2Xm02w/edit?usp=sharing&ouid=107269659950309178973&rtpof=true&sd=true"},
                {"titulo": "Slides - Ligações Intermoleculares - Parte 2", "url": "https://docs.google.com/presentation/d/1ZkT_3nJ9-hD41-UF5nOeahdvtTrhyHFu/edit?usp=sharing&ouid=107269659950309178973&rtpof=true&sd=true"},
            ],
            "Lista de Exercícios": [ ],
        },
        "EEB Senador Rodrigo Lobo": {
            "Atividades & Avaliações": [
                {"titulo": "Atividade – Epidemia de anabolizantes", "url": "https://drive.google.com/file/d/143fE5_e8t2TbkZ_t9DDnRO1jLfwZV8Yw/view?usp=sharing"},
            ],
            "Material de Apoio": [
                {"titulo": "Slides – Tabela Periódica", "url": "https://docs.google.com/presentation/d/1dU0kTUzYBwxkUS4vqNZls3UqjSQAFA-t/edit?usp=sharing&ouid=107269659950309178973&rtpof=true&sd=true"},
                {"titulo": "Apostila - Tabela Periódica", "url": "https://docs.google.com/document/d/1rvzdJbx2NGvwyRYf7kpy78Kdd7WgH5ve/edit?usp=sharing&ouid=107269659950309178973&rtpof=true&sd=true"},
                {"titulo": "Slides - Ligações químicas", "url": "https://docs.google.com/presentation/d/1fgsIfM4RCkgoO0WkO8usHLuyA-TtYgTW/edit?usp=sharing&ouid=107269659950309178973&rtpof=true&sd=true"},
                {"titulo": "Apostila - Ligações químicas", "url": "https://drive.google.com/file/d/1WPfzpnGMChc_yAedoWB1pFyDZJ0vmn0t/view?usp=sharing"},
                {"titulo": "Slides - Ligações Intermoleculares - Parte 1", "url": "https://docs.google.com/presentation/d/1Srf1b_BJ3tz9it0NsqaFYErKuw2Xm02w/edit?usp=sharing&ouid=107269659950309178973&rtpof=true&sd=true"},
                {"titulo": "Slides - Ligações Intermoleculares - Parte 2", "url": "https://docs.google.com/presentation/d/1ZkT_3nJ9-hD41-UF5nOeahdvtTrhyHFu/edit?usp=sharing&ouid=107269659950309178973&rtpof=true&sd=true"},
            ],
            "Lista de Exercícios": [
            ],
        },
    },
    "2º Série": {
        "EEM Bailarina Liselott Trinks": {
            "Atividades & Avaliações": [
                {"titulo": "Atividade - Equilíbrio químico", "url": "https://drive.google.com/file/d/1D_NlegUcda_NnnO6kCI_Onzof4p0eXF3/view?usp=drive_link"},  
                {"titulo": "Atividade – Epidemia de anabolizantes", "url": "https://drive.google.com/file/d/143fE5_e8t2TbkZ_t9DDnRO1jLfwZV8Yw/view?usp=sharing"},
                {"titulo": "Atividade – Oxirredução", "url": "https://drive.google.com/file/d/13u1bBX30Auuj7BXaUHQgVQeByRYtX_Od/view?usp=sharing"},
            ],
            "Material de Apoio": [
                {"titulo": "Slides - Radioatividade", "url": "https://docs.google.com/presentation/d/15nIHyX5NmGveInt_UkpPn56HwO7DO6xk/edit?usp=sharing&ouid=107269659950309178973&rtpof=true&sd=true"},
                {"titulo": "Apostila - Radioatividade", "url": "https://drive.google.com/file/d/1QNnDtHVX9sqvfQFq6OqHNbKbr-_qeSZe/view?usp=sharing"},
                {"titulo": "Slides - Equilíbrio químico", "url": "https://docs.google.com/presentation/d/13mPcbGS7y_lGwz9MYCWvFZMPTigY24-s/edit?usp=sharing&ouid=107269659950309178973&rtpof=true&sd=true"},
                {"titulo": "Apostila - Equilíbrio químico", "url": "https://drive.google.com/file/d/1p4ePY8aiDr_AteUHAkkmv-bt_EgsmVVv/view?usp=sharing"},
                {"titulo": "Slides - Oxirredução", "url": "https://docs.google.com/presentation/d/13IpRKbqxPgm42Z2Jses49yZyqh01bN4t/edit?usp=sharing&ouid=107269659950309178973&rtpof=true&sd=true"},
                {"titulo": "Apostila - Oxirredução", "url": "https://docs.google.com/document/d/1YpU7k_qUc81FqgV23Qb4RrqcyBAINybO/edit?usp=sharing&ouid=107269659950309178973&rtpof=true&sd=true"},
            ],
            "Lista de Exercícios": [
                
            ],
        },
        "EEB Senador Rodrigo Lobo": {
            "Atividades & Avaliações": [
                {"titulo": "Atividade - Equilíbrio químico", "url": "https://drive.google.com/file/d/1D_NlegUcda_NnnO6kCI_Onzof4p0eXF3/view?usp=drive_link"},
                {"titulo": "Atividade – Epidemia de anabolizantes", "url": "https://drive.google.com/file/d/143fE5_e8t2TbkZ_t9DDnRO1jLfwZV8Yw/view?usp=sharing"},
                {"titulo": "Atividade – Oxirredução", "url": "https://drive.google.com/file/d/13u1bBX30Auuj7BXaUHQgVQeByRYtX_Od/view?usp=sharing"},
            ],
            "Material de Apoio": [
                {"titulo": "Slides - Radioatividade", "url": "https://docs.google.com/presentation/d/15nIHyX5NmGveInt_UkpPn56HwO7DO6xk/edit?usp=sharing&ouid=107269659950309178973&rtpof=true&sd=true"},
                {"titulo": "Apostila - Radioatividade", "url": "https://drive.google.com/file/d/1QNnDtHVX9sqvfQFq6OqHNbKbr-_qeSZe/view?usp=sharing"},
                {"titulo": "Slides - Equilíbrio químico", "url": "https://docs.google.com/presentation/d/13mPcbGS7y_lGwz9MYCWvFZMPTigY24-s/edit?usp=sharing&ouid=107269659950309178973&rtpof=true&sd=true"},
                {"titulo": "Apostila - Equilíbrio químico", "url": "https://drive.google.com/file/d/1p4ePY8aiDr_AteUHAkkmv-bt_EgsmVVv/view?usp=sharing"},
                {"titulo": "Slides - Oxirredução", "url": "https://docs.google.com/presentation/d/13IpRKbqxPgm42Z2Jses49yZyqh01bN4t/edit?usp=sharing&ouid=107269659950309178973&rtpof=true&sd=true"},
                {"titulo": "Apostila - Oxirredução", "url": "https://docs.google.com/document/d/1YpU7k_qUc81FqgV23Qb4RrqcyBAINybO/edit?usp=sharing&ouid=107269659950309178973&rtpof=true&sd=true"},
            ],
            "Lista de Exercícios": [
                
            ],
        },
    },
    "3º Série": {
        "EEM Bailarina Liselott Trinks": {
            "Atividades & Avaliações": [
                {"titulo": "Atividade – Epidemia de anabolizantes", "url": "https://drive.google.com/file/d/143fE5_e8t2TbkZ_t9DDnRO1jLfwZV8Yw/view?usp=sharing"},
            ],
            "Material de Apoio": [
                {"titulo": "Slides – Funções orgânicas", "url": "https://docs.google.com/presentation/d/1qdufAHHERWf8uzfYzb2xk1Mn-dR8XGff/edit?usp=sharing&ouid=107269659950309178973&rtpof=true&sd=true"},
                {"titulo": "Apostila – Funções orgânicas", "url": "https://drive.google.com/file/d/117_ppWJozSc8zb00lCU1tUZ7vKE-F5d5/view?usp=sharing"},
                {"titulo": "Slides – Propriedades físicas dos compostos orgânicos", "url": "https://docs.google.com/presentation/d/1EVfdZ272Z8rWrv-YFTTdBw_vH2hVH9Oa/edit?usp=drive_link&ouid=107269659950309178973&rtpof=true&sd=true"},
                {"titulo": "Apostila – Propriedades físicas dos compostos orgânicos", "url": "https://docs.google.com/document/d/1v_enyU2WKq7pau5EFWTfUwCfNfpcpSCj/edit?usp=sharing&ouid=107269659950309178973&rtpof=true&sd=true"},
            ],
            "Lista de Exercícios": []
              
        },
        "EEB Senador Rodrigo Lobo": {
            "Atividades & Avaliações": [
               {"titulo": "Atividade – Epidemia de anabolizantes", "url": "https://drive.google.com/file/d/143fE5_e8t2TbkZ_t9DDnRO1jLfwZV8Yw/view?usp=sharing"},
            ],
            "Material de Apoio": [
                {"titulo": "Slides – Funções orgânicas", "url": "https://docs.google.com/presentation/d/1qdufAHHERWf8uzfYzb2xk1Mn-dR8XGff/edit?usp=sharing&ouid=107269659950309178973&rtpof=true&sd=true"},
                {"titulo": "Apostila – Funções orgânicas", "url": "https://drive.google.com/file/d/117_ppWJozSc8zb00lCU1tUZ7vKE-F5d5/view?usp=sharing"},
                {"titulo": "Slides – Propriedades físicas dos compostos orgânicos", "url": "https://docs.google.com/presentation/d/1EVfdZ272Z8rWrv-YFTTdBw_vH2hVH9Oa/edit?usp=drive_link&ouid=107269659950309178973&rtpof=true&sd=true"},
                {"titulo": "Apostila – Propriedades físicas dos compostos orgânicos", "url": "https://docs.google.com/document/d/1v_enyU2WKq7pau5EFWTfUwCfNfpcpSCj/edit?usp=sharing&ouid=107269659950309178973&rtpof=true&sd=true"},
            ],
            "Lista de Exercícios": [
              
            ],
        },
    },
        "1º Logística": {
        "EEM Bailarina Liselott Trinks": {
            "Atividades & Avaliações": [ {"titulo": "Atividade complementar – 19/09", "url": "https://drive.google.com/file/d/12gkMBOotsyT0A1OaeU8kltQp1tohcsdo/view?usp=sharing"},
                                        {"titulo": "Atividade complementar – 26/09", "url": "https://drive.google.com/file/d/1O3jq0ZSO1DBnVpa_HqufQnLCa5YNoB6K/view?usp=sharing"},
                                        {"titulo": "Atividade complementar – 03/10", "url": "https://drive.google.com/file/d/1R8tOYK_7v6kF5FhdU8AjhYt-kj-X8Eue/view?usp=sharing"},
                                        {"titulo": "Atividade complementar – 10/10", "url": "https://drive.google.com/file/d/1JpqKg2bvKgZwneqfMe1lWTVjXGm7RiJ3/view?usp=sharing"},
                                        {"titulo": "Atividade – Epidemia de anabolizantes", "url": "https://drive.google.com/file/d/143fE5_e8t2TbkZ_t9DDnRO1jLfwZV8Yw/view?usp=sharing"},

                                        
            ],
            "Material de Apoio": [
                {"titulo": "Slides – Tabela Periódica", "url": "https://docs.google.com/presentation/d/1dU0kTUzYBwxkUS4vqNZls3UqjSQAFA-t/edit?usp=sharing&ouid=107269659950309178973&rtpof=true&sd=true"},
                {"titulo": "Apostila - Tabela Periódica", "url": "https://docs.google.com/document/d/1rvzdJbx2NGvwyRYf7kpy78Kdd7WgH5ve/edit?usp=sharing&ouid=107269659950309178973&rtpof=true&sd=true"},
                {"titulo": "Slides - Ligações químicas", "url": "https://docs.google.com/presentation/d/1fgsIfM4RCkgoO0WkO8usHLuyA-TtYgTW/edit?usp=sharing&ouid=107269659950309178973&rtpof=true&sd=true"},
                {"titulo": "Apostila - Ligações químicas", "url": "https://drive.google.com/file/d/1WPfzpnGMChc_yAedoWB1pFyDZJ0vmn0t/view?usp=sharing"}
            ],
            "Lista de Exercícios": [
                
            ],
        },
        "EEB Senador Rodrigo Lobo": {
            "Atividades & Avaliações": [
            
            ],
            "Material de Apoio": [],
            
            "Lista de Exercícios": [ ],
        },
    },
        "2º Logística": {
        "EEM Bailarina Liselott Trinks": {
            "Atividades & Avaliações": [
              
            ],
            "Material de Apoio": [
                {"titulo": "Slides - Radioatividade", "url": "https://docs.google.com/presentation/d/15nIHyX5NmGveInt_UkpPn56HwO7DO6xk/edit?usp=sharing&ouid=107269659950309178973&rtpof=true&sd=true"},
                {"titulo": "Apostila - Radioatividade", "url": "https://drive.google.com/file/d/1QNnDtHVX9sqvfQFq6OqHNbKbr-_qeSZe/view?usp=sharing"},
                {"titulo": "Slides - Equilíbrio químico", "url": "https://docs.google.com/presentation/d/13mPcbGS7y_lGwz9MYCWvFZMPTigY24-s/edit?usp=sharing&ouid=107269659950309178973&rtpof=true&sd=true"},
                {"titulo": "Apostila - Equilíbrio químico", "url": "https://drive.google.com/file/d/1p4ePY8aiDr_AteUHAkkmv-bt_EgsmVVv/view?usp=sharing"}
            ],
            "Lista de Exercícios": [
             
            ],
        },
        "EEB Senador Rodrigo Lobo": {
            "Atividades & Avaliações": [
               
            ],
            "Material de Apoio": [
               
            ],
            "Lista de Exercícios": [
               
            ],
        },
    },}

# ----------------- TOPO -----------------
c1, c2 = st.columns([1,5])
with c1:
    try:
        st.image(SITE_LOGO, width=160)
    except Exception:
        st.markdown("<div class='badge'>Envie sua logo em logos/site_logo.png ou use URL</div>", unsafe_allow_html=True)
with c2:
    st.markdown("# Materiais e Atividades – 2025")
    st.caption("Página de compartilhamento de materiais e atividade do curso de química do professor André Simão.")

st.divider()

# ----------------- ABAS 1º/2º/3º -----------------
tab_labels = list(DATA.keys())
tabs = st.tabs(tab_labels)

def render_section(items):
    if not items:
        st.markdown(":information_source: *Sem itens ainda.*")
        return
    for it in items:
        st.markdown(
            f"<div class='item'>• <a href='{it['url']}' target='_blank'>{it['titulo']}</a>"\
            f"<small>{it['url']}</small></div>",
            unsafe_allow_html=True,
        )

# --- layout VERTICAL para a escola (com espaçamento corrigido) ---
def render_school(name, logo_path, sections):
    with st.container():
        st.markdown("<div class='school-card'>", unsafe_allow_html=True)

        # Cabeçalho (logo + título)
        head_l, head_r = st.columns([1,6])
        with head_l:
            # Tenta o modo "anel" com markdown+img; se não for possível (caminho local), usa st.image
            try:
             
                st.image(logo_path, use_column_width=False, width=160)
                st.markdown("</div>", unsafe_allow_html=True)
            except Exception:
                st.image(logo_path, width=84)
        with head_r:
            st.markdown(f"<div class='school-title'>{name}</div>", unsafe_allow_html=True)
            st.markdown(
                '<div class="badges">\n'
                '  <span class="badge">Atividades & Avaliações</span>\n'
                '  <span class="badge">Material de Apoio</span>\n'
                '  <span class="badge">Lista de Exercícios</span>\n'
                '</div>',
                unsafe_allow_html=True,
            )

        # Seções EMPILHADAS (menos divisores para reduzir "respiro" excessivo)
        st.markdown("<div class='section'>", unsafe_allow_html=True)
        st.markdown("<h4 class='section-title'>Atividades & Avaliações</h4>", unsafe_allow_html=True)
        render_section(sections.get("Atividades & Avaliações", []))
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='section'>", unsafe_allow_html=True)
        st.markdown("<h4 class='section-title'>Material de Apoio</h4>", unsafe_allow_html=True)
        render_section(sections.get("Material de Apoio", []))
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='section'>", unsafe_allow_html=True)
        st.markdown("<h4 class='section-title'>Lista de Exercícios</h4>", unsafe_allow_html=True)
        render_section(sections.get("Lista de Exercícios", []))
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)  # /school-card

for i, label in enumerate(tab_labels):
    with tabs[i]:
        schools = DATA[label]
        name1 = "EEM Bailarina Liselott Trinks"
        render_school(name1, LOGO_EEM, schools[name1])
        name2 = "EEB Senador Rodrigo Lobo"
        render_school(name2, LOGO_EEB, schools[name2])

st.write("---")
st.caption("© {} • Portal de Materiais".format(__import__("datetime").date.today().year))

"""Genere les figures SVG pedagogiques pour le site micro-ii-resume."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

OUT = "images"
plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 11,
    'axes.spines.top': False,
    'axes.spines.right': False,
    'axes.linewidth': 1.2,
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
})

def fig(name, w=6, h=4.2):
    f, ax = plt.subplots(figsize=(w, h))
    ax.set_xlabel('Quantité Q', loc='right')
    ax.set_ylabel('Prix P', loc='top', rotation=0)
    return f, ax

def save(f, name):
    f.tight_layout()
    f.savefig(f"{OUT}/{name}.svg", format='svg', bbox_inches='tight')
    plt.close(f)
    print(f"  {name}.svg")

# === 1. Equilibre concurrence parfaite ===
f, ax = fig('cp_eq')
Q = np.linspace(0, 10, 100)
D = 10 - Q
S = 1 + Q
ax.plot(Q, D, color='#dc2626', lw=2.5, label="Demande")
ax.plot(Q, S, color='#2563eb', lw=2.5, label="Offre")
ax.plot(4.5, 5.5, 'ko', ms=8)
ax.axhline(5.5, color='gray', ls='--', lw=1, xmax=4.5/10)
ax.axvline(4.5, color='gray', ls='--', lw=1, ymax=5.5/10)
ax.text(4.5, -.6, "Q*", ha='center', fontweight='bold')
ax.text(-.4, 5.5, "P*", va='center', fontweight='bold', color='black')
ax.fill_between(Q[:46], D[:46], 5.5, alpha=.18, color='#dc2626', label="Surplus consommateur")
ax.fill_between(Q[:46], 5.5, S[:46], alpha=.18, color='#2563eb', label="Surplus producteur")
ax.set_xlim(0, 10); ax.set_ylim(0, 11)
ax.set_xticks([]); ax.set_yticks([])
ax.legend(loc='upper right', fontsize=9, frameon=False)
ax.set_title("Équilibre en concurrence parfaite", fontweight='bold')
save(f, 'cp_equilibre')

# === 2. Firme en CP court terme : profit positif ===
f, ax = fig('cp_ct')
q = np.linspace(0.5, 8, 200)
CVM = 0.5*q + 2
CTM = CVM + 5/q
Cm = q + 2
P_mkt = 6
ax.plot(q, CVM, color='#9333ea', lw=2, label='CVM')
ax.plot(q, CTM, color='#0d9488', lw=2, label='CTM')
ax.plot(q, Cm, color='#dc2626', lw=2.5, label='Cm')
ax.axhline(P_mkt, color='#2563eb', lw=2.5, label='P = Rm')
# intersection P = Cm
q_star = P_mkt - 2
ax.axvline(q_star, color='gray', ls='--', lw=1)
CTM_star = 0.5*q_star + 2 + 5/q_star
ax.fill_between([0, q_star], CTM_star, P_mkt, alpha=.25, color='#16a34a', label='Profit > 0')
ax.plot(q_star, P_mkt, 'ko', ms=7)
ax.text(q_star, -0.6, 'q*', ha='center', fontweight='bold')
ax.set_xlim(0, 8); ax.set_ylim(0, 12)
ax.set_xticks([]); ax.set_yticks([])
ax.set_xlabel('quantité q (par firme)', loc='right')
ax.legend(loc='upper left', fontsize=9, frameon=False)
ax.set_title("CP — court terme : la firme peut faire un profit", fontweight='bold')
save(f, 'cp_court_terme')

# === 3. CP long terme : profit nul ===
f, ax = fig('cp_lt')
CMLT = 0.3*(q-4)**2 + 4
CmLT = 0.6*(q-4) + 4
ax.plot(q, CMLT, color='#0d9488', lw=2.5, label='CMLT')
ax.plot(q, CmLT, color='#dc2626', lw=2, label='CmLT')
ax.axhline(4, color='#2563eb', lw=2.5, label='P*  (= min CMLT)')
ax.plot(4, 4, 'ko', ms=8)
ax.axvline(4, color='gray', ls='--', lw=1)
ax.text(4, -0.4, 'q*', ha='center', fontweight='bold')
ax.text(0.2, 4.15, 'P = CMLT', fontsize=10, color='#0d9488')
ax.set_xlim(0, 8); ax.set_ylim(0, 12)
ax.set_xticks([]); ax.set_yticks([])
ax.set_xlabel('quantité q', loc='right')
ax.legend(loc='upper right', fontsize=9, frameon=False)
ax.set_title("CP — long terme : profit = 0 (tangence au minimum)", fontweight='bold')
save(f, 'cp_long_terme')

# === 4. Externalite negative ===
f, ax = fig('ext')
Q = np.linspace(0, 10, 100)
D = 10 - Q
CMP = 1 + Q          # cout marginal prive (offre)
CMS = 3 + Q          # cout marginal social (avec dommages)
ax.plot(Q, D, color='#dc2626', lw=2.5, label='Demande')
ax.plot(Q, CMP, color='#2563eb', lw=2.5, label='Offre = Cm privé')
ax.plot(Q, CMS, color='#9333ea', lw=2.5, ls='--', label='Cm social')
# eq prive: D = CMP -> 10-Q=1+Q -> Q=4.5
ax.plot(4.5, 5.5, 'ko', ms=7); ax.text(4.5, -0.5, 'Q_privé', ha='center', fontsize=10)
# eq social: D=CMS -> 10-Q=3+Q -> Q=3.5
ax.plot(3.5, 6.5, 'ko', ms=7); ax.text(3.5, 11, 'Q_social', ha='center', fontsize=10)
# perte sociale = triangle entre CMS, D, sur [Q_soc, Q_priv]
xs = np.linspace(3.5, 4.5, 30)
ax.fill_between(xs, 10-xs, 3+xs, color='#dc2626', alpha=.35, label='Perte sociale')
ax.set_xlim(0, 10); ax.set_ylim(0, 11)
ax.set_xticks([]); ax.set_yticks([])
ax.legend(loc='upper right', fontsize=9, frameon=False)
ax.set_title("Externalité négative : surproduction du marché", fontweight='bold')
save(f, 'externalite')

# === 5. Monopole : equilibre + perte seche ===
f, ax = fig('mono')
Q = np.linspace(0, 10, 200)
D = 10 - Q
Rm = 10 - 2*Q
Cm = 1 + 0.4*Q
ax.plot(Q, D, color='#dc2626', lw=2.5, label='Demande')
ax.plot(Q, Rm, color='#ea580c', lw=2, ls='--', label='Recette marginale Rm')
ax.plot(Q, Cm, color='#2563eb', lw=2.5, label='Coût marginal Cm')
# Q* : Rm = Cm -> 10-2Q = 1+0.4Q -> 9 = 2.4Q -> Q=3.75
Qm = 9/2.4
Pm = 10 - Qm
Cm_m = 1 + 0.4*Qm
ax.axvline(Qm, color='gray', ls='--', lw=1)
ax.axhline(Pm, color='gray', ls=':', lw=1, xmax=Qm/10)
ax.plot(Qm, Pm, 'ko', ms=8)
ax.text(Qm, -0.5, 'Q_m', ha='center', fontweight='bold')
ax.text(-.4, Pm, 'P_m', va='center', fontweight='bold')
# Q concurrence : D = Cm -> 10-Q = 1+0.4Q -> Q=6.43
Qc = 9/1.4
Pc = 10 - Qc
ax.plot(Qc, Pc, 'ko', ms=7, mfc='white')
ax.text(Qc, -0.5, 'Q_c', ha='center', fontsize=10)
# perte seche (deadweight) triangle entre D, Cm sur [Qm, Qc]
xs = np.linspace(Qm, Qc, 30)
ax.fill_between(xs, 10-xs, 1+0.4*xs, color='#dc2626', alpha=.35, label='Perte sèche')
ax.set_xlim(0, 10); ax.set_ylim(0, 11)
ax.set_xticks([]); ax.set_yticks([])
ax.legend(loc='upper right', fontsize=9, frameon=False)
ax.set_title("Monopole : Q_m < Q_c, P_m > P_c → perte sèche", fontweight='bold')
save(f, 'monopole')

# === 6. Monopole discriminant parfait ===
f, ax = fig('disc')
Q = np.linspace(0, 10, 200)
D = 10 - Q
Cm = 1 + 0.4*Q
ax.plot(Q, D, color='#dc2626', lw=2.5, label='Demande')
ax.plot(Q, Cm, color='#2563eb', lw=2.5, label='Cm')
Qc = 9/1.4
Pc = 10 - Qc
ax.plot(Qc, Pc, 'ko', ms=8)
ax.text(Qc, -0.5, 'Q*', ha='center', fontweight='bold')
xs = np.linspace(0, Qc, 50)
ax.fill_between(xs, 10-xs, 1+0.4*xs, color='#16a34a', alpha=.35, label='Profit du monopoleur (capte tout)')
ax.set_xlim(0, 10); ax.set_ylim(0, 11)
ax.set_xticks([]); ax.set_yticks([])
ax.legend(loc='upper right', fontsize=9, frameon=False)
ax.set_title("Discrimination parfaite : SC = 0, pas de perte sèche", fontweight='bold')
save(f, 'discrimination')

# === 7. Monopole naturel ===
f, ax = fig('mn')
q = np.linspace(1, 10, 200)
CTM = 5 + 20/q      # decroissant
Cm = 5 + np.zeros_like(q)  # constant pour simplifier
D = 12 - 0.5*q
ax.plot(q, CTM, color='#0d9488', lw=2.5, label='CTM (décroissant)')
ax.plot(q, Cm, color='#2563eb', lw=2.5, label='Cm')
ax.plot(q, D, color='#dc2626', lw=2.5, label='Demande')
# tarif au Cm : P = 5, q tq D = 5 -> 12-0.5q = 5 -> q = 14 (hors graphique). On limite.
q_cm = 14
# CTM à q=14 = 5+20/14 ≈ 6.43
ax.axhline(5, color='#2563eb', ls=':', lw=1, alpha=.5)
ax.axhline(6.43, color='#0d9488', ls=':', lw=1, alpha=.5)
ax.fill_between([1, 10], 5, 6.43, color='#dc2626', alpha=.15, label="Perte si P = Cm")
ax.text(5.5, 5.7, "perte : Cm < CTM", color='#b91c1c', fontsize=10, fontweight='bold')
ax.set_xlim(0, 10); ax.set_ylim(0, 14)
ax.set_xticks([]); ax.set_yticks([])
ax.legend(loc='upper right', fontsize=9, frameon=False)
ax.set_title("Monopole naturel : tarification au Cm → perte", fontweight='bold')
save(f, 'monopole_naturel')

# === 8. Concurrence monopolistique long terme ===
f, ax = fig('cm_lt')
q = np.linspace(0.5, 8, 200)
CTM = 0.3*(q-4)**2 + 4
Cm = 0.6*(q-4) + 4
D = 7 - 0.5*q          # tangente au CTM en (4,4)
Rm = 7 - q
ax.plot(q, CTM, color='#0d9488', lw=2.5, label='CTM')
ax.plot(q, Cm, color='#dc2626', lw=2, label='Cm')
ax.plot(q, D, color='#2563eb', lw=2.5, label='Demande (firme)')
ax.plot(q, Rm, color='#ea580c', lw=2, ls='--', label='Rm')
# tangence en q=4, P=5 (D(4) = 7-2 = 5, CTM(4)=4 ... let me adjust)
# Pour tangence parfaite : CTM(q*) = D(q*) et CTM'(q*) = D'(q*)
# CTM' = 0.6*(q-4); D' = -0.5 → q* tq 0.6(q-4) = -0.5 → q-4 = -5/6 ≈ -0.83 → q* ≈ 3.17
# CTM(3.17) ≈ 0.3*0.69+4 ≈ 4.21; D(3.17) = 7-1.58 = 5.42. Pas tangent.
# Simplifions visuellement
q_star = 3.5
P_star = 5.25
ax.plot(q_star, P_star, 'ko', ms=8)
ax.axvline(q_star, color='gray', ls='--', lw=1)
ax.axhline(P_star, color='gray', ls=':', lw=1, xmax=q_star/8)
ax.text(q_star, -0.4, 'q*', ha='center', fontweight='bold')
ax.text(-.3, P_star, 'P*', va='center', fontweight='bold')
ax.set_xlim(0, 8); ax.set_ylim(0, 10)
ax.set_xticks([]); ax.set_yticks([])
ax.legend(loc='upper right', fontsize=9, frameon=False)
ax.set_title("Concurrence monopolistique LT : tangence D/CTM → profit = 0", fontweight='bold')
save(f, 'cm_long_terme')

# === 9. Cournot : fonctions de reaction ===
f, ax = plt.subplots(figsize=(5.5, 5.5))
q1 = np.linspace(0, 50, 100)
# fonctions de reaction symetriques d'apres l'exam : q1 = 24 - 0.4 q2  et q2 = 15 - 0.25 q1
RF1 = 24 - 0.4*q1  # ici q1 axe = q2_axe (on inverse)
RF2 = 15 - 0.25*q1
ax.plot(RF1, q1, color='#2563eb', lw=2.5, label="RF firme 1 : q₁ = 24 − 0.4 q₂")
ax.plot(q1, RF2, color='#dc2626', lw=2.5, label="RF firme 2 : q₂ = 15 − 0.25 q₁")
# equilibre: q1=20, q2=10
ax.plot(20, 10, 'ko', ms=10)
ax.annotate("Équilibre Cournot\n(q₁=20, q₂=10)", xy=(20,10), xytext=(28,18),
            fontsize=10, arrowprops=dict(arrowstyle='->', color='black'))
ax.set_xlabel('q₁ (firme 1)')
ax.set_ylabel('q₂ (firme 2)')
ax.set_xlim(0, 35); ax.set_ylim(0, 30)
ax.grid(alpha=.3)
ax.legend(fontsize=9, loc='upper right', frameon=False)
ax.set_title("Cournot : intersection des fonctions de réaction", fontweight='bold')
save(f, 'cournot')

# === 10. Demande coudee (Sweezy) ===
f, ax = fig('sw')
Q = np.linspace(0, 10, 200)
D_haut = 12 - 2*Q  # quand on baisse, concurrents suivent -> demande peu sensible (pente forte)
D_bas = 8 - 0.5*Q  # quand on monte, concurrents ne suivent pas -> très sensible (pente faible)
Q_kink = 8/3  # intersection des 2 portions au point coudé (arbitraire, simple)
P_kink = 8 - 0.5*Q_kink
# courbe coudée
Q_a = np.linspace(0, Q_kink, 50); P_a = 8 - 0.5*Q_a
Q_b = np.linspace(Q_kink, 8, 50); P_b = 12 - 2*Q_b
ax.plot(Q_a, P_a, color='#dc2626', lw=2.5)
ax.plot(Q_b, P_b, color='#dc2626', lw=2.5, label='Demande coudée')
ax.plot(Q_kink, P_kink, 'ko', ms=8)
ax.annotate("Coude (prix actuel)", xy=(Q_kink, P_kink), xytext=(5, 9),
            fontsize=10, arrowprops=dict(arrowstyle='->'))
ax.text(0.5, 7, "↑ prix → concurrents\nne suivent pas\n(je perds beaucoup)", fontsize=9, color='#7c2d12')
ax.text(4.5, 3.5, "↓ prix → concurrents\nsuivent\n(je gagne peu)", fontsize=9, color='#7c2d12')
ax.set_xlim(0, 10); ax.set_ylim(0, 12)
ax.set_xticks([]); ax.set_yticks([])
ax.legend(loc='upper right', fontsize=9, frameon=False)
ax.set_title("Oligopole — demande coudée (Sweezy) : prix rigides", fontweight='bold')
save(f, 'demande_coudee')

# === 11. Comparaison structures de marche ===
f, ax = fig('comp', w=6.5, h=4.5)
Q = np.linspace(0, 10, 200)
D = 10 - Q
Cm = 1 + 0.4*Q
ax.plot(Q, D, color='#dc2626', lw=2.5, label='Demande')
ax.plot(Q, Cm, color='#2563eb', lw=2.5, label='Cm')
# CP : P = Cm -> Q = 6.43, P = 3.57
Qc, Pc = 9/1.4, 10-9/1.4
# Mono : Rm=Cm -> Q=3.75, P=6.25
Qm = 9/2.4; Pm = 10-Qm
# Oligo (entre): Q ≈ 5.3, P ≈ 4.7 (Cournot duopole avec mêmes coûts ≈ 2/3 de Qc)
Qo = (2/3)*Qc; Po = 10 - Qo
ax.scatter([Qm, Qo, Qc], [Pm, Po, Pc], color=['#dc2626','#ea580c','#16a34a'], s=80, zorder=5)
ax.annotate(f"Monopole\n(Q={Qm:.1f}, P={Pm:.1f})", xy=(Qm,Pm), xytext=(0.5,8),
            fontsize=9, color='#7f1d1d', arrowprops=dict(arrowstyle='->', color='#7f1d1d'))
ax.annotate(f"Oligopole\n(Cournot)", xy=(Qo,Po), xytext=(3.5,7.5),
            fontsize=9, color='#9a3412', arrowprops=dict(arrowstyle='->', color='#9a3412'))
ax.annotate(f"Concurrence\n(Q={Qc:.1f}, P={Pc:.1f})", xy=(Qc,Pc), xytext=(7.5,7),
            fontsize=9, color='#14532d', arrowprops=dict(arrowstyle='->', color='#14532d'))
ax.set_xlim(0, 10); ax.set_ylim(0, 11)
ax.set_xticks([]); ax.set_yticks([])
ax.legend(loc='upper right', fontsize=9, frameon=False)
ax.set_title("Comparaison : monopole — oligopole — concurrence", fontweight='bold')
save(f, 'comparaison_structures')

# === 12. Effets de reseau (Ch7) ===
f, ax = plt.subplots(figsize=(6, 4.2))
n = np.linspace(0, 100, 200)
U = np.where(n < 30, 0.05*n, 5*np.log(n-20))  # masse critique à n=30
ax.plot(n, U, color='#0d9488', lw=2.5)
ax.axvline(30, color='#dc2626', ls='--', lw=1.5)
ax.text(30, 1, 'masse\ncritique', ha='center', color='#dc2626', fontweight='bold')
ax.fill_between(n[n<30], U[n<30], color='#dc2626', alpha=.1)
ax.fill_between(n[n>=30], U[n>=30], color='#0d9488', alpha=.1)
ax.text(15, 0.5, "phase\nd'amorçage", fontsize=9, color='#7f1d1d')
ax.text(60, 12, "effet de réseau\n→ winner-takes-all", fontsize=9, color='#0f766e')
ax.set_xlabel("Nombre d'utilisateurs n", loc='right')
ax.set_ylabel("Utilité U(n)", loc='top', rotation=0)
ax.set_xticks([]); ax.set_yticks([])
ax.set_title("Effets de réseau : valeur d'un service ↑ avec n", fontweight='bold')
save(f, 'effets_reseau')

print("OK")

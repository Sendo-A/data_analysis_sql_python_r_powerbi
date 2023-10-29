#!/usr/bin/env python
# coding: utf-8

# <center>Projet sur le traitement et l’analyse des données du recensement général de la population et de l’habitat de 2014 (RGPH2014) du Maroc</center>

# In[7]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np


# ####  1. Créer le fichier notebook et charger dans un DataFrame (dfcom : DataFrame des communes) le contenu de la première feuille du fichier Excel (RGPH2004_2014_Commune.xlsx)

# In[8]:


# 1.Chargement dans un DataFramele premières feuille du fichier excel
dfcom=pd.read_excel('RGPH2014_Commune.xlsx', sheet_name="RGPH2014_data")


# In[165]:


# affichage du 5 premiers lignes pour avoir une idée sur le contenu de la data
dfcom.head()


# #### 2. Afficher le nombre de lignes et de colonnes de dfcom

# In[166]:


# 2.Affichage de nombre de ligne et colonne
print('On a 1689 lignes et 125 colonnes')
dfcom.shape


# #### 3. Calculer la population municipale totale, la population masculine, la population féminine et le nombre de ménages du Maroc en 2014

# In[167]:


# 3.Calculer la population municipale totale, la population masculine, la population féminine et le nombre de ménages du Maroc en 2014
print('la poulation total, masculine, féminine et le nombre de ménages sont par ordre')
dfcom[['pop_t', 'pop_m','pop_f','NbMg_T']].sum()


# #### 4. Afficher les communes dont la population (pop_t) est égale à zéro

# In[168]:


# 4.1 Afficher les communes dont la population (pop_t) est égale à zéro.
print('les communes dont la population (pop_t) est égale à zéro.')
dfcom.loc[dfcom['pop_t']==0,['nom_commune','pop_t']]


# In[9]:


# 4.2 supprimer définitivement les communes oû la valeur egal 0 de dfcom 
index_Names = dfcom[ dfcom['pop_t'] == 0 ].index
dfcom.drop(index_Names , inplace=True)


# #### 5.  Ajouter dans dfcom une nouvelle colonne appelée « superficie » et calculer la valeur de cette colonne

# In[170]:


# 5.Ajouter dans dfcom une nouvelle colonne appelée « superficie » et calculer la valeur de cette colonne
dfcom['superficie'] = dfcom['pop_t'] / dfcom['densite']  


# #### 6. Ajouter la colonne « type_commune » à dfcom et calculer sa valeur à partir de la colonne « code_ac » en se basant sur l'enonce

# In[173]:


# 6.Ajouter la colonne « type_commune » à dfcom et calculer sa valeur à partir de la colonne « code_ac » en se basant sur la table de correspondance
conditions = [
    (dfcom['code_ac'] == 1),
    (dfcom['code_ac'] == 2),
    (dfcom['code_ac'] == 3),
    (dfcom['code_ac'] == 4),
    (dfcom['code_ac'] == 5)]

values = ['Urbain', 'Rural', 'Centre urbain', 'Centre urbain', 'Centre_urbain']
dfcom['type_commune'] = np.select(conditions, values)


# #### 7. Calculer le nombre de communes rurales ayant un ou plusieurs centres urbains puis calculer le nombre de communes rurales ayant une population supérieure à la population de leur(s) centre(s) urbain(s)

# In[457]:


# 7.Calculer le nombre de communes rurales ayant un ou plusieurs centres urbains
print("le nombre de communes rurales ayant un ou plusieurs centres urbains est de")
dfcom[dfcom['type_commune']=='Centre urbain']['nom_commune'].nunique()


# In[72]:


# 7.calculer le nombre de communes rurales ayant une population supérieure à la population de leur(s) centre(s) urbain(s)
print("le nombre de communes rurales dont la pop_t supérieure à la pop_t de leur(s) centre(s) urbain(s) est de :")
sum(dfcom[dfcom['type_commune']== 'Rural']['pop_t']>dfcom[dfcom['type_commune']== 'Centre urbain']['pop_t'].count())


# #### 8. Calculer la moyenne et l’écart-type de la population des communes à caractère urbain (communes de type urbain ou centre urbain) et ceux des communes rurales

# In[176]:


# 8.1 Calculer la moyenne de la population des communes à caractère urbain (communes de type urbain ou centre urbain) 
print('la moyenne de la population des communes de type centre urbain ou urbain est de :')
round(dfcom[(['type_commune']=='Centre urbain')|(dfcom['type_commune']=='Urbain')]['pop_t'].mean())


# In[177]:


# 8.2 Calculer l’écart-type de la population des communes à caractère urbain (communes de type urbain ou centre urbain) 
print('l’écart-type de la population des communes de type centre urbain ou urbain est de :')
round(dfcom[(['type_commune']=='Centre urbain')|(dfcom['type_commune']=='Urbain')]['pop_t'].std())


# In[178]:


# 8.3 Calculer la moyenne de la population des communes à caractère rural 
print('la moyenne de la population des communes de type centre rural est de :')
round(dfcom[dfcom['type_commune']=='Rural']['pop_t'].mean())


# In[179]:


# 8.4 Calculer l’écart-type de la population des communes à caractère rural 
print('l’écart-type de la population des communes de type centre rural est de :')
round(dfcom[dfcom['type_commune']=='Rural']['pop_t'].std())


# #### 9. Calculer le nombre de valeurs uniques dans le champ « nom_commune » et Afficher dans un nouveau dataframe (dfcom_duplic) les communes ayant le même nom tout en affichant le nom de leur province

# In[180]:


# 9.1 Calculer le nombre de valeurs uniques dans le champ « nom_commune »
print('le nombre de valeurs uniques dans le champ « nom_commune » ',
dfcom['nom_commune'].nunique())


# In[181]:


# 9.Afficher dans un nouveau dataframe (dfcom_duplic) les communes ayant le même nom tout en affichant le nom de leur province
print('les communes ayant le même nom tout en affichant le nom de leur province')
dfcom_duplic=pd.DataFrame(dfcom, columns=['nom_province','nom_commune'])
dfcom_duplic[dfcom_duplic.duplicated(['nom_province','nom_commune'])]


# In[182]:


type(dfcom_duplic)


# #### 10. Calculer le nombre de commune dont le nom commence par le terme « Sidi » sans tenir en compte la casse (le terme peut être en minuscule, majuscule ou bien un mélange des deux)

# In[643]:


# 10.Calculer le nombre de commune dont le nom commence par le terme « Sidi » sans tenir en compte la casse (le terme peut être en minuscule, majuscule ou bien un mélange des deux)
print('le nombre de commune dont le nom commence par le terme « Sidi » sans tenir en compte la casse est de')
dfcom['nom_commune'].str.upper().str.startswith('SIDI').sum()


# #### 11. Donner le nom de la commune urbaine (code_ac == 1) ayant le taux net d’activité le plus bas et celle ayant le taux net d’activité le plus haut

# In[610]:


# 11.Donner le nom de la commune urbaine (code_ac == 1) ayant le taux net d’activité le plus bas et celle ayant le taux net d’activité le plus haut
dfcom[dfcom['ta_t']==dfcom[dfcom["code_ac"] == 1]['ta_t'].min()]['nom_commune']


# #### 12. Calculer le nombre de communes ayant un taux net d’activité inférieur à la moyenne des taux nets d’activité

# In[185]:


type_c1.loc[type_c1['ta_t'] == type_c1['ta_t'].max()]['nom_commune']


# In[187]:


# 12.Calculer le nombre de communes ayant un taux net d’activité inférieur à la moyenne des taux nets d’activit
print("le nombre de communes ayant un taux d'activité inférieur à la moyenne")
sum(dfcom['ta_t']<dfcom['ta_t'].mean())


# #### 13.Reproduire à partir des données dfcom, le graphique

# In[461]:


dfcom_moins_15=[round(sum(dfcom[dfcom['type_commune']!='Rural']['mq_t']*dfcom[dfcom['type_commune']!='Rural']['pop_t']/100)/sum(dfcom[dfcom['type_commune']!='Rural']['pop_t'])*100,1),
                round(sum(dfcom[dfcom['type_commune']=='Rural']['mq_t']*dfcom[dfcom['type_commune']=='Rural']['pop_t']/100)/sum(dfcom[dfcom['type_commune']=='Rural']['pop_t'])*100,1),
                round(sum(dfcom['mq_t']*dfcom['pop_t']/100)/sum(dfcom['pop_t'])*100,1)]
dfcom_15_à_59=[round(sum(dfcom[dfcom['type_commune']!='Rural']['qcq_t']*dfcom[dfcom['type_commune']!='Rural']['pop_t']/100)/sum(dfcom[dfcom['type_commune']!='Rural']['pop_t'])*100,1),
               round(sum(dfcom[dfcom['type_commune']=='Rural']['qcq_t']*dfcom[dfcom['type_commune']=='Rural']['pop_t']/100)/sum(dfcom[dfcom['type_commune']=='Rural']['pop_t'])*100,1),
               round(sum(dfcom['qcq_t']*dfcom['pop_t']/100)/sum(dfcom['pop_t'])*100,1)]
dfcom_plus_60=[round(sum(dfcom[dfcom['type_commune']!='Rural']['soix_t']*dfcom[dfcom['type_commune']!='Rural']['pop_t']/100)/sum(dfcom[dfcom['type_commune']!='Rural']['pop_t'])*100,1),
               round(sum(dfcom[dfcom['type_commune']=='Rural']['soix_t']*dfcom[dfcom['type_commune']=='Rural']['pop_t']/100)/sum(dfcom[dfcom['type_commune']=='Rural']['pop_t'])*100,1),
               round(sum(dfcom['soix_t']*dfcom['pop_t']/100)/sum(dfcom['pop_t'])*100,1)]

data = {'moins de 15 ans':dfcom_moins_15,
        '15-59 ans':dfcom_15_à_59, 
        '60 ans et plus':dfcom_plus_60}

dtc = pd.DataFrame(data, index =['Urbain',
                                'Rural',
                                'Total'])
dtc=dtc.transpose()

display(dtc)
dtc = pd.DataFrame({'moins de 15 ans': dfcom_moins_15,
                    '15-59 ans':dfcom_15_à_59,
                    '60 ans et plus':dfcom_plus_60,}, index =['Urbain','Rural', 'Total'])
dtc.style.set_caption("Hello World")


ax=dtc.plot.bar()
ax.set_ylabel('Population (%)',fontsize=10)
ax.yaxis.set_label_coords(0.05, .8)
plt.xticks(rotation=-30)
plt.ylim([0, 75])
plt.legend(loc="lower center", bbox_to_anchor=(0.5, -0.3), ncol=3,frameon= False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)


# #### 14. Représenter graphiquement la répartition des ménages urbains par type d’occupation de logement (villa, maison marocaine, appartement, bidonville, habitation rurale)

# In[190]:


dfcom_uvilla=[round(sum(dfcom[dfcom['type_commune']!='Rural']['villa_u']*dfcom[dfcom['type_commune']!='Rural']['pop_t']/100)/sum(dfcom[dfcom['type_commune']!='Rural']['pop_t'])*100,1)]
dfcom_appa_u=[round(sum(dfcom[dfcom['type_commune']!='Rural']['appa_u']*dfcom[dfcom['type_commune']!='Rural']['pop_t']/100)/sum(dfcom[dfcom['type_commune']!='Rural']['pop_t'])*100,1)]
dfcom_mm_u=[round(sum(dfcom[dfcom['type_commune']!='Rural']['mm_u']*dfcom[dfcom['type_commune']!='Rural']['pop_t']/100)/sum(dfcom[dfcom['type_commune']!='Rural']['pop_t'])*100,1)]
dfcom_som_u=[round(sum(dfcom[dfcom['type_commune']!='Rural']['som_u']*dfcom[dfcom['type_commune']!='Rural']['pop_t']/100)/sum(dfcom[dfcom['type_commune']!='Rural']['pop_t'])*100,1)]
dfcom_rural_u=[round(sum(dfcom[dfcom['type_commune']!='Rural']['rural_u']*dfcom[dfcom['type_commune']!='Rural']['pop_t']/100)/sum(dfcom[dfcom['type_commune']!='Rural']['pop_t'])*100,1)]

print("la répartition des ménages urbains par type d’occupation de logement (villa, maison marocaine, appartement, bidonville, habitation rurale)")
data = {'villa':dfcom_uvilla,
        'maison marocaine':dfcom_appa_u, 
        'appartement':dfcom_mm_u,
        'bidonvilla':dfcom_som_u,
        'habitation rurale':dfcom_rural_u}
 
dtu = pd.DataFrame(data, index =['Urbain'])
dtu=dtu.transpose()
display(dtu)

# create random data
names='villa', 'maison marocaine', 'appartement', 'bidonvilla','habitation rurale'
values=[4.4,16.8,71.1,5.2,1.4]

# Label distance: gives the space between labels and the center of the pie
colors = ['#4F6272', '#B7C3F3', '#DD7596', '#8EB897', '#FFA500']
plt.pie(values, labels=names, labeldistance=1.15,wedgeprops = { 'linewidth' : 1, 'edgecolor' : 'white' }, colors=colors);
plt.show();


# ####  15. Représenter graphiquement le taux net d’activité (ta_t) en fonction du taux d’analphabétisme de la population âgée de 10 ans et plus (anlph_t). Commenter le graphique

# In[191]:


print("representation graphique de taux net d’activité en fonction du taux d’analphabétisme de la population âgée de 10 ans et plus")
anlph_t=round(dfcom['pop_t']*dfcom['anlph_t']/100,1)
ta_t=round(dfcom['pop_t']*dfcom['ta_t']/100,1)


data = {'ta_t':ta_t,
        'anlph_t':anlph_t}
 
dtt = pd.DataFrame(data)

display(dtt)
sns.regplot(dtt["ta_t"], dtt["anlph_t"], line_kws={"color":"r","alpha":0.7,"lw":5})
plt.show()
### on voie que le taux


# #### 16. D’après les données représentées dans dfcom, quels sont les facteurs explicatifs du taux de pauvreté globale. Est-ce que ces facteurs sont les mêmes en milieu urbain et en milieu rural ?

# In[463]:


# Les facteurs explicatifs du taux de pauvreté globale
d_corr=dfcom.corr()
threshold=0.8
haut_corr=abs(d_corr['TPG2014_T'])
result=haut_corr[haut_corr>0.8]
result


# In[193]:


# 16.2 Est-ce que ces facteurs sont les mêmes en milieu urbain et en milieu rural ?
# la correltaion entre "TPG2014_T" et les autres varibales dans le mlieu Urbain
corr_ur=dfcom[dfcom['type_commune']!='Rural'].corr()['TPG2014_T'][:]
Threshold=0.8
haut_cru=corr_ur[corr_ur>0.8]
haut_cru


# In[194]:


# la correltaion entre "TPG2014_T" et les autres varibales dans le mlieu Rural
corr_ru=dfcom[dfcom['type_commune']=='Rural'].corr()['TPG2014_T'][:]
Threshold=0.8
haut_cru=corr_ru[corr_ru>0.8]
haut_cru


# In[ ]:


# les variables qui impact directement le taux de pauvreté dans le milieu rural sont dirrerents que celles du mulieu urbain on a 
pour le milieu Urbian les facteurs suivants
            pauv2014_T   =  Taux de pauvreté monétaire (Total)
            volum_T       0.951003
            sev_T         0.923734
            vul_T         0.844052
            DFP_Pmon_u    0.950484


# #### 17. Générer un nouveau DataFrame (DataFrame des Provinces : dfprov)

# In[464]:


# definir les colonnes puis gnérer les données
dfprov = dfcom[['code_province','nom_province','pop_t','pop_m','pop_f','NbMg_T','eau_t','elec_t']].copy()
dfprov['nb_com_u'] = dfcom['type_commune']!= 'Rural'
dfprov['nb_com_r'] = dfcom['type_commune']== 'Rural'
dfprov['nb_com_u'] = dfprov['nb_com_u'].astype(int)
dfprov['nb_com_r'] = dfprov['nb_com_r'].astype(int)
dfprov['pop_u']=dfcom[dfcom['type_commune']!='Rural']['pop_t']
dfprov['pop_r']=dfcom[dfcom['type_commune']=='Rural']['pop_t']
dfprov['NbMg_U']=dfcom[dfcom['type_commune']!='Rural']['NbMg_T']
dfprov['NbMg_R']=dfcom[dfcom['type_commune']=='Rural']['NbMg_T']
dfprov


# In[465]:


# agregation par code de province
dfprov.groupby('code_province')
by_code_province=dfprov.groupby('code_province')
by_code_province.sum()


# #### générer un nouveau DataFrame (DataFrame des Régions : dfreg) qui donne les mêmes informations indiquées ci-dessus en remplaçant l’agrégat province par région (agrégation par code_region)

# In[466]:


# remplaçant le code de province par code de la region
dfreg=dfprov
dfreg['code_province'] = dfcom['code_region']
dfreg.rename( columns={'code_province':'code_region'} ,inplace=True)
dfreg


# In[584]:


# agregation par code _region
dfprov.groupby('code_region')
by_code_region=dfprov.groupby('code_region')
dfreg=by_code_region.sum()
dfreg


# #### 18.En faisant le webscraping du site web (http://cartesanitaire.sante.gov.ma) ajouter à dfreg, les informations suivantes (données par région) 

# In[406]:


import requests 
from bs4 import BeautifulSoup
url = "http://cartesanitaire.sante.gov.ma/ftnrd?p_idniveau=4&p_idreg=6"
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
res


# In[407]:


tables = soup.find_all("table")  # returns a list of tables
print(f'Total tables: {len(tables)}')
dfh=tables


# #### 18.1 le webscraping du site web (http://cartesanitaire.sante.gov.ma) 

# In[507]:


# copie html dans un editeur de text pour cerner les position de chaque table pouis generer les avec une loup
col_names=["region_name",
           "hosp_nbr","bed_nbr",
           "func_bed_nbr","hémo_center_nbr",
           "urg_bed_nbr","clinic_nbr",
           "offic_nbr","cab_nbr",
           "gen_med_nbr","spec_med_nbr",
           "phar_med_nbr",
           "chir_med_nbr","cor_med_nbr"]
dfm_reg=pd.DataFrame(columns=col_names)


for i in range(1,13):
    # get the url :
    url = f"http://cartesanitaire.sante.gov.ma/ftnrd?p_idniveau=4&p_idreg={i}"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    #region name
    region_name=soup.find("span",{"id":"lblRegion"}).text.split(":")[1].strip()
    #Nbr d’hôpitaux et nbr de lits existants et nbr de lits fonctionnels
    hosp_table=soup.find_all("table",{"class":"table table-bordered"})[4]
    for hosp in hosp_table.find_all("tbody"):
        rows=hosp.find_all("tr")
        hosp_nbr=rows[-1].find_all("td",{"style":"text-align: center"})[0].text
        bed_nbr=rows[-1].find_all("td",{"style":"text-align: center"})[1].text
        func_bed_nbr=rows[-1].find_all("td",{"style":"text-align: center"})[2].text
    # nbr centres d’hémodialyse
    hémo_center=soup.find_all("table",{"class":"table table-bordered"})[5]
    for center in hémo_center.find_all("tbody"):
        rows=center.find_all("tr")
        hémo_center_nbr=rows[0].find("td",{"style":"text-align: center"}).text
    # nbr lit d’urgence
    urg_bed=soup.find_all("table",{"class":"table table-bordered"})[9]
    for urg in urg_bed.find_all("tbody"):
        rows=urg.find_all("tr")
        urg_bed_nbr=rows[-1].find_all("td",{"style":"text-align: center"})[1].text
    # nbr cliniques, officines de pharmacie et laboratoire
    clin_table=soup.find_all("table",{"class":"table table-bordered"})[12]
    for clin in clin_table.find_all("tbody"):
        rows=clin.find_all("tr")
        clinic_nbr=rows[0].find("td",{"style":"text-align: center"}).text
        offic_nbr=rows[4].find("td",{"style":"text-align: center"}).text
        cab_nbr=rows[3].find("td",{"style":"text-align: center"}).text
    # med generalistes, specialiste, phamacistes, chirurgien dentistes, et corps médical
    med_table=soup.find_all("table",{"class":"table table-bordered"})[14]
    for med in med_table.find_all("tbody"):
        rows=med.find_all("tr")
        gen_med_nbr=rows[0].find_all("td", {"style":"text-align: center;font-weight:bold"})[1].text
        spec_med_nbr=rows[1].find_all("td", {"style":"text-align: center;font-weight:bold"})[1].text
        phar_med_nbr=rows[3].find_all("td", {"style":"text-align: center;font-weight:bold"})[1].text
        chir_med_nbr=rows[4].find_all("td", {"style":"text-align: center;font-weight:bold"})[1].text
        cor_med_nbr=rows[9].find_all("td", {"style":"text-align: center;font-weight:bold"})[-1].text

    health_list=[region_name, 
                 hosp_nbr, bed_nbr, 
                 func_bed_nbr, hémo_center_nbr, 
                 urg_bed_nbr, clinic_nbr, offic_nbr, 
                 cab_nbr, gen_med_nbr, spec_med_nbr, 
                 phar_med_nbr, chir_med_nbr , cor_med_nbr]
    # Transformer les chiffre extrait du site en int()
    for i in range(len(health_list[i])):
        try:
            health_list[i]=int(health_list[i])
        except :
            pass
    dfm_reg.loc[len(dfm_reg)]=health_list
dfm_reg


# In[549]:


for i in range(len(health_list[i])):
    try:
        health_list[i]=int(health_list[i])
    except :
        pass
    dfm_reg.loc[len(dfm_reg)]=health_list


# #### 18.2 ajouter à dfreg, les informations suivantes (données par région) :

# In[585]:


# changer l'index du dfm_reg pour qu'on puisse concatener respectivement les colonnes
dfm_reg.index = np.arange(1, len(dfm_reg)+1)
frames = [dfreg, dfm_reg]
dfreg = pd.concat(frames, axis=1)


# In[587]:


dfreg["hosp_nbr"] = dfreg["hosp_nbr"].astype(int)
dfreg["bed_nbr"] = dfreg["bed_nbr"].astype(int)
dfreg["func_bed_nbr"] = dfreg["func_bed_nbr"].astype(int)
dfreg["urg_bed_nbr"] = dfreg["urg_bed_nbr"].astype(int)
dfreg["clinic_nbr"] = dfreg["clinic_nbr"].astype(int)
dfreg["offic_nbr"] = dfreg["offic_nbr"].astype(int)
dfreg["cab_nbr"] = dfreg["cab_nbr"].astype(int)
dfreg["gen_med_nbr"] = dfreg["gen_med_nbr"].astype(int)
dfreg["spec_med_nbr"] = dfreg["spec_med_nbr"].astype(int)
dfreg["phar_med_nbr"] = dfreg["phar_med_nbr"].astype(int)
dfreg["chir_med_nbr"] = dfreg["chir_med_nbr"].astype(int)
dfreg["cor_med_nbr"] = dfreg["cor_med_nbr"].astype(int)
dfreg


# In[594]:


#extraire les nome des colonnes pour repositionner la colonne nom de la region 
print(dfreg.columns)


# In[511]:


# chnager l'order des colonnes defini la colonne region_name en premier
dfreg=dfreg[['region_name','pop_t', 'pop_m', 'pop_f', 'NbMg_T', 'eau_t', 'elec_t', 'nb_com_u',
       'nb_com_r', 'pop_u', 'pop_r', 'NbMg_U', 'NbMg_R',
       'hosp_nbr', 'bed_nbr', 'func_bed_nbr', 'hémo_center_nbr', 'urg_bed_nbr',
       'clinic_nbr', 'offic_nbr', 'cab_nbr', 'gen_med_nbr', 'spec_med_nbr',
       'phar_med_nbr', 'chir_med_nbr', 'cor_med_nbr']]
dfreg


# #### 19. Analyser en s’appuyant sur des graphiques, la relation entre les offres de soins et les caractéristiques démographiques des régions

# In[600]:


colors = ['#4F6272', '#B7C3F3', '#DD7596', '#8EB897', '#FFA500',]
plt.pie(data=dfreg, labels='region_name',x='hosp_nbr', labeldistance=1.15,wedgeprops = { 'linewidth' : 1, 'edgecolor' : 'white' }, colors=colors);
plt.show();


# In[ ]:





# In[625]:


dfreg.plot.bar(x='region_name', y=['bed_nbr','func_bed_nbr','urg_bed_nbr'], figsize=(20,6))


# In[633]:


sns.jointplot(x='gen_med_nbr',y='pop_t',data=dfreg,kind='scatter',height=6,
    ratio=6,
    space=1.5)


# In[589]:


dfreg.plot.bar(x='region_name',y='func_bed_nbr', figsize=(20,6))


# #### 20. Exporter les DataFrames « dfprov » et « dfreg » vers le fichier Excel (« resultats_votre- nom.xlsx » en les mettant sur deux feuilles différentes (Attention ! : Deux feuilles du même fichier Excel)

# In[618]:


# Exporter le dataframe dfprov vers le fichier excel "data/poprov.xlsx" --> méthode to_excel()
dfprov.to_excel(r'data\resultat_CHAJIA_ABDELHADI_et_EL-IDRRISSI_MUSTAPHA.xlsx')


# In[617]:


dfreg.to_excel(r'data\resultat_CHAJIA_ABDELHADI_et_EL-IDRRISSI_MUSTAPHA.xlsx')


# In[ ]:





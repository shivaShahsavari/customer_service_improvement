import pandas as pd
import numpy as np
from scipy.stats import mstats
########Calcaulating the differences regarding the actual_prep
Data = pd.read_csv("incident_task_combined.csv",encoding = "ISO-8859-1",header=0)
conditions = [ (Data['start_delay_status'] =='not_delayed'), (Data['start_delay_status'] =='delayed')]
values_int = [1, 0]
Data['delay_status_int']=np.select(conditions, values_int)
##########################Column : start_delay_status #############################

kruskal_Actual_dur=Data[['calc_actual','delay_status_int']]
ACTUAL_END_DUR = kruskal_Actual_dur['calc_actual'].to_numpy()
DELAY_STATUS_DUR = kruskal_Actual_dur['delay_status_int'].to_numpy()
'''
print("Kruskal Wallis H-test for DELAY_STATUS test:")

H_actual_dur, pval_actual_dur = mstats.kruskalwallis(DELAY_STATUS_DUR,ACTUAL_END_DUR)

print("H-statistic:", H_actual_dur)
print("P-Value:", pval_actual_dur)

if pval_actual_dur < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval_actual_dur > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")
print("######################")
'''
##########################Column : TYPE_KLANT #############################
condition2 = [ (Data['TYPE_KLANT'] =='Klant Primair'), (Data['TYPE_KLANT'] =='Dummy - Overig'),(Data['TYPE_KLANT'] =='Dummy - Tenderned'),(Data['TYPE_KLANT'] =='Other')]
values2_int = [1,2,3,4]
Data['type_klant_int']=np.select(condition2, values2_int)
kruskal_typ_klant=Data[['calc_actual','type_klant_int']]
ACTUAL_DUR = kruskal_typ_klant['calc_actual'].to_numpy()
type_klant = kruskal_typ_klant['type_klant_int'].to_numpy()
'''
print("Kruskal Wallis H-test for TYPE_KLANT test:")
H_type_klant, pval_type_klant = mstats.kruskalwallis(type_klant,ACTUAL_DUR)

print("H-statistic:", H_type_klant)
print("P-Value:", pval_type_klant)

if pval_type_klant < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval_type_klant > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")
print("######################")
'''
##########################Column : TASK_TYPE #############################
condition3 = [ (Data['TASK_TYPE'] =='Overigen'), (Data['TASK_TYPE'] =='Terugbelafspraak')]
values3_int = [1,2]
Data['task_type_int']=np.select(condition3, values3_int)
kruskal_task_type=Data[['calc_actual','task_type_int']]
ACTUAL_DUR = kruskal_task_type['calc_actual'].to_numpy()
task_type = kruskal_task_type['task_type_int'].to_numpy()
'''
print("Kruskal Wallis H-test for TASK_TYPE test:")
H_task_type, pval_task_type = mstats.kruskalwallis(task_type,ACTUAL_DUR)

print("H-statistic:", H_task_type)
print("P-Value:", pval_task_type)

if pval_task_type < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval_task_type > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")
print("######################")
'''
##########################Column : INCIDENT_TYPE #############################
condition4 = [ (Data['INCIDENT_TYPE'] =='Gerichte vraag over zaak/aanvraag. niet zijnde status'), (Data['INCIDENT_TYPE'] =='Other'),
(Data['INCIDENT_TYPE'] =='Dienstverzoek'),(Data['INCIDENT_TYPE'] =='Email')]
values4_int = [1,2,3,4]
Data['incident_type_int']=np.select(condition4, values4_int)
kruskal_incident_type=Data[['calc_actual','incident_type_int']]
ACTUAL_DUR = kruskal_incident_type['calc_actual'].to_numpy()
incident_type = kruskal_incident_type['incident_type_int'].to_numpy()
'''
print("Kruskal Wallis H-test for INCIDENT_TYPE test:")
H_incident_type, pval_incident_type = mstats.kruskalwallis(incident_type,ACTUAL_DUR)

print("H-statistic:", H_incident_type)
print("P-Value:", pval_incident_type)

if pval_incident_type < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval_incident_type > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")
print("######################")
'''
##########################Column : PRODUCT_DESCRIPTION_CODE #############################
Data['prod_desc_code_int']=Data['PRODUCT_DESCRIPTION_CODE'].str[3:]
kruskal_prod_desc_code=Data[['calc_actual','prod_desc_code_int']]
ACTUAL_DUR = kruskal_prod_desc_code['calc_actual'].to_numpy()
prod_desc_code = kruskal_prod_desc_code['prod_desc_code_int'].to_numpy()
'''
print("Kruskal Wallis H-test for PRODUCT_DESCRIPTION_CODE test:")
H_prod_desc_code, pval_prod_desc_code = mstats.kruskalwallis(prod_desc_code,ACTUAL_DUR)

print("H-statistic:", H_prod_desc_code)
print("P-Value:", pval_prod_desc_code)

if pval_prod_desc_code < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval_prod_desc_code > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")
print("######################")
'''
##########################Column : CALLER_TYPE_NAME #############################
condition7 = [ (Data['CALLER_TYPE_NAME'] =='Organization'),(Data['CALLER_TYPE_NAME'] =='Person') ]
values7_int = [1,2]
Data['caller_type_name_int']=np.select(condition7, values7_int)
kruskal_caller_type_name=Data[['calc_actual','caller_type_name_int']]
ACTUAL_DUR = kruskal_caller_type_name['calc_actual'].to_numpy()
caller_type_name = kruskal_caller_type_name['caller_type_name_int'].to_numpy()
'''
print("Kruskal Wallis H-test for CALLER_TYPE_NAME test:")
H_caller_type_name, pval_caller_type_name = mstats.kruskalwallis(caller_type_name,ACTUAL_DUR)

print("H-statistic:", H_caller_type_name)
print("P-Value:", pval_caller_type_name)

if pval_caller_type_name < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval_caller_type_name > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")
print("######################")
'''
##########################Column : OWNER #############################
condition8 = [ (Data['OWNER'] =='EMPL0181'),(Data['OWNER'] =='EMPL0200'), (Data['OWNER'] =='EMPL0265'), (Data['OWNER'] =='Other') ]
values8_int = [1,2,3,4]
Data['OWNER_int']=np.select(condition8, values8_int)
kruskal_OWNER=Data[['calc_actual','OWNER_int']]
ACTUAL_DUR = kruskal_OWNER['calc_actual'].to_numpy()
OWNER = kruskal_OWNER['OWNER_int'].to_numpy()
'''
print("Kruskal Wallis H-test for OWNER test:")
H_OWNER, pval_OWNER = mstats.kruskalwallis(OWNER,ACTUAL_DUR)

print("H-statistic:", H_OWNER)
print("P-Value:", pval_OWNER)

if pval_OWNER < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval_OWNER > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")
print("######################")
'''
##########################Column : SR_CR_CHANNEL_BETEKENIS #############################
condition9 = [ (Data['OWNER'] =='Berichtenbox'),(Data['OWNER'] =='E-mail'), (Data['OWNER'] =='Telefoon'), (Data['OWNER'] =='Other') ]
values9_int = [1,2,3,4]
Data['CHANNEL_BETEKENIS_int']=np.select(condition9, values9_int)
kruskal_CHANNEL_BETEKENIS=Data[['calc_actual','CHANNEL_BETEKENIS_int']]
ACTUAL_DUR = kruskal_CHANNEL_BETEKENIS['calc_actual'].to_numpy()
CHANNEL_BETEKENIS = kruskal_CHANNEL_BETEKENIS['CHANNEL_BETEKENIS_int'].to_numpy()
'''
print("Kruskal Wallis H-test for SR_CR_CHANNEL_BETEKENIS test:")
H_CHANNEL_BETEKENIS, pval_CHANNEL_BETEKENIS = mstats.kruskalwallis(CHANNEL_BETEKENIS,ACTUAL_DUR)

print("H-statistic:", H_CHANNEL_BETEKENIS)
print("P-Value:", pval_CHANNEL_BETEKENIS)

if pval_CHANNEL_BETEKENIS < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval_CHANNEL_BETEKENIS > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")
print("######################")
'''
##########################Column : Opdrachtgever #############################
condition10 = [ (Data['Opdrachtgever'] =='1BRS'),(Data['Opdrachtgever'] =='Meststoffen'), 
(Data['Opdrachtgever'] =='WD Dierregistraties (Sector)'), (Data['Opdrachtgever'] =='Other') ]
values10_int = [1,2,3,4]
Data['client_int']=np.select(condition10, values10_int)
kruskal_client=Data[['calc_actual','client_int']]
ACTUAL_DUR = kruskal_client['calc_actual'].to_numpy()
client = kruskal_client['client_int'].to_numpy()
'''
print("Kruskal Wallis H-test for Opdrachtgever test:")
H_client, pval_client = mstats.kruskalwallis(client,ACTUAL_DUR)

print("H-statistic:", H_client)
print("P-Value:", pval_client)

if pval_client < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval_client > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")
print("######################")
'''
##########################Column : RESPONSIBILITY_NAME #############################
condition11 = [ (Data['RESPONSIBILITY_NAME'] =='1BRS'),(Data['RESPONSIBILITY_NAME'] =='Meststoffen'), 
(Data['RESPONSIBILITY_NAME'] =='WD Dierregistraties (Sector)'), (Data['RESPONSIBILITY_NAME'] =='Other') ]
values11_int = [1,2,3,4]
Data['respons_name_int']=np.select(condition11, values11_int)
kruskal_respons_name=Data[['calc_actual','respons_name_int']]
ACTUAL_DUR = kruskal_respons_name['calc_actual'].to_numpy()
respons_name = kruskal_respons_name['respons_name_int'].to_numpy()
'''
print("Kruskal Wallis H-test for RESPONSIBILITY_NAME test:")
H_respons_name, pval_respons_name = mstats.kruskalwallis(respons_name,ACTUAL_DUR)

print("H-statistic:", H_respons_name)
print("P-Value:", pval_respons_name)

if pval_respons_name < 0.05:
    print("Reject NULL hypothesis - Significant differences exist between groups.")
if pval_respons_name > 0.05:
    print("Accept NULL hypothesis - No significant difference between groups.")
print("######################")
'''
##############################################################################
#################################AD_HOC TEST #################################

################ start_delay_status
import scikit_posthocs as sp
print("post hoc test for start_delay_status")
pht_start_delay_status=sp.posthoc_dunn (Data,'calc_actual','start_delay_status','bonferroni')
print(pht_start_delay_status.stack()[pht_start_delay_status.stack() < 0.05].rename_axis(('idx','cols')).reset_index(name='val'))
################ TYPE_KLANT
print("post hoc test for TYPE_KLANT")
pht_type_klant=sp.posthoc_dunn (Data,'calc_actual','TYPE_KLANT','bonferroni')
print(pht_type_klant.stack()[pht_type_klant.stack() < 0.05].rename_axis(('idx','cols')).reset_index(name='val'))
################ TASK_TYPE
print("post hoc test for TASK_TYPE")
pht_task_type=sp.posthoc_dunn (Data,'calc_actual','TASK_TYPE','bonferroni')
print(pht_task_type.stack()[pht_task_type.stack() < 0.05].rename_axis(('idx','cols')).reset_index(name='val'))
################ INCIDENT_TYPE
print("post hoc test for INCIDENT_TYPE")
pht_incident_type=sp.posthoc_dunn (Data,'calc_actual','INCIDENT_TYPE','bonferroni')
print(pht_incident_type.stack()[pht_incident_type.stack() < 0.05].rename_axis(('idx','cols')).reset_index(name='val'))
################ PRODUCT_DESCRIPTION_CODE
print("post hoc test for PRODUCT_DESCRIPTION_CODE")
pht_prod_desc_code=sp.posthoc_dunn (Data,'calc_actual','PRODUCT_DESCRIPTION_CODE','bonferroni')
print(pht_prod_desc_code.stack()[pht_prod_desc_code.stack() < 0.05].rename_axis(('idx','cols')).reset_index(name='val'))
################ CALLER_TYPE_NAME
print("post hoc test for CALLER_TYPE_NAME")
pht_caller_typ_name=sp.posthoc_dunn (Data,'calc_actual','CALLER_TYPE_NAME','bonferroni')
print(pht_caller_typ_name.stack()[pht_caller_typ_name.stack() < 0.05].rename_axis(('idx','cols')).reset_index(name='val'))
################ OWNER
print("post hoc test for OWNER")
pht_owner=sp.posthoc_dunn (Data,'calc_actual','OWNER','bonferroni')
print(pht_owner.stack()[pht_owner.stack() < 0.05].rename_axis(('idx','cols')).reset_index(name='val'))
################ SR_CR_CHANNEL_BETEKENIS 
print("post hoc test for SR_CR_CHANNEL_BETEKENIS ")
pht_chnl_betekenis=sp.posthoc_dunn (Data,'calc_actual','SR_CR_CHANNEL_BETEKENIS','bonferroni')
print(pht_chnl_betekenis.stack()[pht_chnl_betekenis.stack() < 0.05].rename_axis(('idx','cols')).reset_index(name='val'))
################ Opdrachtgever 
print("post hoc test for Opdrachtgever ")
pht_client=sp.posthoc_dunn (Data,'calc_actual','Opdrachtgever','bonferroni')
print(pht_client.stack()[pht_client.stack() < 0.05].rename_axis(('idx','cols')).reset_index(name='val'))
################ RESPONSIBILITY_NAME 
print("post hoc test for RESPONSIBILITY_NAME ")
pht_resp_name=sp.posthoc_dunn (Data,'calc_actual','RESPONSIBILITY_NAME','bonferroni')
print(pht_resp_name.stack()[pht_resp_name.stack() < 0.05].rename_axis(('idx','cols')).reset_index(name='val'))


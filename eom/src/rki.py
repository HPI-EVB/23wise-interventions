import pandas as pd


def get_grippeweb():
    # load grippeweb data & parse dates
    grippeweb_original = pd.read_csv('https://raw.githubusercontent.com/robert-koch-institut/GrippeWeb_Daten_des_Wochenberichts/main/GrippeWeb_Daten_des_Wochenberichts.tsv',
    sep='\t', index_col='Kalenderwoche')
    grippeweb_original.index = pd.to_datetime(grippeweb_original.index + '-1', format='%G-W%V-%u')

    # filter & accumulate
    return grippeweb_original.loc[
         grippeweb_original.Altersgruppe.str.contains('15-34|35-59') & # Region 'Osten' only has 00+ age group
        (grippeweb_original.Region == 'Bundesweit') &
        (grippeweb_original.Erkrankung == 'ARE')
    ]\
        .groupby('Kalenderwoche')\
        .Inzidenz.mean()\
        .reset_index()\
        .rename(columns={ 'Inzidenz': 'GrippeWeb', 'Kalenderwoche': 'Week' })

def get_consultations():
    # load consultations data & parse dates
    consultation_original = pd.read_csv('https://raw.githubusercontent.com/robert-koch-institut/ARE-Konsultationsinzidenz/main/ARE-Konsultationsinzidenz.tsv',
    sep='\t', index_col='Kalenderwoche')
    consultation_original.index = pd.to_datetime(consultation_original.index + '-1', format='%G-W%V-%u')

    # filter & accumulate
    return consultation_original.loc[
        consultation_original.Altersgruppe.str.contains('15-34|35-59') &
        consultation_original.Bundesland.str.contains('Bundesweit')
    ]\
        .groupby('Kalenderwoche')\
        .ARE_Konsultationsinzidenz.mean()\
        .reset_index()\
        .rename(columns={ 'ARE_Konsultationsinzidenz': 'SEED-ARE', 'Kalenderwoche': 'Week' })

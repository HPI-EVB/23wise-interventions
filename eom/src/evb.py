import pandas as pd

from src.database import read_sql

def get_evb_incidence():
    # --------------------------------------------------------------------------
    # Schichtfunktionen --------------------------------------------------------
    
    ignored_shifts = [
    # from sickness shifts
        'K>6', # länger 6 wochen krank -> nicht inzidenz
        'KK', # kind krank -> nicht inzidenz
    # from absent non-sick
        # '!', # urlaub, hier meldet man sich trotzdem krank
        'ABW-Sonstige', # sonstige sind zu vielfältig
        'Sonstige',
        # 'AH', # einsatz außer haus
        'AM', # Abwesenheitsmeldung, würden sich sonst krank melden
        'AWU', # arbeits-/wegeunfall -> werden nicht von maßnahmen beeinflusst
        # 'A-ZG', # ausgleich zeitguthaben, betrachtet wie urlaub
        # 'BR', # betriebsratstag, würden sich auch krank melden
        'BV', # beschäftigungsverbot, beeinflussen inzidenz nicht
        # 'DR', # dienstreise, würden sich auch krank melden
        'EU-Re', # erwerbsunfähigkeitsrente, i.e. > 1.5J abwesend
        'EZ', # elternzeit, lange nicht da
        # 'F', # fortbildung, würden sich krank melden
        # 'KA', # kurzarbeit, würden sich auch krank melden
        'KUR', # kur, länger nicht da
        'MU', # mutterschutz, länger nicht da
        'QT', # quarantäne
        # 'R', # regenerationstag, würde sich auch krank melden
        # 'S', # streik, sonderurlaub, würden sich auch krank melden
        # 'U', # urlaub, würden sich krank melden
        # 'WB', # weiterbildung, würden sich krank melden
        # 'X', # dienstfrei, würden sich auch krank melden; machen sie aber nicht -> WEIHNACHTSKNICKE
        # 'X-F', # ersatzruhetag, würden sich auch krank melden
        # 'X-S' # ersatzruhetag, würden sich auch krank melden
    ]
    sql_ignored_shifts = ' AND '.join((f"neu_kurz NOT ILIKE('{shift}')" for shift in ignored_shifts))
    sql_sickness_abbr = f'''
        SELECT neu_kurz as abbr, string_agg(sdienst_lang, ', ') as description FROM spxdb_archiv_2023.sdienst_mapping
        WHERE sdienst_lang ILIKE('%krank%') AND sdienst_lang NOT ILIKE('%nicht krank%') AND {sql_ignored_shifts}
        GROUP BY abbr
    '''
    
    sql_all_abbr = f'''
        SELECT neu_kurz as abbr, string_agg(sdienst_lang, ', ') as description FROM spxdb_archiv_2023.sdienst_mapping
        WHERE {sql_ignored_shifts}
        GROUP BY abbr
    '''
    
    # --------------------------------------------------------------------------
    # Inzidenz im EVB ----------------------------------------------------------
    
    def _sql_shifts_from_abbr(abbr: str) -> str:
        return f'''WITH mapping AS ({abbr})
            SELECT *
            FROM mapping JOIN spxdb_archiv_2023.monatsplan_adapted AS plan
            ON mapping.abbr = plan.sdienst_kurz_adapted
            WHERE plan.mpebene = 1 -- filter for "ist" (vs. e.g. "soll")
        '''
    sql_sickness_plan = _sql_shifts_from_abbr(sql_sickness_abbr)
    sql_all_plan = _sql_shifts_from_abbr(sql_all_abbr)
    
    def _counts(plan: str, name: str) -> pd.DataFrame:
        return read_sql(f'''
            WITH plan AS ({plan})
            SELECT
                DATE_TRUNC('week', (DATE '1990-01-01' + (tag_f * INTERVAL '1 day'))) AS "Kalenderwoche",
                COUNT(*) as "{name}"
             FROM plan GROUP BY "Kalenderwoche";
        ''')
    
    sickness_count = _counts(sql_sickness_plan, 'sick')
    all_count = _counts(sql_all_plan, 'all')
    
    evb = pd.merge(sickness_count, all_count, on='Kalenderwoche')
    evb['EVB'] = evb['sick'] / evb['all'] * 100000
    evb = evb.drop(columns=['sick', 'all'])
    
    return evb

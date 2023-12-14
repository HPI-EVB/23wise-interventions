from pandas import read_csv

def load_icd_mapping(file_path='src/icd10gm2023syst_kodes_20221206.txt'):
    column_names = [
    'classification_level', 'key_number_location', 'four_five_steller_type',
    'chapter_number', 'first_three_digits', 'full_key_number',
    'key_number_no_dash', 'key_number_no_dot', 'class_title',
    'three_digit_title', 'four_digit_title', 'five_digit_title',
    'usage_primary', 'usage_secondary', 'mortality_list_1', 'mortality_list_2',
    'mortality_list_3', 'mortality_list_4', 'morbidity_list', 'gender_association',
    'gender_error_type', 'lower_age_limit', 'upper_age_limit', 'age_error_type',
    'rare_disease_flag', 'key_number_content_flag', 'ifsg_notification_flag',
    'ifsg_labor_flag'
    ]

    icd_data = read_csv(file_path, delimiter=';', header=None, names=column_names)
    return icd_data
import pandas as pd

from cov19.model import CovidModel

# make prediction for input csv
feature_set = ['Patient age quantile',
               'Hematocrit',
               'Hemoglobin',
               'Platelets',
               'Mean platelet volume ',
               'Red blood Cells',
               'Lymphocytes',
               'Mean corpuscular hemoglobin concentration\xa0(MCHC)',
               'Leukocytes',
               'Basophils',
               'Mean corpuscular hemoglobin (MCH)',
               'Eosinophils',
               'Mean corpuscular volume (MCV)',
               'Monocytes',
               'Red blood cell distribution width (RDW)',
               'Serum Glucose',
               'Respiratory Syncytial Virus',
               'Influenza A',
               'Influenza B',
               'Parainfluenza 1',
               'CoronavirusNL63',
               'Rhinovirus/Enterovirus',
               'Coronavirus HKU1',
               'Parainfluenza 3',
               'Chlamydophila pneumoniae',
               'Adenovirus',
               'Parainfluenza 4',
               'Coronavirus229E',
               'CoronavirusOC43',
               'Inf A H1N1 2009',
               'Bordetella pertussis',
               'Metapneumovirus',
               'Parainfluenza 2',
               'Neutrophils',
               'Urea',
               'Proteina C reativa mg/dL',
               'Creatinine',
               'Potassium',
               'Sodium',
               'Influenza B, rapid test',
               'Influenza A, rapid test',
               'Alanine transaminase',
               'Aspartate transaminase',
               'Gamma-glutamyltransferase\xa0',
               'Total Bilirubin',
               'Direct Bilirubin',
               'Indirect Bilirubin',
               'Alkaline phosphatase',
               'Ionized calcium\xa0',
               'Strepto A',
               'Magnesium',
               'pCO2 (venous blood gas analysis)',
               'Hb saturation (venous blood gas analysis)',
               'Base excess (venous blood gas analysis)',
               'pO2 (venous blood gas analysis)',
               'Total CO2 (venous blood gas analysis)',
               'pH (venous blood gas analysis)',
               'HCO3 (venous blood gas analysis)',
               'Rods #',
               'Segmented',
               'Promyelocytes',
               'Metamyelocytes',
               'Myelocytes',
               'Myeloblasts',
               'Urine - Esterase',
               'Urine - Aspect',
               'Urine - pH',
               'Urine - Hemoglobin',
               'Urine - Bile pigments',
               'Urine - Ketone Bodies',
               'Urine - Density',
               'Urine - Urobilinogen',
               'Urine - Protein',
               'Urine - Leukocytes',
               'Urine - Crystals',
               'Urine - Red blood cells',
               'Urine - Hyaline cylinders',
               'Urine - Granular cylinders',
               'Urine - Yeasts',
               'Urine - Color',
               'Relationship (Patient/Normal)',
               'International normalized ratio (INR)',
               'Lactic Dehydrogenase',
               'Creatine phosphokinase\xa0(CPK)\xa0',
               'Ferritin',
               'Arterial Lactic Acid',
               'Lipase dosage',
               'Hb saturation (arterial blood gases)',
               'pCO2 (arterial blood gas analysis)',
               'Base excess (arterial blood gas analysis)',
               'pH (arterial blood gas analysis)',
               'Total CO2 (arterial blood gas analysis)',
               'HCO3 (arterial blood gas analysis)',
               'pO2 (arterial blood gas analysis)',
               'Arteiral Fio2',
               'Phosphor',
               'ctO2 (arterial blood gas analysis)']

if __name__ == '__main__':
    model = CovidModel('cov19model.joblib', feature_set)
    df = pd.read_csv('covid_test.csv')
    for row in df.to_dict('records'):
        try:
            print(model.predict(row))
        except TypeError as e:
            print(e)
import argparse

import pandas as pd

SELECTED_COLUMNS = ["Patient age quantile",
                    "Hematocrit",
                    "Hemoglobin",
                    "Platelets",
                    "Mean platelet volume ",
                    "Red blood Cells",
                    "Lymphocytes",
                    "Leukocytes",
                    "Basophils",
                    "Mean corpuscular hemoglobin (MCH)",
                    "Eosinophils",
                    "Mean corpuscular volume (MCV)",
                    "Monocytes",
                    "Red blood cell distribution width (RDW)",
                    "Serum Glucose",
                    "Respiratory Syncytial Virus",
                    "Influenza A",
                    "Influenza B",
                    "Parainfluenza 1",
                    "CoronavirusNL63",
                    "Rhinovirus/Enterovirus",
                    "Coronavirus HKU1",
                    "Parainfluenza 3",
                    "Chlamydophila pneumoniae",
                    "Adenovirus",
                    "Parainfluenza 4",
                    "Coronavirus229E",
                    "CoronavirusOC43",
                    "Inf A H1N1 2009",
                    "Bordetella pertussis",
                    "Metapneumovirus",
                    "Parainfluenza 2",
                    "Neutrophils",
                    "Urea",
                    "Proteina C reativa mg/dL",
                    "Creatinine",
                    "Potassium",
                    "Sodium",
                    "Influenza B, rapid test",
                    "Influenza A, rapid test",
                    "Alanine transaminase",
                    "Aspartate transaminase",
                    "Total Bilirubin",
                    "Direct Bilirubin",
                    "Indirect Bilirubin",
                    "Alkaline phosphatase",
                    "Strepto A",
                    "Magnesium",
                    "pCO2 (venous blood gas analysis)",
                    "Hb saturation (venous blood gas analysis)",
                    "Base excess (venous blood gas analysis)",
                    "pO2 (venous blood gas analysis)",
                    "Total CO2 (venous blood gas analysis)",
                    "pH (venous blood gas analysis)",
                    "HCO3 (venous blood gas analysis)",
                    "Rods #",
                    "Segmented",
                    "Promyelocytes",
                    "Metamyelocytes",
                    "Myelocytes",
                    "Myeloblasts",
                    "Urine - Esterase",
                    "Urine - Aspect",
                    "Urine - pH",
                    "Urine - Hemoglobin",
                    "Urine - Bile pigments",
                    "Urine - Ketone Bodies",
                    "Urine - Density",
                    "Urine - Urobilinogen",
                    "Urine - Protein",
                    "Urine - Leukocytes",
                    "Urine - Crystals",
                    "Urine - Red blood cells",
                    "Urine - Hyaline cylinders",
                    "Urine - Granular cylinders",
                    "Urine - Yeasts",
                    "Urine - Color",
                    "Relationship (Patient/Normal)",
                    "International normalized ratio (INR)",
                    "Lactic Dehydrogenase",
                    "Ferritin",
                    "Arterial Lactic Acid",
                    "Lipase dosage",
                    "Hb saturation (arterial blood gases)",
                    "pCO2 (arterial blood gas analysis)",
                    "Base excess (arterial blood gas analysis)",
                    "pH (arterial blood gas analysis)",
                    "Total CO2 (arterial blood gas analysis)",
                    "HCO3 (arterial blood gas analysis)",
                    "pO2 (arterial blood gas analysis)",
                    "Arteiral Fio2",
                    "Phosphor",
                    "ctO2 (arterial blood gas analysis)"]


def preprocess(df, include_target=False):
    # select columns
    if include_target:
        SELECTED_COLUMNS.append("SARS-Cov-2 exam result")
    df = df[SELECTED_COLUMNS]

    # dataprep categorical
    mask_pos_neg = {'positive': 1, 'negative': 0}
    mask_detected = {'detected': 1, 'not_detected': 0}
    mask_notdone_absent_present = {'not_done': 0, 'absent': 1, 'present': 2}
    mask_normal = {'normal': 1}
    mask_urine_color = {'light_yellow': 1, 'yellow': 2, 'citrus_yellow': 3, 'orange': 4}
    mask_urine_aspect = {'clear': 1, 'lightly_cloudy': 2, 'cloudy': 3, 'altered_coloring': 4}
    mask_realizado = {'Não Realizado': 0}
    mask_urine_leuk = {'<1000': 1000}
    mask_urine_crys = {'Ausentes': 1, 'Urato Amorfo --+': 0, 'Oxalato de Cálcio +++': 0,
                       'Oxalato de Cálcio -++': 0, 'Urato Amorfo +++': 0}

    df = df.replace(mask_detected)
    df = df.replace(mask_pos_neg)
    df = df.replace(mask_notdone_absent_present)
    df = df.replace(mask_normal)
    df = df.replace(mask_realizado)
    df = df.replace(mask_urine_leuk)
    df = df.replace(mask_urine_color)
    df = df.replace(mask_urine_aspect)
    df = df.replace(mask_urine_crys)

    df['Urine - pH'] = df['Urine - pH'].astype('float')
    df['Urine - Leukocytes'] = df['Urine - Leukocytes'].astype('float')
    df.fillna(999999, inplace=True)
    return df


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='input_file', help='path to input csv', action='store')
    parser.add_argument('-o', dest='output_file', help='path to output csv', default='preprocessed.csv', action='store')
    args = parser.parse_args()
    input_df = pd.read_csv(args.input_file)
    pre_processed_df = preprocess(input_df, include_target=True)
    pre_processed_df.to_csv(args.output_file, index=False)

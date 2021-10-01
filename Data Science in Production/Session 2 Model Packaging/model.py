from joblib import load


class MlModel:
    def __init__(self, path, feature_set):
        self.model = load(path)
        self.feature_set = feature_set

    def predict(self, data):
        self.validate_input(data)
        preprocessed_data = self.pre_process(data)
        return self.model.predict(preprocessed_data)

    @staticmethod
    def pre_process(data):
        return data

    @staticmethod
    def validate_input(data):
        pass


class CovidModel(MlModel):
    def pre_process(df):
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
        df = df.fillna(999)
        return df

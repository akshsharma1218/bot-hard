
import ktrain
def pred(que):
    predictor=ktrain.load_predictor(r'bert_model')
    return predictor.predict(que)
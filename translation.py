from transformers import AutoTokenizer, AutoModelForSequenceClassification
tokenizer = AutoTokenizer.from_pretrained("papluca/xlm-roberta-base-language-detection")
model = AutoModelForSequenceClassification.from_pretrained("papluca/xlm-roberta-base-language-detection")

from transformers import MBartForConditionalGeneration, MBartTokenizer
from transformers import MBart50TokenizerFast
class Translator:

    '''
        Install Requirements -
        pip install pickle5 transformers==4.12.2 sentencepiece
        MBart Documentation
        https://huggingface.co/transformers/model_doc/mbart.html
        Get the supported lang codes
        https://huggingface.co/facebook/mbart-large-50-one-to-many-mmt
        Class - Translator
        Initializes MBart Seq2Seq Model and Tokenizer
        Helper func to translate input language to desired target language
        Supported Languages: English, Gujarati, Hindi, Bengali, Malayalam, Marathi, Tamil, Telugu, Urdu
        
    '''

    def __init__(self):
        
        self.model = MBartForConditionalGeneration.from_pretrained('facebook/mbart-large-50-many-to-many-mmt')
        self.tokenizer = MBart50TokenizerFast.from_pretrained('facebook/mbart-large-50-many-to-many-mmt')
        self.supported_langs = ['en_XX', 'gu_IN', 'hi_IN', 'bn_IN', 'ml_IN', 'mr_IN', 'ta_IN', 'te_IN','ur_PK']

    def translate(self, input_text, src_lang, tgt_lang):

        if src_lang not in self.supported_langs:
            raise RuntimeError('Unsupported source language.')
        if tgt_lang not in self.supported_langs:
            raise RuntimeError('Unsupported target language.')

        self.tokenizer.src_lang = src_lang
        encoded_text = self.tokenizer(input_text, return_tensors='pt')
        generated_tokens = self.model.generate(**encoded_text, forced_bos_token_id=self.tokenizer.lang_code_to_id[tgt_lang])
        output_text_arr = self.tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)

        if len(output_text_arr) > 0:
            return output_text_arr[0]
        else:
            raise RuntimeError('Failed to generate output. Output Text Array is empty.')
#driver function
def translator(txt, lang):
    codes = {'Hindi':'hi_IN','Bengali':'bn_IN', 'Gujarati':'gu_IN','Malayalam':'ml_IN','Marathi':'mr_IN','Tamil':'ta_IN','Telugu':'te_IN','Urdu':'ur_PK'}
    lang_code = codes[lang]
    obj = Translator()
    translated_txt=obj.translate(txt,lang_code,'en_XX')
    return translated_txt
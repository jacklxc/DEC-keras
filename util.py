import re
import sent2vec

def clean_num(word):
    # check if the word contain number and no letters
    if any(char.isdigit() for char in word):
        try:
            num = float(word.replace(',', ''))
            return '<NUM>'
        except:
            if not any(char.isalpha() for char in word):
                return '<NUM>'
    return word

def clean_url(word):
    """
        Clean specific data format from social media
    """
    # clean urls
    word = re.sub(r'https? : \/\/.*[\r\n]*', '<URL>', word)
    word = re.sub(r'exlink', '<URL>', word)
    return word

def clean_words(str_seqs):
    processed_seqs = []
    for str_seq in str_seqs:
        processed_clauses = []
        for clause in str_seq:
            filtered = []
            tokens = clause.split()                 
            for word in tokens:
                word = clean_url(word)
                word = clean_num(word)
                filtered.append(word)
            filtered_clause = " ".join(filtered)
            processed_clauses.append(filtered_clause)
        processed_seqs.append(processed_clauses)
    return processed_seqs

def loadBioSent2VecModel(model_path):
    """
    Load bioSent2VecModel, which is ~ 20 GB.
    Input: model_path
    Returns: model object
    """
    model = sent2vec.Sent2vecModel()
    try:
        model.load_model(model_path)
        print('Model successfully loaded!')
    except Exception as e:
        print(e)
    return model
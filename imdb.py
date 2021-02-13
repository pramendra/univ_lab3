import os

def load_imdb():
    X_train = []
    y_train = []

    path = './aclImdb/train/pos/'
    X_train.extend([open(path + f, encoding='utf8').read() for f in os.listdir(path) if f.endswith('.txt')])
    y_train.extend([1 for _ in range(2000)])

    print("train positive reviews read")

    path = './aclImdb/train/neg/'
    X_train.extend([open(path + f, encoding='utf8').read() for f in os.listdir(path) if f.endswith('.txt')])
    y_train.extend([0 for _ in range(2000)])

    print("train negative reviews read")

    X_test = []
    y_test = []
    
    path = './aclImdb/test/pos/'
    X_test.extend([open(path + f, encoding='utf8').read() for f in os.listdir(path) if f.endswith('.txt')])
    y_test.extend([1 for _ in range(2000)])

    print("test positive reviews read")

    path = './aclImdb/test/neg/'
    X_test.extend([open(path + f, encoding='utf8').read() for f in os.listdir(path) if f.endswith('.txt')])
    y_test.extend([0 for _ in range(2000)])

    print("test negative reviews read")
    
    return (X_train, y_train), (X_test, y_test)
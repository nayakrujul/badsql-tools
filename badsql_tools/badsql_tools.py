import argparse, badsql

def mkdb():
    parser = argparse.ArgumentParser(prog ='badsql',
                                     description ='badsql mkdb')
  
    parser.add_argument('headers', metavar ='headers', type=str, nargs='*', help ='headers')

    args = parser.parse_args()

    db = badsql.db(list(args.headers))
    db.display()
    db.save('test')

def insertrow():
    parser = argparse.ArgumentParser(prog ='badsql',
                                     description ='badsql insertrow')

    parser.add_argument('pos', metavar ='pos', type=int, nargs=1, help= 'pos')
  
    parser.add_argument('values', metavar ='values', type=list, nargs='*', help ='values')

    args = parser.parse_args()

    try:
        db = badsql.load('test')
        db.insert(args.pos[0], [''.join([str(x) for x in y]) for y in args.values])
        db.display()
        db.save('test')
    except Exception as e:
        print('Error occurred:', e)

def select():
    parser = argparse.ArgumentParser(prog ='badsql',
                                     description ='badsql select')
    parser.add_argument('query', metavar ='query', type=str, nargs=1, help= 'query')

    parser.add_argument('save', metavar ='save', type=bool, nargs='?', const=False, help= 'save')

    args = parser.parse_args()

    try:
        db = badsql.load('test')
        new_db = db.select(args.query[0])
        new_db.display()
        if args.save:
            new_db.save('test')
    except Exception as e:
        print('Error occurred:', e)

def display():
    try:
        badsql.load('test').display()
    except Exception as e:
        print('Error occurred:', e)

def removerow():
    parser = argparse.ArgumentParser(prog ='badsql',
                                     description ='badsql removerow')

    parser.add_argument('pos', metavar ='pos', type=int, nargs=1, help= 'pos')

    args = parser.parse_args()

    try:
        db = badsql.load('test')
        db.delete(args.pos[0])
        db.display()
        db.save('test')
    except Exception as e:
        print('Error occurred:', e)
        

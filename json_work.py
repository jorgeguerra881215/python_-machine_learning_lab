import json

def init():
    path = 'data/example.txt'
    records = [json.loads(line) for line in open(path)]
    return records




if __name__ == "__main__":
    output = init()
    print output[0]
    print '//////'
    print output[0]['g']
    print 'finish'
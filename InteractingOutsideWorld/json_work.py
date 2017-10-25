import json

def read_json_and_build_object():
    path = 'data/example.txt'
    records = [json.loads(line) for line in open(path)]
    return records

#Using simple python library (Harder Way)
from collections import defaultdict
def get_most_often_attribute(attribute, n = 10):
    data = read_json_and_build_object()
    item_list = [item[attribute] for item in data if attribute in item]
    count_dict = defaultdict(int) #values will initialize to 0
    for x in item_list:
        count_dict[x] += 1
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]

#Using simple python library (Harder Way)
from collections import Counter
def get_most_often_attribute_2(attribute, n = 10):
    data = read_json_and_build_object()
    item_list = [item[attribute] for item in data if attribute in item]
    counts = Counter(item_list)
    return counts.most_common(n)



#Using Pandas (more easy way)
import pandas as pd
from pandas import DataFrame, Series
def get_most_often_attribute_pandas(attribute, n = 10):
    data = read_json_and_build_object()
    data_frame = DataFrame(data)
    counts_attribute = data_frame[attribute].value_counts()
    return counts_attribute[:n]

if __name__ == "__main__":
    output_object = read_json_and_build_object()
    print output_object[0]
    print output_object[0]['tz']

    print '\n'
    more_often = get_most_often_attribute_2('tz')
    print more_often

    print '\n'
    print get_most_often_attribute_pandas('tz')
    print '//////'
    #print output_object[0]['g']
    print 'finish'
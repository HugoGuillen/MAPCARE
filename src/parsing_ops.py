import os
from os import path,listdir
import pandas as pd
import re
import networkx as nx
import xml.etree.ElementTree as ET

def parse_ops(input_xml, abbv_path,output_parsed):
    tree = ET.parse(input_xml)
    root = tree.getroot()
    G = nx.DiGraph()
    labels = {'root':'root'}
    ROOT = 'root'
    # Parse through each 'Modifier' element
    for _class in root.findall('Class'):
        code = _class.get('code')        
        superclasses = _class.findall('SuperClass')
        if len(superclasses)==0:        
            superclass=ROOT
        else:
            superclass = superclasses[0].get('code')        
        for label in _class.findall(".//Rubric[@kind='preferred']/Label"):
            text = label.text.strip() if label.text else ""
            if superclass==ROOT:
                text = text.lower()
            # print(code,text)
        G.add_node(code)
        if superclass is not None:
            G.add_edge(superclass,code)
        labels[code] = text

    rows = []
    # leaves = [x for x in G.nodes() if G.out_degree(x)==0 and G.in_degree(x)==1]
    leaves = [x for x in G.nodes()]
    for leaf in leaves:    
        s = ': '.join([labels[x] for x in nx.shortest_path(G,source=ROOT,target=leaf) if x!=ROOT])
        rows.append((leaf,s))    
    df = pd.DataFrame(rows,columns=['code','label'])
    # df.to_csv(output_parsed,index=None,encoding='utf-8-sig')
    # print('# Wrote',output_parsed)

    abb = pd.read_csv(abbv_path,sep='\t',comment='#',header=None)
    abb.columns = ['x','y']
    abb_dict = abb.set_index('x')['y'].to_dict()
    abb_sorted = sorted(abb_dict.keys(),key=lambda x:-len(x))

    def substitute_abbv(x,prefix='',suffix=''):
        for a in abb_sorted:
            a2 = prefix+a+suffix
            x = x.replace(a2,prefix+abb_dict[a]+suffix)
        return x

    # df = pd.read_csv(input_parsed,encoding='utf-8-sig')
    df = df[df['code']!='root']    

    df['label'] = df['label'].apply(lambda x:substitute_abbv(x,prefix=' ',suffix=' '))
    df['label'] = df['label'].apply(lambda x:substitute_abbv(x,prefix=' ',suffix=''))
    df['label'] = df['label'].apply(lambda x:substitute_abbv(x,prefix='',suffix=' '))
    df['label'] = df['label'].apply(lambda x:substitute_abbv(x,prefix='[',suffix=''))
    df['label'] = df['label'].apply(lambda x:substitute_abbv(x,prefix='',suffix=']'))

    df.to_csv(output_parsed,index=None,encoding='utf-8-sig')
    print('# Wrote',output_parsed)
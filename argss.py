'''




optional arguments lai -- or - ko use garinxa



varibale lai short form ma use garna - sign ko use garina

aani full length ma use garna -- ko use garinxa
'''

from argparse import ArgumentParser

parser=ArgumentParser()


parser.add_argument('-x','--x_value',action='store_true')

'''
note here -x vanda paxadi value dinu pardaina as given

action=store_true

so time -x lekhni bittikai x_value ma true gaye ra basdinxa

note --x_value ni dina milxa 

so python argss.py -x or --x_value




'''

args=parser.parse_args()

#note x.full name chai use garni
print(args.x_value)


#yo aailae -x lekhae true huni teso wala lai verbose vaninxa
#yo enable vaya paxi certain feature dini testo hunxa
#x==v and x_value==verbose



'''
yo optional arguments aagaadi diye ni hunxa paxadi diyae ni hunxa 

meaning

 python argss.py 1 -x 8 2 3 4

vanna khojae ko x ko avlue 2 ho aani yo optional ho aani yo jaa dida ni hunxa
optional ho vanae ra chinna ko lagi - or -- use vako hunxa





'''
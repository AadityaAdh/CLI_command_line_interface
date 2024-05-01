'''

CLI vanae ko command line interface ho

yedi command line aathawa terminal bata kei command diyinxa instead of
any forms of GUI vanae tellai CLI vaninxa

basic example in PIP command in python

another is doing various git operations from terminal

so to create CLI we use argparse library

aaba CLI lai function ko rup ma bhujam

as we have function_name(arguments)

vanya jastai gari

CLI ma pani terminal bata testai khal ko operation hunxa

filename arg1,arg2    yesari diyinxa terminal bata CLI commands

'''



from argparse import ArgumentParser


#creating object of Argument parser
parser=ArgumentParser()

'''
aaba yo file lae k k argument linxa tyo specfy garnu parxa

'''


parser.add_argument('number1',help='First no to be entered for addition')


#aaba yo number lai access garni tarika

#user_passed_args=parser.parse_args()


#aaba tyo specific argument access garna

#print(user_passed_args.number1)

#yo run garnauna aaru jasto mathi run button ma hichni haina
#terminal ma jani aani
#python main.py your_argument value
#so you can do like
#python main.py 1
#then it will output 1



'''
aaba tyo pathako inter ko data type

malai integer nai chainxa natra accept gardina vanna ko lagi

tyo argument vitra type=int


'''
parser.add_argument('my_value',type=int)

#aaba python main.py 1(yo chai mathi ko argument ho ) aaab
#garyo vanae error aauxa invalid int value vanxa
#tara tesko thau ma 4 diyo vanae milxa

#argumentss=parser.parse_args()


'''
yedi kunai CLI lae k k argument linxa tha xaina vanae

filename paxadi -h or -help gare paxi dinxa
so python main.py -h
'''


'''

note python main.py mara gare pani run hunxa

maening these positional argument are not always required

unless we do required=True in add_argument statement



'''





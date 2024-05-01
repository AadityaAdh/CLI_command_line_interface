from argparse import ArgumentParser

parser=ArgumentParser()



parser.add_argument('num1')
parser.add_argument('num2')
parser.add_argument('-o','--operation')

args=parser.parse_args()


print(args.num1)
print(args.operation)
print(args.num2)




'''
basically positional argument ko order matter garxa

optional argument chai positioional ko bich bich ma ghusayae ni hunxa
optional dini tarika vanae ko - or -- le

so simply in tester.py

terter.py 1 -o add 2 and tester.py 1 2 -o add gives same result


'''
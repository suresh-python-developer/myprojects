import pandas

alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")


new_dic = {row.letter:row.code for (index,row)in alphabets.iterrows()}
print(new_dic)
def phonetic():
    word = input("enter the word : ").upper()
    try:
        output = new_list = [new_dic[letter] for letter in word]
    except KeyError:
        print("sorry the enter only alphabet")
        phonetic()
    else:
        print(output)
phonetic()
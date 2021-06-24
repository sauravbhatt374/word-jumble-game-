import random

if __name__=='__main__':
    #open the txt file containg all the words   
    with open("words.txt", "r") as file:
        data = file.read() #read the file
        words = data.split()
    #selecting a random word from the txt file
        word = random.randint(0, len(words)-1)
        main_word= (words[word].upper())
        #main_word will be jumbled
        # print(main_word)
        #coverting the main_word to list to shuffle it
        list_main=list(main_word)
        random.shuffle(list_main)
    #reconverting list_main though it was not necessory 
        for x in range(len(list_main)):
            print(list_main[x],end=" ")
            jumbled_word=(words[word].upper())
    
    print(' \nYou got Five turns')
    for i in range(0,5):
        guess_user=str(input('Guess the word \n').upper())
        if guess_user==main_word:
            print(guess_user, 'is the right answer')
            break
        elif guess_user!=main_word:
            print(' Wrong Guess \n')
        else:
            pass
    if guess_user!=main_word:
        print(guess_user,' is the wrong guess try again')
        print(main_word,' is the correct answer' )

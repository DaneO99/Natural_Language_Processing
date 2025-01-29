import re
import os

########################################################################################
# Function definitions                                                                 #
########################################################################################

#Function to print out the song
#If the value is "True," the word has been guessed- display it
#Otherwise, the word has not been guessed- display a blank for each letter
def print_song(song):
  for word in song:
    if word[1] == True:
      print(word[0], end = " ")
    else:
      for char in word[0]:
        print("_", end = "")

      print(end = " ")

#Function to check the user's guess against each word in the song list
#Use regex to ignore capitalization and strip punctuation
#If the guess is in the song, set the value to "True" to display word
def guess_word(guess, song):
  for word in song:
    temp = re.sub(r'\W', '', word[0])
    if temp.casefold() == guess.casefold():
      word[1] = True

#Function to check if all words have been guessed
#Loop through each word in song list, if any of them are still "False"
#there are still unguessed words, need to keep going
def play_again(song):
  flag = False

  for word in song:
    if word[1] == False:
      flag = True

  return flag

########################################################################################
# Main gameplay                                                                        #
########################################################################################
song = []

#Read in each word from the song and append to the list
#In the beginning all words are set to "False" as nothing has been guessed
with open("TennesseWhiskey.txt",'r') as file:   
  for line in file:        
    for word in line.split():
      song.append([word, False])

#Print initial gameplay board
print_song(song)
print()
flag = True

#Loop to repeatedly get user guess, check if in song, and print updated gameplay board
#Break out when all words are guessed
while flag:
  guess = input("Guess a word: ")
  guess_word(guess, song)

  os.system('clear')
  print_song(song)
  print()

  flag = play_again(song)


{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "187885e9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "def hangman():\n",
    "    word=random.choice([\"turtle\", \"garfield\", \"alligator\", \"headphones\", \"wedding dress\", \"violin\",\"newspaper\", \"raincoat\", \"chameleon\",\"cardboard\", \"oar\", \"drip\", \"shampoo\", \"timemachine\", \"yardstick\", \"think\", \"lace\", \"darts\", \"avocado\", \"bleach\",\"curtain\", \"extensioncord\", \"dent\", \"birthday\", \"lap\", \"sandbox\", \"bruise\", \"fog\", \"sponge\", \"wig\", \"pilot\", \"mascot\", \"fireman\", \"zoo\", \"sushi\", \"fizz\", \"ceiling\", \"postoffice\", \"season\", \"internet\"])\n",
    "    validletters='abcdefghijklmnopqrstuvwxyz'\n",
    "    attempts=10\n",
    "    guessmade=''\n",
    "    while len(word)>0:\n",
    "        main=\"\"\n",
    "        missed=0\n",
    "        for letters in word:\n",
    "            if letters in guessmade:\n",
    "                main=main+letters\n",
    "            else:\n",
    "                main=main+\"_\"+\" \"\n",
    "        if main==word:\n",
    "            print(main)\n",
    "            print(\"Wohooo!! You won.\")\n",
    "            break\n",
    "        print(\"Guess the word:\",main)\n",
    "        guess=input()\n",
    "        if guess in validletters:\n",
    "            guessmade=guessmade+guess\n",
    "        else:\n",
    "            print('Enter a valid character!')\n",
    "            guess=input()\n",
    "        if guess not in word:\n",
    "            attempts=attempts-1\n",
    "            if attempts==9:\n",
    "                print(\"9 attempts left\")\n",
    "                print(\"--------\")\n",
    "            if attempts==8:\n",
    "                print(\"8 attempts left\")\n",
    "                print(\"--------\")\n",
    "                print(\"    0   \")\n",
    "            if attempts==7:\n",
    "                print(\"7 attempts left\")\n",
    "                print(\"--------\")\n",
    "                print(\"    0   \")\n",
    "                print(\"    |   \")\n",
    "            if attempts==6:\n",
    "                print(\"6 attempts left\")\n",
    "                print(\"--------\")\n",
    "                print(\"    0   \")\n",
    "                print(\"    |   \")\n",
    "                print(\"   /    \")\n",
    "            if attempts==5:\n",
    "                print(\"5 attempts left\")\n",
    "                print(\"--------\")\n",
    "                print(\"    0   \")\n",
    "                print(\"    |   \")\n",
    "                print(\"   / \\  \")\n",
    "            if attempts==4:\n",
    "                print(\"4 attempts left\")\n",
    "                print(\"--------\")\n",
    "                print(\"   \\0   \")\n",
    "                print(\"    |   \")\n",
    "                print(\"   / \\  \")\n",
    "            if attempts==3:\n",
    "                print(\"3 attempts left\")\n",
    "                print(\"--------\")\n",
    "                print(\"   \\0/  \")\n",
    "                print(\"    |   \")\n",
    "                print(\"   / \\  \")\n",
    "            if attempts==2:\n",
    "                print(\"2 attempts left\")\n",
    "                print(\"--------\")\n",
    "                print(\"--------\")\n",
    "                print(\"   \\0/| \")\n",
    "                print(\"    |   \")\n",
    "                print(\"   / \\  \")\n",
    "            if attempts==1:\n",
    "                print(\"1 attempts left\")\n",
    "                print(\"Last Breathe Counting....\")\n",
    "                print(\"--------\")\n",
    "                print(\"--------\")\n",
    "                print(\"  |\\0/| \")\n",
    "                print(\"    |   \")\n",
    "                print(\"   / \\  \")\n",
    "            if attempts==0:\n",
    "                print(\"0 attempts left\")\n",
    "                print(\"You lost the game. You let a kind man die.\")\n",
    "                break\n",
    "            \n",
    "\n",
    "name= input(\"Enter the player name:\")\n",
    "print(\"Welcome to the game \"+name)\n",
    "print(\"-----------------------------\")\n",
    "print(\"Try to catch the word in less than 10 attempts\")\n",
    "hangman()\n",
    "print()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c35d7597",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "53aed269",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

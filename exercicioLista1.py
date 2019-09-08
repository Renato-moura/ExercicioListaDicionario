{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "1 Faça um programa que decide se duas listas são iguais. Duas listas são iguais se possuem os mesmos valores e na mesma ordem."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "listas diferentes\n"
     ]
    }
   ],
   "source": [
    "lista = [1,2,3,4,5,6]\n",
    "lista2 = [1,2,3,4,5,7]\n",
    "\n",
    "if len(lista) == len(lista2):\n",
    "    for i in lista:\n",
    "        if iguais == 1:\n",
    "            if lista[i-1] == lista2[i-1]:\n",
    "                #print (\"lista iguais\")\n",
    "                iguais = 1\n",
    "            else:\n",
    "                #print (\"listas diferentes\")\n",
    "                iguais = 0\n",
    "else:\n",
    "    print(\"lista diferentes\")\n",
    "\n",
    "if iguais == 0:\n",
    "    print(\"listas diferentes\")\n",
    "elif iguais == 1:\n",
    "    print(\"lista iguais\")"
   ]
  },
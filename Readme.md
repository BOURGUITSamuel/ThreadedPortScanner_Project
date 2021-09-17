# Python3-PortScanner
Scanner de port Python utilisant le multithreading.

# Getting Started
Un scanner de ports est simplement un script qui essaie d'�tablir une connexion avec un p�riph�rique via une liste de ports, de cette mani�re nous pouvons voir quels ports sont ouverts sur un p�riph�rique.
Il s'agit d'un simple script de scanner de port multithread r�alis� avec python, car il faut au moins une seconde pour v�rifier si un port est ouvert ou ferm� en raison de la n�cessit� d'attendre le d�lai d'attente pour v�rifier s'il est ferm� ou si le retard est caus� par un retard de connexion, ce script vous permet de choisir combien de threads vous souhaitez utiliser pour le scan, l'avantage d'utiliser plusieurs threads est que chaque thread serait capable de scanner diff�rents ports en m�me temps
# Prerequisites
Le programme peut �tre ex�cut� sur un syst�me d'exploitation Windows(en utilisant un IDE ou la version windows de python) ou Linux.

Le programme a �t� con�u avec le langage Python (version3).

le module python 'colorama' est requis : https://pypi.org/project/colorama/

le module python 'pyfiglet' est requis :  https://pypi.org/project/pyfiglet/#description

# Installing & Using
1- Copiez le fichier dans le r�pertoire de votre choix.

2- Lancez le programme avec la commande suivante : python ThreadedPortScanner.py.py

3- Vous pouvez appliquer vos propres param�tres en modifiant le script.

# Running the tests
Le programme a �t� con�u dans un environnement de d�veloppement int�gr�(IDE) sur l'OS Windows 10 64Bits.

Le programme a �t� test� sur l'OS Debian 64bits.
# Versioning
Version 1.0

# Authors
Jean - Samuel BOURGUIT Administrateur Infrastuture et Cloud

# License
    Apache License
    Version 2.0, January 2004
    http://www.apache.org/licenses/
https://www.apache.org/licenses/LICENSE-2.0.txt
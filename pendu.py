#coding:utf-8
from random import randrange
def menu():
	print("Bienvenue dans pendu\n1-Appuie 1 pour voir l'aide\n2-Appuie 2 pour jouer")
	while 1:
		choix=input("Ton choix: ")
		if choix!='1' and choix!='2':
			print("Valeur du choix incorrecte")
			continue
		elif choix=='1' or choix=='2':
			if choix=='1':
				print("------------------Bienvenue---------------------\n---------------------AIDE----------------------------\nL'ordinateur choisit un mot au hasard dans une liste, un mot de huit lettres maximum. Le joueur tente de trouver les lettrescomposant le mot. À chaque coup, il saisit une lettre. Si la lettre figure dans le mot, l'ordinateur affiche le mot avec les lettres déjà trouvées. Celles qui ne le sont pas encore sont remplacées par des étoiles (*). Le joueur a 8 chances. Au delà, il a perdu.")
				menu()
				break
			elif choix=='2':
				jeu()
				break
def jeu():
	continuer_partie=0
	while 1:
		if continuer_partie==1:
			break
		try:
			fichier=open("fichierpendu","r")
			contenu=fichier.readlines()
			fichier.close()
			continuer_partie=0
			while continuer_partie==0:
				mot_a_deviner=contenu[randrange(len(contenu))]
				mot_a_deviner=mot_a_deviner.replace('\n','')
				score=len(mot_a_deviner)
				chaine=str()
				i=0
				while i<len(mot_a_deviner):
					chaine+='*'
					i+=1
				i=0
				while chaine!=mot_a_deviner and score>=1:
					print("Le mot a deviner est: {}".format(chaine))
					caractere="par"
					while len(caractere)!=1:
						try:
							caractere=input("Donner une lettre du mot: ")
						except:
							pass
					nbre=mot_a_deviner.upper().find(caractere.upper())
					if nbre!=-1:
						copie_chaine=chaine
						chaine=str()
						i=0
						while i<len(mot_a_deviner):
							if  mot_a_deviner.upper()[i]==caractere.upper():
								chaine+=mot_a_deviner[i]
							else:
								chaine+=copie_chaine[i]
							i+=1
					else:
						score=score-1
				if score>=1:
					print("----------------Bravo tu as trouvé le mot à dévinner et ton score est {}.\nLe mot a deviner est bien: {}".format(score,mot_a_deviner))
				elif score==0:
					print("---------------------Tu as perdu..Le mot était: {}".format(mot_a_deviner))
				print("---------------->Continuer(o/n)?")
				choix=input("Votre choix: ")
				while choix!='o' and choix!='n':
					choix=input("Votre choix: ")
				if choix=='o':
					continuer_partie=0
				else:
					continuer_partie=1
		except:
			fichier=open("fichierpendu","w")
			fichier.write("Papa\nMaman\nTata\nAudrey\nYasmine\nDavid\nDaniel")
			fichier.close()
"""def inserer_score(nom,score):
	insertion=0
	while insertion==0:
		try:
			fichier=open("score","r")
			while fichier.readline():
				if fichier.readline().find(nom):
					i=fichier.readline().find(nom)
					while fichier.readline()[i]!=':':
						i+=1
					i+=1
					score_precedant=str()
					while fichier.readline()[i]!='\n':
						score_precedant+=fichier.readline()[i]
					score_precedant=int(score_precedant)
					score_precedant+=score
					fichier.close()
					fichier=open("score","w")

			fichier.close()
		except:
			fichier=open("score","w")
			fichier.close()"""
menu()

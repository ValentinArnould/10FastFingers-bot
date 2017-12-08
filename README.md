# 10FastFingers-bot

Petit bot pour exploser vos records sur 10FastFingers  
  
Voici un petit programme développé sous sikuliX (version 1.1.1 pour moi)  
  
Il permet de faire des records de frappe sur ce site:  
https://10fastfingers.com/typing-test/french  
  
Testé sur le français, je pense qu'il fonctionne sous toute langue  
  
Pré requis:  
Télécharger SikuliX (le setup.jar suffit)  
Le programme ne gère pas la préparation,  
vous devez générer un test, et copier le contenu   
de la &lt;div&gt; contenant les mots, le coller dans un bloc note,  
et supprimer les syntaxes :  
&lt;span wordnr="  
" class="highlight"&gt;  
" class=""&gt;  
  
ainsi que remplacer &lt;/span&gt;_ par ! (_ est un espace, à inclure)  
dans SikuliX, vous devrez reprendre les screenshots de reconnaissance pour le bot :  
Un pour accéder au bloc note (il ne doit effectuer qu'un seul clic et pouvoir tout copier)  
Un pour accéder à la page de 10fastfingers  
Un pour sélectionner la barre d'écriture du test  
  
Vous pouvez dé-commenter la fonction sleep à la fin du programme, afin que le bot ne finisse  
pas trop vite le test (sans sleep, le bot finit la liste de mots avec 17 secondes d'avance)  
Il faut refaire la liste de mots dans le bloc note à chaque génération de test  
Prendre des screenshots plus gros pour que le bot les reconnaisse bien (un élément qui ne change pas)  
Eviter de cacher les endroits que le bot doit reconnaître

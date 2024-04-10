# TER - signatures et isomorphismes

Dans le cadre de notre TER, nous avons choisi un sujet d'algorithmique. Le but de notre projet est de comparer plusieurs méthodes de génération de signatures pour des graphes planaires (3-connexes). Nous avons implémenté l’algorithme classique de raffinement de
partitions de Tarjan ainsi qu'un algorithme «naïf». Nous souhaitons obtenir les implémentations les plus rapides possibles de ces deux algorithmes afin de comparer leurs performances entre elles d'une part, mais également avec des méthodes plus générales comme celle de «nauty and traces».

## Utilisation

Nous aimerions pouvoir lancer toutes nos commandes depuis une interface graphique. Pour ce faire il suffira d'exécuter la commande suivante : 
```
python src/main.py
```

## Organisation

Notre avons organisé notre travail en trois répertoires : 
- FichierTests
- Graphiques
- src

### FichierTests

Le répertoire contient des graphes planaires 3-connexes que nous avons générés grâce à l'algorithme plantri.
Les fichiers dont le nom commence par «graph» sont issus de la représentation ASCII de plantri.
```
./plantri -p -a V graphN.txt
```
 Les fichiers dont le nom commence par « ex » sont issus de la représentation binaire de plantri (binary code).
```
./plantri -p V graph.V
```
Ces commandes ont été lancées depuis un terminal. Par convention, plantri génère des graphes 3-connexes. L'ajout de l'option ``-p`` permet de spécifier qu'ils doivent être planaires simples. Plantri ajoute tous les graphes planaires 3-connexes de taille N aux fichiers spécifiés. Il nous a donc fallu les traiter pour obtenir les graphes suivants (un par fichier).

Voir [Documentation plantri](https://users.cecs.anu.edu.au/~bdm/plantri/plantri-guide.txt) pour davantage de précision.

### Graphiques

Le répertoire contient des graphiques représentant en moyenne le temps d'exécution d'un des algorithmes de signature en fonction du nombre de sommets du graphe. 

### src

Le fichier source contient les méthodes que nous avons implémentées. 

**Utilitaires**

Le fichier 

**Complexité**

 ``complexite.py`` permet de générer les graphiques dont nous venons de parler dans la section précédente. Pour l'algorithme de partitionnement de Tarjan, la complexité attendue est en $V\log(V)$, où $V$ est le nombre de sommets du graphe. Pour l'algorithme naïf, la complexité attendue est en $A^3$, où $A$ est le nombre d'arêtes du graphe.





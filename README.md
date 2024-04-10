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

### SRC

Le répertoire source contient les méthodes que nous avons implémentées. 

**Utilitaires**

Le fichier ``Utils.py`` comprend les méthodes permettant de lire les fichiers de graphe planaire pour les utiliser par la suite dans nos algorithmes, une méthode permettant de générer des isomorphes à partir d'un graphe, ainsi qu'une méthode permettant de visualiser le graphe. 

**Signature Naïve**

Nous avons commencé par implémenter un algorithme de génération de signatures peu efficace, d'où l'appellation naïve  : ``SignatureNaive.py``. Il repose sur le parcours en profondeur des arêtes du graphe, en prenant successivement l'arête la plus à droite de l'arête que l'on traite par convention. Ce parcours est effectué autant de fois qu'il y a d'arêtes non orientées (elles correspondent à l'arête initiale du parcours). On renomme ensuite les sommets pour ces parcours. La signature correspond au parcours le plus petit (en taille et dans l'ordre alphabétique). 

**Signature Tarjan**

Cette version de l'algorithme de signature correspond à celle imaginée par Tarjan, reposant sur le partitionnement des arêtes selon certains critères.
Cette version de l'algorithme de signature correspond à celle imaginée par Tarjan, reposant sur le partitionnement des arêtes selon certains critères : `` SignatureVlogV.py`` et ``DefineLambda.py``. Nous nous sommes appuyées sur son article de recherche «J.E. Hopcroft and R.E. Tarjan. A V log V algorithm for isomorphism of triconnected planar graphs».



**Complexité**

 ``complexite.py`` permet de générer les graphiques dont nous venons de parler dans la section précédente. Pour l'algorithme de partitionnement de Tarjan, la complexité attendue est en $V\log(V)$, où $V$ est le nombre de sommets du graphe. Pour l'algorithme naïf, la complexité attendue est en $A^3$, où $A$ est le nombre d'arêtes du graphe.

**Isomorphisme**

Pour savoir si deux graphes sont isomorphes, nous comparons leur signature issue d'un de nos algorithme : ``Isomorphisme.py``.

**Interface Graphique**

``main.py``

><span style="color:orange">⚠️ Warning</span>
>
> L'interface graphique n'est pas encore utilisable !




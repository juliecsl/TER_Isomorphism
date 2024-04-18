# TER - signatures et isomorphismes
*Réalisé par Julie CIESLA et Pauline HOSTI*
![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

Dans le cadre de notre Travail d'Étude et de Recherche (TER), nous avons choisi un sujet d'algorithmique. Notre objectif principal est de comparer diverses méthodes de calcul d'isomorphisme de graphes planaires en utilisant la génération de signatures. Pour cela, nous avons mis en œuvre deux approches principales : l'algorithme classique de raffinement de partitions de Tarjan et une méthode plus simple que nous qualifions de « naïve ». 

Notre but étant d'obtenir les performances les plus élevées possibles et de comparer ces deux approches entre elles d'une part, mais également avec des méthodes plus générales comme celles de "nauty" et "traces".

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
## 📑 Manuel utilisateur

Nous aimerions pouvoir lancer toutes nos commandes depuis une interface graphique. Pour ce faire il suffira d'exécuter la commande suivante : 
```
python src/main.py
```

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
## 🛠️ Manuel technique

### Prérequis 
 - **Système Unix** du fait de l'utilisation de la librairie pynauty.
 - **Python**: 3.11

### Librairies
 - **pynauty**: 2.8.6
 - **pandas**: 2.2.2
 - **networkx**
 - **matplotlib**: 3.8.4

 Pour installer une librairie faire
 ```
pip install <nom librairie>
```


### Organisation

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

Nous avons commencé par implémenter un algorithme de génération de signatures peu efficace, d'où l'appellation naïve  : ``SignatureNaive.py``. Il repose sur le parcours en profondeur des arêtes du graphe, en prenant successivement l'arête la plus à droite de l'arête que l'on traite par convention. Ce parcours est effectué autant de fois qu'il y a d'arêtes orientées (elles correspondent à l'arête initiale du parcours). On renomme ensuite les sommets pour ces parcours. La signature correspond au parcours le plus petit (en taille et dans l'ordre alphabétique). 

**Signature Weinberg**

Il s'agit de l'algorithme de signature imaginée par Weinberg. Il repose sur les parcours eulérien du graphe. Ce parcours est effectué autant de fois qu'il y a d'arêtes orientées (elles correspondent à l'arête initiale du parcours). On renomme ensuite les sommets pour ces parcours. La signature correspond au parcours le plus petit (en taille et dans l'ordre alphabétique). 

**Signature Tarjan**

Cette version de l'algorithme de signature correspond à celle imaginée par Tarjan, reposant sur le partitionnement des arêtes selon certains critères.
Cette version de l'algorithme de signature correspond à celle imaginée par Tarjan, reposant sur le partitionnement des arêtes selon certains critères : `` SignatureVlogV.py`` et ``DefineLambda.py``. Nous nous sommes appuyées sur son article de recherche «J.E. Hopcroft and R.E. Tarjan. A V log V algorithm for isomorphism of triconnected planar graphs».

**Nauty**

Nous avons réalisé un fichier à part, ``Nauty.py``, pour gérer la bibliothèque ``pynauty`` accessible seulement depuis une machine Unix. Ce fichier contient les méthodes nous permettant d'effectuer le calcul de signature découvert par Brendan D.McKay sur nos exemples. 

**Isomorphisme**

Pour savoir si deux graphes sont isomorphes, nous comparons leur signature issue d'un de nos algorithme : ``Isomorphisme.py``.

**Complexité**

 ``complexite.py`` permet de générer les graphiques dont nous venons de parler dans la section précédente. Pour l'algorithme de partitionnement de Tarjan, la complexité attendue est en $V\log(V)$, où $V$ est le nombre de sommets du graphe. Pour l'algorithme naïf, la complexité attendue est en $V^2$, où $V$ est le nombre d'arêtes du graphe.

**Interface Graphique**

``main.py``

><span style="color:orange">⚠️ Warning</span>
>
> L'interface graphique n'est pas encore utilisable !

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)
## 📂 Contenu du projet

```
.
├── 1-FichierTests
│   ├── ex5_1.txt
│   ├── ...
│   └── graph30_2ISO.txt
├── 2-Graphique
│   ├── ToutISO.png
│   ├── ...
│   └── ...
├── 3-src
│   ├── SignatureNaive.py
│   ├── SignatureVlogV.py
│   └── ...
├── .gitignore
└── README.md
```




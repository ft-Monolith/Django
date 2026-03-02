#!/bin/sh

# curl -s -I "$1"
#   -s (silent)    : Désactive la barre de progression de curl
#   -I (head)      : Récupère seulement les en-têtes HTTP, pas le contenu
#   "$1"           : Premier argument passé au script (l'URL bit.ly)
#
# grep "Location:"
#   Filtre les lignes qui contiennent "Location:" (l'en-tête de redirection HTTP)
#
# cut -d' ' -f2-
#   -d' '          : Utilise l'espace comme délimiteur
#   -f2-           : Extrait du champ 2 jusqu'à la fin (l'URL réelle du lien)

curl -s -I "$1" | grep -i "Location:" | cut -d' ' -f2-

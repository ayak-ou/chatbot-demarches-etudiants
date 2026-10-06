# Chatbot démarches administratives pour étudiants internationaux

Assistant conversationnel qui guide les étudiants internationaux de l'ENSICAEN 
dans leurs démarches administratives en France : titre de séjour, logement,
CAF, Ameli, compte bancaire.

## Pourquoi ce projet

Les démarches administratives ont toujours été un sujet qui bloque la plupart
des étudiants internationaux. Je le sais par mon expérience personnelle, par le
témoignage de mes amis, et par les statistiques du formulaire que j'ai envoyé à
mes camarades de l'ENSICAEN : 27 % des étudiants bloquent sur le logement et
30 % sur la demande de titre de séjour. Parmi ceux qui ont fait la demande de
titre de séjour, 91,7 % l'ont trouvée difficile. Pour le logement, 49,6 % l'ont
trouvé difficile et 45,9 % moyen.

J'ai moi-même galéré avec ces démarches et j'ai fait plusieurs erreurs, dont
j'ai payé les pénalités. C'est humain. Aujourd'hui, je veux avertir mes amis et
les futures générations pour qu'ils ne reproduisent pas ces erreurs.

Je veux avoir un impact positif sur la vie étudiante, et apporter un petit
changement dont j'aurais eu besoin moi-même et que je n'ai pas trouvé.
« Be the change you want to see. »

C'est aussi l'occasion de mettre en pratique les outils que j'ai appris pendant
mes deux années à l'ENSICAEN.

## Ce que fait le chatbot

- Identifie la situation de l'étudiant
- Indique les étapes à suivre et les délais
- Signale les erreurs fréquentes et leurs conséquences
- Renvoie vers les sites officiels

## Démarches couvertes

- [x] Titre de séjour : première année (VLS-TS)
- [x] Titre de séjour : renouvellement
- [ ] Logement (CROUS, Visale)
- [ ] Ameli (carte Vitale, CSS)
- [ ] CAF
- [ ] Compte bancaire

## Fonctionnement (RAG)

1. Les fiches sources (dossier `data/`) sont rédigées à partir des sites
   officiels et complétées par des conseils pratiques issus de l'expérience d'étudiants.
2. Les fiches sont découpées en morceaux et indexées dans une base vectorielle.
3. Pour chaque question, les morceaux les plus pertinents sont retrouvés.
4. La réponse est générée avec l'API Claude, à partir de ces morceaux
   uniquement, avec les liens officiels.


## Structure du dépôt

data/      Fiches sources en Markdown
src/       Code Python
tests/     Questions types et réponses attendues




## Données et confidentialité

Aucune donnée personnelle n'est publiée. Seuls des résultats agrégés du
sondage sont utilisés.

## Avertissement

Ce chatbot ne remplace pas un conseil juridique. Les règles peuvent changer :
vérifiez toujours sur les sites officiels.

## Auteure

Aya, étudiante en 2e année à l'ENSICAEN (informatique, IA et cybersécurité).
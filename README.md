# Système de Trading Multi-Agents avec KQML

Système de trading en temps réel utilisant KQML (Knowledge Query and Manipulation Language) pour la communication entre agents.

## Architecture

```
trading_system/
├── agents/
│   ├── base_agent.py      # Classe agent de base avec gestion KQML
│   ├── market_agent.py    # Gestion des données et prix du marché
│   └── trading_agent.py   # Décisions de trading et portefeuille
├── communication/
│   └── kqml.py           # Structure des messages KQML
├── data/
│   └── market_data.py    # Récupération des données YFinance
└── main.py               # Point d'entrée du système
```

## Installation

```bash
# Installation des dépendances
pip install yfinance pandas numpy colorama

# Lancement du système
python main.py
```

## Communication entre Agents

### Types de Messages
- ASK: Demande de données marché
- TELL: Réponse avec les prix
- SUBSCRIBE: Inscription aux mises à jour

### Logique de Trading
- Achat: Quand capital > coût de 100 actions
- Vente: Quand profit > 2%
- Suivi des positions par symbole

## Utilisation

Commandes:
- `f`: Récupérer nouvelles données
- `q`: Quitter le système

## Couleurs des Sorties
- Vert: Messages envoyés
- Bleu: Messages reçus
- Jaune: Décisions de trading
- Cyan: État du système

## Exemple de Sortie
```
[19:55:25] Récupération des données...
[TRADE] Achat de 100 actions GOOGL à 198.76€
Valeur du Portefeuille: 100,000.00€
Position AAPL: 100 actions @ 166.11€
```

## Visualisation des Communications

### Analyse de Trading
```
[ANALYSE TRADING] AAPL
Prix Actuel: 166.11€
SIGNAL ACHAT: Capital suffisant (100,000.00€) pour 100 actions
[TRADE EXÉCUTÉ] Achat de 100 actions à 166.11€
```

### Messages KQML
```
ASK: trader demande prix AAPL
TELL: market répond avec prix: 166.11€
```

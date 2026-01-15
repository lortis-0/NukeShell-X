🇬🇧 English :

# NukeShell‑X

NukeShell‑X is a Discord bot developed in **Python**, fully controlled via the **command line (CMD)**.  
No commands are executed from Discord itself: **everything is handled locally**, through the command-line interface.

---

## 📌 Overview

NukeShell‑X allows you to quickly destroy a server with all possible options via a bot.  
The bot connects to Discord, but the user interacts **exclusively through the CMD**.

The tool is **100% customizable** using a single configuration file.

---

## ⚙️ How It Works

- Connects to Discord using a bot token  
- 100% command-line interface — no Discord commands  
- Simple on-screen instructions  
- Loads all parameters from `config.json`  
- All actions are executed with configurable delays  

---

## ✨ Features

- Deletes **all channels and roles**
- Creates **multiple text channels**
  - Number of channels is configurable  
  - Channel name is fully customizable  
- Spams messages in **all created channels**
  - Message is customizable  
  - Can include `@everyone` possible to add to your message  
- Sends a **DM to all server members**
  - DM message is fully customizable  
- Renames **all members of the server**
  - Nickname fully customizable
- Renames the **Discord server**
- ⏱All actions use **custom delays** to control execution speed  

Everything is controlled via the `config.json` file.

---

## 🛠️ Configuration

Before using the bot, **the `config.json` file must be properly configured**.

It allows you to define:
- Discord bot token  
- Delays between each action  
- Channel names  
- Spam messages (`@everyone`)
- DM message sent to members  
- Nickname applied to all members  
- Number of channels and messages  

❗ Without a valid configuration, the bot will not work.

---

## 📦 Installation

### Requirements
- **Python 3.10 or higher**  
- A valid Discord bot with the required permissions  

### Steps
1. Install dependencies by running `install.bat`  
2. Configure the `config.json` file  
3. Start the bot:
   - Double-click `start.bat`  
   **or**  
   - Open a terminal in the folder and run:
     ```
     python main.py
     ```

---

## ▶️ Usage

Once the bot is running, the CMD interface will appear.

Simply enter the **Discord server ID** when prompted.

The bot will automatically execute all configured actions.

---

## 📫 Networks & Contact

- **Discord**: creditagricoles  
- **Telegram**: lortiss  

---

🇫🇷 Français :

# NukeShell‑X

NukeShell‑X est un bot Discord développé en **Python**, entièrement contrôlé via le **terminal (CMD)** pour rester anonyme.  
Aucune commande n’est exécutée depuis Discord : **tout est géré localement**, via l’interface en ligne de commande.

---

## 📌 Présentation

NukeShell‑X permet de détruire rapidement un serveur avec toute les options possible via un bot.  
Le bot se connecte à Discord, mais l’utilisateur interagit **uniquement depuis le CMD**.

L’outil est **100 % personnalisable** via un seul fichier de configuration.

---

## ⚙️ Fonctionnement

- Connexion à Discord via un token de bot  
- Interface 100 % en ligne de commande  
- Instructions affichées directement dans le terminal  
- Chargement des paramètres depuis `config.json`  
- Actions exécutées avec des délais configurables  

---

## ✨ Fonctionnalités

- Suppression de **tous les salons et rôles** 
- Création de **plusieurs salons textuels**
  - Nombre de salons configurable  
  - Nom des salons entièrement personnalisable  
- Spam de messages dans **tous les salons créés**
  - Message personnalisable  
  - Mention `@everyone` possible à ajouter dans votre message
- Envoi d’un **message privé à tous les membres (DMALL)**
  - Message DM entièrement personnalisable  
- Renommage de **tous les membres du serveur**
  - Pseudo entièrement personnalisable   
- Renommage du **serveur Discord**
- ⏱Délais personnalisés pour chaque action  

Tout est contrôlé via le fichier `config.json`.

---

## 🛠️ Configuration

Avant toute utilisation, **le fichier `config.json` doit être configuré correctement**.

Il permet de définir :
- Le token du bot Discord  
- Les délais entre chaque action  
- Le nom des salons créés  
- Le message de spam (`@everyone`)  
- Le message envoyé en DM  
- Le pseudo appliqué à tous les membres  
- Le nombre de salons et de messages  

❗ Sans une configuration valide, le bot ne fonctionnera pas.

---

## 📦 Installation

### Prérequis
- **Python 3.10 ou supérieur**  
- Un bot Discord valide avec les permissions nécessaires  

### Étapes
1. Installer les dépendances via `install.bat`  
2. Configurer le fichier `config.json`  
3. Lancer le bot :
   - Double-cliquez sur `start.bat`  
   **ou**
   - Ouvrez un terminal dans le dossier et tapez :
     ```
     python main.py
     ```

---

## ▶️ Utilisation

Une fois le bot lancé, l’interface CMD s’affiche.

Entrez simplement **l’ID du serveur Discord** lorsque le terminal le demande.

Le bot exécutera automatiquement toutes les actions configurées.

---

## 📫 Réseaux & Contact

- **Discord** : creditagricoles  
- **Telegram** : lortiss
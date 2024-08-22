# Verwende das offizielle Node.js Image
FROM node:18

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere die package.json und package-lock.json ins Arbeitsverzeichnis
COPY package*.json ./

# Installiere Abhängigkeiten
RUN npm install

# Kopiere den Rest des Quellcodes in das Arbeitsverzeichnis
COPY . .

# Exponiere den Port, auf dem die App läuft
EXPOSE 3000

# Starte die Anwendung
CMD ["npm", "start"]

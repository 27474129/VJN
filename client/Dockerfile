FROM node:17-alpine

WORKDIR /app

COPY package.json .
RUN npm install
RUN npm install typescript -g
COPY . .

EXPOSE 8004
CMD ["npm", "start"]

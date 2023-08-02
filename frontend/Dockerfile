FROM node:alpine

WORKDIR /app
ENV PATH /app:$PATH
ENV CHOKIDAR_USEPOLLING = true
COPY package*.json ./
RUN npm install

COPY ./ ./
EXPOSE 5173

# CMD ["npm", "run", "dev"]
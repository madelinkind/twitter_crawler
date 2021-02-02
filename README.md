# twitter_crawler

## Build Docker image

docker build --tag madelinkind/twitter-crawler:0.1 .
docker run --name twitter-crawler madelinkind/twitter-crawler:0.1

docker logs -f twitter-crawler --tail 30

docker container start twitter-crawler
docker container stop twitter-crawler
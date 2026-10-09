# A small web server with the sample assets inside.
# sample-assets.zip is not in the repo, it is a file of the release. Download it next to
# this Dockerfile before building (the workflow does it on its own).
FROM alpine:3.20 AS unpack
RUN apk add --no-cache unzip
COPY sample-assets.zip /tmp/sample-assets.zip
RUN mkdir /assets && unzip -q /tmp/sample-assets.zip -d /assets

FROM nginx:1.27-alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=unpack /assets /usr/share/nginx/html
EXPOSE 80

#!/bin/bash

RELEASE=$(curl -s https://api.github.com/repos/swagger-api/swagger-ui/releases/latest | grep tag_name | cut -d '"' -f 4)
echo "Downloading release ${RELEASE}"

pushd flask_swagger_ui/dist > /dev/null

OUTPUT_FILE=${RELEASE}.tar.gz
curl -s https://api.github.com/repos/swagger-api/swagger-ui/releases/latest | grep tarball_url | cut -d '"' -f 4 | wget -q -O "${OUTPUT_FILE}" -i -
tar --wildcards --strip-components=2 -xvf ${OUTPUT_FILE} '*/dist'
echo "${RELEASE}" > VERSION
rm index.html
rm ${OUTPUT_FILE}
popd > /dev/null

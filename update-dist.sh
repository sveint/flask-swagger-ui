#!/bin/bash

RELEASE=$(curl -s https://api.github.com/repos/swagger-api/swagger-ui/releases/latest | grep tag_name | cut -d '"' -f 4)
echo "Downloading release ${RELEASE}"

pushd flask_swagger_ui/dist > /dev/null

OUTPUT_FILE=${RELEASE}.tar.gz
curl -s https://api.github.com/repos/swagger-api/swagger-ui/releases/latest | grep tarball_url | cut -d '"' -f 4 | wget -q -O "${OUTPUT_FILE}" -i -

if [ "$(uname)" == "Darwin" ]; then
    tar --strip-components=2 -xvf ${OUTPUT_FILE} '*/dist'
elif [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    tar --wildcards --strip-components=2 -xvf ${OUTPUT_FILE} '*/dist'
fi

echo "${RELEASE}" > VERSION
rm index.html
rm ${OUTPUT_FILE}
popd > /dev/null

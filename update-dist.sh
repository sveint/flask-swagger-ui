#!/bin/bash
set -euo pipefail

LATEST_RELEASE=$(curl -s https://api.github.com/repos/swagger-api/swagger-ui/releases/latest)
RELEASE=$(echo "$LATEST_RELEASE" | jq -r .tag_name)
echo "Downloading release ${RELEASE}"

pushd flask_swagger_ui/dist > /dev/null

OUTPUT_FILE=${RELEASE}.tar.gz
TARBALL_URL=$(echo "$LATEST_RELEASE" | jq -r .tarball_url)
curl -sL -o "${OUTPUT_FILE}" "${TARBALL_URL}"
tar --wildcards --strip-components=2 -xvf "${OUTPUT_FILE}" '*/dist'
echo "${RELEASE}" > VERSION

rm -f index.html
rm -f swagger-initializer.js
rm -f swagger-ui-es-bundle.js
rm -f swagger-ui-es-bundle-core.js
rm -f *.map
rm -f "${OUTPUT_FILE}"

popd > /dev/null

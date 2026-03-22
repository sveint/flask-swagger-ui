#!/bin/bash

RELEASES_URL="https://api.github.com/repos/swagger-api/swagger-ui/releases"
LATEST_RELEASE=$(curl -s $RELEASES_URL/latest)
RELEASE=$(echo "$LATEST_RELEASE" | grep tag_name | cut -d '"' -f 4)
echo "Downloading release ${RELEASE}"

pushd flask_swagger_ui/dist > /dev/null

OUTPUT_FILE=${RELEASE}.tar.gz
TARBALL_URL=$(echo "$LATEST_RELEASE" | grep tarball_url | cut -d '"' -f 4)
curl -sL -o "${OUTPUT_FILE}" "${TARBALL_URL}"
# Check if GNU or BSD tar
WILDCARD_FLAG=$(tar --version | grep -q GNU && echo "--wildcards" || echo "")
tar $WILDCARD_FLAG --strip-components=2 -xvf ${OUTPUT_FILE} '*/dist'
echo "${RELEASE}" > VERSION
rm index.html
rm ${OUTPUT_FILE}
popd > /dev/null

RELEASE_NUMBER=$(echo "${RELEASE}" | sed 's/^v//g')
# use sed to update the version in setup.py, which is in the format version="x.y.z"
sed -i '' -E "s/version=\"[0-9]+\.[0-9]+\.[0-9]+\"/version=\"${RELEASE_NUMBER}\"/g" setup.py
# use sed to update the version in README.md, which is in the format 'Included Swagger UI version: x.y.z'
sed -i '' -E "s/Included Swagger UI version: [0-9]+\.[0-9]+\.[0-9]+/Included Swagger UI version: ${RELEASE_NUMBER}/g" README.md

git add README.md setup.py
git add flask_swagger_ui/dist
git commit -m "Update to version ${RELEASE_NUMBER}" -m "see $RELEASES_URL/tag/${RELEASE}"
git tag $RELEASE

#!/bin/bash
# Update firefox to the latest version (Linux)

# Directory containes the firefox installation exp: /home/firefox
WORKING_DIR="/home"
[ ! -d $WORKING_DIR/firefox ] && printf "\U274C Directory ${WORKING_DIR}/firefox DOES NOT exists." && exit

# Get Arch 64 or 32
ARCH=${ARCH:-$(uname -m)}
if [ "$ARCH" = "x86_64" ]; then
  LIBDIRSUFFIX="64"
elif [[ "$ARCH" = i?86 ]]; then
  ARCH=i686
  LIBDIRSUFFIX=""
else
  echo "The architecture $ARCH is not supported." >&2
  exit 1
fi

TMP="/tmp"
FFLANG=${FFLANG:-en-US}
FFCHANNEL=${FFCHANNEL:-latest}
FFPACKAGE="https://download.mozilla.org/?product=firefox-${FFCHANNEL}&os=linux${LIBDIRSUFFIX}&lang=${FFLANG}"

INSTALLED_VERSION=$(${WORKING_DIR}/firefox/firefox -v |awk '{print $3}' )
NEW_VERSION=$(curl --silent https://product-details.mozilla.org/1.0/firefox_versions.json | jq -r '.LATEST_FIREFOX_VERSION')

if [ "$INSTALLED_VERSION" = "$NEW_VERSION" ]; then
   printf "We are running the latest version of Firefox \U1F918"
else
	printf "Installing the new version of Firefox  -> [ $NEW_VERSION ] \U1F50E"
	wget --show-progress -q -O "$TMP/firefox-$NEW_VERSION.tar.bz2" $FFPACKAGE
	tar xvf $TMP/firefox-$NEW_VERSION.tar.*
	sudo rm -rf ${WORKING_DIR}/firefox
	sudo cp -R $TMP/firefox ${WORKING_DIR}
	printf "\nDone\nTest installed version \U1F47E -> $(${WORKING_DIR}/firefox/firefox -v)"
fi

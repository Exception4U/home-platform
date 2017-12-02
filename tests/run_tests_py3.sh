#!/bin/bash

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

export PYTHONPATH=$DIR/../:$PYTHONPATH

# Convert SUNCG test data
$DIR/../scripts/convert_suncg.sh "$DIR/data/suncg"

# Create output directories
mkdir -p ${DIR}/report3/profile
mkdir -p ${DIR}/report3/coverage

# Cleanup previous reports
target=${DIR}/report3/coverage/
if find "$target" -mindepth 1 -print -quit | grep -q .; then
    # Output folder not empty, erase all existing files
    rm ${DIR}/report3/coverage/*
fi

# Run unit tests and coverage analysis for the 'action' module
nosetests3 --verbosity 3 --with-coverage --cover-html --cover-html-dir=${DIR}/report3/coverage \
--cover-erase --cover-tests --cover-package=home_platform,home_platform.acoustics,home_platform.core,home_platform.physics,home_platform.rendering,home_platform.suncg,home_platform.utils,home_platform.env,home_platform.constants,home_platform.semantic
if type "x-www-browser" > /dev/null; then
	x-www-browser ${DIR}/report3/coverage/index.html
fi

# For profiler sorting options, see:
# https://docs.python.org/2/library/profile.html#pstats.Stats

#PROFILE_FILE=${DIR}/report/profile/profile.out
#python -m cProfile -o ${PROFILE_FILE} `which nosetests` ${DIR}
#runsnake ${PROFILE_FILE}

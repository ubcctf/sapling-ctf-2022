#!/bin/bash
read -p "MAKE SURE THE CHANGES ARE COMMITED CAUSE GIT ARCHIVE PULLS FROM HEAD" _notused
git archive -o players.zip HEAD players/
unzip -l players.zip > players.zip.listing
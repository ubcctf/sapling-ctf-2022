#!/bin/bash
docker build . -t web-valentina
docker run -p 8999:8999 -t --name valentina-chall web-valentina
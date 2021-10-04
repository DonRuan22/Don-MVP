#!/bin/bash
ls
#rasa run actions
rasa run --credentials credentials.yml --enable-api --cors “*” --debug
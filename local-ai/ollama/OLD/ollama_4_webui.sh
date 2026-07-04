#! /usr/bin/bash

docker run -d	\
	--name open-webui	\
	-p 3000:8080	\
	--add-host=host.docker.internal:host-gateway	\
	-e OLLAMA_BASE_URL=http://host.docker.internal:11434	\
	ghcr.io/open-webui/open-webui:v0.5.7


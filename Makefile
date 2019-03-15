rundb: 
	docker run -d \
	--publish=7474:7474 --publish=7687:7687 \
	--volume="${PWD}/data:/data" \
	--volume="${PWD}/logs:/logs" \
	--volume="${PWD}/import:/var/lib/neo4j/import" \
	--env NEO4J_AUTH=none \
	--name="curious_george" \
	neo4j
	echo "done"

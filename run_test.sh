playerID=$(curl --data 'param=cesar'  http://localhost:1866/join | jsawk -a 'return this.playerID')
echo $playerID
exit
while 1 do
	curl --data 'param=cesar'  http://localhost:1866/join
done

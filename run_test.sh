curl --data 'param=cesar1'  http://localhost:1866/join &
curl --data 'param=cesar2'  http://localhost:1866/join &
curl --data 'param=cesar3'  http://localhost:1866/join &
curl --data 'param=cesar4'  http://localhost:1866/join &

for i in {0..100}
do
	curl --data 'param=up'  http://localhost:1866/ABC/ABC/ABCD
done
for i in {0..100}
do
        curl --data 'param=down'  http://localhost:1866/ABC/ABC/ABCD
done
for i in {0..100}
do
        curl --data 'param=left'  http://localhost:1866/ABC/ABC/ABCD
done
for i in {0..100}
do
        curl --data 'param=right'  http://localhost:1866/ABC/ABC/ABCD
done


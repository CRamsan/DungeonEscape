curl --data 'param=cesar1'  http://localhost:1866/join &
curl --data 'param=cesar2'  http://localhost:1866/join &
curl --data 'param=cesar3'  http://localhost:1866/join &
curl --data 'param=cesar4'  http://localhost:1866/join &

while :
do
    r=$((RANDOM%4))
    for i in {1..20}
    do
        case "$r" in
            0)
		curl --data 'param=up' http://localhost:1866/ABC/ABC/ABCD
                ;;
            1)
		curl --data 'param=down' http://localhost:1866/ABC/ABC/ABCD
                ;;
            2)
		curl --data 'param=right' http://localhost:1866/ABC/ABC/ABCD
                ;;
            3)
		curl --data 'param=left' http://localhost:1866/ABC/ABC/ABCD
                ;;
         esac
     done
done

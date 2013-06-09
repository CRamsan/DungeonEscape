curl --data 'param=cesar1'  http://localhost:8888/join &
curl --data 'param=cesar2'  http://localhost:8888/join &
curl --data 'param=cesar3'  http://localhost:8888/join &
curl --data 'param=cesar4'  http://localhost:8888/join &

while :
do
    read -n 1 key
    for i in {1..20}
    do
    case $key in
        'A')
	    curl --data 'param=up' http://localhost:8888/ABC/ABC/ABCD
            echo
            ;;
        'B')
	    curl --data 'param=down' http://localhost:8888/ABC/ABC/ABCD
            echo
            ;;
        'C')
	    curl --data 'param=right' http://localhost:8888/ABC/ABC/ABCD
            echo
            ;;
        'D')
	    curl --data 'param=left' http://localhost:8888/ABC/ABC/ABCD
            echo
            ;;
    esac
    done
    echo "--------------"
done

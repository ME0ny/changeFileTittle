mkdir "январь" "февраль" "март" "апрель" "май" "июнь" "июль" "август" "сентябрь" "октябрь" "ноябрь" "декабрь"
echo "Какие файлы искать:"
read reg
stat --printf "%n %y\n" $reg | awk '{print $1,$2}' | sed -r 's/-/ /g' | awk '{print $1, $3}' > files
cat files | while read y

do
name=$(echo $y | awk '{print $1}')
month=$(echo $y | awk '{print $2}') 
case "$month" in
	"01")
	mv $name "январь/"
	;;
	"02")
	mv $name "февраль/"
	;;
	"03")
	mv $name "март/"
	;;
	"04")
	mv $name "апрель/"
	;;
	"05")
	mv $name "май/"
	;;
	"06")
	mv $name "июнь/"
	;;	
	"07")
	mv $name "июль/"
	;;
	"08")
	mv $name "август/"
	;;
	"09")
	mv $name "сентябрь/"
	;;
	"10")
	mv $name "октябрь/"
	;;
	"11")
	mv $name "ноябрь/"
	;;
	"12")
	mv $name "декабрь/"
	;;
	esac
done
rm files

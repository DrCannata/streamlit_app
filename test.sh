if [ $# -ne 1 ]
then
	echo "Usage: $0 SQLQuery"
	exit 1
fi

sql -S OMLUSER/Cenne#e49Cenne#e49@150.136.183.171/DB23AI_PDB1.sub08201532330.philfnvcn.oraclevcn.com <<!
SET SQLFORMAT JSON-FORMATTED
set feedback off
$1;
!

# streamlit_app

#
wget --no-check-certificate -c --header "Cookie: oraclelicense=accept-securebackup-cookie" https://download.oracle.com/otn_software/linux/instantclient/19800/oracle-instantclient19.8-basic-19.8.0.0.0-1.x86_64.rpm  
sudo update-alternatives --config x-www-browser  
cd /home/vscode/.vscode-remote/extensions/oracle.sql-developer-24.3.0-linux-x64/dbtools/sqlcl  

curl --output sqlcl-latest.zip https://download.oracle.com/otn_software/java/sqldeveloper/sqlcl-latest.zip  

export JAVA_HOME="/home/vscode/.vscode-remote/extensions/oracle.sql-developer-24.3.1-linux-x64/dbtools/jdk/"   
export PATH=$JAVA_HOME:$PATH

./sqlcl/bin/sql OMLUSER/Cenne#e49Cenne#e49@150.136.183.171/DB23AI_PDB1.sub08201532330.philfnvcn.oraclevcn.com  

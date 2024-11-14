import subprocess
import json

#subprocess.call("/workspaces/streamlit_app/test.sh", shell=True)
result = subprocess.run('/workspaces/streamlit_app/test.sh "select * from carnot" | grep -vi "rows selected"', shell=True, stdout=subprocess.PIPE)

# print(result.stdout)
json_object = json.loads(result.stdout)
# print(json_object)
print(json_object["results"])
import subprocess
import json

#subprocess.call("/workspaces/streamlit_app/test.sh", shell=True)
#result = subprocess.run('"/Users/pcannata/Mine/My Repositories/AI/Python/Streamlit/streamlit_app/test.sh" "select * from dual"', shell=True, stdout=subprocess.PIPE)
result = subprocess.run('"/Users/pcannata/Mine/My Repositories/AI/Python/Streamlit/streamlit_app/test.sh" "select \'First\' as attr union select \'Second\' as attr"', shell=True, stdout=subprocess.PIPE)

# print(result.stdout)
json_object = json.loads(result.stdout)
# print(json_object)
print(json_object["results"])
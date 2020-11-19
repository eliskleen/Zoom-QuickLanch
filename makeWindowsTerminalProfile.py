import json

if __name__ == "__main__":
    #fileToOpen = input()
    
    file = open("testFile.json", 'r')
    json_data = json.load(file)
    parsed_json = (json.loads(json_data))
    #print(json.dumps(parsed_json, indent=4, sort_keys=True))
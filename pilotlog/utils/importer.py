import json
from pprint import pprint


class JSONImporter():

    def __init__(self, file_path):
        self.file_path = file_path

    def import_data(self):
        """Import data from JSON file."""

        with open(self.file_path, 'r') as f:
            data = str(f.read()).replace("\\", "")
            data = json.loads(data)
            tables = {}
            users = {}
            platforms = {}
            keys = None
            count = 0
            tables2 = []
            for i in data:
                tables2.append(i["table"])
                count += 1
                if i["table"].lower() in tables:
                    tables[i["table"].lower()] += 1
                else:
                    tables[i["table"].lower()] = 1
                    print("\n" + i["table"].lower())
                    print(i["_modified"])
                    pprint([i["meta"]])

                if i['user_id'] in users:
                    users[i["user_id"]] += 1
                else:
                    users[i["user_id"]] = 1
                if i["platform"] in platforms:
                    platforms[i["platform"]] += 1
                else:
                    platforms[i["platform"]] = 1
                if keys is None:
                    keys = i.keys()

            print('tables: ')
            pprint(tables)

            print('users: ')
            pprint(users)

            print('platforms: ')
            pprint(platforms)

            print('keys: ')
            pprint(keys)

            print('count: ', count)

            print('tables2: ')
            pprint(list(set(tables2)))

        return []

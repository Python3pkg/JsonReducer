# JsonReducer

This is a package based on the concept of Smaller Serialized Data, the implementation reduces the lenght of a JSON response as shown in the example.

### Input (Array with multiple Dictionaries)
``` Python
[{
  "id":1,
  "name":"Rodolfo",
  "username":"rodolfomg"
 },
 {
  "id":2,
  "name":"Pedro",
  "username":"pedro47"
}]
 ``` 
 
### Output (Serialized Dictionary)
 ``` Python
{
  "id": [1, 2],
  "name":["Rodolfo","Pedro"],
  "username":["rodolfomg","pedro47"]
}
 ```
 
# Installation
Install package using pip

    pip install JsonReducer

# Usage
``` Python

import JsonReducer
from .models import Users

def get_users(request):
    users = User.objects.all().values()
    users_list = list(users)
    return JsonResponse(JsonReduce.reduce(users_list), safe=False)
  
```

# KHU Seraph Docker


## Prerequisite
- KHU_Seraph_django/secret.json
```
{
    "SECRET_KEY": <Your Django Secret Key>,
    "EMAIL_HOST_USER": <Username to use for the SMTP server defined in EMAIL_HOST>,
    "EMAIL_HOST_PASSWORD": <Password to use for the SMTP server defined in EMAIL_HOST>
}
```


- KHU_Seraph_django/global_vars.py
```
IPS = [
    <IP addreses of each node>
]

# Cluster names
CLUSTER_ALL = 'All'
CLUSTER_A = 'a'
CLUSTER_B = 'b'
CLUSTER_C = 'c'

CLUSTER_NAMES = (
    CLUSTER_A,
    CLUSTER_B,
    CLUSTER_C
)

# Department names
DEPART_ALL = 'All'
DEPART_EE = 'EE'
DEPART_BME = 'BE'
DEPART_CE = 'CE'
DEPART_SWCON = 'SWCON'
DEPART_AI = 'AI'

# User types
USERTYPE_ADMIN = 'Adminisrator'
USERTYPE_UNDERGRAD = 'Undergraduate'
USERTYPE_INTERN = 'Undergraduate Researcher'
USERTYPE_MASTER = 'Master'
USERTYPE_PHD = 'PhD'
USERTYPE_PROFESSOR = 'Professor'
USERTYPE_OTHERS = 'Others'
```

## Run
```
docker build -t seraph/django .
docker build -t seraph/nginx .
docker-compose up -d --build
```
import yaml

def test_yaml():
    evn = {
        "default": "dev",
        "hosts": {
            "dev": "127.0.0.1",
            "test": "128.1.0.2",
            "product": "127.2.0.3"
        }
    }
    with open("env_config.yaml", "w") as f:
        yaml.safe_dump(data=evn, stream=f)
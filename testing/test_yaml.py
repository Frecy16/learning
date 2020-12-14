import yaml


def test_yaml2():
    env = {
        "default": "test",
        "testing-studio":
        {
            "dev": "127.0.0.1",
            "test": "www.baidu.com"
        }
    }
    with open("env.yaml","w") as f:
        yaml.safe_dump(data=env, stream=f)

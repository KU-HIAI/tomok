# -*- coding: utf-8 -*-
""" KU-DONGIL-DEMO API """

# python
import sys

# 3rd-party
import hydra
from omegaconf import DictConfig

# framework
from utils import print_config
from ifc import ifc_init
from acc import acc_init


def launch_server(config):
    server = hydra.utils.instantiate(config.server)
    app = server.app
    app.app["config"] = config
    acc_init(app.app)
    app.run(port=config.server.app_port)


@hydra.main(config_path="configs/", config_name="serve.yaml", version_base="1.1")
def hydra_entry(config: DictConfig):
    config.server.app_port = int(config.server.app_port)
    if config.work_dir not in sys.path:
        sys.path.append(config.work_dir)  # for vscode debug
    # Pretty print config using Rich library
    if config.get("print_config"):
        print_config(config, resolve=True)
    launch_server(config)


if __name__ == "__main__":
    hydra_entry()